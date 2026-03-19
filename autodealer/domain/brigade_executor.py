"""SQLAlchemy 2.0 ORM model for the brigade_executor table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class BrigadeExecutor(Base):
    __tablename__ = "brigade_executor"

    brigade_executor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
