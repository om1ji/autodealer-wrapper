"""SQLAlchemy 2.0 ORM model for the service_calculation_goods table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceCalculationGoods(Base):
    __tablename__ = "service_calculation_goods"

    service_calculation_goods_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_calculation_item_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_calculation_item.service_calculation_item_id"), nullable=True)
    shop_nomenclature_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    cost: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False, server_default="0")
    discount_fix: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
