"""SQLAlchemy 2.0 ORM model for the currency_rate table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CurrencyRate(Base):
    __tablename__ = "currency_rate"

    currency_rate_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    currency_main_id: Mapped[int] = mapped_column(Integer, ForeignKey("currency.currency_id"), nullable=False)
    currency_relation_id: Mapped[int] = mapped_column(Integer, ForeignKey("currency.currency_id"), nullable=False)
    rate: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    rate_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
