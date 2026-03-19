"""SQLAlchemy 2.0 ORM model for the service_tools_attribute table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceToolsAttribute(Base):
    __tablename__ = "service_tools_attribute"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    directory_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), primary_key=True)
