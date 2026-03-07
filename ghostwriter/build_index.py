from __future__ import annotations

import json
from pathlib import Path

from embeddings import embed_text
from chunking import build_chunks
from vector_store import build_index
from retrieve import (
    ensure_corpus,
    load_frameworks,
    load_research_files,
    load_notes_files,
)

BASE_DIR = Path(__file__).resolve().parent
CACHE_DIR = BASE_DIR / "cache"

CHUNKS_FILE = CACHE_DIR / "chunks.jsonl"


def write_chunks(chunks):
    CACHE_DIR.mkdir(exist_ok=True)

    with CHUNKS_FILE.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")


def load_chunks():
    if not CHUNKS_FILE.exists():
        return []

    chunks = []

    for line in CHUNKS_FILE.read_text(encoding="utf-8").splitlines():
        chunks.append(json.loads(line))

    return chunks


def collect_blog_chunks():
    corpus = ensure_corpus()

    chunks = []

    for doc in corpus:
        chunks.extend(build_chunks(doc))

    return chunks


def collect_framework_chunks():
    frameworks = load_frameworks()

    chunks = []

    for fw in frameworks:
        text = "\n".join(
            [
                fw.get("name", ""),
                fw.get("summary", ""),
                " ".join(fw.get("key_claims", [])),
                " ".join(fw.get("argument_patterns", [])),
                fw.get("body", ""),
            ]
        )

        chunks.append(
            {
                "text": text,
                "source_path": fw.get("path"),
                "title": fw.get("name"),
                "topics": fw.get("topics", []),
                "kind": "framework",
                "chunk_index": 0,
            }
        )

    return chunks


def collect_research_chunks():
    files = load_research_files()

    chunks = []

    for item in files:
        chunks.extend(
            build_chunks(
                {
                    "path": item["path"],
                    "title": item["name"],
                    "content": item["content"],
                    "topics": [],
                    "categories": [],
                    "kind": "research",
                }
            )
        )

    return chunks


def collect_notes_chunks():
    files = load_notes_files()

    chunks = []

    for item in files:
        chunks.extend(
            build_chunks(
                {
                    "path": item["path"],
                    "title": item["name"],
                    "content": item["content"],
                    "topics": [],
                    "categories": [],
                    "kind": "notes",
                }
            )
        )

    return chunks


def main():
    print("\nBuilding semantic index\n")

    chunks = []

    print("Collecting blog chunks...")
    chunks.extend(collect_blog_chunks())

    print("Collecting framework chunks...")
    chunks.extend(collect_framework_chunks())

    print("Collecting research chunks...")
    chunks.extend(collect_research_chunks())

    print("Collecting notes chunks...")
    chunks.extend(collect_notes_chunks())

    print(f"Total chunks: {len(chunks)}")

    write_chunks(chunks)

    vectors = []
    metadata = []

    print("\nEmbedding chunks...\n")

    for chunk in chunks:
        vec = embed_text(chunk["text"])

        vectors.append(vec)
        metadata.append(chunk)

    print("Building FAISS index...")

    build_index(vectors, metadata)

    print("\nIndex build complete.\n")


if __name__ == "__main__":
    main()