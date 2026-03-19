"""SQLAlchemy 2.0 ORM model for the action_works table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ActionWorks(Base):
    __tablename__ = "action_works"

    action_works_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    service_common_work_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("service_common_work.service_common_work_id"), nullable=True)
    action_goods_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("action_goods.action_goods_id"), nullable=True)
    quantity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
