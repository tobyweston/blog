from __future__ import annotations

import json
import os
from pathlib import Path
from typing import List

import numpy as np
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
EMBEDDINGS_FILE = BASE_DIR / "cache" / "embeddings.json"

MODEL = "text-embedding-3-small"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def cosine_similarity(a: List[float], b: List[float]) -> float:
    a = np.array(a)
    b = np.array(b)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0.0:
        return 0.0
    return float(np.dot(a, b) / denom)


def embed_text(text: str) -> List[float]:
    response = client.embeddings.create(
        model=MODEL,
        input=text,
    )
    return response.data[0].embedding


def load_embeddings():
    if not EMBEDDINGS_FILE.exists():
        return {}
    return json.loads(EMBEDDINGS_FILE.read_text())


def save_embeddings(data):
    EMBEDDINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    EMBEDDINGS_FILE.write_text(json.dumps(data))


def embed_documents(docs):
    embeddings = load_embeddings()
    for doc in docs:
        key = doc["path"]
        if key in embeddings:
            continue
        text = doc["content"][:4000]
        embeddings[key] = embed_text(text)
        print("embedded:", key)
    save_embeddings(embeddings)


def search(query, docs, limit=5):
    embeddings = load_embeddings()
    query_vec = embed_text(query)
    scored = []
    for doc in docs:
        key = doc["path"]
        if key not in embeddings:
            continue
        score = cosine_similarity(query_vec, embeddings[key])
        scored.append((score, doc))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [doc for _, doc in scored[:limit]]
