"""SQLAlchemy 2.0 ORM model for the ac_basket_group table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class AcBasketGroup(Base):
    __tablename__ = "ac_basket_group"

    ac_basket_group_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("ac_basket_group.ac_basket_group_id"), nullable=True, server_default="0")
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
