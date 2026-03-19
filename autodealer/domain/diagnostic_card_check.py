"""SQLAlchemy 2.0 ORM model for the diagnostic_card_check table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardCheck(Base):
    __tablename__ = "diagnostic_card_check"

    diagnostic_card_check_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    diagnostic_card_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card.diagnostic_card_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    limit_upper: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    limit_lower: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    check_value: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    aggregate: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    unit_number: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    check_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
