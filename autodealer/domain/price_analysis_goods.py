"""SQLAlchemy 2.0 ORM model for the price_analysis_goods table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PriceAnalysisGoods(Base):
    __tablename__ = "price_analysis_goods"

    price_analysis_goods_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=True)
    price_analysis_view_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_analysis_view.price_analysis_view_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number_original: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    cost1: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    cost2: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    cost3: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    cost4: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    cost5: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    cost6: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
