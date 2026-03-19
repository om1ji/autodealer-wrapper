"""SQLAlchemy 2.0 ORM model for the department table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Department(Base):
    __tablename__ = "department"

    department_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
