"""SQLAlchemy 2.0 ORM model for the time_board_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class TimeBoardType(Base):
    __tablename__ = "time_board_type"

    time_board_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    color: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    time_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
