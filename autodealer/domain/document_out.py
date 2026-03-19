"""SQLAlchemy 2.0 ORM model for the document_out table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentOut(Base):
    __tablename__ = "document_out"

    document_out_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False)
    document_in_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_in.document_in_id"), nullable=True)
    source_document_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=True)
    organization_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    organization_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    organization_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    client_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    client_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    source_info_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("source_info.source_info_id"), nullable=True)
    division_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    return_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    summa: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    date_accept: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    date_payment: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True, server_default="0")
    discont_card_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("card_info.card_info_id"), nullable=True)
    flag: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    basis_doc: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    basis_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    basis_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    summa_bonus: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    round_value: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, server_default="0")
