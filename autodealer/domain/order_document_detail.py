"""SQLAlchemy 2.0 ORM model for the order_document_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrderDocumentDetail(Base):
    __tablename__ = "order_document_detail"

    order_document_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_header_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out_header.document_out_header_id"), nullable=False)
    document_registry_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    order_document_state: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="0")
    model_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_link.model_link_id"), nullable=True)
    date_delivery: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    send_message: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
