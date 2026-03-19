"""SQLAlchemy 2.0 ORM model for the shop_price_list table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopPriceList(Base):
    __tablename__ = "shop_price_list"

    shop_price_list_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    price_names: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    margin1: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin2: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin3: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin4: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin5: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin6: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin1_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=True)
    margin2_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=True)
    margin3_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=True)
    margin4_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=True)
    margin5_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=True)
    margin6_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=True)
