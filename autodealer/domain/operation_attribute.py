"""SQLAlchemy 2.0 ORM model for the operation_attribute table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OperationAttribute(Base):
    __tablename__ = "operation_attribute"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), primary_key=True)
