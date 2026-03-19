"""SQLAlchemy 2.0 ORM model for the payment_out table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PaymentOut(Base):
    __tablename__ = "payment_out"

    payment_out_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    payment_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment.payment_id"), nullable=False)
