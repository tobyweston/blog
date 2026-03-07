"""Tests for embeddings.py"""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest


from embeddings import cosine_similarity, embed_documents, load_embeddings, save_embeddings, search


# ---------------------------------------------------------------------------
# cosine_similarity
# ---------------------------------------------------------------------------

class TestCosineSimilarity:
    def test_identical_vectors_return_one(self):
        v = [1.0, 0.0, 0.0]
        assert cosine_similarity(v, v) == pytest.approx(1.0)

    def test_orthogonal_vectors_return_zero(self):
        a = [1.0, 0.0]
        b = [0.0, 1.0]
        assert cosine_similarity(a, b) == pytest.approx(0.0)

    def test_opposite_vectors_return_minus_one(self):
        a = [1.0, 0.0]
        b = [-1.0, 0.0]
        assert cosine_similarity(a, b) == pytest.approx(-1.0)

    def test_similar_vectors_return_high_score(self):
        a = [1.0, 1.0, 0.0]
        b = [1.0, 0.9, 0.1]
        score = cosine_similarity(a, b)
        assert score > 0.95

    def test_returns_float(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        result = cosine_similarity(a, b)
        assert isinstance(result, float)


# ---------------------------------------------------------------------------
# load_embeddings / save_embeddings
# ---------------------------------------------------------------------------

class TestLoadSaveEmbeddings:
    def test_load_returns_empty_dict_when_no_file(self, tmp_path):
        with patch("embeddings.EMBEDDINGS_FILE", tmp_path / "embeddings.json"):
            result = load_embeddings()
        assert result == {}

    def test_save_and_load_round_trip(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"
        data = {"doc/a.md": [0.1, 0.2, 0.3], "doc/b.md": [0.4, 0.5, 0.6]}

        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path):
            save_embeddings(data)
            loaded = load_embeddings()

        assert loaded == data

    def test_save_creates_parent_directories(self, tmp_path):
        nested = tmp_path / "a" / "b" / "embeddings.json"
        data = {"key": [1.0, 2.0]}

        with patch("embeddings.EMBEDDINGS_FILE", nested):
            save_embeddings(data)

        assert nested.exists()


# ---------------------------------------------------------------------------
# embed_documents
# ---------------------------------------------------------------------------

class TestEmbedDocuments:
    def test_skips_already_embedded_docs(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"
        existing = {"path/a.md": [0.1, 0.2]}
        embeddings_path.write_text(json.dumps(existing))

        docs = [{"path": "path/a.md", "content": "some content"}]

        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path), \
             patch("embeddings.embed_text") as mock_embed:
            embed_documents(docs)
            mock_embed.assert_not_called()

    def test_embeds_new_documents(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"

        docs = [{"path": "path/new.md", "content": "new content here"}]
        fake_vec = [0.5, 0.5, 0.5]

        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path), \
             patch("embeddings.embed_text", return_value=fake_vec) as mock_embed:
            embed_documents(docs)
            mock_embed.assert_called_once()

        saved = json.loads(embeddings_path.read_text())
        assert saved["path/new.md"] == fake_vec

    def test_truncates_content_to_4000_chars(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"
        long_content = "x" * 10000
        docs = [{"path": "doc.md", "content": long_content}]

        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path), \
             patch("embeddings.embed_text", return_value=[0.1]) as mock_embed:
            embed_documents(docs)
            called_with = mock_embed.call_args[0][0]
            assert len(called_with) == 4000


# ---------------------------------------------------------------------------
# search
# ---------------------------------------------------------------------------

class TestSearch:
    def _make_docs(self, paths):
        return [{"path": p, "content": f"content for {p}"} for p in paths]

    def test_returns_top_n_results(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"

        paths = [f"doc{i}.md" for i in range(10)]
        stored = {p: [float(i), 0.0] for i, p in enumerate(paths)}
        embeddings_path.write_text(json.dumps(stored))

        docs = self._make_docs(paths)
        query_vec = [9.0, 0.0]  # most similar to doc9

        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path), \
             patch("embeddings.embed_text", return_value=query_vec):
            results = search("some query", docs, limit=3)

        assert len(results) == 3

    def test_skips_docs_without_embeddings(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"
        stored = {"only-this.md": [1.0, 0.0]}
        embeddings_path.write_text(json.dumps(stored))

        docs = self._make_docs(["only-this.md", "missing.md"])
        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path), \
             patch("embeddings.embed_text", return_value=[1.0, 0.0]):
            results = search("query", docs, limit=5)

        assert len(results) == 1
        assert results[0]["path"] == "only-this.md"

    def test_results_ordered_by_similarity(self, tmp_path):
        embeddings_path = tmp_path / "embeddings.json"

        stored = {
            "low.md": [0.0, 1.0],
            "high.md": [1.0, 0.0],
        }
        embeddings_path.write_text(json.dumps(stored))

        docs = self._make_docs(["low.md", "high.md"])
        query_vec = [1.0, 0.0]  # identical to high.md

        with patch("embeddings.EMBEDDINGS_FILE", embeddings_path), \
             patch("embeddings.embed_text", return_value=query_vec):
            results = search("query", docs, limit=5)

        assert results[0]["path"] == "high.md"
        assert results[1]["path"] == "low.md"

