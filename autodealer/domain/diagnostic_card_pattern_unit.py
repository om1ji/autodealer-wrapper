"""SQLAlchemy 2.0 ORM model for the diagnostic_card_pattern_unit table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardPatternUnit(Base):
    __tablename__ = "diagnostic_card_pattern_unit"

    diagnostic_card_pattern_unit_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    diagnostic_card_unit_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card_unit.diagnostic_card_unit_id"), nullable=False)
    diagnostic_card_pattern_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card_pattern.diagnostic_card_pattern_id"), nullable=False)
    check1: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    check2: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
