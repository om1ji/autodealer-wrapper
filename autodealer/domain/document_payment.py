"""SQLAlchemy 2.0 ORM model for the document_payment table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentPayment(Base):
    __tablename__ = "document_payment"

    document_payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False, server_default="14")
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
    organization_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    organization_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=False)
    client_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    client_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    tax_schemes_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=True)
    code_bk_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("code_bk.code_bk_id"), nullable=True)
    code_okato_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("code_okato.code_okato_id"), nullable=True)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    date_create: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    type_pay: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    basis_pay: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    kind_pay: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    sequence_pay: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    direction_pay: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    date_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    status: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    payment_kind: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    summa: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    code_pay: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False, server_default="4")
    flag: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    index_direction_text: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    summa_nds: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    nalog_period: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    nalog_document_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    nalog_document_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    is_nalog_payment: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    document_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    accounting_item_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("accounting_item.accounting_item_id"), nullable=True)
    wallet_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=True)
