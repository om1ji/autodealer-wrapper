"""SQLAlchemy 2.0 ORM model for the document_cargo table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentCargo(Base):
    __tablename__ = "document_cargo"

    document_cargo_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    sender_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=True)
    sender_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    sender_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    receiver_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    receiver_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    receiver_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    addon_number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    addon_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    update_sender: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    update_receiver: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    payer_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=True)
    payer_contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    payer_requisite_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("requisite.requisite_id"), nullable=True)
    update_payer: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    use_main_payment: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    shipment_doc_positions: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shipment_doc_number: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shipment_doc_date: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    shipment_doc_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
