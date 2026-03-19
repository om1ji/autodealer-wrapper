"""SQLAlchemy 2.0 ORM model for the operation_comment table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OperationComment(Base):
    __tablename__ = "operation_comment"

    operation_comment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    operation_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation.operation_id"), nullable=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
