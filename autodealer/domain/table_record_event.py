"""SQLAlchemy 2.0 ORM model for the table_record_event table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class TableRecordEvent(Base):
    __tablename__ = "table_record_event"

    table_record_event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    table_name: Mapped[str] = mapped_column(String(350), nullable=False)
    record_id: Mapped[int] = mapped_column(Integer, nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    action_name: Mapped[str] = mapped_column(String(255), nullable=False)
    event_data: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
