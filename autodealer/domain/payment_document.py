"""SQLAlchemy 2.0 ORM model for the payment_document table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PaymentDocument(Base):
    __tablename__ = "payment_document"

    payment_document_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    payment_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment.payment_id"), nullable=False)
