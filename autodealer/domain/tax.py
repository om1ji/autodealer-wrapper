"""SQLAlchemy 2.0 ORM model for the tax table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Float, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Tax(Base):
    __tablename__ = "tax"

    tax_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tax_schemes_id: Mapped[int] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=False)
    nds: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False, server_default="0")
    k_nds: Mapped[float] = mapped_column(Float, nullable=False, server_default="0")
    tax_date: Mapped[date] = mapped_column(Date, nullable=False)
