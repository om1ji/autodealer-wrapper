"""High-level service functions for AutoDealer domain operations.

These functions wrap multi-step ORM inserts into single atomic calls,
hiding the directory_registry / trigger bookkeeping from the caller.
"""

from __future__ import annotations

from datetime import date
from typing import Optional


from sqlalchemy import text

from autodealer.connection import session_scope
from autodealer.domain.client import Client
from autodealer.domain.directory_registry import DirectoryRegistry
from autodealer.domain.model_detail import ModelDetail
from autodealer.domain.model_link import ModelLink

# metatable_id=1 → ORGANIZATION
_METATABLE_ORGANIZATION = 1
# metatable_id=3 → CLIENT
_METATABLE_CLIENT = 3
# metatable_id=4 → MODEL_DETAIL (справочник autodealer)
_METATABLE_MODEL_DETAIL = 4
# Системный пользователь по умолчанию
_SYSTEM_USER_ID = 1
# client_tree_id=1 — «Физические лица»
_CLIENT_TREE_PHYSICAL = 1


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
# Клиенты
# ---------------------------------------------------------------------------


def find_client_by_phone(phone: str) -> Optional[int]:
    """Найти клиента по номеру телефона (поле mobile в contact).

    Возвращает ``client_id`` или ``None`` если не найден.

    Example::

        client_id = find_client_by_phone("79991697059")
    """
    if not phone:
        return None
    with session_scope() as session:
        dr_id = session.execute(
            text(
                "SELECT c.directory_registry_link_id FROM contact c"
                " WHERE c.mobile = :phone AND c.hidden = 0"
                " ROWS 1"
            ),
            {"phone": phone},
        ).scalar()
        if dr_id is None:
            return None
        return session.execute(
            text("SELECT client_id FROM client WHERE directory_registry_id = :dr_id"),
            {"dr_id": dr_id},
        ).scalar()


def create_client(
    fullname: str,
    *,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    birth: Optional[date] = None,
    sex: Optional[int] = None,
    discount: float = 0.0,
    discount_work: float = 0.0,
    client_tree_id: int = _CLIENT_TREE_PHYSICAL,
    created_by_user_id: int = _SYSTEM_USER_ID,
) -> int:
    """Создать клиента в Firebird.

    Атомарно создаёт цепочку:
    ``DirectoryRegistry (metatable=3)`` → ``Client`` → ``Contact`` (если есть phone/email).

    Args:
        fullname: Полное имя клиента (обязательно).
        phone: Мобильный телефон.
        email: Email.
        birth: Дата рождения.
        sex: 1=муж, 2=жен, None=не указан.
        discount: Скидка на товары %.
        discount_work: Скидка на работы %.
        client_tree_id: Папка клиентов (1=Физлица, 2=Юрлица, 3=VIP).
        created_by_user_id: Пользователь-создатель.

    Returns:
        ``client_id`` созданного клиента.

    Example::

        from datetime import date
        from autodealer.services import create_client

        client_id = create_client(
            "Иванов Иван Иванович",
            phone="79991234567",
            email="ivan@example.com",
            birth=date(1990, 5, 15),
            sex=1,
            discount=5.0,
        )
    """
    shortname = fullname[:30]

    with session_scope() as session:
        # 1. DirectoryRegistry
        dr = DirectoryRegistry(
            metatable_id=_METATABLE_CLIENT,
            create_user_id=created_by_user_id,
            change_user_id=created_by_user_id,
        )
        session.add(dr)
        session.flush()
        dr_id = dr.directory_registry_id

        # 2. Client
        session.execute(
            text(
                "INSERT INTO client"
                " (directory_registry_id, client_tree_id, fullname, shortname,"
                "  face, hidden, discount, discount_work, sex, birth)"
                " VALUES"
                " (:dr_id, :tree_id, :fullname, :shortname,"
                "  0, 0, :discount, :discount_work, :sex, :birth)"
            ),
            {
                "dr_id": dr_id,
                "tree_id": client_tree_id,
                "fullname": fullname,
                "shortname": shortname,
                "discount": discount,
                "discount_work": discount_work,
                "sex": sex,
                "birth": birth,
            },
        )
        client_id = session.execute(
            text("SELECT client_id FROM client WHERE directory_registry_id = :dr_id"),
            {"dr_id": dr_id},
        ).scalar()

        # 3. Contact (если есть phone или email)
        if phone or email:
            session.execute(
                text(
                    "INSERT INTO contact"
                    " (directory_registry_link_id, mobile, email,"
                    "  default_contact, hidden, face)"
                    " VALUES (:dr_id, :mobile, :email, 1, 0, 0)"
                ),
                {"dr_id": dr_id, "mobile": phone, "email": email},
            )

    return client_id


def add_vehicle_to_client(
    client_id: int,
    make: str,
    model_name: str,
    *,
    regno: Optional[str] = None,
    vin: Optional[str] = None,
    year: Optional[int] = None,
    color: Optional[str] = None,
    default_car: bool = False,
    created_by_user_id: int = _SYSTEM_USER_ID,
) -> int:
    """Добавить автомобиль клиенту по имени марки и модели.

    Автоматически находит или создаёт ``mark``, ``model``, ``color``,
    затем создаёт ``model_detail`` + ``model_link``.

    Идемпотентность: если машина с таким ``regno`` уже существует в БД —
    возвращает существующий ``model_detail_id`` без создания дубликата.

    Args:
        client_id: PK клиента в Firebird.
        make: Марка («Toyota», «BMW»).
        model_name: Модель («Camry», «X5»).
        regno: Госномер.
        vin: VIN-номер.
        year: Год выпуска (например 2020).
        color: Цвет строкой («Белый», «Чёрный»).
        default_car: Пометить как основное авто клиента.
        created_by_user_id: Пользователь-создатель.

    Returns:
        ``model_detail_id`` созданного или уже существующего автомобиля.

    Example::

        from autodealer.services import add_vehicle_to_client

        md_id = add_vehicle_to_client(
            client_id=42,
            make="Toyota",
            model_name="Camry",
            regno="А001ВС77",
            year=2020,
            color="Белый",
            default_car=True,
        )
    """
    # Проверяем дубликат по госномеру
    if regno:
        existing = find_vehicle_by_regno(regno)
        if existing is not None:
            return existing

    mark_id = get_or_create_mark(make)
    model_id = get_or_create_model(mark_id, model_name)
    color_id = get_or_create_color(color) if color else None
    year_date = date(year, 1, 1) if year else None

    link = create_vehicle_for_client(
        client_id=client_id,
        model_id=model_id,
        regno=regno,
        vin=vin,
        year_of_production=year_date,
        color_id=color_id,
        default_car=default_car,
        created_by_user_id=created_by_user_id,
    )
    return link.model_detail_id


def get_or_create_mark(name: str) -> int:
    """Найти марку по имени или создать новую. Возвращает mark_id."""
    # raw SQL: ORM filter на String-полях бьёт баг sqlalchemy-firebird render_bind_cast
    with session_scope() as session:
        existing = session.execute(
            text("SELECT mark_id FROM mark WHERE name = :name"), {"name": name}
        ).scalar()
        if existing is not None:
            return existing
        session.execute(
            text("INSERT INTO mark (name, hidden) VALUES (:name, 0)"), {"name": name}
        )
        return session.execute(
            text("SELECT mark_id FROM mark WHERE name = :name"), {"name": name}
        ).scalar()


def get_or_create_model(mark_id: int, model_name: str) -> int:
    """Найти модель по марке и имени или создать новую. Возвращает model_id."""
    with session_scope() as session:
        existing = session.execute(
            text(
                "SELECT model_id FROM model WHERE mark_id = :mark_id AND name = :name"
            ),
            {"mark_id": mark_id, "name": model_name},
        ).scalar()
        if existing is not None:
            return existing
        session.execute(
            text(
                "INSERT INTO model (mark_id, name, hidden) VALUES (:mark_id, :name, 0)"
            ),
            {"mark_id": mark_id, "name": model_name},
        )
        return session.execute(
            text(
                "SELECT model_id FROM model WHERE mark_id = :mark_id AND name = :name"
            ),
            {"mark_id": mark_id, "name": model_name},
        ).scalar()


def get_or_create_color(name: str) -> Optional[int]:
    """Найти цвет по имени или создать новый. Возвращает color_id или None если name пустой."""
    if not name:
        return None
    with session_scope() as session:
        existing = session.execute(
            text("SELECT color_id FROM color WHERE name = :name"), {"name": name}
        ).scalar()
        if existing is not None:
            return existing
        session.execute(
            text("INSERT INTO color (name, hidden) VALUES (:name, 0)"), {"name": name}
        )
        return session.execute(
            text("SELECT color_id FROM color WHERE name = :name"), {"name": name}
        ).scalar()


def find_vehicle_by_regno(regno: str) -> Optional[int]:
    """Найти автомобиль по госномеру. Возвращает model_detail_id или None."""
    if not regno:
        return None
    # Используем raw SQL чтобы обойти баг sqlalchemy-firebird visit_VARCHAR
    with session_scope() as session:
        return session.execute(
            text("SELECT model_detail_id FROM model_detail WHERE regno = :regno"),
            {"regno": regno},
        ).scalar()


def find_vehicle_by_vin(vin: str) -> Optional[int]:
    """Найти автомобиль по VIN. Возвращает model_detail_id или None."""
    if not vin:
        return None
    with session_scope() as session:
        return session.execute(
            text("SELECT model_detail_id FROM model_detail WHERE vin = :vin"),
            {"vin": vin},
        ).scalar()


def create_vehicle_for_client(
    *,
    client_id: int,
    model_id: int,
    vin: Optional[str] = None,
    regno: Optional[str] = None,
    year_of_production: Optional[date] = None,
    color_id: Optional[int] = None,
    car_engine_type_id: Optional[int] = None,
    car_gearbox_type_id: Optional[int] = None,
    car_body_type_id: Optional[int] = None,
    car_fuel_type_id: Optional[int] = None,
    engine_number: Optional[str] = None,
    chassis: Optional[str] = None,
    body: Optional[str] = None,
    notes: Optional[str] = None,
    default_car: bool = False,
    created_by_user_id: int = _SYSTEM_USER_ID,
) -> ModelLink:
    """Create a vehicle and attach it to a client.

    Performs three inserts in a single transaction:
    1. ``directory_registry`` — audit record for the new model_detail.
    2. ``model_detail``       — the specific vehicle (VIN, regno, specs).
    3. ``model_link``         — the link between the vehicle and the client.

    Args:
        client_id: PK of the client who owns the vehicle.
        model_id: PK of the make/model (e.g. Toyota Camry → ``model.model_id``).
        vin: Vehicle identification number.
        regno: State registration plate (госномер).
        year_of_production: Year/date of manufacture.
        color_id: FK to ``color`` table.
        car_engine_type_id: FK to ``car_engine_type``.
        car_gearbox_type_id: FK to ``car_gearbox_type``.
        car_body_type_id: FK to ``car_body_type``.
        car_fuel_type_id: FK to ``car_fuel_type``.
        engine_number: Engine serial number.
        chassis: Chassis number.
        body: Body number.
        notes: Free-text notes.
        default_car: If ``True``, marks this as the client's primary vehicle.
        created_by_user_id: User performing the operation (written to
            ``directory_registry``). Defaults to the system user (id=1).

    Returns:
        The newly created :class:`~autodealer.domain.model_link.ModelLink`
        instance (detached from session).

    Raises:
        ValueError: If the client with ``client_id`` does not exist.

    Example:
        >>> from autodealer.services import create_vehicle_for_client
        >>> link = create_vehicle_for_client(
        ...     client_id=100,
        ...     model_id=7,          # Audi A3
        ...     vin="WAUZZZ8P9BA012345",
        ...     regno="А001ВС77",
        ...     default_car=True,
        ... )
        >>> print(link.model_link_id)
    """
    with session_scope() as session:
        client = session.get(Client, client_id)
        if client is None:
            raise ValueError(f"Client with id={client_id} does not exist.")

        client_directory_registry_id = client.directory_registry_id
        session.expunge(client)

    # --- Step 1: directory_registry для model_detail ---
    dir_reg = DirectoryRegistry.objects.create(
        metatable_id=_METATABLE_MODEL_DETAIL,
        create_user_id=created_by_user_id,
        change_user_id=created_by_user_id,
    )

    # --- Step 2: model_detail ---
    detail_fields: dict = dict(
        model_id=model_id,
        directory_registry_id=dir_reg.directory_registry_id,
    )
    optional = dict(
        vin=vin,
        regno=regno,
        year_of_production=year_of_production,
        color_id=color_id,
        car_engine_type_id=car_engine_type_id,
        car_gearbox_type_id=car_gearbox_type_id,
        car_body_type_id=car_body_type_id,
        car_fuel_type_id=car_fuel_type_id,
        engine_number=engine_number,
        chassis=chassis,
        body=body,
        notes=notes,
    )
    detail_fields.update({k: v for k, v in optional.items() if v is not None})
    model_detail = ModelDetail.objects.create(**detail_fields)

    # --- Step 3: model_link (привязка к клиенту) ---
    model_link = ModelLink.objects.create(
        model_detail_id=model_detail.model_detail_id,
        directory_registry_link_id=client_directory_registry_id,
        default_car=1 if default_car else 0,
    )

    return model_link


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
    """Одна строка услуги в заказ-наряде."""

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
        model_link_id: Привязанное авто (из document_service_detail).
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
        self.model_link_id: Optional[int] = row.get("model_link_id")
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
                    "       dsd.model_link_id"
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
    model_link_id: Optional[int] = None,
    date_accept: Optional[object] = None,
    created_by_user_id: int = _SYSTEM_USER_ID,
) -> int:
    """Создать заказ-наряд с услугами для клиента.

    Создаёт цепочку:
    1. ``document_out``           — документ (Заказ-наряд, client_id, summa).
    2. ``document_out_header``    — заголовок (номер, дата, user_id).
    3. ``document_service_detail``— привязка авто (model_link_id), если передан.
    4. ``service_work`` × N      — строки услуг.

    Args:
        client_id: PK клиента в Firebird.
        items: Список услуг (:class:`ServiceOrderItem`).
        model_link_id: PK из ``model_link`` — привязка конкретного авто к документу.
        date_accept: Дата/время приёма авто (``datetime``). По умолчанию — сейчас.
        created_by_user_id: user_id исполнителя (записывается в ``document_out_header``).

    Returns:
        ``document_out_id`` созданного заказ-наряда.

    Example::

        from autodealer.services import create_service_order, ServiceOrderItem
        doc_id = create_service_order(
            client_id=42,
            model_link_id=7,
            items=[
                ServiceOrderItem("Экспресс мойка", price=600, time_value=20),
                ServiceOrderItem("Чернение резины", price=150, time_value=10),
            ],
        )
    """
    from datetime import datetime as _dt

    if not items:
        raise ValueError("items не может быть пустым")

    accept_dt = date_accept or _dt.now()
    summa = sum(i.price * i.quantity for i in items)

    with session_scope() as session:
        # 1. document_out
        session.execute(
            text(
                "INSERT INTO document_out"
                " (document_type_id, client_id, summa, date_accept)"
                " VALUES (:doc_type, :client_id, :summa, :date_accept)"
            ),
            {
                "doc_type": _DOCUMENT_TYPE_SERVICE_ORDER,
                "client_id": client_id,
                "summa": summa,
                "date_accept": accept_dt,
            },
        )
        document_out_id = session.execute(
            text(
                "SELECT MAX(document_out_id) FROM document_out"
                " WHERE document_type_id = :doc_type AND client_id = :client_id"
            ),
            {"doc_type": _DOCUMENT_TYPE_SERVICE_ORDER, "client_id": client_id},
        ).scalar()

        # 2. document_out_header
        session.execute(
            text(
                "INSERT INTO document_out_header"
                " (document_out_id, document_type_id, user_id, date_create)"
                " VALUES (:doc_out_id, :doc_type, :user_id, :date_create)"
            ),
            {
                "doc_out_id": document_out_id,
                "doc_type": _DOCUMENT_TYPE_SERVICE_ORDER,
                "user_id": created_by_user_id,
                "date_create": accept_dt,
            },
        )

        # 3. document_service_detail (привязка авто, опционально)
        if model_link_id is not None:
            doh_id = session.execute(
                text(
                    "SELECT document_out_header_id FROM document_out_header"
                    " WHERE document_out_id = :doc_out_id"
                ),
                {"doc_out_id": document_out_id},
            ).scalar()
            session.execute(
                text(
                    "INSERT INTO document_service_detail"
                    " (document_out_header_id, model_link_id)"
                    " VALUES (:doh_id, :model_link_id)"
                ),
                {"doh_id": doh_id, "model_link_id": model_link_id},
            )

        # 4. service_work — строки услуг
        for pos, item in enumerate(items, 1):
            params: dict = {
                "doc_out_id": document_out_id,
                "name": item.name,
                "price": item.price,
                "time_value": item.time_value,
                "quantity": item.quantity,
                "pos": pos,
            }
            if item.external_id:
                session.execute(
                    text(
                        "INSERT INTO service_work"
                        " (document_out_id, name, price, time_value, quantity,"
                        "  position_number, external_id)"
                        " VALUES (:doc_out_id, :name, :price, :time_value, :quantity,"
                        "  :pos, :ext_id)"
                    ),
                    {**params, "ext_id": item.external_id},
                )
            else:
                session.execute(
                    text(
                        "INSERT INTO service_work"
                        " (document_out_id, name, price, time_value, quantity,"
                        "  position_number)"
                        " VALUES (:doc_out_id, :name, :price, :time_value, :quantity,"
                        "  :pos)"
                    ),
                    params,
                )

    return document_out_id
