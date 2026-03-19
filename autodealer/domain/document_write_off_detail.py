"""SQLAlchemy 2.0 ORM model for the document_write_off_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentWriteOffDetail(Base):
    __tablename__ = "document_write_off_detail"

    document_write_off_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_header_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out_header.document_out_header_id"), nullable=False)
    com_members: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    subject: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    solution: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    charge: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
