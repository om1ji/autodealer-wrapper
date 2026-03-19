"""SQLAlchemy 2.0 ORM model for the requisite table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Requisite(Base):
    __tablename__ = "requisite"

    requisite_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_link_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    bank_id: Mapped[int] = mapped_column(Integer, ForeignKey("bank.bank_id"), nullable=False)
    settle_account: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    default_requisite: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
