"""SQLAlchemy 2.0 ORM model for the inspection_car_image table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, LargeBinary, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class InspectionCarImage(Base):
    __tablename__ = "inspection_car_image"

    inspection_car_image_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    picture: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    cloud_upload_version: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    cloud_upload_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_change: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
