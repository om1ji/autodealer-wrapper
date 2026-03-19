"""SQLAlchemy 2.0 ORM model for the searching_phrase table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class SearchingPhrase(Base):
    __tablename__ = "searching_phrase"

    searching_phrase_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    phrase: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    periodicity_run: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    periodicity_day: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
