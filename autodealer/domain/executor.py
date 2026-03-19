"""SQLAlchemy 2.0 ORM model for the executor table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, Float, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Executor(Base):
    __tablename__ = "executor"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    brigade_structure_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brigade_executor_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    service_work_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    directory_registry_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    executor_registry_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    tariff: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    percent_exec_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    percent_work_party: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(94), nullable=True)
    birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    sex: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    hidden: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
