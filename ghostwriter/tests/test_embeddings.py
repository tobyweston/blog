"""Tests for embeddings.py

embeddings.py exposes:
  - embed_text(text: str) -> List[float]
  - embed_batch(texts: list[str]) -> list[list[float]]

Both call the OpenAI embeddings API which is patched out in all tests.
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from embeddings import embed_batch, embed_text
import embeddings as _embeddings_module


@pytest.fixture(autouse=True)
def reset_embeddings_client():
    """Reset the lazy singleton so each test starts clean."""
    _embeddings_module._client = None
    yield
    _embeddings_module._client = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _mock_client(vectors: list[list[float]]):
    """Return a mock OpenAI client whose embeddings.create returns *vectors*."""
    mock_response = MagicMock()
    mock_response.data = [MagicMock(embedding=v) for v in vectors]
    mock_c = MagicMock()
    mock_c.embeddings.create.return_value = mock_response
    return mock_c


def _patch_client(vectors):
    """Context manager that patches _get_client to return a mock."""
    return patch("embeddings._get_client", return_value=_mock_client(vectors))


# ---------------------------------------------------------------------------
# embed_text
# ---------------------------------------------------------------------------

class TestEmbedText:
    def test_returns_list_of_floats(self):
        fake_vec = [0.1, 0.2, 0.3]
        with _patch_client([fake_vec]):
            result = embed_text("Hello world")
        assert result == fake_vec

    def test_empty_string_returns_empty_list_without_api_call(self):
        with patch("embeddings._get_client") as mock_get:
            result = embed_text("")
            mock_get.assert_not_called()
        assert result == []

    def test_whitespace_only_returns_empty_list_without_api_call(self):
        with patch("embeddings._get_client") as mock_get:
            result = embed_text("   \n  ")
            mock_get.assert_not_called()
        assert result == []

    def test_calls_correct_model(self):
        mock_c = _mock_client([[0.5, 0.5]])
        with patch("embeddings._get_client", return_value=mock_c):
            embed_text("some text")
        assert mock_c.embeddings.create.call_args.kwargs["model"] == "text-embedding-3-small"

    def test_passes_text_as_input(self):
        mock_c = _mock_client([[0.1]])
        with patch("embeddings._get_client", return_value=mock_c):
            embed_text("test content")
        assert mock_c.embeddings.create.call_args.kwargs["input"] == "test content"

    def test_returns_first_embedding_from_response(self):
        """Only the first data item's embedding should be returned."""
        vec_a, vec_b = [1.0, 0.0], [0.0, 1.0]
        with _patch_client([vec_a, vec_b]):
            result = embed_text("hello")
        assert result == vec_a


# ---------------------------------------------------------------------------
# embed_batch
# ---------------------------------------------------------------------------

class TestEmbedBatch:
    def test_empty_list_returns_empty_without_api_call(self):
        with patch("embeddings._get_client") as mock_get:
            result = embed_batch([])
            mock_get.assert_not_called()
        assert result == []

    def test_single_text_returns_single_vector(self):
        fake_vec = [0.1, 0.9]
        with _patch_client([fake_vec]):
            result = embed_batch(["hello"])
        assert result == [fake_vec]

    def test_multiple_texts_returns_multiple_vectors(self):
        vecs = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
        with _patch_client(vecs):
            result = embed_batch(["a", "b", "c"])
        assert result == vecs

    def test_calls_api_once_for_whole_batch(self):
        mock_c = _mock_client([[0.1], [0.2], [0.3]])
        with patch("embeddings._get_client", return_value=mock_c):
            embed_batch(["x", "y", "z"])
        assert mock_c.embeddings.create.call_count == 1

    def test_passes_texts_as_input(self):
        texts = ["alpha", "beta"]
        mock_c = _mock_client([[0.1], [0.2]])
        with patch("embeddings._get_client", return_value=mock_c):
            embed_batch(texts)
        assert mock_c.embeddings.create.call_args.kwargs["input"] == texts

    def test_uses_correct_model(self):
        mock_c = _mock_client([[0.1], [0.2]])
        with patch("embeddings._get_client", return_value=mock_c):
            embed_batch(["a", "b"])
        assert mock_c.embeddings.create.call_args.kwargs["model"] == "text-embedding-3-small"

    def test_result_length_matches_input_length(self):
        vecs = [[float(i)] for i in range(7)]
        with _patch_client(vecs):
            result = embed_batch([f"text {i}" for i in range(7)])
        assert len(result) == 7
