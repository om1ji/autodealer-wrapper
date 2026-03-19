"""SQLAlchemy 2.0 ORM model for the signature_users table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class SignatureUsers(Base):
    __tablename__ = "signature_users"

    signature_users_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    signature_id: Mapped[int] = mapped_column(Integer, ForeignKey("signature.signature_id"), nullable=False)
