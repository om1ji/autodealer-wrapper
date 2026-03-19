# autodealer

Python ORM-обёртка над базой данных системы АвтоДилер (Firebird).

## Установка

```bash
pip install -r requirements.txt
```

На macOS также нужен клиент Firebird:
```bash
brew install firebird
```

---

## Настройка подключения

### Через `.env`

```env
DB_HOST=192.168.88.64
DB_PORT=3050
DB_DATABASE=C:\Program Files (x86)\AutoDealer\AutoDealer\Database\StOm1.fdb
DB_USER=SYSDBA
DB_PASSWORD=masterkey
DB_CHARSET=UTF8
```

### Или явно в коде

```python
from autodealer.connection import configure_database

configure_database(
    host="192.168.88.64",
    port=3050,
    database=r"C:\Program Files (x86)\AutoDealer\AutoDealer\Database\StOm1.fdb",
    user="SYSDBA",
    password="masterkey",
    charset="UTF8",
)
```

> `configure_database` нужно вызвать **до** импорта моделей, если `.env` не используется.

---

## Модели

Каждая таблица БД представлена отдельным классом в `autodealer/domain/`.
Имена полей совпадают с именами колонок в БД (строчные).

```python
from autodealer.domain.bank import Bank
from autodealer.domain.users import Users
# или всё сразу:
from autodealer.domain import Bank, Users
```

Посмотреть список колонок модели:

```python
print(Bank.__table__.columns.keys())
# ['bank_id', 'name', 'bik', 'korr_account', 'address', 'notes', 'hidden']
```

---

## QuerySet API

Каждая модель имеет менеджер `objects` с Django-подобным интерфейсом.

### Чтение

```python
# Все записи
banks = Bank.objects.all()

# Количество
Bank.objects.count()

# Первый / последний
Bank.objects.first()
Bank.objects.last()

# Проверка существования
Bank.objects.exists()
```

### Фильтрация

```python
# Точное совпадение
Bank.objects.filter(hidden=0)
Bank.objects.exclude(hidden=1)

# Цепочки
Bank.objects.filter(hidden=0).order_by('name').limit(10)
```

#### Поддерживаемые лукапы

| Лукап | SQL |
|---|---|
| `field=value` / `field__exact=value` | `= value` |
| `field__contains="текст"` | `LIKE %текст%` |
| `field__icontains="текст"` | `ILIKE %текст%` |
| `field__startswith="А"` | `LIKE А%` |
| `field__endswith="ов"` | `LIKE %ов` |
| `field__gt=5` | `> 5` |
| `field__gte=5` | `>= 5` |
| `field__lt=5` | `< 5` |
| `field__lte=5` | `<= 5` |
| `field__in=[1, 2, 3]` | `IN (1, 2, 3)` |
| `field__isnull=True` | `IS NULL` |

### Сортировка и пагинация

```python
# ASC / DESC (префикс -)
Bank.objects.order_by('name')
Bank.objects.order_by('-name')

# Пагинация
Bank.objects.limit(20).offset(40)
```

### get() — одна запись

```python
from autodealer.queryset import DoesNotExist, MultipleObjectsReturned

try:
    bank = Bank.objects.get(bank_id=1)
except DoesNotExist:
    print("Не найдено")
except MultipleObjectsReturned:
    print("Найдено несколько записей")
```

### values() — список словарей

```python
# Все поля
Bank.objects.all().values()

# Только нужные поля
Bank.objects.filter(hidden=0).values('bank_id', 'name')
# [{'bank_id': 1, 'name': 'Сбербанк'}, ...]
```

### Запись

```python
# Создание
bank = Bank.objects.create(name="Тинькофф", bik="044525974", hidden=0)
print(bank.bank_id)  # ID присвоен после сохранения

# Bulk update
Bank.objects.filter(hidden=1).update(hidden=0)

# Bulk delete
Bank.objects.filter(hidden=1).delete()
```

### Итерация

```python
for bank in Bank.objects.filter(hidden=0):
    print(bank.name)
```

---

## Low-level: session_scope

Для сложных запросов, транзакций или операций с несколькими моделями:

```python
from sqlalchemy import select
from autodealer.connection import session_scope
from autodealer.domain.bank import Bank

with session_scope() as session:
    result = session.execute(
        select(Bank).where(Bank.hidden == 0).order_by(Bank.name)
    ).scalars().all()
```

---

## Генерация моделей

Модели генерируются автоматически из схемы живой БД:

```bash
python autodealer/tools/generate_models.py
```

Скрипт подключается к БД, интроспектирует все таблицы и создаёт (перезаписывает) файлы в `autodealer/domain/`. Запускать при изменении схемы БД.
