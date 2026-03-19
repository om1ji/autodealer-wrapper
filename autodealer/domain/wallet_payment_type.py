"""SQLAlchemy 2.0 ORM model for the wallet_payment_type table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class WalletPaymentType(Base):
    __tablename__ = "wallet_payment_type"

    wallet_payment_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    wallet_id: Mapped[int] = mapped_column(Integer, ForeignKey("wallet.wallet_id"), nullable=False)
    payment_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment_type.payment_type_id"), nullable=False)
    default_wallet: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
