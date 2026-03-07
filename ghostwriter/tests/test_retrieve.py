"""Tests for retrieve.py"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


from retrieve import (
    gather_candidate_files,
    infer_post_slug,
    iter_text_files,
    load_frameworks,
    load_notes_files,
    load_research_files,
    load_text_file,
    pick_frameworks,
    pick_notes,
    pick_research,
    pick_topic_samples,
    pick_voice_anchors,
    score_text,
    slugify,
    tokenize,
)


# ---------------------------------------------------------------------------
# tokenize / slugify
# ---------------------------------------------------------------------------

class TestTokenize:
    def test_extracts_words(self):
        tokens = tokenize("Hello World foo")
        assert "hello" in tokens
        assert "world" in tokens
        assert "foo" in tokens

    def test_minimum_length_three(self):
        tokens = tokenize("ab abc abcd")
        assert "ab" not in tokens
        assert "abc" in tokens
        assert "abcd" in tokens

    def test_case_insensitive(self):
        tokens = tokenize("Engineering ENGINEERING engineering")
        assert len(tokens) == 1

    def test_returns_set(self):
        result = tokenize("hello hello world")
        assert isinstance(result, set)


class TestSlugify:
    def test_basic_slugification(self):
        assert slugify("Hello World") == "hello-world"

    def test_strips_special_chars(self):
        assert slugify("Hello, World!") == "hello-world"

    def test_collapses_multiple_hyphens(self):
        assert slugify("Hello   World") == "hello-world"

    def test_strips_leading_trailing_hyphens(self):
        result = slugify("  --  Hello  --  ")
        assert not result.startswith("-")
        assert not result.endswith("-")

    def test_empty_string(self):
        assert slugify("") == ""


# ---------------------------------------------------------------------------
# score_text
# ---------------------------------------------------------------------------

class TestScoreText:
    def test_exact_match_scores_higher_than_no_match(self):
        blob = "engineering leadership deployment pipelines"
        high = score_text(blob, "engineering deployment")
        low = score_text(blob, "cooking recipes baking")
        assert high > low

    def test_no_overlap_returns_zero(self):
        assert score_text("engineering testing", "cooking baking") == 0

    def test_full_overlap_returns_word_count(self):
        assert score_text("alpha beta gamma", "alpha beta gamma") == 3


# ---------------------------------------------------------------------------
# load_text_file
# ---------------------------------------------------------------------------

class TestLoadTextFile:
    def test_loads_content_and_metadata(self, tmp_path):
        path = tmp_path / "my-research.md"
        path.write_text("# Research\nsome content", encoding="utf-8")

        result = load_text_file(path)
        assert result["path"] == str(path)
        assert result["name"] == "my-research"
        assert "some content" in result["content"]


# ---------------------------------------------------------------------------
# iter_text_files
# ---------------------------------------------------------------------------

class TestIterTextFiles:
    def test_yields_md_and_txt_only(self, tmp_path):
        (tmp_path / "a.md").touch()
        (tmp_path / "b.txt").touch()
        (tmp_path / "c.py").touch()
        names = {p.name for p in iter_text_files(tmp_path)}
        assert names == {"a.md", "b.txt"}

    def test_returns_empty_for_missing_directory(self, tmp_path):
        assert iter_text_files(tmp_path / "nope") == []

    def test_returns_sorted(self, tmp_path):
        (tmp_path / "z.md").touch()
        (tmp_path / "a.md").touch()
        paths = iter_text_files(tmp_path)
        assert paths == sorted(paths)


# ---------------------------------------------------------------------------
# infer_post_slug
# ---------------------------------------------------------------------------

class TestInferPostSlug:
    def test_slugifies_topic(self):
        assert infer_post_slug("My Great Topic") == "my-great-topic"

    def test_returns_none_for_none(self):
        assert infer_post_slug(None) is None

    def test_returns_none_for_empty_string(self):
        assert infer_post_slug("") is None

    def test_returns_none_for_whitespace_only(self):
        assert infer_post_slug("   ") is None


# ---------------------------------------------------------------------------
# gather_candidate_files
# ---------------------------------------------------------------------------

class TestGatherCandidateFiles:
    def test_loads_common_files(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        (common / "shared.md").write_text("Shared content", encoding="utf-8")

        files = gather_candidate_files(
            common_dir=common,
            posts_dir=tmp_path / "post",
        )
        assert any(f["name"] == "shared" for f in files)

    def test_loads_per_post_files_when_topic_given(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        post_dir = tmp_path / "post" / "my-topic"
        post_dir.mkdir(parents=True)
        (post_dir / "notes.md").write_text("Post-specific notes", encoding="utf-8")

        files = gather_candidate_files(
            common_dir=common,
            posts_dir=tmp_path / "post",
            topic_or_query="My Topic",
        )
        assert any(f["name"] == "notes" for f in files)

    def test_merges_common_and_post_files(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        (common / "shared.md").write_text("Shared", encoding="utf-8")
        post_dir = tmp_path / "post" / "my-topic"
        post_dir.mkdir(parents=True)
        (post_dir / "specific.md").write_text("Specific", encoding="utf-8")

        files = gather_candidate_files(
            common_dir=common,
            posts_dir=tmp_path / "post",
            topic_or_query="My Topic",
        )
        names = {f["name"] for f in files}
        assert "shared" in names
        assert "specific" in names

    def test_explicit_paths_override_directory_scan(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        (common / "ignored.md").write_text("Should be ignored", encoding="utf-8")
        explicit = tmp_path / "explicit.md"
        explicit.write_text("Explicit content", encoding="utf-8")

        files = gather_candidate_files(
            common_dir=common,
            posts_dir=tmp_path / "post",
            explicit_paths=[str(explicit)],
        )
        names = {f["name"] for f in files}
        assert names == {"explicit"}

    def test_skips_missing_explicit_paths(self, tmp_path):
        files = gather_candidate_files(
            common_dir=tmp_path / "common",
            posts_dir=tmp_path / "post",
            explicit_paths=[str(tmp_path / "missing.md")],
        )
        assert files == []

    def test_no_post_dir_match_still_returns_common(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        (common / "shared.md").write_text("Shared", encoding="utf-8")

        files = gather_candidate_files(
            common_dir=common,
            posts_dir=tmp_path / "post",
            topic_or_query="topic-with-no-post-dir",
        )
        assert len(files) == 1
        assert files[0]["name"] == "shared"


# ---------------------------------------------------------------------------
# load_frameworks
# ---------------------------------------------------------------------------

VALID_FRAMEWORK_MD = textwrap.dedent("""\
    ---
    name: Trust Lifecycle
    slug: trust-lifecycle
    topics:
      - trust
      - delivery
    when_to_use:
      - when discussing team dynamics
    summary: A framework for thinking about trust.
    key_claims:
      - Trust is earned incrementally
    argument_patterns:
      - show don't tell
    example_phrasing:
      - "trust is built through..."
    guardrails:
      - avoid prescriptive advice
    ---
    Body content of the framework.
""")


class TestLoadFrameworks:
    def test_loads_valid_framework(self, tmp_path):
        fw_file = tmp_path / "trust-lifecycle.md"
        fw_file.write_text(VALID_FRAMEWORK_MD, encoding="utf-8")

        with patch("retrieve.FRAMEWORKS_DIR", tmp_path):
            frameworks = load_frameworks()

        assert len(frameworks) == 1
        fw = frameworks[0]
        assert fw["name"] == "Trust Lifecycle"
        assert fw["summary"] == "A framework for thinking about trust."
        assert "Trust is earned incrementally" in fw["key_claims"]
        assert "Body content" in fw["body"]

    def test_skips_file_without_frontmatter(self, tmp_path):
        bad_file = tmp_path / "no-frontmatter.md"
        bad_file.write_text("Just a body, no frontmatter.", encoding="utf-8")

        with patch("retrieve.FRAMEWORKS_DIR", tmp_path):
            frameworks = load_frameworks()

        assert frameworks == []

    def test_returns_empty_list_when_dir_missing(self, tmp_path):
        missing = tmp_path / "no_frameworks"
        with patch("retrieve.FRAMEWORKS_DIR", missing):
            frameworks = load_frameworks()
        assert frameworks == []

    def test_sorted_by_filename(self, tmp_path):
        for name in ["b-fw.md", "a-fw.md"]:
            path = tmp_path / name
            path.write_text(VALID_FRAMEWORK_MD, encoding="utf-8")

        with patch("retrieve.FRAMEWORKS_DIR", tmp_path):
            frameworks = load_frameworks()

        names = [fw["name"] for fw in frameworks]
        # both will have the same "name" from frontmatter, but should load both
        assert len(names) == 2


# ---------------------------------------------------------------------------
# load_research_files / load_notes_files
# ---------------------------------------------------------------------------

class TestLoadResearchFiles:
    def test_loads_all_files_when_no_paths_given(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        (common / "research1.md").write_text("Research one", encoding="utf-8")
        (common / "research2.txt").write_text("Research two", encoding="utf-8")
        (common / "skip.py").write_text("not loaded", encoding="utf-8")

        with patch("retrieve.RESEARCH_COMMON_DIR", common), \
             patch("retrieve.RESEARCH_POSTS_DIR", tmp_path / "post"):
            files = load_research_files()

        names = {f["name"] for f in files}
        assert "research1" in names
        assert "research2" in names
        assert "skip" not in names

    def test_loads_specific_paths(self, tmp_path):
        path = tmp_path / "specific.md"
        path.write_text("Specific content", encoding="utf-8")

        files = load_research_files([str(path)])
        assert len(files) == 1
        assert "Specific content" in files[0]["content"]

    def test_skips_missing_specific_paths(self, tmp_path):
        missing = str(tmp_path / "does_not_exist.md")
        files = load_research_files([missing])
        assert files == []


class TestLoadNotesFiles:
    def test_loads_notes_from_directory(self, tmp_path):
        common = tmp_path / "common"
        common.mkdir()
        (common / "note1.md").write_text("Note one", encoding="utf-8")

        with patch("retrieve.NOTES_COMMON_DIR", common), \
             patch("retrieve.NOTES_POSTS_DIR", tmp_path / "post"):
            files = load_notes_files()

        assert len(files) == 1
        assert "Note one" in files[0]["content"]

    def test_loads_specific_notes_paths(self, tmp_path):
        path = tmp_path / "my-note.md"
        path.write_text("My note content", encoding="utf-8")
        files = load_notes_files([str(path)])
        assert len(files) == 1


# ---------------------------------------------------------------------------
# pick_frameworks
# ---------------------------------------------------------------------------

class TestPickFrameworks:
    def _make_framework(self, name, summary, topics=None):
        return {
            "name": name,
            "slug": name.lower().replace(" ", "-"),
            "summary": summary,
            "topics": topics or [],
            "when_to_use": [],
            "key_claims": [],
            "argument_patterns": [],
            "example_phrasing": [],
            "guardrails": [],
            "body": "",
        }

    def test_returns_top_matching_frameworks(self):
        frameworks = [
            self._make_framework("Trust Framework", "about trust and delivery in teams"),
            self._make_framework("Code Review Framework", "about code quality engineering review"),
            self._make_framework("Unrelated Framework", "about cooking and recipes"),
        ]

        with patch("retrieve.load_frameworks", return_value=frameworks):
            results = pick_frameworks("code quality engineering review", limit=2)

        names = [fw["name"] for fw in results]
        assert "Code Review Framework" in names

    def test_respects_limit(self):
        frameworks = [
            self._make_framework(f"Framework {i}", f"about topic {i} engineering")
            for i in range(10)
        ]

        with patch("retrieve.load_frameworks", return_value=frameworks):
            results = pick_frameworks("engineering", limit=3)

        assert len(results) <= 3

    def test_falls_back_to_top_when_no_match(self):
        frameworks = [
            self._make_framework("Framework A", "about engineering systems"),
            self._make_framework("Framework B", "about deployment pipelines"),
        ]

        with patch("retrieve.load_frameworks", return_value=frameworks):
            results = pick_frameworks("cooking", limit=2)

        assert len(results) == 2


# ---------------------------------------------------------------------------
# pick_voice_anchors
# ---------------------------------------------------------------------------

class TestPickVoiceAnchors:
    def _make_corpus(self):
        return [
            {"kind": "blog", "content": "Post content", "date": "2024-01-01", "title": "Post A"},
            {"kind": "blog", "content": "Post content", "date": "2023-06-01", "title": "Post B"},
            {"kind": "unpublished", "content": "Draft content", "date": "2024-05-01", "title": "Draft"},
            {"kind": "blog", "content": "", "date": "2024-03-01", "title": "Empty"},
        ]

    def test_returns_only_blog_posts(self):
        corpus = self._make_corpus()
        with patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_voice_anchors()
        kinds = {doc["kind"] for doc in results}
        assert kinds == {"blog"}

    def test_excludes_empty_content(self):
        corpus = self._make_corpus()
        with patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_voice_anchors()
        for doc in results:
            assert doc["content"].strip() != ""

    def test_sorted_by_date_descending(self):
        corpus = self._make_corpus()
        with patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_voice_anchors()
        dates = [doc["date"] for doc in results]
        assert dates == sorted(dates, reverse=True)

    def test_respects_limit(self):
        corpus = [
            {"kind": "blog", "content": f"Content {i}", "date": f"202{i}-01-01", "title": f"Post {i}"}
            for i in range(10)
        ]
        with patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_voice_anchors(limit=3)
        assert len(results) == 3


# ---------------------------------------------------------------------------
# pick_research / pick_notes
# ---------------------------------------------------------------------------

class TestPickResearch:
    """pick_research without explicit paths delegates to semantic_search (FAISS vector path)."""

    def _make_hit(self, tmp_path, name="relevant"):
        path = tmp_path / f"{name}.md"
        path.write_text("engineering deployment pipelines testing", encoding="utf-8")
        return [{"source_path": str(path), "score": 0.9}]

    def test_returns_results_from_semantic_search(self, tmp_path):
        hits = self._make_hit(tmp_path)
        with patch("retrieve.semantic_search", return_value=hits), \
             patch("retrieve.rehydrate_text_files", return_value=[{"name": "relevant", "content": "..."}]):
            results = pick_research("engineering deployment", limit=5)
        assert len(results) >= 1

    def test_returns_up_to_limit(self, tmp_path):
        hits = [{"source_path": str(tmp_path / f"doc{i}.md"), "score": 0.9} for i in range(5)]
        rehydrated = [{"name": f"doc{i}", "content": "..."} for i in range(5)]
        with patch("retrieve.semantic_search", return_value=hits), \
             patch("retrieve.rehydrate_text_files", return_value=rehydrated):
            results = pick_research("engineering", limit=2)
        assert len(results) <= 2

    def test_explicit_paths_bypass_semantic_search(self, tmp_path):
        """When paths= is given the keyword-scoring path is used, not semantic_search."""
        path = tmp_path / "explicit.md"
        path.write_text("engineering deployment pipelines testing", encoding="utf-8")
        with patch("retrieve.semantic_search") as mock_ss:
            results = pick_research("engineering", paths=[str(path)])
        mock_ss.assert_not_called()
        assert len(results) == 1

    def test_explicit_paths_ranked_by_keyword_score(self, tmp_path):
        high = tmp_path / "high.md"
        low = tmp_path / "low.md"
        high.write_text("engineering deployment pipelines testing analysis", encoding="utf-8")
        low.write_text("cooking recipes baking", encoding="utf-8")
        results = pick_research("engineering deployment", paths=[str(high), str(low)])
        # high-scoring doc should come first
        assert results[0]["name"] == "high"


class TestPickNotes:
    """pick_notes without explicit paths delegates to semantic_search (FAISS vector path)."""

    def test_returns_results_from_semantic_search(self, tmp_path):
        path = tmp_path / "ideas.md"
        path.write_text("system design architecture microservices", encoding="utf-8")
        hits = [{"source_path": str(path), "score": 0.9}]
        rehydrated = [{"name": "ideas", "content": "system design architecture microservices"}]
        with patch("retrieve.semantic_search", return_value=hits), \
             patch("retrieve.rehydrate_text_files", return_value=rehydrated):
            results = pick_notes("microservices architecture", limit=5)
        assert len(results) >= 1

    def test_explicit_paths_bypass_semantic_search(self, tmp_path):
        path = tmp_path / "my-note.md"
        path.write_text("microservices architecture patterns", encoding="utf-8")
        with patch("retrieve.semantic_search") as mock_ss:
            results = pick_notes("microservices", paths=[str(path)])
        mock_ss.assert_not_called()
        assert len(results) == 1

    def test_returns_empty_when_no_hits(self):
        with patch("retrieve.semantic_search", return_value=[]), \
             patch("retrieve.rehydrate_text_files", return_value=[]):
            results = pick_notes("unknown topic")
        assert results == []


# ---------------------------------------------------------------------------
# pick_topic_samples
# ---------------------------------------------------------------------------

class TestPickTopicSamples:
    """pick_topic_samples uses semantic_search first, falls back to keyword scoring."""

    def _make_corpus(self):
        return [
            {
                "path": "/blog/post-a.md",
                "kind": "blog",
                "title": "Engineering Deployment",
                "description": "About deployment pipelines",
                "categories": ["engineering"],
                "topics": ["deployment"],
                "content": "engineering deployment pipelines testing",
                "date": "2024-01-01",
            },
            {
                "path": "/blog/post-b.md",
                "kind": "blog",
                "title": "Cooking Basics",
                "description": "About cooking",
                "categories": ["lifestyle"],
                "topics": [],
                "content": "cooking recipes baking bread",
                "date": "2023-06-01",
            },
        ]

    def test_returns_hits_from_semantic_search(self):
        corpus = self._make_corpus()
        hits = [{"source_path": "/blog/post-a.md", "score": 0.9}]
        with patch("retrieve.semantic_search", return_value=hits), \
             patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_topic_samples("deployment engineering", limit=3)
        assert len(results) == 1
        assert results[0]["title"] == "Engineering Deployment"

    def test_falls_back_to_keyword_when_no_semantic_hits(self):
        corpus = self._make_corpus()
        with patch("retrieve.semantic_search", return_value=[]), \
             patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_topic_samples("deployment engineering", limit=3)
        assert any(r["title"] == "Engineering Deployment" for r in results)

    def test_respects_limit(self):
        corpus = [
            {
                "path": f"/blog/post-{i}.md",
                "kind": "blog",
                "title": f"Post {i}",
                "description": "",
                "categories": ["engineering"],
                "topics": [],
                "content": f"engineering content post {i}",
                "date": f"202{i % 10}-01-01",
            }
            for i in range(10)
        ]
        hits = [{"source_path": f"/blog/post-{i}.md", "score": 0.9} for i in range(10)]
        with patch("retrieve.semantic_search", return_value=hits), \
             patch("retrieve.ensure_corpus", return_value=corpus):
            results = pick_topic_samples("engineering", limit=3)
        assert len(results) <= 3

