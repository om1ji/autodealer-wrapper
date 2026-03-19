"""SQLAlchemy 2.0 ORM model for the mark table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Mark(Base):
    __tablename__ = "mark"

    mark_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
