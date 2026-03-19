"""SQLAlchemy 2.0 ORM model for the calls_uiscom_record table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsUiscomRecord(Base):
    __tablename__ = "calls_uiscom_record"

    calls_uiscom_record_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calls_uiscom_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls_uiscom.calls_uiscom_id"), nullable=False)
    link: Mapped[str] = mapped_column(String(5000), nullable=False)
    call_id: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    ext: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
