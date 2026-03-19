"""SQLAlchemy 2.0 ORM model for the online_store_order_document table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OnlineStoreOrderDocument(Base):
    __tablename__ = "online_store_order_document"

    online_store_order_document_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    online_store_order_id: Mapped[int] = mapped_column(Integer, ForeignKey("online_store_order.online_store_order_id"), nullable=False)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    recalc_status: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
