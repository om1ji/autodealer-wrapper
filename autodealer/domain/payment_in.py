"""SQLAlchemy 2.0 ORM model for the payment_in table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PaymentIn(Base):
    __tablename__ = "payment_in"

    payment_in_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_in_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_in.document_in_id"), nullable=False)
    payment_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment.payment_id"), nullable=False)
