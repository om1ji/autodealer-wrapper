"""SQLAlchemy 2.0 ORM model for the document_planning_executor table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentPlanningExecutor(Base):
    __tablename__ = "document_planning_executor"

    document_planning_executor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_planning_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_planning.document_planning_id"), nullable=False)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    date_start: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    date_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    all_time: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    executor_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
