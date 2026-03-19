"""SQLAlchemy 2.0 ORM model for the identification_doc table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class IdentificationDoc(Base):
    __tablename__ = "identification_doc"

    identification_doc_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_link_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    identification_doc_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("identification_doc_type.identification_doc_type_id"), nullable=False)
    series: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    given_where: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    given_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    default_identification_doc: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
