"""SQLAlchemy 2.0 ORM model for the price_analysis_filter table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PriceAnalysisFilter(Base):
    __tablename__ = "price_analysis_filter"

    price_analysis_filter_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shop_nomenclature_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature.shop_nomenclature_id"), nullable=True)
    use_search_mode: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    use_search_name: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    use_search_code: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    use_search_number: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    use_search_notes: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    use_search_word: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    use_search_date: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    search_date_start: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    search_date_end: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    filter_param: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    attrib_search: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
