"""SQLAlchemy 2.0 ORM model for the price_analysis_view table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PriceAnalysisView(Base):
    __tablename__ = "price_analysis_view"

    price_analysis_view_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price_analysis_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_analysis_tree.price_analysis_tree_id"), nullable=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    provider_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    currency_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    price_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    price_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
