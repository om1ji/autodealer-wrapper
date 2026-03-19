"""SQLAlchemy 2.0 ORM model for the money_document_payment table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class MoneyDocumentPayment(Base):
    __tablename__ = "money_document_payment"

    money_document_payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    money_document_detail_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("money_document_detail.money_document_detail_id"), nullable=True)
    payment_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payment.payment_id"), nullable=True)
