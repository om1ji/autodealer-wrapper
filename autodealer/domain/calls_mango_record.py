"""SQLAlchemy 2.0 ORM model for the calls_mango_record table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsMangoRecord(Base):
    __tablename__ = "calls_mango_record"

    calls_mango_record_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calls_mango_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls_mango.calls_mango_id"), nullable=False)
    recording_id: Mapped[str] = mapped_column(String(255), nullable=False)
