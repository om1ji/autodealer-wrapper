"""SQLAlchemy 2.0 ORM model for the store table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Store(Base):
    __tablename__ = "store"

    store_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("store.store_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_for_sale: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    fullname: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_for_abcp: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
