"""SQLAlchemy 2.0 ORM model for the planning_pattern_task table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PlanningPatternTask(Base):
    __tablename__ = "planning_pattern_task"

    planning_pattern_task_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_complex_work_item_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_complex_work_item.service_complex_work_item_id"), nullable=True)
    caption: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    caption_style: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    content: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    content_style: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    panel_style: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    content_pattern: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    notify_sound: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    alert_enabled: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    alert_minute: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="5")
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
