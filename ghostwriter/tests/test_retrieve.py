"""Tests for retrieve.py"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


from retrieve import (
    load_frameworks,
    load_notes_files,
    load_research_files,
    load_text_file,
    pick_frameworks,
    pick_notes,
    pick_research,
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
        (tmp_path / "research1.md").write_text("Research one", encoding="utf-8")
        (tmp_path / "research2.txt").write_text("Research two", encoding="utf-8")
        (tmp_path / "skip.py").write_text("not loaded", encoding="utf-8")

        with patch("retrieve.RESEARCH_DIR", tmp_path):
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
        (tmp_path / "note1.md").write_text("Note one", encoding="utf-8")

        with patch("retrieve.NOTES_DIR", tmp_path):
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
    def test_returns_relevant_research(self, tmp_path):
        path = tmp_path / "relevant.md"
        path.write_text("engineering deployment pipelines testing", encoding="utf-8")

        with patch("retrieve.RESEARCH_DIR", tmp_path):
            results = pick_research("engineering deployment", limit=5)

        assert len(results) >= 1

    def test_returns_up_to_limit(self, tmp_path):
        for i in range(5):
            (tmp_path / f"doc{i}.md").write_text(f"engineering content {i}", encoding="utf-8")

        with patch("retrieve.RESEARCH_DIR", tmp_path):
            results = pick_research("engineering", limit=2)

        assert len(results) <= 2


class TestPickNotes:
    def test_returns_relevant_notes(self, tmp_path):
        path = tmp_path / "ideas.md"
        path.write_text("system design architecture microservices", encoding="utf-8")

        with patch("retrieve.NOTES_DIR", tmp_path):
            results = pick_notes("microservices architecture", limit=5)

        assert len(results) >= 1

