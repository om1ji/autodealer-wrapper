"""SQLAlchemy 2.0 ORM model for the diagnostic_document table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticDocument(Base):
    __tablename__ = "diagnostic_document"

    diagnostic_document_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    diagnostic_document_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("diagnostic_document_tree.diagnostic_document_tree_id"), nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
