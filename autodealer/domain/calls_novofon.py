"""SQLAlchemy 2.0 ORM model for the calls_novofon table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsNovofon(Base):
    __tablename__ = "calls_novofon"

    calls_novofon_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calls_register_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls_register.calls_register_id"), nullable=False)
    pbx_call_id: Mapped[str] = mapped_column(String(255), nullable=False)
    is_recorded: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    internal: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    caller_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    called_did: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    destination: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    disposition: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    last_internal: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    status_code: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    call_id_with_rec: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    call_start: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    call_status: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    duration_str: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
