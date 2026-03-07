from __future__ import annotations

import re
from typing import List, Dict


def split_paragraphs(text: str) -> List[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs


def split_sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def chunk_text(
        text: str,
        max_chars: int = 1200,
        overlap: int = 200,
) -> List[str]:
    """
    Split text into overlapping chunks.

    Overlap helps preserve context across boundaries.
    """

    text = text.strip()
    if not text:
        return []

    chunks: List[str] = []

    start = 0
    length = len(text)

    while start < length:
        end = start + max_chars
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += max_chars - overlap

    return chunks


def build_chunks(doc: Dict) -> List[Dict]:
    """
    Convert a document into multiple chunk objects.
    """

    content = doc.get("content", "").strip()

    chunks = []

    for idx, chunk in enumerate(chunk_text(content)):
        chunks.append(
            {
                "text": chunk,
                "source_path": doc.get("path"),
                "title": doc.get("title"),
                "date": doc.get("date"),
                "topics": doc.get("topics", []),
                "categories": doc.get("categories", []),
                "chunk_index": idx,
                "kind": doc.get("kind"),
            }
        )

    return chunks