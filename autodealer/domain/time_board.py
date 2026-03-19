"""SQLAlchemy 2.0 ORM model for the time_board table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class TimeBoard(Base):
    __tablename__ = "time_board"

    time_board_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_structure_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_structure.organization_structure_id"), nullable=False)
    time_board_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("time_board_type.time_board_type_id"), nullable=True)
    time_board_date: Mapped[date] = mapped_column(Date, nullable=False)
    time_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
