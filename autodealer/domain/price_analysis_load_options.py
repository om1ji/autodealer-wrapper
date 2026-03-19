"""SQLAlchemy 2.0 ORM model for the price_analysis_load_options table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PriceAnalysisLoadOptions(Base):
    __tablename__ = "price_analysis_load_options"

    price_analysis_load_options_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    option_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    config: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
