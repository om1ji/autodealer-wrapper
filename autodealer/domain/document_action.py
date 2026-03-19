"""SQLAlchemy 2.0 ORM model for the document_action table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentAction(Base):
    __tablename__ = "document_action"

    document_action_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
    action_datetime: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
