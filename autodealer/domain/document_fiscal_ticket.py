"""SQLAlchemy 2.0 ORM model for the document_fiscal_ticket table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, Integer, LargeBinary, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentFiscalTicket(Base):
    __tablename__ = "document_fiscal_ticket"

    document_fiscal_ticket_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    check_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    document_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_registry.document_registry_id"), nullable=True)
    document_cash_order_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_cash_orders.document_cash_order_id"), nullable=True)
    z_report: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    fiscal_sign: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    tax_system: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    fr_device_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("organization_device.organization_device_id"), nullable=True)
    receipt_uuid: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    receipt_uuid_backup: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
