"""SQLAlchemy 2.0 ORM model for the dynamic_margin_range table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DynamicMarginRange(Base):
    __tablename__ = "dynamic_margin_range"

    dynamic_margin_range_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dynamic_margin_id: Mapped[int] = mapped_column(Integer, ForeignKey("dynamic_margin.dynamic_margin_id"), nullable=False)
    range_from: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    range_to: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    margin: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    round_to: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
