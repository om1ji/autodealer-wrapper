"""SQLAlchemy 2.0 ORM model for the document_return_cln_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentReturnClnDetail(Base):
    __tablename__ = "document_return_cln_detail"

    document_return_cln_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_header_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out_header.document_out_header_id"), nullable=True)
    reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    attorney_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    through_person: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    summa_work: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
