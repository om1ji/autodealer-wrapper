"""SQLAlchemy 2.0 ORM model for the order_alloc_order_in table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrderAllocOrderIn(Base):
    __tablename__ = "order_alloc_order_in"

    order_alloc_order_in_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_goods_in_id: Mapped[int] = mapped_column(Integer, ForeignKey("order_goods_in.order_goods_in_id"), nullable=False)
    order_goods_id: Mapped[int] = mapped_column(Integer, ForeignKey("order_goods.order_goods_id"), nullable=False)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
