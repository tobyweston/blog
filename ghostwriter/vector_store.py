from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Tuple

import faiss
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
CACHE_DIR = BASE_DIR / "cache"

INDEX_FILE = CACHE_DIR / "faiss.index"
META_FILE = CACHE_DIR / "chunk_meta.json"

CACHE_DIR.mkdir(exist_ok=True)


def load_index() -> Tuple[faiss.IndexFlatIP, List[Dict]]:
    """
    Load FAISS index and metadata.
    """

    if not INDEX_FILE.exists() or not META_FILE.exists():
        raise RuntimeError("Vector index not built. Run build_index.py")

    index = faiss.read_index(str(INDEX_FILE))
    metadata = json.loads(META_FILE.read_text())

    return index, metadata


def save_index(index: faiss.IndexFlatIP, metadata: List[Dict]) -> None:
    """
    Persist FAISS index and metadata.
    """

    faiss.write_index(index, str(INDEX_FILE))
    META_FILE.write_text(json.dumps(metadata, indent=2))


def build_index(vectors: List[List[float]], metadata: List[Dict]) -> None:
    """
    Create FAISS index from embedding vectors.
    """

    if not vectors:
        raise RuntimeError("No vectors supplied to index")

    dim = len(vectors[0])

    index = faiss.IndexFlatIP(dim)

    matrix = np.array(vectors).astype("float32")

    # normalise for cosine similarity
    faiss.normalize_L2(matrix)

    index.add(matrix)

    save_index(index, metadata)


def search(
        query_vector: List[float],
        limit: int = 5,
) -> List[Dict]:
    """
    Perform semantic search.
    """

    index, metadata = load_index()

    vector = np.array([query_vector]).astype("float32")
    faiss.normalize_L2(vector)

    scores, indices = index.search(vector, limit)

    results = []

    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue

        item = metadata[idx].copy()
        item["score"] = float(score)

        results.append(item)

    return results