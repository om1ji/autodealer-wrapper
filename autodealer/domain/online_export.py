"""SQLAlchemy 2.0 ORM model for the online_export table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OnlineExport(Base):
    __tablename__ = "online_export"

    # WARNING: No primary key in schema — first column used as pseudo-PK
    online_export_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    export_state_data: Mapped[str] = mapped_column(Text, nullable=False)
