"""SQLAlchemy 2.0 ORM model for the document_organizer_rule table. AUTO-GENERATED — do not edit manually."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from autodealer.connection import Base


class DocumentOrganizerRule(Base):
    __tablename__ = "document_organizer_rule"

    document_organizer_rule_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("document_type.document_type_id"), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    filter_param: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    use_mark: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    mark: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    use_tree: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    tree_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    enable: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    stop: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
    rule_position: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    use_search_folder: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
    use_search_folder_filter: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="0")
