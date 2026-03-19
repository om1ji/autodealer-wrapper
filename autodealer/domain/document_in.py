"""SQLAlchemy 2.0 ORM model for the document_in table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentIn(Base):
    __tablename__ = "document_in"

    document_in_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_in_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_in_tree.document_in_tree_id"), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("provider.provider_id"), nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    bill_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    account_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    date_registration: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_transit: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    summa1: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False, server_default="0")
    summa2: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    state: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    provider_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False, server_default="9")
    manager_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("manager.manager_id"), nullable=True)
    flag: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, server_default="1")
    barcode: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    bill_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    account_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
