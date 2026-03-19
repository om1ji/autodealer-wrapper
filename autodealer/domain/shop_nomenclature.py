"""SQLAlchemy 2.0 ORM model for the shop_nomenclature table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional
from decimal import Decimal

from sqlalchemy import BigInteger, ForeignKey, Integer, LargeBinary, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class ShopNomenclature(Base):
    __tablename__ = "shop_nomenclature"

    shop_nomenclature_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    directory_registry_id: Mapped[int] = mapped_column(Integer, ForeignKey("directory_registry.directory_registry_id"), nullable=False)
    shop_nomenclature_tree_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("shop_nomenclature_tree.shop_nomenclature_tree_id"), nullable=True)
    shortname: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number_manufacture: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    number_original: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    goods_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("goods_type.goods_type_id"), nullable=False)
    unit_id: Mapped[int] = mapped_column(Integer, ForeignKey("unit.unit_id"), nullable=False)
    tax_schemes_id: Mapped[int] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=False)
    margin1: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin2: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin3: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin4: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin5: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    margin6: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    country_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("country.country_id"), nullable=True)
    producer_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("producer.producer_id"), nullable=True)
    tare_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("tare.tare_id"), nullable=True)
    packing_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("packing.packing_id"), nullable=True)
    material_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("material.material_id"), nullable=True)
    stock_min: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    stock_max: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    dop_info: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ole: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    default_cost: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 4), nullable=True)
    default_margin: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    default_count: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    bar_code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    ac_doc_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    uid: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    barcode_type: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    price_analysis_goods_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    mark: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    default_count_in: Mapped[Optional[Decimal]] = mapped_column(Numeric(18, 3), nullable=True)
    max_discount: Mapped[Optional[Decimal]] = mapped_column(Numeric(15, 2), nullable=True)
    abc_exclude: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    xyz_exclude: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    merge_flag: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    tax_schemes_material_id: Mapped[int] = mapped_column(Integer, ForeignKey("tax_schemes.tax_schemes_id"), nullable=False)
    uuid: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    search_value_text: Mapped[Optional[str]] = mapped_column(String(5000), nullable=True)
    search_value_nums: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    search_value_bar_code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    marking: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    tcd_article_number: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    tcd_generic_article_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    tcd_legacy_article_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    search_value_number_manufacture: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    search_value_number_original: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    marking_goods_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("marking_goods_type.marking_goods_type_id"), nullable=True)
    barcode_extra: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    search_value_barcode_extra: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
