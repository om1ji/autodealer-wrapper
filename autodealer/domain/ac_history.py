"""SQLAlchemy 2.0 ORM model for the ac_history table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AcHistory(Base):
    __tablename__ = "ac_history"

    ac_history_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    history_date: Mapped[date] = mapped_column(Date, nullable=False)
    mark_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    ac_mark_id: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    model_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    map: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    tree_name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    ac_doc_id: Mapped[int] = mapped_column(Integer, nullable=False)
    uid: Mapped[int] = mapped_column(Integer, nullable=False)
