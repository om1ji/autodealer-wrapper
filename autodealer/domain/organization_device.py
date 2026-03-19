"""SQLAlchemy 2.0 ORM model for the organization_device table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrganizationDevice(Base):
    __tablename__ = "organization_device"

    organization_device_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    server_addr: Mapped[str] = mapped_column(String(255), nullable=False)
    server_port: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    device_id: Mapped[str] = mapped_column(String(255), nullable=False)
    device_type: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    manufacturer: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    manufacturer_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    wallet_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=True)
