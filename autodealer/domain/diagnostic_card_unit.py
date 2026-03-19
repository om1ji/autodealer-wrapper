"""SQLAlchemy 2.0 ORM model for the diagnostic_card_unit table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardUnit(Base):
    __tablename__ = "diagnostic_card_unit"

    diagnostic_card_unit_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("diagnostic_card_unit.diagnostic_card_unit_id"), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    card_version: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
