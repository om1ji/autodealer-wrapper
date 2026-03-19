"""SQLAlchemy 2.0 ORM model for the video_registration table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class VideoRegistration(Base):
    __tablename__ = "video_registration"

    video_registration_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    regno: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    normalized_regno: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    camera: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    date_in: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    photo_in: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    date_out: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    photo_out: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    state: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    tmp: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
