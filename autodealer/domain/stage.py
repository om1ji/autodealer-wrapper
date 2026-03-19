"""SQLAlchemy 2.0 ORM model for the stage table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Stage(Base):
    __tablename__ = "stage"

    stage_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    required: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    position_no: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    stage_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    visible_online: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    cloud_upload_version: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    cloud_upload_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_change: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
