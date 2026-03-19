# autodealer — контекст проекта

## Что это

Python ORM-обёртка над базой данных системы **АвтоДилер** (Firebird).
Пакет: `autodealer/`. Версия: 0.0.1.

## База данных

- **Сервер**: 192.168.88.64:3050 (Windows, Firebird)
- **Тестовая**: `C:\Program Files (x86)\AutoDealer\AutoDealer\Database\StOm1.fdb`
- **User**: SYSDBA / masterkey
- **Charset**: UTF8
- `.env` сейчас указывает на `StOm1.fdb`

## Структура пакета

```
autodealer/
  connection.py       # DatabaseConfig, get_engine(), session_scope(), Base, configure_database()
  queryset.py         # QuerySet, Manager — Django-like ORM API (Model.objects.filter(...))
  __init__.py         # реэкспорт из connection.py
  domain/
    __init__.py       # авто-импорт всех 286 моделей
    bank.py           # пример: class Bank(Base)
    users.py          # ...
    ...               # по одному файлу на каждую таблицу StOm1.fdb
  tools/
    __init__.py
    generate_models.py  # интроспектирует БД и перегенерирует domain/
```

## Ключевые решения

- **Модели статичные** — генерируются один раз скриптом, не используют reflection при импорте
- **Стиль моделей** — SQLAlchemy 2.0, `Mapped[T]` / `mapped_column()` (Django-like явные поля)
- **QuerySet** — `Model.objects` — дескриптор `Manager` на `Base`, возвращает `QuerySet(Model)`
- **Типы Firebird** — sqlalchemy-firebird возвращает типы с префиксом `FB` (FBINTEGER, FBVARCHAR и т.д.) — в генераторе срезается через `.removeprefix("FB")`
- **Circular import** — `queryset.py` импортирует `session_scope`/`get_engine` лениво внутри методов; `Manager` навешивается на `Base` после определения обоих классов
- **GC warning** от драйвера Firebird при выходе — фиксится через `get_engine().dispose()` в `finally`

## Как перегенерировать модели

```bash
python autodealer/tools/generate_models.py
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

## Зависимости

- SQLAlchemy 2.0.44
- sqlalchemy-firebird 2.1
- firebird-driver 2.0.2
- python-dotenv 1.2.1
- Sphinx (документация)

## venv

```bash
source venv/bin/activate
```
