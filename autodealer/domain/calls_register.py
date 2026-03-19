"""SQLAlchemy 2.0 ORM model for the calls_register table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsRegister(Base):
    __tablename__ = "calls_register"

    calls_register_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    employee_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    compantion_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    call_status: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    call_direction: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    handled: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    notification_required: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    telephone_type: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    extension: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    records_available: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
