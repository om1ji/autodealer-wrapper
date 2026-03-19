"""SQLAlchemy 2.0 ORM model for the questionary_question table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class QuestionaryQuestion(Base):
    __tablename__ = "questionary_question"

    questionary_question_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    order_index: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("questionary_question.questionary_question_id"), nullable=True)
