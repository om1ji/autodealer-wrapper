"""SQLAlchemy 2.0 ORM model for the planning_view table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PlanningView(Base):
    __tablename__ = "planning_view"

    planning_view_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    view_param: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
