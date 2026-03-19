"""SQLAlchemy 2.0 ORM model for the message_client_queue table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class MessageClientQueue(Base):
    __tablename__ = "message_client_queue"

    message_client_queue_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    contact_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contact.contact_id"), nullable=True)
    pattern_delivery_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("pattern_delivery.pattern_delivery_id"), nullable=True)
    message_history_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("message_history.message_history_id"), nullable=True)
