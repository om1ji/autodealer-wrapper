"""SQLAlchemy 2.0 ORM model for the cloud_common_param table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class CloudCommonParam(Base):
    __tablename__ = "cloud_common_param"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    manager_uploaded: Mapped[int] = mapped_column(SmallInteger, primary_key=True, server_default="0")
    board_config_uploaded: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
