"""SQLAlchemy 2.0 ORM model for the common_config table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from datetime import date

from sqlalchemy import Date, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CommonConfig(Base):
    __tablename__ = "common_config"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    update_current_rest_last_date: Mapped[date] = mapped_column(Date, primary_key=True)
    order_organization_ignore: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
