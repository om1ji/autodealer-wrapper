"""SQLAlchemy 2.0 ORM model for the external_files table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ExternalFiles(Base):
    __tablename__ = "external_files"

    external_files_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_dir_id: Mapped[int] = mapped_column(Integer, ForeignKey("external_dir.external_dir_id"), nullable=False)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    name_original: Mapped[str] = mapped_column(String(512), nullable=False)
    deleted: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
