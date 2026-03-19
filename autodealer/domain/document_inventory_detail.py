"""SQLAlchemy 2.0 ORM model for the document_inventory_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentInventoryDetail(Base):
    __tablename__ = "document_inventory_detail"

    document_inventory_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_header_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out_header.document_out_header_id"), nullable=True)
    shop_material_response_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_material_response.shop_material_response_id"), nullable=True)
    store_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("store.store_id"), nullable=True)
    reason: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    take_fact: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
