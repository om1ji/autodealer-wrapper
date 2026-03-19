"""SQLAlchemy 2.0 ORM model for the payment_for_registry table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PaymentForRegistry(Base):
    __tablename__ = "payment_for_registry"

    payment_for_registry_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_link_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    payment_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment.payment_id"), nullable=False)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organization_unlock.organization_id"), nullable=False)
