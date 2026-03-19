"""SQLAlchemy 2.0 ORM model for the document_planning_remind table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentPlanningRemind(Base):
    __tablename__ = "document_planning_remind"

    document_planning_remind_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_planning_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_planning.document_planning_id"), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
