"""SQLAlchemy 2.0 ORM model for the goods_out_alloc_order table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsOutAllocOrder(Base):
    __tablename__ = "goods_out_alloc_order"

    goods_out_alloc_order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_out_id: Mapped[int] = mapped_column(Integer, nullable=False)
    order_goods_id: Mapped[int] = mapped_column(Integer, ForeignKey("order_goods.order_goods_id"), nullable=False)
    alloc_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
