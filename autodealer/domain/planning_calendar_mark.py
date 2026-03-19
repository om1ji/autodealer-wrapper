"""SQLAlchemy 2.0 ORM model for the planning_calendar_mark table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PlanningCalendarMark(Base):
    __tablename__ = "planning_calendar_mark"

    planning_calendar_mark_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calendar_mark_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    shape: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    color: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
