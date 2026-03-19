"""SQLAlchemy 2.0 ORM model for the service_work_manager_structure table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceWorkManagerStructure(Base):
    __tablename__ = "service_work_manager_structure"

    manager_structure_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_work_id: Mapped[int] = mapped_column(Integer, ForeignKey("service_work.service_work_id"), nullable=False)
    manager_id: Mapped[int] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=False)
    percent_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    tariff: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    party: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
