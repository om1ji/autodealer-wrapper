"""SQLAlchemy 2.0 ORM model for the user_store_right table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class UserStoreRight(Base):
    __tablename__ = "user_store_right"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), primary_key=True)
    store_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("store.store_id"), nullable=True)
    store_right: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
