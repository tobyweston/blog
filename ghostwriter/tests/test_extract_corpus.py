"""Tests for extract_corpus.py"""
from __future__ import annotations

import textwrap
from datetime import date, datetime
from pathlib import Path

import pytest

from extract_corpus import (
    clean_body,
    derive_date,
    derive_title,
    derive_year,
    iter_files,
    load_document,
    normalise_list,
    split_frontmatter,
)


# ---------------------------------------------------------------------------
# split_frontmatter
# ---------------------------------------------------------------------------

class TestSplitFrontmatter:
    def test_valid_frontmatter(self):
        from datetime import date as dt_date
        text = "---\ntitle: Hello\ndate: 2024-01-01\n---\nBody text."
        data, body = split_frontmatter(text)
        # YAML parses bare ISO dates as datetime.date objects
        assert data["title"] == "Hello"
        assert data["date"] == dt_date(2024, 1, 1)
        assert body.strip() == "Body text."

    def test_no_frontmatter(self):
        text = "Just some content"
        data, body = split_frontmatter(text)
        assert data == {}
        assert body == "Just some content"

    def test_empty_frontmatter(self):
        # "---\n---" has no content between delimiters so the regex doesn't match;
        # the whole string is returned as body with an empty dict.
        text = "---\n---\nBody."
        data, body = split_frontmatter(text)
        assert data == {}
        assert "Body." in body

    def test_malformed_yaml_returns_empty_dict(self):
        text = "---\n: bad: yaml: {{{\n---\nBody."
        data, body = split_frontmatter(text)
        assert data == {}
        assert "Body." in body

    def test_frontmatter_with_list_values(self):
        text = "---\ncategories:\n  - engineering\n  - testing\n---\nContent."
        data, body = split_frontmatter(text)
        assert data["categories"] == ["engineering", "testing"]

    def test_body_preserved_exactly(self):
        text = "---\ntitle: Test\n---\nLine 1\n\nLine 2\n"
        _, body = split_frontmatter(text)
        assert "Line 1" in body
        assert "Line 2" in body


# ---------------------------------------------------------------------------
# normalise_list
# ---------------------------------------------------------------------------

class TestNormaliseList:
    def test_none_returns_empty(self):
        assert normalise_list(None) == []

    def test_list_of_strings(self):
        assert normalise_list(["a", "b", "c"]) == ["a", "b", "c"]

    def test_list_with_empty_strings_filtered(self):
        assert normalise_list(["a", "", " ", "b"]) == ["a", "b"]

    def test_comma_separated_string(self):
        result = normalise_list("engineering, testing, python")
        assert result == ["engineering", "testing", "python"]

    def test_single_string(self):
        assert normalise_list("only-one") == ["only-one"]

    def test_other_type_coerced(self):
        result = normalise_list(42)
        assert result == ["42"]

    def test_list_with_non_strings_coerced(self):
        result = normalise_list([1, 2, 3])
        assert result == ["1", "2", "3"]


# ---------------------------------------------------------------------------
# derive_title
# ---------------------------------------------------------------------------

class TestDeriveTitle:
    def test_from_frontmatter(self, tmp_path):
        path = tmp_path / "some-slug.md"
        path.touch()
        title = derive_title(path, {"title": "My Great Post"})
        assert title == "My Great Post"

    def test_falls_back_to_slug(self, tmp_path):
        path = tmp_path / "my-cool-post.md"
        path.touch()
        title = derive_title(path, {})
        assert title == "My Cool Post"

    def test_strips_date_prefix_from_slug(self, tmp_path):
        path = tmp_path / "2024-03-15-my-article.md"
        path.touch()
        title = derive_title(path, {})
        assert title == "My Article"

    def test_strips_whitespace_from_frontmatter_title(self, tmp_path):
        path = tmp_path / "post.md"
        path.touch()
        title = derive_title(path, {"title": "  Trimmed  "})
        assert title == "Trimmed"


# ---------------------------------------------------------------------------
# derive_date
# ---------------------------------------------------------------------------

class TestDeriveDate:
    def test_date_from_frontmatter_string(self, tmp_path):
        path = tmp_path / "post.md"
        path.touch()
        assert derive_date(path, {"date": "2024-06-15"}) == "2024-06-15"

    def test_date_from_frontmatter_date_object(self, tmp_path):
        path = tmp_path / "post.md"
        path.touch()
        assert derive_date(path, {"date": date(2024, 6, 15)}) == "2024-06-15"

    def test_date_from_frontmatter_datetime_object(self, tmp_path):
        path = tmp_path / "post.md"
        path.touch()
        assert derive_date(path, {"date": datetime(2024, 6, 15, 12, 0)}) == "2024-06-15"

    def test_date_from_filename(self, tmp_path):
        path = tmp_path / "2024-03-01-my-post.md"
        path.touch()
        assert derive_date(path, {}) == "2024-03-01"

    def test_no_date_returns_empty_string(self, tmp_path):
        path = tmp_path / "no-date-post.md"
        path.touch()
        assert derive_date(path, {}) == ""

    def test_frontmatter_date_takes_priority_over_filename(self, tmp_path):
        path = tmp_path / "2020-01-01-old-post.md"
        path.touch()
        assert derive_date(path, {"date": "2024-06-15"}) == "2024-06-15"


# ---------------------------------------------------------------------------
# derive_year
# ---------------------------------------------------------------------------

class TestDeriveYear:
    def test_valid_date_string(self):
        assert derive_year("2024-06-15") == 2024

    def test_invalid_format_returns_none(self):
        assert derive_year("not-a-date") is None

    def test_empty_string_returns_none(self):
        assert derive_year("") is None

    def test_partial_date_returns_none(self):
        assert derive_year("2024-06") is None


# ---------------------------------------------------------------------------
# clean_body
# ---------------------------------------------------------------------------

class TestCleanBody:
    def test_removes_mdx_imports(self):
        text = "import Foo from './Foo.astro'\nSome content."
        result = clean_body(text)
        assert "import" not in result
        assert "Some content." in result

    def test_removes_mdx_exports(self):
        text = "export const x = 1\nSome content."
        result = clean_body(text)
        assert "export" not in result

    def test_removes_fenced_code_blocks(self):
        text = "Before.\n```python\nprint('hello')\n```\nAfter."
        result = clean_body(text)
        assert "print" not in result
        assert "Before." in result
        assert "After." in result

    def test_unwraps_inline_code(self):
        text = "Use `git commit` to save."
        result = clean_body(text)
        assert "`" not in result
        assert "git commit" in result

    def test_strips_markdown_images(self):
        text = "See ![alt text](https://example.com/img.png) for details."
        result = clean_body(text)
        assert "![" not in result
        assert "alt text" in result

    def test_strips_markdown_links_keeps_text(self):
        text = "Read [the docs](https://example.com) now."
        result = clean_body(text)
        assert "[" not in result
        assert "the docs" in result

    def test_strips_html_tags(self):
        text = "Hello <strong>world</strong>."
        result = clean_body(text)
        assert "<strong>" not in result
        assert "world" in result

    def test_normalises_excessive_newlines(self):
        text = "Para one.\n\n\n\n\nPara two."
        result = clean_body(text)
        assert "\n\n\n" not in result

    def test_strips_leading_trailing_whitespace(self):
        text = "  \n  Content.  \n  "
        result = clean_body(text)
        assert result == "Content."


# ---------------------------------------------------------------------------
# iter_files
# ---------------------------------------------------------------------------

class TestIterFiles:
    def test_yields_md_files(self, tmp_path):
        (tmp_path / "post.md").touch()
        (tmp_path / "article.mdx").touch()
        (tmp_path / "readme.txt").touch()
        paths = list(iter_files(tmp_path))
        names = {p.name for p in paths}
        assert "post.md" in names
        assert "article.mdx" in names
        assert "readme.txt" not in names

    def test_nonexistent_directory_yields_nothing(self, tmp_path):
        missing = tmp_path / "does_not_exist"
        assert list(iter_files(missing)) == []

    def test_results_are_sorted(self, tmp_path):
        (tmp_path / "b-post.md").touch()
        (tmp_path / "a-post.md").touch()
        paths = list(iter_files(tmp_path))
        names = [p.name for p in paths]
        assert names == sorted(names)


# ---------------------------------------------------------------------------
# load_document  (integration)
# ---------------------------------------------------------------------------

class TestLoadDocument:
    def test_loads_basic_document(self, tmp_path):
        content = textwrap.dedent("""\
            ---
            title: My Post
            date: 2024-06-15
            categories:
              - engineering
            topics:
              - testing
            description: A test post
            draft: false
            ---
            This is the body of the post.
        """)
        path = tmp_path / "2024-06-15-my-post.md"
        path.write_text(content, encoding="utf-8")

        doc = load_document(path, "blog")

        assert doc.title == "My Post"
        assert doc.date == "2024-06-15"
        assert doc.year == 2024
        assert doc.kind == "blog"
        assert doc.categories == ["engineering"]
        assert doc.topics == ["testing"]
        assert doc.description == "A test post"
        assert doc.draft is False
        assert "body of the post" in doc.content
        assert doc.word_count > 0

    def test_infers_title_from_slug_when_missing(self, tmp_path):
        content = "---\n---\nSome content."
        path = tmp_path / "my-great-article.md"
        path.write_text(content, encoding="utf-8")
        doc = load_document(path, "blog")
        assert doc.title == "My Great Article"

    def test_word_count_matches_content(self, tmp_path):
        content = "---\ntitle: Test\n---\none two three four five"
        path = tmp_path / "test.md"
        path.write_text(content, encoding="utf-8")
        doc = load_document(path, "blog")
        assert doc.word_count == 5

