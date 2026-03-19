"""SQLAlchemy 2.0 ORM model for the techno_vector_order table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class TechnoVectorOrder(Base):
    __tablename__ = "techno_vector_order"

    techno_vector_order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model_detail_id: Mapped[int] = mapped_column(Integer, ForeignKey("model_detail.model_detail_id"), nullable=False)
    document_service_detail_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_service_detail.document_service_detail_id"), nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=True)
    order_id: Mapped[str] = mapped_column(String(255), nullable=False)
    report: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
