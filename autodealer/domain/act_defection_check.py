"""SQLAlchemy 2.0 ORM model for the act_defection_check table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ActDefectionCheck(Base):
    __tablename__ = "act_defection_check"

    act_defection_check_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("act_defection_check.act_defection_check_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    check_all: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
