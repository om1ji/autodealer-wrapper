"""SQLAlchemy 2.0 ORM model for the model_detail table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Float, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ModelDetail(Base):
    __tablename__ = "model_detail"

    model_detail_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model_id: Mapped[int] = mapped_column(Integer, ForeignKey("model.model_id"), nullable=False)
    directory_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    color_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("color.color_id"), nullable=True)
    year_of_production: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    power_engine: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    power_engine_watt: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    regno: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    vin: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    chassis: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    body: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    place_passenger: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    max_mass: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    tonnage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    engine_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    car_gearbox_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_gearbox_type.car_gearbox_type_id"), nullable=True)
    car_engine_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_engine_type.car_engine_type_id"), nullable=True)
    car_body_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_body_type.car_body_type_id"), nullable=True)
    dop_info: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    car_fuel_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_fuel_type.car_fuel_type_id"), nullable=True)
    car_brake_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("car_brake_type.car_brake_type_id"), nullable=True)
    empty_mass: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    normalized_regno: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    search_value_text: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    search_value_nums: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
