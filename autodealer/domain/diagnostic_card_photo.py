"""SQLAlchemy 2.0 ORM model for the diagnostic_card_photo table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardPhoto(Base):
    __tablename__ = "diagnostic_card_photo"

    diagnostic_card_photo_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    diagnostic_card_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card.diagnostic_card_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
