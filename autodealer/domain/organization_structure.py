"""SQLAlchemy 2.0 ORM model for the organization_structure table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrganizationStructure(Base):
    __tablename__ = "organization_structure"

    organization_structure_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    job_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("job.job_id"), nullable=True)
    department_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("department.department_id"), nullable=True)
    responsible_person_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    responsible_person_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    bookkeeper_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    diagnostic_executor_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    diagnostic_executor_reason: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
