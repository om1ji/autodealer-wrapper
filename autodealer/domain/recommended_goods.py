"""SQLAlchemy 2.0 ORM model for the recommended_goods table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class RecommendedGoods(Base):
    __tablename__ = "recommended_goods"

    recommended_goods_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model_detail_id: Mapped[int] = mapped_column(Integer, ForeignKey("model_detail.model_detail_id"), nullable=False)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
