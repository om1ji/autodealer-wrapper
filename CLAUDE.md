# autodealer — контекст проекта

## Что это

Python ORM-обёртка над базой данных системы **АвтоДилер** (Firebird).
Пакет: `autodealer/`. Версия: 0.1.0.

## База данных

- **Сервер**: 192.168.88.64:3050 (Windows, Firebird)
- **Тестовая**: `C:\Program Files (x86)\AutoDealer\AutoDealer\Database\StOm1.fdb`
- **User**: SYSDBA / masterkey
- **Charset**: UTF8

## Структура пакета

```
autodealer/
  __init__.py         # реэкспорт из connection.py
  connection.py       # DatabaseConfig, get_engine(), session_scope(), Base, configure_database()
  queryset.py         # QuerySet, Manager — Django-like ORM API (Model.objects.filter(...))
  services.py         # create_service_order, get_service_order, get/create organization, ...
  actions/
    __init__.py
    client.py         # create_client, add_vehicle_to_client, get_client_vehicles,
                      # create_vehicle_for_client, get_or_create_mark/model/color, ...
    payment.py        # create_payment, create_payment_split, get_payments,
                      # get_wallets, get_payment_types, WalletInfo, PaymentTypeInfo, ...
  domain/
    __init__.py       # авто-импорт всех 288 моделей
    bank.py           # пример: class Bank(Base)
    ...               # по одному файлу на каждую таблицу StOm1.fdb
  integration/
    __init__.py
    rocketwash.py     # маппинг RocketWash → AutoDealer (service_id → complex_work,
                      # car_type_id → категория, resolve mapped services)
  tools/
    __init__.py
    generate_models.py   # интроспектирует БД и перегенерирует domain/
    seed_test_db.py      # заполняет StOm1.fdb тестовыми данными (идемпотентно)
```

## Ключевые решения

- **Модели статичные** — генерируются один раз скриптом, не используют reflection при импорте
- **Стиль моделей** — SQLAlchemy 2.0, `Mapped[T]` / `mapped_column()` (Django-like явные поля)
- **QuerySet** — `Model.objects` — дескриптор `Manager` на `Base`, возвращает `QuerySet(Model)`
- **Типы Firebird** — sqlalchemy-firebird возвращает типы с префиксом `FB` (FBINTEGER, FBVARCHAR и т.д.) — в генераторе срезается через `.removeprefix("FB")`
- **Circular import** — `queryset.py` импортирует `session_scope`/`get_engine` лениво внутри методов; `Manager` навешивается на `Base` после определения обоих классов
- **GC warning** от драйвера Firebird при выходе — фиксится через `get_engine().dispose()` в `finally`

## Запуск

```bash
uv run python main.py
```

## Как перегенерировать модели

```bash
uv run python autodealer/tools/generate_models.py
```

Перезаписывает все файлы в `autodealer/domain/`.

## QuerySet API (кратко)

```python
Bank.objects.all()
Bank.objects.filter(hidden=0).order_by('-name').limit(10)
Bank.objects.filter(name__icontains='сбер').first()
Bank.objects.get(bank_id=1)
Bank.objects.create(name='...', bik='...')
Bank.objects.filter(hidden=1).update(hidden=0)
Bank.objects.filter(hidden=1).delete()
Bank.objects.values('bank_id', 'name')
```

## High-level функции (`services.py`, `actions/`)

### Заказ-наряд (`services.py`)

`client_car` — **обязательный** параметр: заказ-наряд нельзя создать без привязки авто клиента.

```python
from autodealer.services import create_service_order, ServiceOrderItem

doc_id = create_service_order(
    client_id=920,
    organization_id=1,
    document_out_tree_id=3,              # папка «АвтоМойка»
    date_start=now,
    date_finish=now + timedelta(hours=1),
    client_car=959,                      # model_link_id — ОБЯЗАТЕЛЬНО
    notes="Комплексная мойка",
    service_order_suffix="К",
    items=[ServiceOrderItem("Мойка", price=600.0, time_value=20)],
)
```

Цепочка в БД:
`document_out` → `document_registry` → `document_out_header` → `document_service_detail` (всегда, `model_link_id` + `date_start` + `summa_work`) → `service_work × N`.

Ключевые поля:
- `document_out.date_accept` = `date_start` (дата приёма авто)
- `document_out_header.date_create` = `date_start`
- `document_service_detail.date_start` = `date_start`
- `document_service_detail.summa_work` = сумма всех позиций
- `document_out_header.state` = 2 («Черновик»)

### Оплата заказ-наряда (`actions/payment.py`)

```python
from autodealer.actions.payment import (
    get_wallets, get_payment_types, get_payments,
    create_payment, create_payment_split, PaymentSplitItem,
)

wallets = get_wallets(organization_id=1)        # list[WalletInfo]
types   = get_payment_types()                   # list[PaymentTypeInfo]

payment_id = create_payment(
    document_out_id=doc_id,
    summa=2300.0,
    wallet_id=1,        # 1=Наличный расчет, 3=Сбербанк, 4=ТБанк
    payment_type_id=1,  # 1=Наличный, 2=Безналичный, 7=Банковская карта
)

ids = create_payment_split(
    document_out_id=doc_id,
    parts=[
        PaymentSplitItem(wallet_id=1, payment_type_id=1, summa=1000.0),
        PaymentSplitItem(wallet_id=4, payment_type_id=7, summa=1300.0),
    ],
)

payments = get_payments(doc_id)                 # list[PaymentRecord]
```

Цепочка: `payment` → `payment_out` + `payment_document` + `money_document_detail` (accounting_item_id=3 «Поступление от клиента») + `money_document_payment` + `UPDATE document_out.date_payment`.

### Клиенты и авто (`actions/client.py`)

```python
from autodealer.actions.client import create_client, add_vehicle_to_client, get_client_vehicles

client_id = create_client("Иванов Иван", phone="79991234567")
add_vehicle_to_client(client_id, make="Toyota", model_name="Camry", regno="А001ВС77")
cars = get_client_vehicles(client_id)  # list[ModelLink]
```

`add_vehicle_to_client` возвращает `model_detail_id`.
`get_client_vehicles` возвращает `list[ModelLink]` — у каждого есть `.model_link_id` (нужен для `client_car`).

### Организации (`services.py`)

```python
from autodealer.services import get_organization, list_organizations, create_organization

org = get_organization(1)           # OrganizationInfo | None
orgs = list_organizations()         # list[OrganizationInfo]

org = create_organization(
    "ООО СК-Авто",
    shortname="СК-Авто",
    inn="1655012345",
    wallet_names=["Наличные", "Банковская карта"],
)
```

## Зависимости

- SQLAlchemy ≥ 2.0
- sqlalchemy-firebird ≥ 2.1
- firebird-driver ≥ 2.0
- python-dotenv ≥ 1.0
- Sphinx ≥ 8.0 (документация)
