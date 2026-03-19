"""SQLAlchemy 2.0 ORM model for the goods_in_alloc_order_in table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsInAllocOrderIn(Base):
    __tablename__ = "goods_in_alloc_order_in"

    goods_in_alloc_order_in_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_goods_in_id: Mapped[int] = mapped_column(Integer, ForeignKey("order_goods_in.order_goods_in_id"), nullable=False)
    goods_in_id: Mapped[int] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=False)
    alloc_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
