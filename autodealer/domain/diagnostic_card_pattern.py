"""SQLAlchemy 2.0 ORM model for the diagnostic_card_pattern table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardPattern(Base):
    __tablename__ = "diagnostic_card_pattern"

    diagnostic_card_pattern_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    card_version: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
