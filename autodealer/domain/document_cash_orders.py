"""SQLAlchemy 2.0 ORM model for the document_cash_orders table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentCashOrders(Base):
    __tablename__ = "document_cash_orders"

    document_cash_order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    organization_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    organization_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    document_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=False)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    clause_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("clause.clause_id"), nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    client_doc_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("identification_doc.identification_doc_id"), nullable=True)
    check_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    document_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    prefix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    suffix: Mapped[Optional[str]] = mapped_column(String(5), nullable=True)
    summ: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    state: Mapped[int] = mapped_column(Integer, nullable=False, server_default="4")
    docnotes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    flag: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    fullnumber: Mapped[Optional[str]] = mapped_column(String(21), nullable=True)
    document_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    operation_type: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    cashier_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    accounting_item_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("accounting_item.accounting_item_id"), nullable=True)
    wallet_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=True)
