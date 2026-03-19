"""SQLAlchemy 2.0 ORM model for the goods_move table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsMove(Base):
    __tablename__ = "goods_move"

    goods_move_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    goods_in_from: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=True)
    goods_in_to: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=True)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
