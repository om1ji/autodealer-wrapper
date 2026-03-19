"""SQLAlchemy 2.0 ORM model for the shop_price table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopPrice(Base):
    __tablename__ = "shop_price"

    shop_price_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_price_group_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_price_group.shop_price_group_id"), nullable=True)
    shop_price_list_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_price_list.shop_price_list_id"), nullable=False)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    price_position: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="1")
    price1: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    price2: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    price3: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    price4: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    price5: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    price6: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
