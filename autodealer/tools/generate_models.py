"""Generate SQLAlchemy 2.0 Mapped ORM models from a live Firebird database.

Usage:
    python autodealer/tools/generate_models.py
"""

from __future__ import annotations

import keyword
import re
import sys
from pathlib import Path
from textwrap import dedent

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

from sqlalchemy import inspect as sa_inspect

from autodealer.connection import get_engine

# ---------------------------------------------------------------------------
# Type mapping
# ---------------------------------------------------------------------------

SIMPLE_TYPE_MAP: dict[str, str] = {
    "INTEGER": "Integer",
    "SMALLINT": "SmallInteger",
    "BIGINT": "BigInteger",
    "FLOAT": "Float",
    "DOUBLE_PRECISION": "Float",
    "DOUBLE PRECISION": "Float",
    "REAL": "Float",
    "DATE": "Date",
    "TIME": "Time",
    "TIMESTAMP": "DateTime",
    "DATETIME": "DateTime",
    "BLOB": "LargeBinary",
    "BINARY": "LargeBinary",
    "BOOLEAN": "Boolean",
    "NULLTYPE": "LargeBinary",
}

PYTHON_ANN_MAP: dict[str, str] = {
    "Integer": "int",
    "SmallInteger": "int",
    "BigInteger": "int",
    "Float": "float",
    "Numeric": "Decimal",
    "String": "str",
    "Text": "str",
    "Date": "date",
    "Time": "time",
    "DateTime": "datetime",
    "LargeBinary": "bytes",
    "Boolean": "bool",
}

STDLIB_IMPORTS: dict[str, str] = {
    "date": "from datetime import date",
    "time": "from datetime import time",
    "datetime": "from datetime import datetime",
    "Decimal": "from decimal import Decimal",
}

RESERVED = set(keyword.kwlist) | {"metadata", "type", "query", "registry"}


def sqla_type_to_str(col_type) -> tuple[str, str]:
    """Return (type_expr_for_mapped_column, import_name)."""
    cls_name = type(col_type).__name__
    # sqlalchemy-firebird prefixes its types with "FB" (e.g. FBINTEGER, FBVARCHAR)
    normalized = cls_name.upper().removeprefix("FB")

    # Parameterised string types
    if normalized in ("VARCHAR", "CHAR", "NVARCHAR", "NCHAR"):
        length = getattr(col_type, "length", None)
        expr = f"String({length})" if length else "String"
        return expr, "String"

    # Text blob (Firebird BLOB SUB_TYPE 1)
    if normalized == "BLOB":
        subtype = getattr(col_type, "subtype", 0)
        if subtype == 1:
            return "Text", "Text"
        return "LargeBinary", "LargeBinary"

    # TEXT is always a text blob
    if normalized == "TEXT":
        return "Text", "Text"

    # Parameterised numeric
    if normalized in ("NUMERIC", "DECIMAL"):
        p = getattr(col_type, "precision", None)
        s = getattr(col_type, "scale", None)
        if p is not None and s is not None:
            return f"Numeric({p}, {s})", "Numeric"
        if p is not None:
            return f"Numeric({p})", "Numeric"
        return "Numeric", "Numeric"

    mapped = SIMPLE_TYPE_MAP.get(normalized)
    if mapped:
        return mapped, mapped

    print(f"  [WARN] Unknown type '{cls_name}' (normalized: '{normalized}'), falling back to LargeBinary", file=sys.stderr)
    return "LargeBinary", "LargeBinary"


# ---------------------------------------------------------------------------
# Name conversion
# ---------------------------------------------------------------------------


def table_to_class_name(table_name: str) -> str:
    """BANK -> Bank, CLIENT_ORDER -> ClientOrder"""
    return "".join(word.capitalize() for word in table_name.split("_"))


def table_to_stem(table_name: str) -> str:
    """BANK -> bank, CLIENT_ORDER -> client_order"""
    return table_name.lower()


def safe_col_name(col_name: str) -> tuple[str, str | None]:
    """Return (python_attr_name, original_name_or_None).

    If the column name clashes with a Python/SQLAlchemy reserved word,
    append an underscore and record the original name for mapped_column(name=...).
    """
    if col_name.lower() in RESERVED:
        return col_name + "_", col_name
    return col_name, None


# ---------------------------------------------------------------------------
# File generation
# ---------------------------------------------------------------------------


def generate_model_source(
    table_name: str,
    columns: list[dict],
    pk_cols: list[str],
    fk_map: dict[str, tuple[str, str]],
) -> str:
    used_sqla: set[str] = set()
    used_stdlib: set[str] = set()
    needs_optional = False

    col_lines: list[str] = []
    composite_pk = len(pk_cols) > 1

    # If no PK detected, use first column as pseudo-PK so SQLAlchemy is satisfied
    pseudo_pk = not pk_cols and columns
    if pseudo_pk:
        pk_cols = [columns[0]["name"]]

    for col in columns:
        raw_name = col["name"]
        nullable = col.get("nullable", True)
        default = col.get("default")
        is_pk = raw_name in pk_cols

        sqla_expr, import_name = sqla_type_to_str(col["type"])
        py_ann = PYTHON_ANN_MAP.get(import_name, "object")

        used_sqla.add(import_name)

        # mapped_column args — positional args first, then keyword args
        positional_args: list[str] = [sqla_expr]
        keyword_args: list[str] = []

        if raw_name in fk_map:
            ref_table, ref_col = fk_map[raw_name]
            positional_args.append(f'ForeignKey("{ref_table}.{ref_col}")')
            used_sqla.add("ForeignKey")
        if is_pk:
            keyword_args.append("primary_key=True")
        if not is_pk:
            keyword_args.append(f"nullable={nullable}")
        if default is not None:
            safe_default = str(default).replace('"', '\\"')
            keyword_args.append(f'server_default="{safe_default}"')

        mc_args = positional_args + keyword_args

        attr_name, original_name = safe_col_name(raw_name)
        if original_name:
            mc_args.append(f'name="{original_name}"')

        # Mapped[T] annotation
        if nullable and not is_pk:
            mapped_type = f"Optional[{py_ann}]"
            needs_optional = True
        else:
            mapped_type = py_ann

        if py_ann in STDLIB_IMPORTS:
            used_stdlib.add(py_ann)

        mc_call = f"mapped_column({', '.join(mc_args)})"
        col_lines.append(f"    {attr_name}: Mapped[{mapped_type}] = {mc_call}")

    # Build import block
    stdlib_lines: list[str] = sorted(
        {STDLIB_IMPORTS[s] for s in used_stdlib if s in STDLIB_IMPORTS}
    )
    if needs_optional:
        stdlib_lines.insert(0, "from typing import Optional")

    sqla_names = sorted(used_sqla)
    sqla_import = "from sqlalchemy import " + ", ".join(sqla_names)

    pk_comment = "    # Composite primary key\n" if composite_pk else ""
    no_pk_warning = (
        "    # WARNING: No primary key in schema — first column used as pseudo-PK\n"
        if pseudo_pk
        else ""
    )

    parts: list[str] = [
        f'"""SQLAlchemy 2.0 ORM model for the {table_name} table. AUTO-GENERATED — do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
    ]

    if stdlib_lines:
        parts.extend(stdlib_lines)
        parts.append("")

    parts.extend([
        sqla_import,
        "from sqlalchemy.orm import Mapped, mapped_column",
        "",
        "from autodealer.connection import Base",
        "",
        "",
        f"class {table_to_class_name(table_name)}(Base):",
        f'    __tablename__ = "{table_name}"',
        "",
        pk_comment + no_pk_warning + "\n".join(col_lines),
    ])

    return "\n".join(parts) + "\n"


def regenerate_domain_init(domain_dir: Path, stems: list[str]) -> None:
    lines = [
        '"""ORM model imports. AUTO-GENERATED by autodealer/tools/generate_models.py."""',
        "",
    ]
    for stem in sorted(stems):
        class_name = table_to_class_name(stem.upper())
        lines.append(f"from autodealer.domain.{stem} import {class_name}")
    lines.append("")

    (domain_dir / "__init__.py").write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    engine = get_engine()
    inspector = sa_inspect(engine)
    table_names: list[str] = [
        t for t in inspector.get_table_names()
        if not t.startswith("RDB$")
    ]

    domain_dir = PROJECT_ROOT / "autodealer" / "domain"
    domain_dir.mkdir(exist_ok=True)

    generated_stems: list[str] = []

    for table_name in sorted(table_names):
        print(f"  {table_name}...")

        columns = inspector.get_columns(table_name)
        pk_info = inspector.get_pk_constraint(table_name)
        pk_cols: list[str] = pk_info.get("constrained_columns", [])

        fk_map: dict[str, tuple[str, str]] = {}
        for fk in inspector.get_foreign_keys(table_name):
            for local, remote in zip(fk["constrained_columns"], fk["referred_columns"]):
                fk_map[local] = (fk["referred_table"], remote)

        source = generate_model_source(table_name, columns, pk_cols, fk_map)

        stem = table_to_stem(table_name)
        filepath = domain_dir / f"{stem}.py"
        filepath.write_text(source, encoding="utf-8")
        generated_stems.append(stem)

    regenerate_domain_init(domain_dir, generated_stems)

    print(f"\nDone. {len(generated_stems)} model files written to {domain_dir}")


if __name__ == "__main__":
    main()
