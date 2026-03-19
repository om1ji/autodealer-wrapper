"""SQLAlchemy 2.0 ORM model for the document_registry table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, SmallInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentRegistry(Base):
    __tablename__ = "document_registry"

    document_registry_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    metatable_id: Mapped[int] = mapped_column(Integer, nullable=False)
    create_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    create_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default="CURRENT_TIMESTAMP")
    change_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    change_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default="CURRENT_TIMESTAMP")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    lock_user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
    cloud_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    cloud_upload_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    cloud_upload_version: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    document_type_id_cache: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=True)
