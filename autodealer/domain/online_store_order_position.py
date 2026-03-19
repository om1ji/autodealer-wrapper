"""SQLAlchemy 2.0 ORM model for the online_store_order_position table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OnlineStoreOrderPosition(Base):
    __tablename__ = "online_store_order_position"

    online_store_order_position_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    online_store_order_id: Mapped[int] = mapped_column(Integer, ForeignKey("online_store_order.online_store_order_id"), nullable=False)
    order_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("order_goods.order_goods_id"), nullable=True)
    goods_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=True)
    online_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    recalc_status: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    status: Mapped[int] = mapped_column(Integer, nullable=False)
