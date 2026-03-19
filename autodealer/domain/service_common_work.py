"""SQLAlchemy 2.0 ORM model for the service_common_work table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceCommonWork(Base):
    __tablename__ = "service_common_work"

    service_common_work_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_common_work_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_common_work_tree.service_common_work_tree_id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    time_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    factor: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True, server_default="1")
    quantity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="1")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    brigade_executor_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("brigade_executor.brigade_executor_id"), nullable=True)
    price_norm_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_norm.price_norm_id"), nullable=True)
    bar_code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
