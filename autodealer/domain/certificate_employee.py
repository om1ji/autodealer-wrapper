"""SQLAlchemy 2.0 ORM model for the certificate_employee table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CertificateEmployee(Base):
    __tablename__ = "certificate_employee"

    certificate_employee_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    certificate_id: Mapped[int] = mapped_column(Integer, ForeignKey("certificate.certificate_id"), nullable=False)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=False)
    assign_date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
