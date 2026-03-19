"""SQLAlchemy 2.0 ORM model for the clause table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Clause(Base):
    __tablename__ = "clause"

    clause_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    par1: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    par2: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    par3: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    par4: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    par5: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
