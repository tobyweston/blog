"""Tests for plan_post.py"""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from plan_post import build_prompt, csv_list, write_plan


# ---------------------------------------------------------------------------
# csv_list
# ---------------------------------------------------------------------------

class TestCsvList:
    def test_none_returns_empty(self):
        assert csv_list(None) == []

    def test_empty_string_returns_empty(self):
        assert csv_list("") == []

    def test_single_value(self):
        assert csv_list("engineering") == ["engineering"]

    def test_multiple_values_split_and_stripped(self):
        assert csv_list("engineering, testing, deployment") == [
            "engineering", "testing", "deployment"
        ]

    def test_filters_blank_segments(self):
        result = csv_list("engineering,,testing")
        assert result == ["engineering", "testing"]

    def test_trims_whitespace(self):
        assert csv_list("  alpha  ,  beta  ") == ["alpha", "beta"]

    # --- list inputs (from nargs='+') ---

    def test_list_of_single_item(self):
        assert csv_list(["file1.md"]) == ["file1.md"]

    def test_list_of_multiple_items(self):
        assert csv_list(["file1.md", "file2.md"]) == ["file1.md", "file2.md"]

    def test_empty_list_returns_empty(self):
        assert csv_list([]) == []

    def test_list_items_can_themselves_be_comma_separated(self):
        # e.g. user types --research a.md,b.md c.md
        assert csv_list(["a.md,b.md", "c.md"]) == ["a.md", "b.md", "c.md"]

    def test_list_items_stripped(self):
        assert csv_list(["  a.md  ", "  b.md  "]) == ["a.md", "b.md"]


# ---------------------------------------------------------------------------
# write_plan
# ---------------------------------------------------------------------------

class TestWritePlan:
    def test_creates_file(self, tmp_path):
        with patch("plan_post.PLANS_DIR", tmp_path):
            path = write_plan("my topic", "# Plan content")
        assert path.exists()

    def test_file_contains_content(self, tmp_path):
        with patch("plan_post.PLANS_DIR", tmp_path):
            path = write_plan("my topic", "# Plan content")
        assert path.read_text(encoding="utf-8") == "# Plan content"

    def test_filename_contains_slug(self, tmp_path):
        with patch("plan_post.PLANS_DIR", tmp_path):
            path = write_plan("my topic", "content")
        assert "my-topic" in path.name

    def test_filename_contains_today(self, tmp_path):
        from datetime import date
        with patch("plan_post.PLANS_DIR", tmp_path):
            path = write_plan("my topic", "content")
        assert date.today().isoformat() in path.name

    def test_filename_has_plan_md_extension(self, tmp_path):
        with patch("plan_post.PLANS_DIR", tmp_path):
            path = write_plan("my topic", "content")
        assert path.name.endswith(".plan.md")

    def test_empty_topic_falls_back_to_untitled(self, tmp_path):
        with patch("plan_post.PLANS_DIR", tmp_path):
            path = write_plan("", "content")
        assert "untitled" in path.name


# ---------------------------------------------------------------------------
# build_prompt
# ---------------------------------------------------------------------------

SAMPLE_STYLE_PROFILE = {
    "voice_summary": "Thoughtful technical writer",
    "tone": {"overall": "direct", "traits": ["precise"]},
    "dos": ["Be clear"],
    "donts": ["Avoid hype"],
}


class TestBuildPrompt:
    def _call(self, **overrides):
        kwargs = dict(
            topic="software delivery as a trust problem",
            angle="Focus on the feedback loop",
            notes="Think about pipelines",
            audience="Senior engineers",
            style_profile=SAMPLE_STYLE_PROFILE,
            frameworks=[],
            samples=[],
            research=[],
            notes_files=[],
        )
        kwargs.update(overrides)
        return build_prompt(**kwargs)

    def test_prompt_contains_topic(self):
        prompt = self._call()
        assert "software delivery as a trust problem" in prompt

    def test_prompt_contains_angle(self):
        prompt = self._call()
        assert "Focus on the feedback loop" in prompt

    def test_prompt_contains_inline_notes(self):
        prompt = self._call()
        assert "Think about pipelines" in prompt

    def test_prompt_contains_audience(self):
        prompt = self._call()
        assert "Senior engineers" in prompt

    def test_prompt_contains_style_profile(self):
        prompt = self._call()
        assert "Thoughtful technical writer" in prompt

    def test_prompt_mentions_british_english(self):
        prompt = self._call()
        assert "British English" in prompt

    def test_empty_frameworks_shows_none(self):
        prompt = self._call(frameworks=[])
        assert "None" in prompt

    def test_framework_name_appears_in_prompt(self):
        fw = {
            "name": "Trust Lifecycle",
            "summary": "A trust model.",
            "key_claims": ["Trust is earned"],
            "argument_patterns": [],
            "example_phrasing": [],
            "guardrails": [],
        }
        prompt = self._call(frameworks=[fw])
        assert "Trust Lifecycle" in prompt

    def test_research_item_appears_in_prompt(self):
        research = [{"name": "delivery-risk.md", "content": "Risk is a function of feedback speed."}]
        prompt = self._call(research=research)
        assert "delivery-risk.md" in prompt
        assert "Risk is a function" in prompt

    def test_notes_file_appears_in_prompt(self):
        notes_files = [{"name": "rough-ideas.md", "content": "Fragment about trust."}]
        prompt = self._call(notes_files=notes_files)
        assert "rough-ideas.md" in prompt

    def test_sample_excerpt_appears_in_prompt(self):
        samples = [{"title": "Post A", "date": "2024-01-01", "categories": [], "topics": [], "content": "Unique sample content here."}]
        prompt = self._call(samples=samples)
        assert "Unique sample content here." in prompt

    def test_no_angle_falls_back_to_default(self):
        prompt = self._call(angle=None)
        assert "strongest angle" in prompt

    def test_no_notes_shows_none(self):
        prompt = self._call(notes=None)
        assert "None" in prompt

    def test_prompt_requests_post_plan_structure(self):
        prompt = self._call()
        for section in ["## Recommended title", "## Outline", "## Key arguments"]:
            assert section in prompt

    def test_prompt_is_non_empty_string(self):
        prompt = self._call()
        assert isinstance(prompt, str)
        assert len(prompt) > 500

