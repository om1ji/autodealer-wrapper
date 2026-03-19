"""SQLAlchemy 2.0 ORM model for the signature table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Signature(Base):
    __tablename__ = "signature"

    signature_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    require_complete: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
