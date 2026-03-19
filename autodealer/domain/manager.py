"""SQLAlchemy 2.0 ORM model for the manager table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Manager(Base):
    __tablename__ = "manager"

    manager_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_structure_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_structure.organization_structure_id"), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    percent_exec: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    tariff: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    percent_goods: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
