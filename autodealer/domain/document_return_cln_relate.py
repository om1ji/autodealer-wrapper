"""SQLAlchemy 2.0 ORM model for the document_return_cln_relate table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentReturnClnRelate(Base):
    __tablename__ = "document_return_cln_relate"

    document_return_cln_relate_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    goods_out_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=True)
    goods_out_return_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("goods_out.goods_out_id"), nullable=True)
