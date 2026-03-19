"""SQLAlchemy 2.0 ORM model for the goods_in table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class GoodsIn(Base):
    __tablename__ = "goods_in"

    goods_in_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_in_old_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=True)
    goods_in_prev_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_in.goods_in_id"), nullable=True)
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey("store.store_id"), nullable=False)
    document_in_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_in.document_in_id"), nullable=False)
    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=False)
    unit_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=True)
    gtd_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    goods_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    cost1: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    cost2: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    goods_notes: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    is_saled: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    position_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
