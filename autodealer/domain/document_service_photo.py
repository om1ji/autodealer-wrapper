"""SQLAlchemy 2.0 ORM model for the document_service_photo table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentServicePhoto(Base):
    __tablename__ = "document_service_photo"

    document_service_photo: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_service_detail_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_service_detail.document_service_detail_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    hash: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
