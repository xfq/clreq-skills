#!/usr/bin/env python3
"""Check that local relative links in Markdown files resolve to real files.

Scans every ``*.md`` file under the repository root (or the directory passed
with ``--root``) and validates each Markdown link that is not:

* an absolute URL (``http://``, ``mailto:``, ``data:``, ...),
* a root-relative path (``/foo``),
* a same-page anchor (``#section``).

A fragment or query string on a local target (``file.md#section``) is ignored
when resolving the file part, and percent-encoding is decoded first. Targets
that resolve outside the root are reported as well.

Exit codes: 0 = all links resolve, 1 = broken links found.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterator, Sequence
from urllib.parse import unquote, urlsplit

REPO_ROOT = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]*)\)")
SKIP_DIRS = {".git", "node_modules"}


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Check local relative links in Markdown files."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=REPO_ROOT,
        help="Directory to scan for Markdown files (default: repository root).",
    )
    return parser.parse_args(list(argv))


def find_markdown_files(root: Path) -> list[Path]:
    """Return all Markdown files, skipping VCS and dependency directories."""
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.parts)
    )


def iter_links(path: Path) -> Iterator[tuple[int, str]]:
    """Yield ``(line_number, target)`` pairs for every Markdown link."""
    for line_no, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        for match in LINK_RE.finditer(line):
            yield line_no, match.group(1)


def local_target(target: str) -> str | None:
    """Return the file part to verify, or None when the link is not local."""
    stripped = target.strip()
    if stripped.startswith("<") and stripped.endswith(">"):
        stripped = stripped[1:-1]
    if not stripped or stripped.startswith("#"):
        return None
    if stripped.startswith("/") or stripped.startswith("//"):
        return None  # root-relative or protocol-relative
    if urlsplit(stripped).scheme:
        return None  # absolute URL with a scheme (http:, mailto:, data:, ...)
    return urlsplit(stripped).path or None


def check_target(
    root: Path, source: Path, line_no: int, target: str, problems: list[str]
) -> bool:
    """Verify one target, appending a problem entry when it is broken.

    Returns True when the target is a local link that was verified.
    """
    path_part = local_target(target)
    if path_part is None:
        return False
    root_resolved = root.resolve()
    resolved = (source.parent / unquote(path_part)).resolve()
    if not resolved.is_relative_to(root_resolved):
        problems.append(
            f"{source}:{line_no}: target {target!r} resolves outside {root}"
        )
    elif not resolved.is_file():
        problems.append(f"{source}:{line_no}: target {target!r} does not exist")
    return True


def main(argv: Sequence[str]) -> int:
    """Scan Markdown files and report broken local relative links."""
    args = parse_args(argv)
    root = args.root
    if not root.is_dir():
        print(f"error: root directory not found: {root}", file=sys.stderr)
        return 1

    problems: list[str] = []
    files = find_markdown_files(root)
    links_checked = 0

    for path in files:
        for line_no, target in iter_links(path):
            if check_target(root, path, line_no, target, problems):
                links_checked += 1

    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)

    if problems:
        print(
            f"Link check failed: {len(problems)} problem(s) found.",
            file=sys.stderr,
        )
        return 1

    print(
        f"Checked {len(files)} Markdown file(s) and {links_checked} link(s) "
        f"in {root}: all OK."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
