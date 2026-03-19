"""SQLAlchemy 2.0 ORM model for the executor_planning table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime

from sqlalchemy import Date, DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ExecutorPlanning(Base):
    __tablename__ = "executor_planning"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    document_planning_executor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_planning_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    date_start: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    date_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    all_time: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    executor_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    executor_registry_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(94), nullable=True)
    birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    sex: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    hidden: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
