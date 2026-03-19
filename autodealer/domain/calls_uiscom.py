"""SQLAlchemy 2.0 ORM model for the calls_uiscom table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsUiscom(Base):
    __tablename__ = "calls_uiscom"

    calls_uiscom_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calls_register_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls_register.calls_register_id"), nullable=False)
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    call_id: Mapped[str] = mapped_column(String(255), nullable=False)
    sub_call_id: Mapped[str] = mapped_column(String(255), nullable=False)
    extension: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    raw_event_data: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    call_status: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
