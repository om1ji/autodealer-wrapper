"""SQLAlchemy 2.0 ORM model for the organization_numerator table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrganizationNumerator(Base):
    __tablename__ = "organization_numerator"

    organization_numerator_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    enabled: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    period: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
