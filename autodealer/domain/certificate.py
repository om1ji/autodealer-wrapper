"""SQLAlchemy 2.0 ORM model for the certificate table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Certificate(Base):
    __tablename__ = "certificate"

    certificate_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    certificate_type: Mapped[str] = mapped_column(String(20), nullable=False)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    subject: Mapped[str] = mapped_column(String(512), nullable=False)
    issuer: Mapped[str] = mapped_column(String(512), nullable=False)
    valid_from: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    valid_to: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    thumbprint: Mapped[str] = mapped_column(String(100), nullable=False)
    serial_no: Mapped[str] = mapped_column(String(100), nullable=False)
    public_key_alg: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    sign_alg: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    csp_provider_name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
