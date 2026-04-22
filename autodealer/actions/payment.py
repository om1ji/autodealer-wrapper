"""High-level actions: payment creation and retrieval."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import bindparam, text

from autodealer.connection import session_scope

_ACCOUNTING_ITEM_CLIENT_PAYMENT = 3  # «Поступление от клиента»
_SYSTEM_USER_ID = 1  # Системный пользователь по умолчанию

# Типы действий в payment_action (журнал аудита)
_PAYMENT_ACTION_CREATE = 0
_PAYMENT_ACTION_UPDATE = 1
_PAYMENT_ACTION_DELETE = -1

BOT_NOTE_MARKER = "Добавлено ботом"


def _with_bot_marker(notes: Optional[str]) -> str:
    """Добавить маркер :data:`BOT_NOTE_MARKER` к примечанию платежа.

    Помечает платёж как созданный ботом/интеграцией, чтобы каскадное удаление
    заказ-наряда могло отличать автоматические платежи от ручных.
    Если маркер уже присутствует — строка не меняется.
    """
    if not notes:
        return BOT_NOTE_MARKER
    if BOT_NOTE_MARKER in notes:
        return notes
    return f"{BOT_NOTE_MARKER}; {notes}"


# ---------------------------------------------------------------------------
# Справочники
# ---------------------------------------------------------------------------


@dataclass
class WalletInfo:
    """Кошелёк (касса или счёт) организации."""

    wallet_id: int
    name: str
    organization_id: int


@dataclass
class PaymentTypeInfo:
    """Способ оплаты."""

    payment_type_id: int
    name: str


def get_wallets(organization_id: int) -> list[WalletInfo]:
    """Вернуть все кошельки организации.

    Args:
        organization_id: PK организации.

    Returns:
        Список :class:`WalletInfo`.

    Example::

        wallets = get_wallets(1)
        for w in wallets:
            print(w.wallet_id, w.name)
    """
    with session_scope() as session:
        rows = (
            session.execute(
                text(
                    "SELECT wallet_id, name, organization_id"
                    " FROM wallet WHERE organization_id = :oid"
                    " ORDER BY wallet_id"
                ),
                {"oid": organization_id},
            )
            .mappings()
            .all()
        )
    return [WalletInfo(**dict(r)) for r in rows]


def get_payment_types() -> list[PaymentTypeInfo]:
    """Вернуть все активные способы оплаты.

    Returns:
        Список :class:`PaymentTypeInfo`.

    Example::

        for pt in get_payment_types():
            print(pt.payment_type_id, pt.name)
    """
    with session_scope() as session:
        rows = (
            session.execute(
                text(
                    "SELECT payment_type_id, name FROM payment_type"
                    " WHERE hidden = 0 ORDER BY payment_type_id"
                )
            )
            .mappings()
            .all()
        )
    return [PaymentTypeInfo(**dict(r)) for r in rows]


# ---------------------------------------------------------------------------
# Чтение платежей
# ---------------------------------------------------------------------------


@dataclass
class PaymentRecord:
    """Платёж, привязанный к заказ-наряду."""

    payment_id: int
    summa: Decimal
    payment_date: datetime
    payment_type_id: int
    payment_type_name: Optional[str]
    wallet_id: Optional[int]
    wallet_name: Optional[str]
    notes: Optional[str]


def get_payments(document_out_id: int) -> list[PaymentRecord]:
    """Вернуть все платежи по заказ-наряду.

    Args:
        document_out_id: PK заказ-наряда.

    Returns:
        Список :class:`PaymentRecord`. Пустой если платежей нет.

    Example::

        for p in get_payments(42):
            print(p.payment_id, p.summa, p.payment_type_name)
    """
    with session_scope() as session:
        rows = (
            session.execute(
                text(
                    "SELECT p.payment_id, p.summa, p.payment_date,"
                    "       p.payment_type_id, pt.name AS payment_type_name,"
                    "       p.wallet_id, w.name AS wallet_name, p.notes"
                    " FROM payment_out po"
                    " JOIN payment p ON p.payment_id = po.payment_id"
                    " LEFT JOIN payment_type pt ON pt.payment_type_id = p.payment_type_id"
                    " LEFT JOIN wallet w ON w.wallet_id = p.wallet_id"
                    " WHERE po.document_out_id = :doc_id"
                    " ORDER BY p.payment_date"
                ),
                {"doc_id": document_out_id},
            )
            .mappings()
            .all()
        )
    return [PaymentRecord(**dict(r)) for r in rows]


# ---------------------------------------------------------------------------
# Создание платежей
# ---------------------------------------------------------------------------


def create_payment(
    *,
    document_out_id: int,
    summa: float,
    wallet_id: int,
    payment_type_id: int,
    payment_date: Optional[datetime] = None,
    notes: Optional[str] = None,
    created_by_user_id: int = _SYSTEM_USER_ID,
) -> int:
    """Создать документ оплаты для заказ-наряда.

    Атомарно создаёт цепочку:

    1. ``payment``         — запись платежа (сумма, способ, кошелёк).
    2. ``payment_out``     — привязка платежа к ``document_out``.
    3. ``payment_action``  — запись в журнал аудита (``action_type=0``).
    4. Обновляет ``document_out.date_payment``.

    .. note::

       Бухгалтерские проводки (``payment_document``, ``money_document_detail``,
       ``money_document_payment``) намеренно **не создаются** — ручные
       заказ-наряды АвтоМойки тоже их не создают (0/272 в проде). Эти
       проводки генерируются в другом месте (закрытие кассовой смены,
       выгрузка в 1С и т.п.). Дублирование приводит к двойному учёту.

    Args:
        document_out_id: PK заказ-наряда (из :func:`~autodealer.services.create_service_order`).
        summa: Сумма платежа.
        wallet_id: FK в ``wallet`` — касса/счёт списания.
        payment_type_id: FK в ``payment_type`` — способ оплаты
            (1=Наличный, 2=Безналичный, 7=Банковская карта).
        payment_date: Дата/время платежа. По умолчанию — текущее время.
        notes: Примечание к платежу. К любому значению автоматически
            добавляется маркер :data:`BOT_NOTE_MARKER` (``"Добавлено ботом"``),
            чтобы отличать платежи бота от ручных при каскадном удалении.
        created_by_user_id: user_id, записываемый в ``payment_action.user_id``.
            По умолчанию — системный.

    Returns:
        ``payment_id`` созданного платежа.

    Raises:
        ValueError: Если заказ-наряд с ``document_out_id`` не найден.

    Example::

        from autodealer.actions.payment import create_payment

        payment_id = create_payment(
            document_out_id=42,
            summa=2300.0,
            wallet_id=1,        # Наличный расчёт
            payment_type_id=1,  # Наличный
        )
    """
    from autodealer.domain.payment import Payment
    from autodealer.domain.payment_out import PaymentOut

    pay_dt = payment_date or datetime.now()

    with session_scope() as session:
        doc_reg_id = session.execute(
            text(
                "SELECT document_registry_id FROM document_out_header"
                " WHERE document_out_id = :doc_id"
            ),
            {"doc_id": document_out_id},
        ).scalar()

        if doc_reg_id is None:
            raise ValueError(
                f"Заказ-наряд document_out_id={document_out_id} не найден"
                " или не имеет document_registry_id"
            )

        pay = Payment(
            payment_type_id=payment_type_id,
            wallet_id=wallet_id,
            summa=summa,
            payment_date=pay_dt,
            document_registry_id=doc_reg_id,
            notes=_with_bot_marker(notes),
        )
        session.add(pay)
        session.flush()
        payment_id = pay.payment_id

        session.add(PaymentOut(document_out_id=document_out_id, payment_id=payment_id))

        session.execute(
            text(
                "INSERT INTO payment_action"
                " (payment_id, user_id, payment_type_id, action_datetime,"
                "  summa, document_out_id, action_type, payment_date)"
                " VALUES (:pid, :uid, :ptype, :now, :summa, :doc,"
                "         :atype, :pdate)"
            ),
            {
                "pid": payment_id,
                "uid": created_by_user_id,
                "ptype": payment_type_id,
                "now": datetime.now(),
                "summa": summa,
                "doc": document_out_id,
                "atype": _PAYMENT_ACTION_CREATE,
                "pdate": pay_dt,
            },
        )

        session.execute(
            text(
                "UPDATE document_out SET date_payment = :dt"
                " WHERE document_out_id = :doc_id"
            ),
            {"dt": pay_dt, "doc_id": document_out_id},
        )

    return payment_id


def _delete_payment_rows(session, payment_id: int) -> None:
    """Удалить все связанные с платежом записи в рамках переданной сессии.

    Порядок: ``money_document_payment`` → ``money_document_detail``
    → ``payment_document`` → ``payment_action`` → ``payment_out`` → ``payment``.

    Первые три таблицы текущим :func:`create_payment` уже не создаются
    (см. её docstring), но DELETE'ы оставлены — чтобы функция могла
    удалять старые платежи, созданные до этого изменения, а также
    импортированные из других интеграций.

    Не проверяет существование платежа и не управляет транзакцией —
    вызывающий код должен сделать это сам. Используется из
    :func:`delete_payment` (одиночное удаление) и из
    :func:`~autodealer.services.delete_service_order` для атомарного
    каскадного удаления в одной транзакции.
    """
    mdd_ids = [
        row[0]
        for row in session.execute(
            text(
                "SELECT money_document_detail_id FROM money_document_payment"
                " WHERE payment_id = :pid"
            ),
            {"pid": payment_id},
        ).all()
    ]

    session.execute(
        text("DELETE FROM money_document_payment WHERE payment_id = :pid"),
        {"pid": payment_id},
    )
    if mdd_ids:
        session.execute(
            text(
                "DELETE FROM money_document_detail"
                " WHERE money_document_detail_id IN :ids"
            ).bindparams(bindparam("ids", expanding=True)),
            {"ids": mdd_ids},
        )
    session.execute(
        text("DELETE FROM payment_document WHERE payment_id = :pid"),
        {"pid": payment_id},
    )
    session.execute(
        text("DELETE FROM payment_action WHERE payment_id = :pid"),
        {"pid": payment_id},
    )
    session.execute(
        text("DELETE FROM payment_out WHERE payment_id = :pid"),
        {"pid": payment_id},
    )
    session.execute(
        text("DELETE FROM payment WHERE payment_id = :pid"),
        {"pid": payment_id},
    )


def delete_payment(payment_id: int) -> None:
    """Физически удалить платёж со всеми связанными записями.

    Удаляет в обратном порядке создания:

    1. ``money_document_payment``  — связь проводки с платежом.
    2. ``money_document_detail``   — бухгалтерская проводка.
    3. ``payment_document``        — привязка к ``document_registry``.
    4. ``payment_out``             — привязка к ``document_out``.
    5. ``payment``                 — сам платёж.

    ``document_out.date_payment`` не сбрасывается — если удаляется
    одиночный платёж, вызывающий код сам решает, нужно ли пересчитать
    дату по оставшимся платежам. При каскадном удалении заказ-наряда
    поле и так уходит вместе с ``document_out``.

    Args:
        payment_id: PK платежа.

    Raises:
        ValueError: Если платёж не найден.
    """
    with session_scope() as session:
        exists = session.execute(
            text("SELECT 1 FROM payment WHERE payment_id = :pid"),
            {"pid": payment_id},
        ).scalar()
        if not exists:
            raise ValueError(f"Платёж payment_id={payment_id} не найден")

        _delete_payment_rows(session, payment_id)


@dataclass
class PaymentSplitItem:
    """Одна часть разбивки платежа (способ + кошелёк + сумма)."""

    wallet_id: int
    payment_type_id: int
    summa: float
    notes: Optional[str] = None


def create_payment_split(
    *,
    document_out_id: int,
    parts: list[PaymentSplitItem],
    payment_date: Optional[datetime] = None,
) -> list[int]:
    """Создать несколько платежей за один заказ-наряд (разбивка по способам оплаты).

    Каждая часть создаётся независимо через :func:`create_payment`.
    Если хотя бы одна часть упадёт — предыдущие уже будут зафиксированы
    (транзакции независимы). Передавай только корректные данные.

    Args:
        document_out_id: PK заказ-наряда.
        parts: Список :class:`PaymentSplitItem` — по одному на каждый способ оплаты.
        payment_date: Единая дата/время для всех частей. По умолчанию — текущее время.

    Returns:
        Список ``payment_id`` в том же порядке, что и ``parts``.

    Raises:
        ValueError: Если ``parts`` пустой или суммы <= 0.

    Example::

        from autodealer.actions.payment import create_payment_split, PaymentSplitItem

        ids = create_payment_split(
            document_out_id=42,
            parts=[
                PaymentSplitItem(wallet_id=1, payment_type_id=1, summa=1000.0),  # наличные
                PaymentSplitItem(wallet_id=4, payment_type_id=7, summa=1300.0),  # карта
            ],
        )
    """
    if not parts:
        raise ValueError("parts не может быть пустым")

    invalid = [p for p in parts if p.summa <= 0]
    if invalid:
        raise ValueError(f"Сумма платежа должна быть > 0: {invalid}")

    pay_dt = payment_date or datetime.now()

    return [
        create_payment(
            document_out_id=document_out_id,
            summa=part.summa,
            wallet_id=part.wallet_id,
            payment_type_id=part.payment_type_id,
            payment_date=pay_dt,
            notes=part.notes,
        )
        for part in parts
    ]
