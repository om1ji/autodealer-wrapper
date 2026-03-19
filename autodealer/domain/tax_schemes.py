"""SQLAlchemy 2.0 ORM model for the tax_schemes table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class TaxSchemes(Base):
    __tablename__ = "tax_schemes"

    tax_schemes_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    frk_tax_kind: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="254")
    tax_system: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    current_version: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
