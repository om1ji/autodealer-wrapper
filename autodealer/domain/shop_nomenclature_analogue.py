"""SQLAlchemy 2.0 ORM model for the shop_nomenclature_analogue table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopNomenclatureAnalogue(Base):
    __tablename__ = "shop_nomenclature_analogue"

    shop_nomenclature_analogue_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
    shop_nomenclature_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
