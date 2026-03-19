"""SQLAlchemy 2.0 ORM model for the external_test_param table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ExternalTestParam(Base):
    __tablename__ = "external_test_param"

    external_test_param_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    symbol: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    color_value: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    cloud_upload_version: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    cloud_upload_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_change: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
