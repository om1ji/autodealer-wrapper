"""High-level service functions for AutoDealer domain operations.

These functions wrap multi-step ORM inserts into single atomic calls,
hiding the directory_registry / trigger bookkeeping from the caller.
"""

from __future__ import annotations

from typing import Optional

from sqlalchemy import text

from autodealer.connection import session_scope
from datetime import datetime


# metatable_id=1 → ORGANIZATION
_METATABLE_ORGANIZATION = 1
# Системный пользователь по умолчанию
_SYSTEM_USER_ID = 1

_METATABLE_DOCUMENT_OUT = 12

_SERVICE_ORDER_PREFIX = "АВТ"

_DOCUMENT_STATE = {"Оформлен": 4, "Черновик": 2, "Удалён": -1}


# ---------------------------------------------------------------------------
# Организации
# ---------------------------------------------------------------------------


class OrganizationInfo:
    """Агрегат организации: основные поля + кошельки.

    Атрибуты:
        organization_id: PK организации.
        fullname: Полное название.
        shortname: Краткое название.
        inn: ИНН.
        kpp: КПП.
        ogrn: ОГРН.
        address: Адрес.
        face: 0=ЮЛ, 1=ИП/физлицо.
        hidden: 0=активна.
        wallets: Список кошельков ``[{"wallet_id": 3, "name": "Наличные"}]``.
    """

    def __init__(self, row: dict, wallets: list[dict]) -> None:
        self.organization_id: int = row["organization_id"]
        self.fullname: Optional[str] = row.get("fullname")
        self.shortname: Optional[str] = row.get("shortname")
        self.inn: Optional[str] = row.get("inn")
        self.kpp: Optional[str] = row.get("kpp")
        self.ogrn: Optional[str] = row.get("ogrn")
        self.address: Optional[str] = row.get("address")
        self.face: int = row.get("face", 0)
        self.hidden: int = row.get("hidden", 0)
        self.wallets: list[dict] = wallets

    def wallet_id_by_name(self, name: str) -> Optional[int]:
        """Найти wallet_id по части названия (без учёта регистра)."""
        name_lower = name.lower()
        for w in self.wallets:
            if name_lower in w["name"].lower():
                return w["wallet_id"]
        return None

    def __repr__(self) -> str:
        return (
            f"OrganizationInfo(id={self.organization_id},"
            f" name={self.shortname!r}, inn={self.inn!r},"
            f" wallets={len(self.wallets)})"
        )


def get_organization(organization_id: int) -> Optional["OrganizationInfo"]:
    """Загрузить организацию с кошельками по ID.

    Returns:
        :class:`OrganizationInfo` или ``None`` если не найдена.

    Example::

        org = get_organization(1)
        print(org)
        # OrganizationInfo(id=1, name='Наша фирма', inn=None, wallets=2)

        wallet_id = org.wallet_id_by_name("наличн")  # → 1
    """
    with session_scope() as session:
        row = (
            session.execute(
                text(
                    "SELECT organization_id, fullname, shortname, inn, kpp,"
                    "       ogrn, address, face, hidden"
                    " FROM organization WHERE organization_id = :oid"
                ),
                {"oid": organization_id},
            )
            .mappings()
            .first()
        )

        if row is None:
            return None

        wallets = (
            session.execute(
                text(
                    "SELECT wallet_id, name"
                    " FROM wallet WHERE organization_id = :oid"
                    " ORDER BY wallet_id"
                ),
                {"oid": organization_id},
            )
            .mappings()
            .all()
        )

        return OrganizationInfo(dict(row), [dict(w) for w in wallets])


def list_organizations() -> list["OrganizationInfo"]:
    """Вернуть список всех активных организаций с кошельками.

    Example::

        orgs = list_organizations()
        for org in orgs:
            print(org)
    """
    with session_scope() as session:
        rows = (
            session.execute(
                text(
                    "SELECT organization_id, fullname, shortname, inn, kpp,"
                    "       ogrn, address, face, hidden"
                    " FROM organization WHERE hidden = 0"
                    " ORDER BY organization_id"
                )
            )
            .mappings()
            .all()
        )

        result = []
        for row in rows:
            wallets = (
                session.execute(
                    text(
                        "SELECT wallet_id, name FROM wallet"
                        " WHERE organization_id = :oid ORDER BY wallet_id"
                    ),
                    {"oid": row["organization_id"]},
                )
                .mappings()
                .all()
            )
            result.append(OrganizationInfo(dict(row), [dict(w) for w in wallets]))

        return result


def create_organization(
    fullname: str,
    *,
    shortname: Optional[str] = None,
    inn: Optional[str] = None,
    kpp: Optional[str] = None,
    ogrn: Optional[str] = None,
    address: Optional[str] = None,
    face: int = 0,
    wallet_names: Optional[list[str]] = None,
    created_by_user_id: int = _SYSTEM_USER_ID,
) -> "OrganizationInfo":
    """Создать организацию в Firebird.

    Атомарно создаёт ``DirectoryRegistry`` → ``Organization`` → ``Wallet`` (если переданы).

    Args:
        fullname: Полное название (обязательно).
        shortname: Краткое название (по умолчанию — первые 30 символов fullname).
        inn: ИНН.
        kpp: КПП.
        ogrn: ОГРН.
        address: Адрес.
        face: 0=ЮЛ, 1=ИП.
        wallet_names: Список названий касс/счетов для создания.
            Например ``["Наличные", "Банковская карта", "СБП"]``.
        created_by_user_id: Пользователь-создатель.

    Returns:
        :class:`OrganizationInfo` созданной организации.

    Example::

        from autodealer.services import create_organization

        org = create_organization(
            "ООО СК-Авто Казань",
            shortname="СК-Авто",
            inn="1655012345",
            address="г. Казань, ул. Скрябина 8к1",
            wallet_names=["Наличные", "Банковская карта", "СБП"],
        )
        print(org.organization_id)
        print(org.wallets)
        # [{"wallet_id": 7, "name": "Наличные"}, ...]
    """
    from datetime import datetime as _dt

    sname = (shortname or fullname)[:30]

    with session_scope() as session:
        # 1. DirectoryRegistry
        dr = DirectoryRegistry(
            metatable_id=_METATABLE_ORGANIZATION,
            create_user_id=created_by_user_id,
            change_user_id=created_by_user_id,
        )
        session.add(dr)
        session.flush()
        dr_id = dr.directory_registry_id

        # 2. Organization
        session.execute(
            text(
                "INSERT INTO organization"
                " (directory_registry_id, fullname, shortname, inn, kpp, ogrn,"
                "  address, face, hidden, date_closing_period,"
                "  nds, can_sale, can_buy, print_check,"
                "  show_document_in_closing_period)"
                " VALUES"
                " (:dr_id, :fullname, :shortname, :inn, :kpp, :ogrn,"
                "  :address, :face, 0, :date_closing,"
                "  0, 1, 1, 1, 1)"
            ),
            {
                "dr_id": dr_id,
                "fullname": fullname,
                "shortname": sname,
                "inn": inn,
                "kpp": kpp,
                "ogrn": ogrn,
                "address": address,
                "face": face,
                "date_closing": _dt(2000, 1, 1),
            },
        )

        org_id = session.execute(
            text(
                "SELECT organization_id FROM organization"
                " WHERE directory_registry_id = :dr_id"
            ),
            {"dr_id": dr_id},
        ).scalar()

        # 3. Wallets (опционально)
        wallets_created = []
        for wname in wallet_names or []:
            session.execute(
                text(
                    "INSERT INTO wallet (name, organization_id) VALUES (:name, :org_id)"
                ),
                {"name": wname, "org_id": org_id},
            )
            wid = session.execute(
                text(
                    "SELECT MAX(wallet_id) FROM wallet WHERE organization_id = :org_id"
                ),
                {"org_id": org_id},
            ).scalar()
            wallets_created.append({"wallet_id": wid, "name": wname})

    return OrganizationInfo(
        {
            "organization_id": org_id,
            "fullname": fullname,
            "shortname": sname,
            "inn": inn,
            "kpp": kpp,
            "ogrn": ogrn,
            "address": address,
            "face": face,
            "hidden": 0,
        },
        wallets_created,
    )


# ---------------------------------------------------------------------------
# Комплексные работы (service_complex_work)
# ---------------------------------------------------------------------------


def iter_complex_works_by_tree(
    tree_id: int,
) -> "Generator[ServiceComplexWork, None, None]":
    """Генератор всех :class:`~autodealer.domain.service_complex_work.ServiceComplexWork`
    принадлежащих дереву ``tree_id``.

    Обходит ``service_complex_work_item`` → ``service_complex_work`` без загрузки
    всех записей в память сразу.

    Args:
        tree_id: ``service_complex_work_tree_id``.

    Yields:
        Экземпляры :class:`~autodealer.domain.service_complex_work.ServiceComplexWork`
        упорядоченные по ``(service_complex_work_item_id, position_number)``.

    Example::

        from autodealer.services import iter_complex_works_by_tree

        for work in iter_complex_works_by_tree(11):
            print(work.name, work.price)
    """

    from autodealer.domain.service_complex_work import ServiceComplexWork
    from autodealer.domain.service_complex_work_item import ServiceComplexWorkItem

    item_ids = [
        item.service_complex_work_item_id
        for item in ServiceComplexWorkItem.objects.filter(
            service_complex_work_tree_id=tree_id
        ).all()
    ]

    if not item_ids:
        return

    works = (
        ServiceComplexWork.objects.filter(service_complex_work_item_id__in=item_ids)
        .order_by("service_complex_work_item_id", "position_number")
        .all()
    )

    yield from works


# ---------------------------------------------------------------------------
# Каталог услуг (service_common_work)
# ---------------------------------------------------------------------------


def find_service_by_barcode(bar_code: str) -> Optional[int]:
    """Найти услугу в каталоге по bar_code. Возвращает service_common_work_id или None."""
    if not bar_code:
        return None
    with session_scope() as session:
        return session.execute(
            text(
                "SELECT service_common_work_id FROM service_common_work WHERE bar_code = :bc"
            ),
            {"bc": bar_code},
        ).scalar()


def get_or_create_service(
    name: str,
    price: Optional[float] = None,
    time_value: Optional[float] = None,
    bar_code: Optional[str] = None,
    tree_id: Optional[int] = None,
) -> int:
    """Найти услугу в каталоге по bar_code или создать новую.

    Args:
        name: Название услуги (обязательно).
        price: Цена по умолчанию.
        time_value: Длительность в минутах.
        bar_code: Уникальный ключ для идемпотентности (например ``rw:821460``).
        tree_id: FK → ``service_common_work_tree`` (папка в каталоге).

    Returns:
        ``service_common_work_id`` найденной или созданной записи.
    """
    with session_scope() as session:
        if bar_code:
            existing = session.execute(
                text(
                    "SELECT service_common_work_id FROM service_common_work"
                    " WHERE bar_code = :bc"
                ),
                {"bc": bar_code},
            ).scalar()
            if existing is not None:
                return existing

        session.execute(
            text(
                "INSERT INTO service_common_work"
                " (name, price, time_value, bar_code, service_common_work_tree_id)"
                " VALUES (:name, :price, :time_value, :bc, :tree_id)"
            ),
            {
                "name": name[:255],
                "price": price,
                "time_value": time_value,
                "bc": bar_code,
                "tree_id": tree_id,
            },
        )
        lookup = (
            "SELECT service_common_work_id FROM service_common_work WHERE bar_code = :bc"
            if bar_code
            else "SELECT MAX(service_common_work_id) FROM service_common_work WHERE name = :name"
        )
        params = {"bc": bar_code} if bar_code else {"name": name[:255]}
        return session.execute(text(lookup), params).scalar()


# ---------------------------------------------------------------------------
# Заказ-наряд с услугами
# ---------------------------------------------------------------------------

_DOCUMENT_TYPE_SERVICE_ORDER = 11  # «Заказ-наряд»


class ServiceOrderItem:
    """Одна строка услуги в заказ-наряде.

    Attributes:
        name: Название работы / услуги.
        price: Цена в рублях за единицу. При создании документа попадает
            в ``service_work.time_value`` — АвтоДилер для «ручных» записей
            (без привязки к справочнику) показывает цену именно из этого
            поля в сочетании с ``price_norm=1``.
        time_value: Длительность (минуты) — справочная информация, в БД
            **не сохраняется**: в таблице ``service_work`` нет отдельного
            поля под длительность. Оставлено в интерфейсе для совместимости
            и отладки.
        quantity: Количество. Умножается на цену при расчёте суммы документа.
        external_id: Внешний идентификатор (например, ``rw_service_id``).
            Сохраняется в ``service_work.external_id``.
    """

    def __init__(
        self,
        name: str,
        price: float,
        time_value: float = 0.0,
        quantity: int = 1,
        external_id: Optional[str] = None,
    ) -> None:
        self.name = name
        self.price = price
        self.time_value = time_value
        self.quantity = quantity
        self.external_id = external_id


class ServiceOrder:
    """Агрегат заказ-наряда: document_out + document_out_header + service_work строки.

    Используется для чтения существующих документов.
    Для создания — используй :func:`create_service_order`.

    Атрибуты:
        document_out_id: PK документа.
        client_id: FK клиента.
        summa: Итоговая сумма.
        date_accept: Дата/время приёма.
        date_payment: Дата оплаты.
        document_number: Номер документа из document_out_header.
        date_create: Дата создания из document_out_header.
        client_car: Привязанное авто (из document_service_detail).
        items: Список строк услуг (:class:`ServiceOrderItem`).
    """

    def __init__(self, row: dict, items: list[ServiceOrderItem]) -> None:
        self.document_out_id: int = row["document_out_id"]
        self.client_id: Optional[int] = row.get("client_id")
        self.summa: float = row.get("summa") or 0.0
        self.date_accept = row.get("date_accept")
        self.date_payment = row.get("date_payment")
        self.document_number: Optional[int] = row.get("document_number")
        self.date_create = row.get("date_create")
        self.client_car: Optional[int] = row.get("client_car")
        self.items: list[ServiceOrderItem] = items

    def __repr__(self) -> str:
        return (
            f"ServiceOrder(id={self.document_out_id}, client={self.client_id},"
            f" summa={self.summa}, items={len(self.items)})"
        )


def get_service_order(document_out_id: int) -> Optional["ServiceOrder"]:
    """Загрузить заказ-наряд со всеми строками услуг по document_out_id.

    Returns:
        :class:`ServiceOrder` или ``None`` если документ не найден.

    Example::

        order = get_service_order(42)
        if order:
            for item in order.items:
                print(item.name, item.price)
    """
    with session_scope() as session:
        doc = (
            session.execute(
                text(
                    "SELECT do2.document_out_id, do2.client_id, do2.summa,"
                    "       do2.date_accept, do2.date_payment,"
                    "       doh.number AS document_number, doh.date_create,"
                    "       dsd.client_car"
                    " FROM document_out do2"
                    " LEFT JOIN document_out_header doh"
                    "        ON doh.document_out_id = do2.document_out_id"
                    " LEFT JOIN document_service_detail dsd"
                    "        ON dsd.document_out_header_id = doh.document_out_header_id"
                    " WHERE do2.document_out_id = :doc_id"
                ),
                {"doc_id": document_out_id},
            )
            .mappings()
            .first()
        )

        if doc is None:
            return None

        works = (
            session.execute(
                text(
                    "SELECT name, price, time_value, quantity, external_id"
                    " FROM service_work"
                    " WHERE document_out_id = :doc_id"
                    " ORDER BY position_number"
                ),
                {"doc_id": document_out_id},
            )
            .mappings()
            .all()
        )

        items = [
            ServiceOrderItem(
                name=w["name"] or "",
                price=float(w["price"] or 0),
                time_value=float(w["time_value"] or 0),
                quantity=w["quantity"] or 1,
                external_id=w["external_id"],
            )
            for w in works
        ]

        return ServiceOrder(dict(doc), items)


def create_service_order(
    *,
    client_id: int,
    items: list[ServiceOrderItem],
    document_out_tree_id: int,
    organization_id: int,
    client_car: int,
    date_start: datetime,
    date_finish: datetime,
    created_by_user_id: int = _SYSTEM_USER_ID,
    notes: str | None = None,
    service_order_suffix: str | None = None,
) -> int:
    """Создать заказ-наряд с услугами для клиента.

    Создаёт цепочку:
    1. ``document_out``           — документ (Заказ-наряд, client_id, summa).
    2. ``document_out_header``    — заголовок (номер, дата, user_id).
    3. ``document_service_detail``— привязка авто (client_car), если передан.
    4. ``service_work`` × N      — строки услуг.

    Args:
        client_id: PK клиента в Firebird.
        items: Список услуг (:class:`ServiceOrderItem`).
        document_out_tree_id: Папка документов (FK → ``document_out_tree``).
        organization_id: FK организации.
        client_car: PK из ``model_link`` — обязательная привязка авто клиента.
        date_start: Дата/время приёма авто (начало работ).
        date_finish: Дата/время окончания работ.
        created_by_user_id: user_id исполнителя (записывается в ``document_out_header``).
        notes: Примечание к заказ-наряду.
        service_order_suffix: Суффикс номера документа.

    Returns:
        ``document_out_id`` созданного заказ-наряда.

    Raises:
        ValueError: Если ``items`` пустой или ``client_car`` не передан.

    Example::

        from autodealer.services import create_service_order, ServiceOrderItem
        doc_id = create_service_order(
            client_id=42,
            client_car=7,
            organization_id=1,
            document_out_tree_id=3,
            date_start=datetime.now(),
            date_finish=datetime.now() + timedelta(hours=1),
            items=[
                ServiceOrderItem("Экспресс мойка", price=600, time_value=20),
                ServiceOrderItem("Чернение резины", price=150, time_value=10),
            ],
        )
    """
    from datetime import datetime as _dt
    from autodealer.domain.document_out import DocumentOut
    from autodealer.domain.document_out_header import DocumentOutHeader
    from autodealer.domain.document_registry import DocumentRegistry
    from autodealer.domain.document_service_detail import DocumentServiceDetail
    from autodealer.domain.service_work import ServiceWork

    if not items:
        raise ValueError("items не может быть пустым")
    if client_car is None:
        raise ValueError(
            "client_car обязателен — заказ-наряд нельзя создать без"
            " привязки авто клиента (model_link_id)"
        )

    start_dt = date_start or _dt.now()
    finish_dt = date_finish or start_dt
    summa = sum(i.price * i.quantity for i in items)

    with session_scope() as session:
        # 1. document_out
        doc_out = DocumentOut(
            document_type_id=_DOCUMENT_TYPE_SERVICE_ORDER,
            client_id=client_id,
            summa=summa,
            date_accept=start_dt,
            organization_id=organization_id,
        )
        session.add(doc_out)
        session.flush()

        # 2. document_registry
        doc_reg = DocumentRegistry(
            metatable_id=_METATABLE_DOCUMENT_OUT,
            create_user_id=created_by_user_id,
            change_user_id=created_by_user_id,
            create_date=start_dt,
            change_date=start_dt,
            document_type_id_cache=_DOCUMENT_TYPE_SERVICE_ORDER,
        )
        session.add(doc_reg)
        session.flush()

        # 3. document_out_header
        next_number = session.execute(
            text(
                "SELECT MAX(number) + 1 FROM document_out_header WHERE document_type_id = :t"
            ),
            {"t": _DOCUMENT_TYPE_SERVICE_ORDER},
        ).scalar()

        doc_header = DocumentOutHeader(
            document_out_id=doc_out.document_out_id,
            document_type_id=_DOCUMENT_TYPE_SERVICE_ORDER,
            document_out_tree_id=document_out_tree_id,
            document_registry_id=doc_reg.document_registry_id,
            user_id=created_by_user_id,
            date_create=start_dt,
            notes=notes,
            number=next_number,
            suffix=service_order_suffix,
            prefix=_SERVICE_ORDER_PREFIX,
            state=_DOCUMENT_STATE["Черновик"],
        )
        session.add(doc_header)
        session.flush()

        # 4. document_service_detail — всегда создаём, привязка авто опциональна
        session.add(
            DocumentServiceDetail(
                document_out_header_id=doc_header.document_out_header_id,
                model_link_id=client_car,
                date_start=start_dt,
                summa_work=summa,
            )
        )

        # 5. service_work — строки услуг.
        # В АвтоДилере для «ручных» позиций (без rt_work_id/work_source) UI
        # отображает цену из поля time_value при price_norm=1, а не из price.
        # Длительность из ServiceOrderItem.time_value в БД не сохраняется —
        # модель service_work не содержит отдельного поля под «минуты работы».
        for pos, item in enumerate(items, 1):
            session.add(
                ServiceWork(
                    document_out_id=doc_out.document_out_id,
                    name=item.name,
                    time_value=item.price,
                    price_norm=1,
                    quantity=item.quantity,
                    position_number=pos,
                    external_id=item.external_id or None,
                )
            )

        document_out_id = doc_out.document_out_id

    return document_out_id


def delete_service_order(
    document_out_id: int,
    *,
    hard: bool = False,
) -> None:
    """Удалить заказ-наряд.

    **Soft-delete** (по умолчанию): ставит ``document_out_header.state = -1``
    («Удалён») — документ скрывается из UI АвтоДилера, но запись остаётся в БД.

    **Hard-delete** (``hard=True``): физически удаляет все связанные записи
    в обратном порядке создания:
    ``service_work`` → ``document_service_detail`` → ``document_out_header``
    → ``document_registry`` → ``document_out``.

    Перед удалением заказ-наряда автоматически сносятся все **ботовые**
    платежи (помеченные :data:`~autodealer.actions.payment.BOT_NOTE_MARKER`
    в ``payment.notes``) через :func:`~autodealer.actions.payment.delete_payment`.
    Если на документе висят **ручные** платежи (без маркера) — операция
    отказывает: их нужно обработать вручную.

    Args:
        document_out_id: PK заказ-наряда.
        hard: Если ``True`` — физическое удаление из БД.

    Raises:
        ValueError: Если заказ-наряд не найден; при ``hard=True`` также
            если к документу привязаны ручные (не ботовые) платежи.

    Example::

        from autodealer.services import delete_service_order

        delete_service_order(42)              # soft: state = -1
        delete_service_order(42, hard=True)   # полное удаление из БД
    """
    with session_scope() as session:
        header = (
            session.execute(
                text(
                    "SELECT document_out_header_id, document_registry_id"
                    " FROM document_out_header WHERE document_out_id = :id"
                ),
                {"id": document_out_id},
            )
            .mappings()
            .first()
        )

        if header is None:
            raise ValueError(
                f"Заказ-наряд document_out_id={document_out_id} не найден"
            )

        if not hard:
            session.execute(
                text(
                    "UPDATE document_out_header SET state = :state"
                    " WHERE document_out_id = :id"
                ),
                {"state": _DOCUMENT_STATE["Удалён"], "id": document_out_id},
            )
            return

        from autodealer.actions.payment import (
            BOT_NOTE_MARKER,
            _delete_payment_rows,
        )

        payments = session.execute(
            text(
                "SELECT p.payment_id, p.notes FROM payment_out po"
                " JOIN payment p ON p.payment_id = po.payment_id"
                " WHERE po.document_out_id = :id"
            ),
            {"id": document_out_id},
        ).all()

        bot_payment_ids: list[int] = []
        manual_payment_ids: list[int] = []
        for payment_id, notes in payments:
            if notes and BOT_NOTE_MARKER in notes:
                bot_payment_ids.append(payment_id)
            else:
                manual_payment_ids.append(payment_id)

        if manual_payment_ids:
            raise ValueError(
                f"Нельзя удалить заказ-наряд {document_out_id}:"
                f" есть ручные платежи {manual_payment_ids}."
                " Удали их вручную через delete_payment()."
            )

        for pid in bot_payment_ids:
            _delete_payment_rows(session, pid)

        session.execute(
            text("DELETE FROM service_work WHERE document_out_id = :id"),
            {"id": document_out_id},
        )
        session.execute(
            text(
                "DELETE FROM document_service_detail"
                " WHERE document_out_header_id = :hid"
            ),
            {"hid": header["document_out_header_id"]},
        )
        session.execute(
            text(
                "DELETE FROM document_out_header"
                " WHERE document_out_header_id = :hid"
            ),
            {"hid": header["document_out_header_id"]},
        )
        session.execute(
            text("DELETE FROM document_registry WHERE document_registry_id = :rid"),
            {"rid": header["document_registry_id"]},
        )
        session.execute(
            text("DELETE FROM document_out WHERE document_out_id = :id"),
            {"id": document_out_id},
        )


def restore_service_order(
    document_out_id: int,
    *,
    state: int = _DOCUMENT_STATE["Черновик"],
) -> None:
    """Восстановить soft-deleted заказ-наряд.

    Парная операция к :func:`delete_service_order` (с ``hard=False``):
    переводит ``document_out_header.state`` из ``-1`` («Удалён») обратно
    в рабочее состояние.

    Отказывает, если документ не найден или не находится в состоянии ``-1`` —
    чтобы случайно не понизить/поднять state живого документа.

    Args:
        document_out_id: PK заказ-наряда.
        state: Целевой ``state``. По умолчанию ``2`` («Черновик»).
            Можно передать ``4`` («Оформлен»), если нужно сразу
            восстановить документ как завершённый.

    Raises:
        ValueError: Если документ не найден или его ``state != -1``.

    Example::

        from autodealer.services import delete_service_order, restore_service_order

        delete_service_order(42)           # soft: state = -1
        restore_service_order(42)          # state = 2 (Черновик)
        restore_service_order(42, state=4) # state = 4 (Оформлен)
    """
    with session_scope() as session:
        current_state = session.execute(
            text(
                "SELECT state FROM document_out_header"
                " WHERE document_out_id = :id"
            ),
            {"id": document_out_id},
        ).scalar()

        if current_state is None:
            raise ValueError(
                f"Заказ-наряд document_out_id={document_out_id} не найден"
            )
        if current_state != _DOCUMENT_STATE["Удалён"]:
            raise ValueError(
                f"Заказ-наряд document_out_id={document_out_id} не в состоянии"
                f" «Удалён» (state={current_state}). Восстанавливать нечего."
            )

        session.execute(
            text(
                "UPDATE document_out_header SET state = :state"
                " WHERE document_out_id = :id"
            ),
            {"state": state, "id": document_out_id},
        )


def create_payment(
    *,
    document_out_id: int,
    summa: float,
    wallet_id: int,
    payment_type_id: int,
    payment_date: Optional[datetime] = None,
    notes: Optional[str] = None,
) -> int:
    """Создать документ оплаты для заказ-наряда.

    .. deprecated::
        Используй :func:`autodealer.actions.payment.create_payment`.
    """
    from autodealer.actions.payment import create_payment as _create_payment

    return _create_payment(
        document_out_id=document_out_id,
        summa=summa,
        wallet_id=wallet_id,
        payment_type_id=payment_type_id,
        payment_date=payment_date,
        notes=notes,
    )
