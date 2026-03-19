"""SQLAlchemy 2.0 ORM model for the todolist table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Todolist(Base):
    __tablename__ = "todolist"

    todolist_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    task_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    allocated_to: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    priority: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    status: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    create_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    complete: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    complete_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    completion: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
