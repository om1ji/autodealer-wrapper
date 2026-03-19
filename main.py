"""Simple script that prints all rows from the BANK table."""

from __future__ import annotations

import logging
from pprint import pprint

from autodealer import configure_database

configure_database(
    database=r"C:\Program Files (x86)\AutoDealer\AutoDealer\Database\StOm1.fdb",
    user="SYSDBA",
    password="masterkey",
    host="192.168.88.64",
    port=3050,
    charset="UTF8",
)

from autodealer.domain.bank import Bank


def fetch_all_banks() -> list[dict[str, object]]:
    banks = Bank.objects.all()
    return [{col.name: getattr(b, col.name) for col in Bank.__table__.columns} for b in banks]


if __name__ == "__main__":
    try:
        pprint(fetch_all_banks())
    except Exception:
        logging.exception("Ошибка при чтении таблицы BANK")
    finally:
        # Явно закрываем соединение, чтобы избежать мусора GC от драйвера Firebird
        from autodealer import get_engine
        get_engine().dispose()
