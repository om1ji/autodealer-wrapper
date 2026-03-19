"""SQLAlchemy 2.0 ORM model for the service_work_return table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ServiceWorkReturn(Base):
    __tablename__ = "service_work_return"

    service_work_return_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_out.document_out_id"), nullable=False)
    service_work_id: Mapped[int] = mapped_column(Integer, ForeignKey("service_work.service_work_id"), nullable=False)
