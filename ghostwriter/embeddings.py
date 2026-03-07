from __future__ import annotations

import os
from typing import List

from openai import OpenAI


MODEL = "text-embedding-3-small"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def embed_text(text: str) -> List[float]:
    """
    Generate embedding for a piece of text.
    """

    if not text.strip():
        return []

    response = client.embeddings.create(
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

    response = client.embeddings.create(
        model=MODEL,
        input=texts,
    )

    return [item.embedding for item in response.data]