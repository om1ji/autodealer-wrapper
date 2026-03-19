"""SQLAlchemy 2.0 ORM model for the calls_mango table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsMango(Base):
    __tablename__ = "calls_mango"

    calls_mango_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calls_register_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls_register.calls_register_id"), nullable=False)
    call_id: Mapped[str] = mapped_column(String(255), nullable=False)
    entry_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    seq: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    extension: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    call_status: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
