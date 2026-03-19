"""SQLAlchemy 2.0 ORM model for the shop_price_group table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopPriceGroup(Base):
    __tablename__ = "shop_price_group"

    shop_price_group_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_price_list_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_price_list.shop_price_list_id"), nullable=False)
    group_position: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="1")
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_price_group.shop_price_group_id"), nullable=True)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
