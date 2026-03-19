"""SQLAlchemy 2.0 ORM model for the identification_doc_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class IdentificationDocType(Base):
    __tablename__ = "identification_doc_type"

    identification_doc_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
