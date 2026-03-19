"""SQLAlchemy 2.0 ORM model for the operation_remind table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OperationRemind(Base):
    __tablename__ = "operation_remind"

    operation_remind_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    operation_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation.operation_id"), nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
