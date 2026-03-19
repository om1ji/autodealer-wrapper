"""SQLAlchemy 2.0 ORM model for the user_temporary table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class UserTemporary(Base):
    __tablename__ = "user_temporary"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    user_connection_id: Mapped[int] = mapped_column(Integer, primary_key=True, server_default="CURRENT_CONNECTION")
    sid: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    data: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
