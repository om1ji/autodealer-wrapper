"""SQLAlchemy 2.0 ORM model for the operation_link table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OperationLink(Base):
    __tablename__ = "operation_link"

    operation_link_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    operation_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
