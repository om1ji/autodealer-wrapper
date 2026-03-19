"""SQLAlchemy 2.0 ORM model for the bank_exchange table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class BankExchange(Base):
    __tablename__ = "bank_exchange"

    bank_exchange_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    incoming_document_key: Mapped[str] = mapped_column(String(512), nullable=False)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
