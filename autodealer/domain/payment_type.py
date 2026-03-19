"""SQLAlchemy 2.0 ORM model for the payment_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import BigInteger, Integer, LargeBinary, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PaymentType(Base):
    __tablename__ = "payment_type"

    payment_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    system_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    abcp_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    uuid: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
