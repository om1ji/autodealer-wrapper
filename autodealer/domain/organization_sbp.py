"""SQLAlchemy 2.0 ORM model for the organization_sbp table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrganizationSbp(Base):
    __tablename__ = "organization_sbp"

    organization_sbp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    wallet_id: Mapped[int] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    pos_id: Mapped[str] = mapped_column(String(255), nullable=False)
    api_key: Mapped[str] = mapped_column(String(255), nullable=False)
    active: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    provider: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    pos_hash: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
