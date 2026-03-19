"""SQLAlchemy 2.0 ORM model for the money_document_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class MoneyDocumentDetail(Base):
    __tablename__ = "money_document_detail"

    money_document_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    directory_registry_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=True)
    accounting_item_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("accounting_item.accounting_item_id"), nullable=True)
    wallet_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=True)
    payment_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payment_type.payment_type_id"), nullable=True)
    reason: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
