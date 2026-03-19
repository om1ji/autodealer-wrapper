"""SQLAlchemy 2.0 ORM model for the action_goods_nomenclature table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ActionGoodsNomenclature(Base):
    __tablename__ = "action_goods_nomenclature"

    action_goods_nomenclature_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    action_goods_id: Mapped[int] = mapped_column(Integer, ForeignKey("action_goods.action_goods_id"), nullable=False)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
