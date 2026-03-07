from __future__ import annotations

import os
from typing import List

from openai import OpenAI


MODEL = "text-embedding-3-small"

_client: OpenAI | None = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    return _client


def embed_text(text: str) -> List[float]:
    """
    Generate embedding for a piece of text.
    """

    if not text.strip():
        return []

    response = _get_client().embeddings.create(
        model=MODEL,
        input=text,
    )

    return response.data[0].embedding


def embed_batch(texts: list[str]) -> list[list[float]]:
    """
    Batch embedding (faster when indexing many chunks).
    """

    if not texts:
        return []

    response = _get_client().embeddings.create(
        model=MODEL,
        input=texts,
    )

    return [item.embedding for item in response.data]