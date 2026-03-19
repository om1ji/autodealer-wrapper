"""SQLAlchemy 2.0 ORM model for the client_tree table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ClientTree(Base):
    __tablename__ = "client_tree"

    client_tree_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client_tree.client_tree_id"), nullable=True, server_default="0")
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
