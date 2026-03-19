"""SQLAlchemy 2.0 ORM model for the shop_nomenclature_packaging table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopNomenclaturePackaging(Base):
    __tablename__ = "shop_nomenclature_packaging"

    shop_nomenclature_packaging_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
    shop_nomenclature_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
