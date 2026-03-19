"""SQLAlchemy 2.0 ORM model for the document_stage table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentStage(Base):
    __tablename__ = "document_stage"

    document_stage_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    stage_id: Mapped[int] = mapped_column(Integer, ForeignKey("stage.stage_id"), nullable=False)
    manager_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    is_current: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    stage_value: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
