"""SQLAlchemy 2.0 ORM model for the document_pos_terminal table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentPosTerminal(Base):
    __tablename__ = "document_pos_terminal"

    document_pos_terminal_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    organization_device_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_device.organization_device_id"), nullable=True)
    operation_sum: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    operation_status: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    authorization_code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    reference_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    pan: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
