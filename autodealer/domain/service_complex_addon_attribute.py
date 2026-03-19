"""SQLAlchemy 2.0 ORM model for the service_complex_addon_attribute table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceComplexAddonAttribute(Base):
    __tablename__ = "service_complex_addon_attribute"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    service_complex_addon_id: Mapped[int] = mapped_column(Integer, ForeignKey("service_complex_addon.service_complex_addon_id"), primary_key=True)
