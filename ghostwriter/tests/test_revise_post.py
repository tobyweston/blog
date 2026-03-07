"""Tests for revise_post.py"""
from __future__ import annotations

from pathlib import Path

import pytest


from revise_post import REVISION_MODES, slug_suffix


# ---------------------------------------------------------------------------
# slug_suffix
# ---------------------------------------------------------------------------

class TestSlugSuffix:
    def test_lowercases_mode(self):
        assert slug_suffix("TIGHTEN") == "tighten"

    def test_replaces_non_alphanumeric_with_hyphen(self):
        result = slug_suffix("stronger-hook")
        assert result == "stronger-hook"

    def test_strips_leading_trailing_hyphens(self):
        result = slug_suffix("  tighten  ")
        assert not result.startswith("-")
        assert not result.endswith("-")

    def test_collapses_consecutive_non_alphanumeric(self):
        result = slug_suffix("more like me")
        assert "--" not in result
        assert result == "more-like-me"


# ---------------------------------------------------------------------------
# REVISION_MODES registry
# ---------------------------------------------------------------------------

class TestRevisionModes:
    EXPECTED_MODES = {
        "tighten",
        "stronger-hook",
        "more-like-me",
        "less-tutorial",
        "more-opinionated",
        "add-framework",
        "sharpen-argument",
    }

    def test_all_expected_modes_present(self):
        assert set(REVISION_MODES.keys()) == self.EXPECTED_MODES

    def test_all_instructions_are_non_empty_strings(self):
        for mode, instruction in REVISION_MODES.items():
            assert isinstance(instruction, str), f"Mode {mode} instruction is not a string"
            assert len(instruction.strip()) > 0, f"Mode {mode} has empty instruction"

    def test_tighten_mentions_voice(self):
        assert "voice" in REVISION_MODES["tighten"].lower()

    def test_more_like_me_mentions_style_profile(self):
        assert "style profile" in REVISION_MODES["more-like-me"].lower()

    def test_sharpen_argument_mentions_central(self):
        assert "central" in REVISION_MODES["sharpen-argument"].lower()

