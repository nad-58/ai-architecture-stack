"""Validate Markdown links and SVG files used by the repository."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FENCED_BLOCK = re.compile(r"```.*?```", re.DOTALL)


def _clean_link_target(target: str) -> str:
    """Remove optional Markdown title, fragment, brackets, and URL encoding."""
    target = target.strip().strip("<>")
    if ' "' in target:
        target = target.split(' "', 1)[0]
    elif " '" in target:
        target = target.split(" '", 1)[0]
    return unquote(target.split("#", 1)[0].strip())


def check_markdown_links() -> list[str]:
    warnings: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = FENCED_BLOCK.sub("", path.read_text(encoding="utf-8"))
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = _clean_link_target(target)
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                relative = path.relative_to(ROOT)
                message = f"Broken local link in {relative}: {target}"
                warnings.append(message)
                print(f"::warning file={relative}::{message}")
    return warnings


def check_svg_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.svg"):
        try:
            ElementTree.parse(path)
        except ElementTree.ParseError as exc:
            relative = path.relative_to(ROOT)
            message = f"Invalid SVG {relative}: {exc}"
            errors.append(message)
            print(f"::error file={relative}::{message}")
    return errors


def main() -> int:
    link_warnings = check_markdown_links()
    svg_errors = check_svg_files()

    if link_warnings:
        print(f"Found {len(link_warnings)} local-link warning(s).")
    if svg_errors:
        print(f"Documentation checks failed with {len(svg_errors)} invalid SVG file(s).")
        return 1

    strict_links = os.getenv("STRICT_DOC_LINKS", "0") == "1"
    if strict_links and link_warnings:
        print("STRICT_DOC_LINKS=1, so local-link warnings are treated as failures.")
        return 1

    print("Documentation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
