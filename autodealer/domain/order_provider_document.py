"""SQLAlchemy 2.0 ORM model for the order_provider_document table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class OrderProviderDocument(Base):
    __tablename__ = "order_provider_document"

    order_provider_document_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_provider_document_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("order_provider_document_tree.order_provider_document_tree_id"), nullable=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False, server_default="20")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    manager_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=True)
    document_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    summa: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False, server_default="0")
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    flag: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    state: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    barcode: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    date_delivery: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    external_order_system_id: Mapped[Optional[str]] = mapped_column(String(32765), nullable=True)
    external_system_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
