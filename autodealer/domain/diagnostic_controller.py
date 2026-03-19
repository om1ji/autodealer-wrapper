"""SQLAlchemy 2.0 ORM model for the diagnostic_controller table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DiagnosticController(Base):
    __tablename__ = "diagnostic_controller"

    diagnostic_controller_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_structure_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_structure.organization_structure_id"), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    eaisto_login: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    eaisto_pass: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    number: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
