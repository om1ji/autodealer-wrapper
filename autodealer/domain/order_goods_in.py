"""SQLAlchemy 2.0 ORM model for the order_goods_in table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrderGoodsIn(Base):
    __tablename__ = "order_goods_in"

    order_goods_in_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    order_provider_document_id: Mapped[int] = mapped_column(Integer, ForeignKey("order_provider_document.order_provider_document_id"), nullable=False)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    goods_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    goods_state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    provider_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    external_system_type: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    external_system_data: Mapped[Optional[str]] = mapped_column(String(32765), nullable=True)
