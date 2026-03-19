"""SQLAlchemy 2.0 ORM model for the document_planning_link table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentPlanningLink(Base):
    __tablename__ = "document_planning_link"

    document_planning_link_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_planning_id: Mapped[int] = mapped_column(Integer, nullable=False)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
