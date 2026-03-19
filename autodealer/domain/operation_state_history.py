"""SQLAlchemy 2.0 ORM model for the operation_state_history table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OperationStateHistory(Base):
    __tablename__ = "operation_state_history"

    operation_state_history_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    history_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    operation_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation.operation_id"), nullable=True)
    operation_state_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation_state.operation_state_id"), nullable=True)
