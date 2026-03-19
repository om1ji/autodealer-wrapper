"""SQLAlchemy 2.0 ORM model for the planning_pattern_remind table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PlanningPatternRemind(Base):
    __tablename__ = "planning_pattern_remind"

    planning_pattern_remind_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    planning_pattern_task_id: Mapped[int] = mapped_column(Integer, ForeignKey("planning_pattern_task.planning_pattern_task_id"), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
