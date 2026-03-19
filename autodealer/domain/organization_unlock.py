"""SQLAlchemy 2.0 ORM model for the organization_unlock table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrganizationUnlock(Base):
    __tablename__ = "organization_unlock"

    organization_id: Mapped[int] = mapped_column(Integer, primary_key=True)
