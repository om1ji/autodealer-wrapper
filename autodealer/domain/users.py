"""SQLAlchemy 2.0 ORM model for the users table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    user_right: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    user_lock: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    force_logout: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    force_logout_computer: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
