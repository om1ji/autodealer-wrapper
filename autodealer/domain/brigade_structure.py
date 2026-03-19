"""SQLAlchemy 2.0 ORM model for the brigade_structure table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class BrigadeStructure(Base):
    __tablename__ = "brigade_structure"

    brigade_structure_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brigade_executor_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("brigade_executor.brigade_executor_id"), nullable=True)
    percent_work_party: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    percent_exec_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    tariff: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    service_work_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_work.service_work_id"), nullable=True)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
