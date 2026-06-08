"""Validate local Markdown links and SVG files used by the repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                errors.append(f"Broken link in {path.relative_to(ROOT)}: {target}")
    return errors


def check_svg_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.svg"):
        try:
            ElementTree.parse(path)
        except ElementTree.ParseError as exc:
            errors.append(f"Invalid SVG {path.relative_to(ROOT)}: {exc}")
    return errors


def main() -> int:
    errors = check_markdown_links() + check_svg_files()
    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Documentation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
