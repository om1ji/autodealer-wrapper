"""SQLAlchemy 2.0 ORM model for the diagnostic_card_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardDetail(Base):
    __tablename__ = "diagnostic_card_detail"

    diagnostic_card_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    diagnostic_card_unit_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card_unit.diagnostic_card_unit_id"), nullable=False)
    diagnostic_card_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card.diagnostic_card_id"), nullable=False)
    check1: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    check2: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
