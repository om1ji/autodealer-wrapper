"""SQLAlchemy 2.0 ORM model for the accounting_tree table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AccountingTree(Base):
    __tablename__ = "accounting_tree"

    accounting_tree_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("accounting_tree.accounting_tree_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
