"""SQLAlchemy 2.0 ORM model for the ac_bookmark table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AcBookmark(Base):
    __tablename__ = "ac_bookmark"

    ac_bookmark_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    mark_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    ac_mark_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    model_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    tree_name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    ac_doc_id: Mapped[int] = mapped_column(Integer, nullable=False)
    uid: Mapped[int] = mapped_column(Integer, nullable=False)
    detail_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    detail_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
