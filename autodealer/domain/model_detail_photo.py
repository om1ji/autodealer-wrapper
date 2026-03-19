"""SQLAlchemy 2.0 ORM model for the model_detail_photo table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ModelDetailPhoto(Base):
    __tablename__ = "model_detail_photo"

    model_detail_photo_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model_detail_id: Mapped[int] = mapped_column(Integer, ForeignKey("model_detail.model_detail_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
