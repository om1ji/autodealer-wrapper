"""SQLAlchemy 2.0 ORM model for the directory_registry table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DirectoryRegistry(Base):
    __tablename__ = "directory_registry"

    directory_registry_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    metatable_id: Mapped[int] = mapped_column(Integer, nullable=False)
    create_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    create_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default="CURRENT_TIMESTAMP")
    change_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    change_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default="CURRENT_TIMESTAMP")
