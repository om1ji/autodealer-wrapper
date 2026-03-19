"""SQLAlchemy 2.0 ORM model for the document_marking table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentMarking(Base):
    __tablename__ = "document_marking"

    document_marking_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    marking_goods_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("marking_goods_type.marking_goods_type_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    crpt_document_id: Mapped[str] = mapped_column(String(50), nullable=False)
    crpt_document_status: Mapped[str] = mapped_column(String(50), nullable=False)
    crpt_document_type: Mapped[str] = mapped_column(String(50), nullable=False)
    active: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    crpt_document_link_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    crpt_document_error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
