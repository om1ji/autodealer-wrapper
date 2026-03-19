"""SQLAlchemy 2.0 ORM model for the calls_megafon_record table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CallsMegafonRecord(Base):
    __tablename__ = "calls_megafon_record"

    calls_megafon_record_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    calls_megafon_id: Mapped[int] = mapped_column(Integer, ForeignKey("calls_megafon.calls_megafon_id"), nullable=False)
    link: Mapped[str] = mapped_column(String(5000), nullable=False)
    call_id: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    ext: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    rating: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    status: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
