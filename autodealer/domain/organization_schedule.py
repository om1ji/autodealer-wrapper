"""SQLAlchemy 2.0 ORM model for the organization_schedule table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import time

from sqlalchemy import ForeignKey, Integer, Time
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrganizationSchedule(Base):
    __tablename__ = "organization_schedule"

    organization_schedule_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    monday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    monday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    tuesday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    tuesday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    wednesday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    wednesday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    thursday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    thursday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    friday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    friday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    saturday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    saturday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    sunday_from: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    sunday_to: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
