"""SQLAlchemy 2.0 ORM model for the provider table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer, SmallInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class Provider(Base):
    __tablename__ = "provider"

    provider_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client.client_id"), nullable=False)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    deliver_period: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    external_system_type: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    payment_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("payment_type.payment_type_id"), nullable=True)
    abcp_distributor_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    parts_soft_supplier_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    comission: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
