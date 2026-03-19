"""SQLAlchemy 2.0 ORM model for the payment table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Payment(Base):
    __tablename__ = "payment"

    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    payment_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment_type.payment_type_id"), nullable=False)
    payment_relation_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payment.payment_id"), nullable=True)
    payment_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    doc_number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    doc_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    summa: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    wallet_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    external_data: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    organization_sbp_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_sbp.organization_sbp_id"), nullable=True)
