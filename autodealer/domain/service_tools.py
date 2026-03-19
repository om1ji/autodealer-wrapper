"""SQLAlchemy 2.0 ORM model for the service_tools table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceTools(Base):
    __tablename__ = "service_tools"

    service_tools_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_tools_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_tools_tree.service_tools_tree_id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    inventory_number: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    given_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    last_employee_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    back_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    article: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    producer_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("producer.producer_id"), nullable=True)
    cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    directory_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=True)
    bar_code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
