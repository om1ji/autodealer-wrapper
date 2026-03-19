"""SQLAlchemy 2.0 ORM model for the accounting_item table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AccountingItem(Base):
    __tablename__ = "accounting_item"

    accounting_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    accounting_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("accounting_tree.accounting_tree_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    accounting_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
