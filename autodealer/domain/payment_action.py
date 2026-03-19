"""SQLAlchemy 2.0 ORM model for the payment_action table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PaymentAction(Base):
    __tablename__ = "payment_action"

    payment_action_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    payment_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
    payment_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payment_type.payment_type_id"), nullable=True)
    action_datetime: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    document_in_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_in.document_in_id"), nullable=True)
    directory_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    action_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    payment_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
