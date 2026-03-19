"""SQLAlchemy 2.0 ORM model for the cloud_shop_message table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudShopMessage(Base):
    __tablename__ = "cloud_shop_message"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    cloud_shop_message_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    message_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    message_text: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
