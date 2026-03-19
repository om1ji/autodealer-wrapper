"""SQLAlchemy 2.0 ORM model for the goods_reject table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsReject(Base):
    __tablename__ = "goods_reject"

    goods_reject_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    order_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("order_goods.order_goods_id"), nullable=True)
