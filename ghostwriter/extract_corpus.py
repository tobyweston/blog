from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

import yaml

from config import BLOG_DIR, CORPUS_CACHE, INCLUDE_UNPUBLISHED, UNPUBLISHED_DIR


@dataclass
class Document:
    path: str
    kind: str
    title: str
    date: str
    year: int | None
    slug: str
    description: str
    categories: list[str]
    topics: list[str]
    draft: bool
    content: str
    word_count: int


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def iter_files(directory: Path) -> Iterable[Path]:
    if not directory.exists():
        return
    for path in sorted(directory.glob("*")):
        if path.suffix.lower() in {".md", ".mdx"}:
            yield path


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    raw_frontmatter = match.group(1)
    body = text[match.end():]

    try:
        data = yaml.safe_load(raw_frontmatter) or {}
        if not isinstance(data, dict):
            data = {}
    except Exception:
        data = {}

    return data, body


def normalise_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, str):
        # allow comma-separated fallback
        parts = [part.strip() for part in value.split(",")]
        return [part for part in parts if part]
    return [str(value).strip()]


def derive_title(path: Path, frontmatter: dict[str, Any]) -> str:
    title = frontmatter.get("title")
    if title:
        return str(title).strip()

    slug = path.stem
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    return slug.replace("-", " ").strip().title()


def derive_date(path: Path, frontmatter: dict[str, Any]) -> str:
    raw = frontmatter.get("date")
    if raw:
        if isinstance(raw, (datetime, date)):
            return raw.isoformat()[:10]
        return str(raw).strip()[:10]

    match = re.match(r"^(\d{4}-\d{2}-\d{2})-", path.stem)
    return match.group(1) if match else ""


def derive_year(date_text: str) -> int | None:
    match = re.match(r"^(\d{4})-\d{2}-\d{2}$", date_text)
    return int(match.group(1)) if match else None


def clean_body(text: str) -> str:
    # remove MDX imports/exports
    text = re.sub(r"^\s*import\s+.*?$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*export\s+.*?$", "", text, flags=re.MULTILINE)

    # remove fenced code blocks entirely for voice extraction
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)

    # unwrap inline code
    text = re.sub(r"`([^`]+)`", r"\1", text)

    # replace markdown images/links but keep visible text
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r" \1 ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # strip JSX/HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # normalise whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def load_document(path: Path, kind: str) -> Document:
    raw = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(raw)

    date_text = derive_date(path, frontmatter)
    cleaned = clean_body(body)

    return Document(
        path=str(path),
        kind=kind,
        title=derive_title(path, frontmatter),
        date=date_text,
        year=derive_year(date_text),
        slug=path.stem,
        description=str(frontmatter.get("description", "")).strip(),
        categories=normalise_list(frontmatter.get("categories")),
        topics=normalise_list(frontmatter.get("topics")),
        draft=bool(frontmatter.get("draft", False)),
        content=cleaned,
        word_count=len(cleaned.split()),
    )


def build_corpus() -> list[Document]:
    docs: list[Document] = []

    for path in iter_files(BLOG_DIR):
        docs.append(load_document(path, "blog"))

    if INCLUDE_UNPUBLISHED:
        for path in iter_files(UNPUBLISHED_DIR):
            docs.append(load_document(path, "unpublished"))

    return docs


def save_corpus(docs: list[Document]) -> None:
    CORPUS_CACHE.write_text(
        json.dumps([asdict(doc) for doc in docs], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def main() -> None:
    corpus = build_corpus()
    save_corpus(corpus)
    print(f"Cached {len(corpus)} documents to {CORPUS_CACHE}")


if __name__ == "__main__":
    main()