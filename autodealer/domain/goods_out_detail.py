"""SQLAlchemy 2.0 ORM model for the goods_out_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsOutDetail(Base):
    __tablename__ = "goods_out_detail"

    goods_out_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=True)
    goods_in_detail_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=True)
    goods_out_group_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=True)
