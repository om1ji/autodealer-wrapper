"""SQLAlchemy 2.0 ORM model for the order_goods table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrderGoods(Base):
    __tablename__ = "order_goods"

    order_goods_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    goods_state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    goods_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    discount_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    date_delivery: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    cost_in: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    external_system_type: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    external_system_data: Mapped[Optional[str]] = mapped_column(String(32765), nullable=True)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
