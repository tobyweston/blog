"""Tests for evaluate_post.py"""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest


from evaluate_post import build_prompt, load_draft, load_style_profile


# ---------------------------------------------------------------------------
# load_style_profile
# ---------------------------------------------------------------------------

class TestLoadStyleProfile:
    def test_loads_valid_profile(self, tmp_path):
        profile = {"voice_summary": "Technical writer", "tone": {"overall": "direct"}}
        profile_path = tmp_path / "style_profile.json"
        profile_path.write_text(json.dumps(profile), encoding="utf-8")

        with patch("evaluate_post.STYLE_PROFILE_JSON", profile_path):
            result = load_style_profile()

        assert result["voice_summary"] == "Technical writer"

    def test_raises_system_exit_when_missing(self, tmp_path):
        missing = tmp_path / "no_profile.json"
        with patch("evaluate_post.STYLE_PROFILE_JSON", missing):
            with pytest.raises(SystemExit):
                load_style_profile()


# ---------------------------------------------------------------------------
# load_draft
# ---------------------------------------------------------------------------

class TestLoadDraft:
    def test_loads_existing_file(self, tmp_path):
        draft = tmp_path / "draft.md"
        draft.write_text("# My Draft\n\nSome content.", encoding="utf-8")
        content = load_draft(draft)
        assert "My Draft" in content

    def test_raises_system_exit_when_missing(self, tmp_path):
        missing = tmp_path / "not_found.md"
        with pytest.raises(SystemExit):
            load_draft(missing)


# ---------------------------------------------------------------------------
# build_prompt
# ---------------------------------------------------------------------------

class TestBuildPrompt:
    PROFILE = {
        "voice_summary": "Technical engineering writer",
        "tone": {"overall": "direct", "traits": ["precise"]},
        "dos": ["Be clear"],
        "donts": ["Avoid hype"],
    }

    DRAFT = "# My Draft\n\nThis is the draft content.\n"

    def test_prompt_contains_style_profile(self):
        prompt = build_prompt(self.PROFILE, self.DRAFT)
        assert "voice_summary" in prompt
        assert "Technical engineering writer" in prompt

    def test_prompt_contains_draft(self):
        prompt = build_prompt(self.PROFILE, self.DRAFT)
        assert "This is the draft content." in prompt

    def test_prompt_contains_rubric_sections(self):
        prompt = build_prompt(self.PROFILE, self.DRAFT)
        for section in ["Voice fidelity", "Central idea", "Originality", "Clarity"]:
            assert section in prompt

    def test_prompt_asks_for_markdown_output(self):
        prompt = build_prompt(self.PROFILE, self.DRAFT)
        assert "markdown" in prompt.lower()

