from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from config import CORPUS_CACHE, MAX_STYLE_SAMPLES
from extract_corpus import build_corpus, save_corpus


BASE_DIR = Path(__file__).resolve().parent
FRAMEWORKS_DIR = BASE_DIR / "frameworks"

RESEARCH_DIR = BASE_DIR / "research"
RESEARCH_COMMON_DIR = RESEARCH_DIR / "common"
RESEARCH_POSTS_DIR = RESEARCH_DIR / "post"

NOTES_DIR = BASE_DIR / "notes"
NOTES_COMMON_DIR = NOTES_DIR / "common"
NOTES_POSTS_DIR = NOTES_DIR / "post"


def ensure_corpus() -> list[dict[str, Any]]:
    if not CORPUS_CACHE.exists():
        docs = build_corpus()
        save_corpus(docs)
    return json.loads(CORPUS_CACHE.read_text(encoding="utf-8"))


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{2,}", text.lower()))


def slugify(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def score_text(blob: str, query: str) -> int:
    return len(tokenize(blob) & tokenize(query))


def load_frameworks() -> list[dict[str, Any]]:
    frameworks: list[dict[str, Any]] = []

    if not FRAMEWORKS_DIR.exists():
        return frameworks

    for path in sorted(FRAMEWORKS_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, flags=re.DOTALL)
        if not match:
            continue

        frontmatter = yaml.safe_load(match.group(1)) or {}
        body = match.group(2).strip()

        if not isinstance(frontmatter, dict):
            continue

        frameworks.append(
            {
                "path": str(path),
                "name": frontmatter.get("name", path.stem),
                "slug": frontmatter.get("slug", path.stem),
                "topics": frontmatter.get("topics", []) or [],
                "when_to_use": frontmatter.get("when_to_use", []) or [],
                "summary": frontmatter.get("summary", ""),
                "key_claims": frontmatter.get("key_claims", []) or [],
                "argument_patterns": frontmatter.get("argument_patterns", []) or [],
                "example_phrasing": frontmatter.get("example_phrasing", []) or [],
                "guardrails": frontmatter.get("guardrails", []) or [],
                "body": body,
            }
        )

    return frameworks


def load_text_file(path: Path) -> dict[str, Any]:
    return {
        "path": str(path),
        "name": path.stem,
        "content": path.read_text(encoding="utf-8").strip(),
    }


def iter_text_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(
        path
        for path in directory.glob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".txt"}
    )


def infer_post_slug(topic_or_query: str | None) -> str | None:
    if not topic_or_query:
        return None
    slug = slugify(topic_or_query)
    return slug or None


def gather_candidate_files(
        *,
        common_dir: Path,
        posts_dir: Path,
        explicit_paths: list[str] | None = None,
        topic_or_query: str | None = None,
) -> list[dict[str, Any]]:
    files: list[dict[str, Any]] = []

    if explicit_paths:
        for raw_path in explicit_paths:
            path = Path(raw_path)
            if path.exists() and path.is_file():
                files.append(load_text_file(path))
        return files

    for path in iter_text_files(common_dir):
        files.append(load_text_file(path))

    post_slug = infer_post_slug(topic_or_query)
    if post_slug:
        post_dir = posts_dir / post_slug
        for path in iter_text_files(post_dir):
            files.append(load_text_file(path))

    return files


def load_research_files(
        paths: list[str] | None = None,
        topic_or_query: str | None = None,
) -> list[dict[str, Any]]:
    return gather_candidate_files(
        common_dir=RESEARCH_COMMON_DIR,
        posts_dir=RESEARCH_POSTS_DIR,
        explicit_paths=paths,
        topic_or_query=topic_or_query,
    )


def load_notes_files(
        paths: list[str] | None = None,
        topic_or_query: str | None = None,
) -> list[dict[str, Any]]:
    return gather_candidate_files(
        common_dir=NOTES_COMMON_DIR,
        posts_dir=NOTES_POSTS_DIR,
        explicit_paths=paths,
        topic_or_query=topic_or_query,
    )


def pick_frameworks(query: str, limit: int = 3) -> list[dict[str, Any]]:
    frameworks = load_frameworks()
    ranked = sorted(
        frameworks,
        key=lambda fw: score_text(
            " ".join(
                [
                    fw.get("name", ""),
                    fw.get("summary", ""),
                    " ".join(fw.get("topics", [])),
                    " ".join(fw.get("when_to_use", [])),
                    " ".join(fw.get("key_claims", [])),
                    " ".join(fw.get("argument_patterns", [])),
                ]
            ),
            query,
        ),
        reverse=True,
    )

    chosen = [fw for fw in ranked if score_text(fw.get("summary", ""), query) > 0]
    return chosen[:limit] if chosen else ranked[:limit]


def pick_topic_samples(query: str, limit: int = 5) -> list[dict[str, Any]]:
    corpus = ensure_corpus()
    scored = []

    for doc in corpus:
        if not doc.get("content", "").strip():
            continue

        blob = " ".join(
            [
                doc.get("title", ""),
                doc.get("description", ""),
                " ".join(doc.get("categories", [])),
                " ".join(doc.get("topics", [])),
                doc.get("content", "")[:4000],
            ]
        )
        score = score_text(blob, query)
        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda item: (item[0], item[1].get("date", "")), reverse=True)
    return [doc for _, doc in scored[:limit]]


def pick_voice_anchors(limit: int = MAX_STYLE_SAMPLES) -> list[dict[str, Any]]:
    corpus = ensure_corpus()
    candidates = [
        doc
        for doc in corpus
        if doc.get("kind") == "blog" and doc.get("content", "").strip()
    ]
    candidates.sort(key=lambda d: d.get("date", ""), reverse=True)
    return candidates[:limit]


def pick_research(
        query: str,
        paths: list[str] | None = None,
        topic_or_query: str | None = None,
        limit: int = 3,
) -> list[dict[str, Any]]:
    files = load_research_files(paths=paths, topic_or_query=topic_or_query)
    ranked = sorted(
        files,
        key=lambda item: score_text(item.get("content", ""), query),
        reverse=True,
    )
    chosen = [item for item in ranked if score_text(item.get("content", ""), query) > 0]
    return chosen[:limit] if chosen else ranked[:limit]


def pick_notes(
        query: str,
        paths: list[str] | None = None,
        topic_or_query: str | None = None,
        limit: int = 3,
) -> list[dict[str, Any]]:
    files = load_notes_files(paths=paths, topic_or_query=topic_or_query)
    ranked = sorted(
        files,
        key=lambda item: score_text(item.get("content", ""), query),
        reverse=True,
    )
    chosen = [item for item in ranked if score_text(item.get("content", ""), query) > 0]
    return chosen[:limit] if chosen else ranked[:limit]