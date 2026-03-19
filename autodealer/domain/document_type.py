"""SQLAlchemy 2.0 ORM model for the document_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentType(Base):
    __tablename__ = "document_type"

    document_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    shortname: Mapped[str] = mapped_column(String(10), nullable=False)
    flag: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    payment_direction: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    accounting_system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
