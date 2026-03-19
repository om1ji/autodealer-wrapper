"""SQLAlchemy 2.0 ORM model for the document_service_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentServiceDetail(Base):
    __tablename__ = "document_service_detail"

    document_service_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_out_header_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("document_out_header.document_out_header_id"), nullable=True)
    model_link_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("model_link.model_link_id"), nullable=True)
    repair_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("repair_type.repair_type_id"), nullable=True)
    special_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    run_before: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    run_during: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    discount_work: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    summa_work: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    reasons_appeal: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    index_fuel: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    external_test: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    structure_car: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    lkp: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    price_norm_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("price_norm.price_norm_id"), nullable=True)
    date_start: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    rt_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    rt_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    auto_update_date: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    inspection_car_image_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("inspection_car_image.inspection_car_image_id"), nullable=True)
    planning_work_place_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("planning_work_place.planning_work_place_id"), nullable=True)
    addon_terms: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    car_cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    guarante: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    summa_bonus: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    ac_model_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    ac_map: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    doc_date_end_section_link: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    inspection_completeness: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    rmi_car_select: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
