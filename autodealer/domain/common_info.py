"""SQLAlchemy 2.0 ORM model for the common_info table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CommonInfo(Base):
    __tablename__ = "common_info"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    current_version: Mapped[str] = mapped_column(String(10), primary_key=True)
    current_subversion: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    percent_pay_goods: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    percent_pay_works: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    mark_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    params: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    common_data: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sending_success: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    database_guid: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    bonus_notify_last_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    bonus_deadline: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
