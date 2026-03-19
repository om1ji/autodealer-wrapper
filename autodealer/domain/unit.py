"""SQLAlchemy 2.0 ORM model for the unit table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Unit(Base):
    __tablename__ = "unit"

    unit_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    shortname: Mapped[str] = mapped_column(String(10), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    integer_value: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    code_okey: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
