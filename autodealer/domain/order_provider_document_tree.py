"""SQLAlchemy 2.0 ORM model for the order_provider_document_tree table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrderProviderDocumentTree(Base):
    __tablename__ = "order_provider_document_tree"

    order_provider_document_tree_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("order_provider_document_tree.order_provider_document_tree_id"), nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    style: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    node_position: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
