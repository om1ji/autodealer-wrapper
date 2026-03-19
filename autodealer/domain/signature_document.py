"""SQLAlchemy 2.0 ORM model for the signature_document table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class SignatureDocument(Base):
    __tablename__ = "signature_document"

    signature_document_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    signature_id: Mapped[int] = mapped_column(Integer, ForeignKey("signature.signature_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    signature_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
