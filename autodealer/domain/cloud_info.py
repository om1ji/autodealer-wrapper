"""SQLAlchemy 2.0 ORM model for the cloud_info table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudInfo(Base):
    __tablename__ = "cloud_info"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    config: Mapped[str] = mapped_column(Text, primary_key=True)
