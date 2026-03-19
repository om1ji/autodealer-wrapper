"""SQLAlchemy 2.0 ORM model for the diagnostic_card_header table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticCardHeader(Base):
    __tablename__ = "diagnostic_card_header"

    diagnostic_card_header_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    diagnostic_card_id: Mapped[int] = mapped_column(Integer, ForeignKey("diagnostic_card.diagnostic_card_id"), nullable=False)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    document_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=True)
    state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="-1")
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    barcode: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    flag: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
