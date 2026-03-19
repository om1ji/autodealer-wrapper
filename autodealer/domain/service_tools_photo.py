"""SQLAlchemy 2.0 ORM model for the service_tools_photo table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceToolsPhoto(Base):
    __tablename__ = "service_tools_photo"

    service_tools_photo_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_tools_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_tools.service_tools_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
