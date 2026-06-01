#!/usr/bin/env python3
"""Validate the repository shape expected by GitBook Git Sync."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "SUMMARY.md",
    ".gitbook.yaml",
]

EXTERNAL_LINK_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

SECRET_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----"),
    re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def markdown_files() -> list[Path]:
    files = [ROOT / "README.md", ROOT / "SUMMARY.md"]
    files.extend(sorted((ROOT / "docs").rglob("*.md")))
    if (ROOT / "private").exists():
        files.extend(sorted((ROOT / "private").rglob("*.md")))
    return files


def normalize_link(raw: str) -> str:
    link = raw.strip().split()[0].strip("<>")
    return link.split("#", 1)[0]


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required GitBook files: {', '.join(missing)}")


def check_gitbook_yaml() -> None:
    text = (ROOT / ".gitbook.yaml").read_text(encoding="utf-8")
    required_fragments = [
        "root:",
        "structure:",
        "readme: README.md",
        "summary: SUMMARY.md",
    ]
    missing = [fragment for fragment in required_fragments if fragment not in text]
    if missing:
        fail(f".gitbook.yaml is missing expected entries: {', '.join(missing)}")


def check_summary() -> None:
    summary = (ROOT / "SUMMARY.md").read_text(encoding="utf-8")
    links = [normalize_link(match.group(1)) for match in MD_LINK_RE.finditer(summary)]
    private_links = [link for link in links if link.startswith("private/") or "/private/" in link]
    if private_links:
        fail("SUMMARY.md must not link private learning material: " + ", ".join(private_links))

    missing = [
        link
        for link in links
        if link and not EXTERNAL_LINK_RE.match(link) and not (ROOT / link).exists()
    ]
    if missing:
        fail("SUMMARY.md contains links to missing files: " + ", ".join(missing))


def check_markdown_links() -> None:
    broken: list[str] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in MD_LINK_RE.finditer(text):
            raw = match.group(1)
            link = normalize_link(raw)
            if not link or link.startswith("#") or EXTERNAL_LINK_RE.match(link):
                continue
            target = (path.parent / link).resolve()
            if not target.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {raw}")
    if broken:
        fail("broken relative Markdown links:\n" + "\n".join(broken))


def check_high_confidence_secrets() -> None:
    findings: list[str] = []
    scan_roots = [ROOT / "README.md", ROOT / "SUMMARY.md", ROOT / "AGENTS.md", ROOT / "docs"]
    for root in scan_roots:
        paths = [root] if root.is_file() else sorted(root.rglob("*"))
        for path in paths:
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml", ""}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    findings.append(str(path.relative_to(ROOT)))
                    break
    if findings:
        fail("possible high-confidence secrets found in public docs: " + ", ".join(sorted(set(findings))))


def main() -> None:
    check_required_files()
    check_gitbook_yaml()
    check_summary()
    check_markdown_links()
    check_high_confidence_secrets()
    print("GitBook source validation passed.")


if __name__ == "__main__":
    main()
