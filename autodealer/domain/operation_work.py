"""SQLAlchemy 2.0 ORM model for the operation_work table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OperationWork(Base):
    __tablename__ = "operation_work"

    operation_work_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    operation_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation.operation_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    discount_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    time_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    factor: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True, server_default="1")
    quantity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="1")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price_norm: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_work_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    rt_work_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    work_source: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    service_work_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_work.service_work_id"), nullable=True)
    external_id: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
