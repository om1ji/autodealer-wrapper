"""SQLAlchemy 2.0 ORM model for the document_return_pvd_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentReturnPvdDetail(Base):
    __tablename__ = "document_return_pvd_detail"

    document_return_pvd_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_header_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out_header.document_out_header_id"), nullable=False)
    reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    attorney_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    through_person: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
