"""Tests for generate_post.py"""
from __future__ import annotations

import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest


from generate_post import (
    extract_frontmatter_block,
    frontmatter_list_yaml,
    normalise_generated_document,
    parse_plan,
    parse_title_from_frontmatter,
)


# ---------------------------------------------------------------------------
# frontmatter_list_yaml
# ---------------------------------------------------------------------------

class TestFrontmatterListYaml:
    def test_empty_list_returns_empty_brackets(self):
        assert frontmatter_list_yaml([]) == "  []"

    def test_single_item(self):
        result = frontmatter_list_yaml(["engineering"])
        assert "engineering" in result
        assert result.startswith("  -")

    def test_multiple_items(self):
        result = frontmatter_list_yaml(["engineering", "testing"])
        lines = result.strip().splitlines()
        assert len(lines) == 2


# ---------------------------------------------------------------------------
# extract_frontmatter_block
# ---------------------------------------------------------------------------

class TestExtractFrontmatterBlock:
    def test_extracts_frontmatter_and_body(self):
        text = "---\ntitle: Hello\n---\nBody text."
        fm, body = extract_frontmatter_block(text)
        assert fm is not None
        assert "title: Hello" in fm
        assert "Body text." in body

    def test_returns_none_when_no_frontmatter(self):
        text = "Just a body."
        fm, body = extract_frontmatter_block(text)
        assert fm is None
        assert body == "Just a body."

    def test_body_does_not_include_frontmatter_delimiters(self):
        text = "---\ntitle: Test\n---\nThe body."
        _, body = extract_frontmatter_block(text)
        assert "---" not in body


# ---------------------------------------------------------------------------
# parse_title_from_frontmatter
# ---------------------------------------------------------------------------

class TestParseTitleFromFrontmatter:
    def test_parses_unquoted_title(self):
        fm = 'title: Hello World\ndate: 2024-01-01'
        assert parse_title_from_frontmatter(fm) == "Hello World"

    def test_parses_double_quoted_title(self):
        fm = 'title: "Hello World"\ndate: 2024-01-01'
        assert parse_title_from_frontmatter(fm) == "Hello World"

    def test_parses_single_quoted_title(self):
        fm = "title: 'Hello World'\ndate: 2024-01-01"
        assert parse_title_from_frontmatter(fm) == "Hello World"

    def test_returns_none_when_no_title(self):
        fm = "date: 2024-01-01\ndescription: test"
        assert parse_title_from_frontmatter(fm) is None

    def test_returns_none_for_none_input(self):
        assert parse_title_from_frontmatter(None) is None


# ---------------------------------------------------------------------------
# parse_plan
# ---------------------------------------------------------------------------

SAMPLE_PLAN = textwrap.dedent("""\
    # Post Plan

    ## Recommended title
    The Art of Saying No

    ## Alternative titles
    - On Refusing Requests
    - Learning to Push Back

    ## Reader
    Senior engineers dealing with excessive scope.

    ## Central insight
    Saying no is an act of clarity, not obstruction.

    ## Why this matters
    Teams that cannot say no ship the wrong things.

    ## Recommended framework
    Trust Lifecycle

    ## Opening options
    - Start with a story about a bloated sprint
    - Open with the cost of yes

    ## Outline
    1. The problem with yes-culture
    2. What a good no looks like
    3. How to say no without damaging relationships
    4. Practical techniques
    5. The long-term payoff

    ## Key arguments
    - Saying no protects quality
    - No is a form of trust
    - Yes-culture leads to burnout

    ## Things to avoid
    - Being preachy
    - Generic agile advice

    ## Suggested categories
    - engineering
    - leadership

    ## Suggested topics
    - communication
    - team dynamics
""")


class TestParsePlan:
    def test_extracts_recommended_title(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert plan["recommended_title"] == "The Art of Saying No"

    def test_extracts_alternative_titles(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert "On Refusing Requests" in plan["alternative_titles"]
        assert "Learning to Push Back" in plan["alternative_titles"]

    def test_extracts_central_insight(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert "clarity" in plan["central_insight"]

    def test_extracts_outline_as_list(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert len(plan["outline"]) == 5
        assert "yes-culture" in plan["outline"][0]

    def test_extracts_key_arguments(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert any("quality" in arg for arg in plan["key_arguments"])

    def test_extracts_suggested_categories(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert "engineering" in plan["suggested_categories"]
        assert "leadership" in plan["suggested_categories"]

    def test_extracts_suggested_topics(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert "communication" in plan["suggested_topics"]

    def test_extracts_recommended_framework(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert plan["recommended_framework"] == "Trust Lifecycle"

    def test_raw_contains_full_text(self):
        plan = parse_plan_from_str(SAMPLE_PLAN)
        assert "Art of Saying No" in plan["raw"]

    def test_missing_section_returns_empty(self):
        plan = parse_plan_from_str("# Post Plan\n\n## Recommended title\nTitle Only\n")
        assert plan["outline"] == []


def parse_plan_from_str(text: str) -> dict:
    """Helper: write plan to a tmp file and parse it."""
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(text)
        name = f.name
    try:
        return parse_plan(Path(name))
    finally:
        os.unlink(name)


# ---------------------------------------------------------------------------
# normalise_generated_document
# ---------------------------------------------------------------------------

class TestNormaliseGeneratedDocument:
    def test_produces_valid_frontmatter(self):
        raw = "---\ntitle: My Post\n---\n# My Post\n\nBody content here."
        result = normalise_generated_document(
            raw,
            fallback_title="Fallback",
            categories=["engineering"],
            topics=["testing"],
        )
        assert result.startswith("---\n")
        fm, body = extract_frontmatter_block(result)
        assert fm is not None
        assert "title:" in fm
        assert "date:" in fm
        assert "categories:" in fm
        assert "topics:" in fm

    def test_uses_title_from_generated_frontmatter(self):
        raw = "---\ntitle: Generated Title\n---\nBody."
        result = normalise_generated_document(
            raw,
            fallback_title="Fallback",
            categories=[],
            topics=[],
        )
        fm, _ = extract_frontmatter_block(result)
        assert "Generated Title" in fm

    def test_uses_fallback_title_when_none_in_generated(self):
        raw = "No frontmatter here, just body text."
        result = normalise_generated_document(
            raw,
            fallback_title="My Fallback Title",
            categories=[],
            topics=[],
        )
        fm, _ = extract_frontmatter_block(result)
        assert "My Fallback Title" in fm

    def test_injects_categories_and_topics(self):
        raw = "---\ntitle: Test\n---\nBody."
        result = normalise_generated_document(
            raw,
            fallback_title="Test",
            categories=["engineering", "leadership"],
            topics=["deployment"],
        )
        assert "engineering" in result
        assert "deployment" in result

    def test_auto_generates_description_from_body(self):
        raw = "---\ntitle: Test\n---\nThis is the opening paragraph of the post."
        result = normalise_generated_document(
            raw,
            fallback_title="Test",
            categories=[],
            topics=[],
        )
        fm, _ = extract_frontmatter_block(result)
        assert "description:" in fm

    def test_body_is_preserved(self):
        body_text = "This is the real body of the article."
        raw = f"---\ntitle: Test\n---\n{body_text}"
        result = normalise_generated_document(
            raw,
            fallback_title="Test",
            categories=[],
            topics=[],
        )
        assert body_text in result

    def test_result_ends_with_newline(self):
        raw = "---\ntitle: Test\n---\nBody."
        result = normalise_generated_document(
            raw,
            fallback_title="Test",
            categories=[],
            topics=[],
        )
        assert result.endswith("\n")

