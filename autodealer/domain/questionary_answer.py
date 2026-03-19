"""SQLAlchemy 2.0 ORM model for the questionary_answer table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class QuestionaryAnswer(Base):
    __tablename__ = "questionary_answer"

    questionary_answer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    questionary_question_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("questionary_question.questionary_question_id"), nullable=True)
    operation_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("operation.operation_id"), nullable=True)
    answer: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
