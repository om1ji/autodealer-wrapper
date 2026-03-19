"""SQLAlchemy 2.0 ORM model for the planning_work_place table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PlanningWorkPlace(Base):
    __tablename__ = "planning_work_place"

    planning_work_place_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    picture: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    allow_cross_task: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    brigade_executor_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("brigade_executor.brigade_executor_id"), nullable=True)
    color: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    task_time_lenght: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
