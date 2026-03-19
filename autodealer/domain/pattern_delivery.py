"""SQLAlchemy 2.0 ORM model for the pattern_delivery table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class PatternDelivery(Base):
    __tablename__ = "pattern_delivery"

    pattern_delivery_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hidden: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    document_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=True)
    system_id: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    auto_sending: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    auto_sending_time: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    putoff_count_days: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    pattern_client: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    auto_sending_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    putoff_count_hours: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    putoff_count_minutes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    day_time_sending: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    pattern_operation: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    pattern_send_doc: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    pattern_bonus: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    delivery_channel: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
