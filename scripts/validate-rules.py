#!/usr/bin/env python3
"""Validate Atomic Rule Cards against the rule-card JSON Schema.

Every ``*.json`` file under ``rules/`` (or the directory passed with
``--rules``) is validated against ``schema/rule-card.schema.json`` (or the
path passed with ``--schema``). The script also reports duplicate rule ``id``
values across cards, which a per-file schema cannot express.

Exit codes: 0 = all valid, 1 = invalid cards found, 2 = missing dependency.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Validate Atomic Rule Cards against the rule-card schema."
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=REPO_ROOT / "schema" / "rule-card.schema.json",
        help="Path to the rule-card JSON Schema (default: schema/rule-card.schema.json).",
    )
    parser.add_argument(
        "--rules",
        type=Path,
        default=REPO_ROOT / "rules",
        help="Directory containing Atomic Rule Cards (default: rules/).",
    )
    return parser.parse_args(list(argv))


def load_json(path: Path) -> Any:
    """Read and parse a UTF-8 JSON file."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def format_path(path: Sequence[str | int]) -> str:
    """Render a JSON path like ``applies_to.surfaces.0``."""
    return ".".join(str(part) for part in path)


def main(argv: Sequence[str]) -> int:
    """Validate rule cards and report problems, returning the exit code."""
    args = parse_args(argv)
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ModuleNotFoundError:
        print(
            "The jsonschema package is required. Install dev dependencies first:\n"
            f"  python3 -m pip install -r {REPO_ROOT / 'requirements-dev.txt'}",
            file=sys.stderr,
        )
        return 2

    schema = load_json(args.schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    card_paths = sorted(args.rules.rglob("*.json"))
    problems: list[str] = []
    ids: list[str] = []
    seen_errors: set[tuple[str, tuple[str | int, ...]]] = set()

    for path in card_paths:
        try:
            card = load_json(path)
        except json.JSONDecodeError as exc:
            problems.append(f"{path}: invalid JSON ({exc})")
            continue
        if not isinstance(card, dict) or not isinstance(card.get("id"), str):
            continue  # Not a rule card; leave it alone.
        ids.append(card["id"])
        for error in sorted(validator.iter_errors(card), key=lambda e: tuple(e.path)):
            key = (error.message, tuple(error.path))
            if key in seen_errors:
                continue
            seen_errors.add(key)
            location = f" at {format_path(error.path)}" if error.path else ""
            problems.append(f"{path}: {error.message}{location}")

    duplicates = {
        rule_id: count for rule_id, count in Counter(ids).items() if count > 1
    }
    for rule_id, count in duplicates.items():
        problems.append(f"duplicate rule id {rule_id!r} appears in {count} cards")

    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)

    if problems:
        summary = ", ".join(
            [f"{len(problems)} problem(s) found"] +
            ([f"{len(duplicates)} duplicate id(s)"] if duplicates else [])
        )
        print(f"Validation failed: {summary}.", file=sys.stderr)
        return 1

    print(
        f"Validated {len(card_paths)} JSON file(s) in {args.rules} "
        f"against {args.schema}: all OK."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
