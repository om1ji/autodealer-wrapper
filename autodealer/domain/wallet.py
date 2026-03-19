"""SQLAlchemy 2.0 ORM model for the wallet table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Wallet(Base):
    __tablename__ = "wallet"

    wallet_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization.organization_id"), nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
