"""SQLAlchemy 2.0 ORM model for the cloud_parts_soft_user_client table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudPartsSoftUserClient(Base):
    __tablename__ = "cloud_parts_soft_user_client"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client.client_id"), primary_key=True)
    user_key: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
