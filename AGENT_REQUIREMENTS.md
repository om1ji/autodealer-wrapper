# Требования к агенту-парсеру для создания заказ-наряда

## Что должен передать агент для создания заказ-наряда

### 1. Клиент (обязательно)

Нужно **одно из двух**: найти существующего или создать нового.

| Поле | Тип | Обяз. | Примечание |
|---|---|---|---|
| `phone` | `str` | **да** | Ключ для поиска существующего клиента |
| `fullname` | `str` | **да** | Имя — для создания нового |
| `email` | `str` | нет | |

---

### 2. Автомобиль (обязательно)

Нужно найти существующий или создать новый. Результат — `model_link_id`.

| Поле | Тип | Обяз. | Примечание |
|---|---|---|---|
| `regno` | `str` | **да** | Госномер — ключ для поиска (`find_vehicle_by_regno`) |
| `vin` | `str` | нет | Альтернативный ключ поиска |
| `make` | `str` | нет | Марка — нужна при создании нового авто («Toyota») |
| `model_name` | `str` | нет | Модель — нужна при создании («Camry») |
| `year` | `int` | нет | Год выпуска |
| `color` | `str` | нет | Цвет строкой |

---

### 3. Услуги (обязательно, минимум одна)

| Поле | Тип | Обяз. | Примечание |
|---|---|---|---|
| `name` | `str` | **да** | Название услуги |
| `price` | `float` | **да** | Цена за единицу |
| `quantity` | `int` | нет | По умолчанию 1 |
| `time_value` | `float` | нет | Длительность в минутах |
| `external_id` | `str` | нет | ID услуги во внешней системе |

---

### 4. Параметры заказ-наряда

| Поле | Тип | Обяз. | Примечание |
|---|---|---|---|
| `date_start` | `datetime` | **да** | Дата и время приёма авто |
| `date_finish` | `datetime` | **да** | Дата и время окончания работ |
| `organization_id` | `int` | **да** | Константа для конкретной точки |
| `document_out_tree_id` | `int` | **да** | Папка заказ-нарядов (константа) |
| `notes` | `str` | нет | Примечание к заказ-наряду |
| `service_order_suffix` | `str` | нет | Суффикс номера («К», «М» и т.п.) |

---

## Порядок действий агента

```
1. Найти клиента по phone → если нет → create_client(fullname, phone)
2. Найти авто по regno/vin → если нет → add_vehicle_to_client(client_id, make, model_name, regno, ...)
3. Получить model_link_id → get_client_vehicles(client_id)[0].model_link_id
4. create_service_order(client_id, client_car=model_link_id, items=[...], ...)
```

---

## Минимальный набор данных (JSON-пример)

```json
{
  "client": {
    "phone": "79991234567",
    "fullname": "Иванов Иван"
  },
  "car": {
    "regno": "А001ВС77",
    "make": "Toyota",
    "model_name": "Camry"
  },
  "order": {
    "date_start": "2026-04-14T10:00:00",
    "date_finish": "2026-04-14T11:00:00",
    "organization_id": 1,
    "document_out_tree_id": 3,
    "notes": "Комплексная мойка"
  },
  "items": [
    { "name": "Мойка кузова", "price": 600.0, "time_value": 20 },
    { "name": "Чернение резины", "price": 150.0, "time_value": 10 }
  ]
}
```

---

## Функции ORM для каждого шага

```python
from autodealer.actions.client import (
    create_client,
    add_vehicle_to_client,
    get_client_vehicles,
    find_vehicle_by_regno,
    find_vehicle_by_vin,
)
from autodealer.services import create_service_order, ServiceOrderItem
from sqlalchemy import text
from autodealer.connection import session_scope

# 1. Найти клиента по телефону
with session_scope() as session:
    client = session.execute(
        text("SELECT client_id FROM contact c "
             "JOIN directory_registry dr ON dr.directory_registry_id = c.directory_registry_link_id "
             "JOIN client cl ON cl.directory_registry_id = dr.directory_registry_id "
             "WHERE c.mobile = :phone"),
        {"phone": phone}
    ).scalar()

# 2. Найти авто по госномеру
model_detail_id = find_vehicle_by_regno(regno)

# 3. Получить model_link_id
links = get_client_vehicles(client_id)
model_link_id = links[0].model_link_id

# 4. Создать заказ-наряд
doc_id = create_service_order(
    client_id=client_id,
    client_car=model_link_id,
    organization_id=1,
    document_out_tree_id=3,
    date_start=date_start,
    date_finish=date_finish,
    notes=notes,
    items=[
        ServiceOrderItem(name="Мойка кузова", price=600.0, time_value=20),
    ],
)
```
