"""SQLAlchemy 2.0 ORM model for the service_complex_addon table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceComplexAddon(Base):
    __tablename__ = "service_complex_addon"

    service_complex_addon_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_complex_work_item_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_complex_work_item.service_complex_work_item_id"), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    cost: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    unit_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    discount_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    ac_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    audatex_uid: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
