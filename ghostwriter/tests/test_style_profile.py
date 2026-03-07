"""Tests for style_profile.py"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest


from style_profile import (
    build_analysis_prompt,
    choose_analysis_docs,
    ending_lines,
    heuristic_profile,
    metadata_counts,
    opening_lines,
    paragraph_stats,
    render_markdown,
    sentence_stats,
    split_paragraphs,
    split_sentences,
    stopwords,
    tokenise_words,
    top_terms,
)


SAMPLE_DOCS = [
    {
        "kind": "blog",
        "content": "This is the first sentence. Here is a second one. And a third.\n\nNew paragraph here. Another sentence.",
        "date": "2024-01-01",
        "year": 2024,
        "title": "Post One",
        "categories": ["engineering"],
        "topics": ["testing", "deployment"],
        "word_count": 20,
    },
    {
        "kind": "blog",
        "content": "Short post. Very short.\n\nSecond paragraph.",
        "date": "2023-06-01",
        "year": 2023,
        "title": "Post Two",
        "categories": ["engineering", "leadership"],
        "topics": ["testing"],
        "word_count": 10,
    },
    {
        "kind": "unpublished",
        "content": "Draft content here.",
        "date": "2024-05-01",
        "year": 2024,
        "title": "Draft Post",
        "categories": [],
        "topics": [],
        "word_count": 5,
    },
]


# ---------------------------------------------------------------------------
# split_sentences / split_paragraphs
# ---------------------------------------------------------------------------

class TestSplitSentences:
    def test_splits_on_period(self):
        sentences = split_sentences("Hello world. This is a test.")
        assert len(sentences) == 2

    def test_splits_on_exclamation(self):
        sentences = split_sentences("Hello! How are you?")
        assert len(sentences) == 2

    def test_single_sentence(self):
        sentences = split_sentences("Just one sentence.")
        assert len(sentences) == 1

    def test_empty_string(self):
        assert split_sentences("") == []

    def test_strips_whitespace(self):
        sentences = split_sentences("  Hello.  World.  ")
        for s in sentences:
            assert s == s.strip()


class TestSplitParagraphs:
    def test_splits_on_double_newline(self):
        text = "First paragraph.\n\nSecond paragraph."
        paras = split_paragraphs(text)
        assert len(paras) == 2

    def test_filters_empty_paragraphs(self):
        text = "First.\n\n\n\nSecond."
        paras = split_paragraphs(text)
        assert len(paras) == 2

    def test_single_paragraph(self):
        paras = split_paragraphs("Just one paragraph.")
        assert len(paras) == 1


# ---------------------------------------------------------------------------
# tokenise_words / stopwords
# ---------------------------------------------------------------------------

class TestTokeniseWords:
    def test_returns_list_of_lowercase_words(self):
        words = tokenise_words("Engineering Leadership Testing")
        assert words == ["engineering", "leadership", "testing"]

    def test_ignores_numbers(self):
        words = tokenise_words("Version 2.0 released")
        assert "2" not in words

    def test_handles_apostrophes(self):
        words = tokenise_words("it's a don't")
        assert any("'" in w for w in words)


class TestStopwords:
    def test_returns_a_set(self):
        assert isinstance(stopwords(), set)

    def test_contains_common_english_words(self):
        stops = stopwords()
        for word in ["the", "and", "for", "is", "to", "in"]:
            assert word in stops


# ---------------------------------------------------------------------------
# sentence_stats / paragraph_stats
# ---------------------------------------------------------------------------

class TestSentenceStats:
    def test_returns_expected_keys(self):
        stats = sentence_stats(SAMPLE_DOCS[:2])
        assert "mean_words_per_sentence" in stats
        assert "median_words_per_sentence" in stats
        assert "min_words_per_sentence" in stats
        assert "max_words_per_sentence" in stats

    def test_returns_zeros_for_empty_docs(self):
        stats = sentence_stats([{"content": ""}])
        assert stats["mean_words_per_sentence"] == 0.0

    def test_mean_is_positive_for_real_content(self):
        stats = sentence_stats(SAMPLE_DOCS[:2])
        assert stats["mean_words_per_sentence"] > 0


class TestParagraphStats:
    def test_returns_expected_keys(self):
        stats = paragraph_stats(SAMPLE_DOCS[:2])
        assert "mean_sentences_per_paragraph" in stats
        assert "median_sentences_per_paragraph" in stats

    def test_returns_zeros_for_empty_docs(self):
        stats = paragraph_stats([{"content": ""}])
        assert stats["mean_sentences_per_paragraph"] == 0.0


# ---------------------------------------------------------------------------
# opening_lines / ending_lines
# ---------------------------------------------------------------------------

class TestOpeningLines:
    def test_returns_first_paragraph(self):
        docs = [{"content": "Opening para.\n\nMiddle para.\n\nEnding para."}]
        openings = opening_lines(docs)
        assert openings[0] == "Opening para."

    def test_respects_limit(self):
        docs = [{"content": f"Para {i}."} for i in range(20)]
        openings = opening_lines(docs, limit=5)
        assert len(openings) == 5

    def test_skips_docs_with_no_content(self):
        docs = [{"content": ""}, {"content": "Real content."}]
        openings = opening_lines(docs)
        assert len(openings) == 1


class TestEndingLines:
    def test_returns_last_paragraph(self):
        docs = [{"content": "Opening para.\n\nMiddle para.\n\nEnding para."}]
        endings = ending_lines(docs)
        assert endings[0] == "Ending para."

    def test_respects_limit(self):
        docs = [{"content": f"Para {i}."} for i in range(20)]
        endings = ending_lines(docs, limit=4)
        assert len(endings) == 4


# ---------------------------------------------------------------------------
# top_terms
# ---------------------------------------------------------------------------

class TestTopTerms:
    def test_excludes_stopwords(self):
        docs = [{"content": "the and for engineering testing deployment"}]
        terms = [word for word, _ in top_terms(docs, limit=10)]
        stops = stopwords()
        for term in terms:
            assert term not in stops

    def test_excludes_short_words(self):
        docs = [{"content": "ab abc abcd"}]
        terms = [word for word, _ in top_terms(docs, limit=10)]
        for term in terms:
            assert len(term) >= 4

    def test_returns_most_common_first(self):
        docs = [{"content": "engineering engineering engineering testing testing deployment"}]
        terms = [word for word, _ in top_terms(docs, limit=5)]
        assert terms[0] == "engineering"

    def test_respects_limit(self):
        docs = [{"content": " ".join([f"word{i}word" for i in range(50)])}]
        terms = top_terms(docs, limit=10)
        assert len(terms) <= 10


# ---------------------------------------------------------------------------
# metadata_counts
# ---------------------------------------------------------------------------

class TestMetadataCounts:
    def test_counts_categories(self):
        counts = dict(metadata_counts(SAMPLE_DOCS, "categories", limit=10))
        assert counts.get("engineering", 0) == 2
        assert counts.get("leadership", 0) == 1

    def test_counts_topics(self):
        counts = dict(metadata_counts(SAMPLE_DOCS, "topics", limit=10))
        assert counts.get("testing", 0) == 2
        assert counts.get("deployment", 0) == 1

    def test_respects_limit(self):
        result = metadata_counts(SAMPLE_DOCS, "categories", limit=1)
        assert len(result) == 1


# ---------------------------------------------------------------------------
# choose_analysis_docs
# ---------------------------------------------------------------------------

class TestChooseAnalysisDocs:
    def test_returns_only_blog_kind(self):
        docs = choose_analysis_docs(SAMPLE_DOCS, max_docs=10)
        assert all(doc["kind"] == "blog" for doc in docs)

    def test_respects_max_docs(self):
        corpus = [
            {"kind": "blog", "content": "Content", "date": f"202{i}-01-01", "year": 2020 + i,
             "word_count": 100, "title": f"Post {i}"}
            for i in range(10)
        ]
        docs = choose_analysis_docs(corpus, max_docs=3)
        assert len(docs) <= 3

    def test_filters_by_max_age(self):
        corpus = [
            {"kind": "blog", "content": "Old post", "date": "2010-01-01", "year": 2010, "word_count": 100, "title": "Old"},
            {"kind": "blog", "content": "New post", "date": "2024-01-01", "year": 2024, "word_count": 100, "title": "New"},
        ]
        # With max_age_years=5, current_year=2026, cutoff is 2021
        docs = choose_analysis_docs(corpus, max_docs=10, max_age_years=5)
        titles = [d["title"] for d in docs]
        assert "New" in titles
        assert "Old" not in titles

    def test_includes_all_when_max_age_is_none(self):
        docs = choose_analysis_docs(SAMPLE_DOCS[:2], max_docs=10, max_age_years=None)
        assert len(docs) == 2

    def test_fallback_to_all_when_age_filter_removes_everything(self):
        corpus = [
            {"kind": "blog", "content": "Old post", "date": "2010-01-01", "year": 2010, "word_count": 100, "title": "Old"},
        ]
        # max_age_years=1 would filter out 2010, but we fall back to all
        docs = choose_analysis_docs(corpus, max_docs=10, max_age_years=1)
        assert len(docs) == 1

    def test_sorted_by_date_descending(self):
        corpus = [
            {"kind": "blog", "content": "Post A", "date": "2022-01-01", "year": 2022, "word_count": 50, "title": "A"},
            {"kind": "blog", "content": "Post B", "date": "2024-01-01", "year": 2024, "word_count": 100, "title": "B"},
        ]
        docs = choose_analysis_docs(corpus, max_docs=10)
        assert docs[0]["title"] == "B"


# ---------------------------------------------------------------------------
# heuristic_profile
# ---------------------------------------------------------------------------

class TestHeuristicProfile:
    def test_returns_required_keys(self):
        profile = heuristic_profile(SAMPLE_DOCS[:2])
        required_keys = [
            "voice_summary", "tone", "rhythm", "structure",
            "rhetorical_patterns", "signature_moves", "favourite_themes",
            "vocabulary", "humour", "dos", "donts", "prompt_instructions",
        ]
        for key in required_keys:
            assert key in profile, f"Missing key: {key}"

    def test_tone_has_traits_list(self):
        profile = heuristic_profile(SAMPLE_DOCS[:2])
        assert isinstance(profile["tone"]["traits"], list)

    def test_vocabulary_has_common_terms(self):
        profile = heuristic_profile(SAMPLE_DOCS[:2])
        assert isinstance(profile["vocabulary"]["common_terms"], list)

    def test_british_english_in_prompt_instructions(self):
        profile = heuristic_profile(SAMPLE_DOCS[:2])
        instructions_text = " ".join(profile["prompt_instructions"]).lower()
        assert "british" in instructions_text


# ---------------------------------------------------------------------------
# render_markdown
# ---------------------------------------------------------------------------

class TestRenderMarkdown:
    def test_renders_voice_summary(self):
        profile = heuristic_profile(SAMPLE_DOCS[:1])
        md = render_markdown(profile, SAMPLE_DOCS[:1])
        assert "# Toby Weston Style Profile" in md
        assert profile["voice_summary"] in md

    def test_includes_source_posts(self):
        profile = heuristic_profile(SAMPLE_DOCS[:1])
        md = render_markdown(profile, SAMPLE_DOCS[:1])
        assert "Post One" in md

    def test_includes_all_sections(self):
        profile = heuristic_profile(SAMPLE_DOCS[:1])
        md = render_markdown(profile, SAMPLE_DOCS[:1])
        for section in ["## Tone", "## Rhythm", "## Structure", "## Vocabulary", "## Humour", "## Dos", "## Don'ts"]:
            assert section in md


# ---------------------------------------------------------------------------
# build_analysis_prompt
# ---------------------------------------------------------------------------

class TestBuildAnalysisPrompt:
    SENTENCE_METRICS = {"mean_words_per_sentence": 12.5, "median_words_per_sentence": 11.0,
                        "min_words_per_sentence": 4, "max_words_per_sentence": 32}
    PARAGRAPH_METRICS = {"mean_sentences_per_paragraph": 3.1, "median_sentences_per_paragraph": 3.0}
    TOP_WORDS = [("engineering", 42), ("deployment", 18)]
    CATEGORIES = [("engineering", 30), ("leadership", 10)]
    TOPICS = [("testing", 20), ("delivery", 15)]
    OPENINGS = ["Every system is a bet.", "The problem with most pipelines is invisible."]
    ENDINGS = ["That is the only metric that matters.", "Start there."]

    def _call(self, docs=None, **overrides):
        kwargs = dict(
            docs=docs or SAMPLE_DOCS[:2],
            sentence_metrics=self.SENTENCE_METRICS,
            paragraph_metrics=self.PARAGRAPH_METRICS,
            top_words=self.TOP_WORDS,
            categories=self.CATEGORIES,
            topics=self.TOPICS,
            openings=self.OPENINGS,
            endings=self.ENDINGS,
        )
        kwargs.update(overrides)
        return build_analysis_prompt(**kwargs)

    def test_returns_non_empty_string(self):
        assert isinstance(self._call(), str)
        assert len(self._call()) > 200

    def test_contains_sentence_metrics(self):
        prompt = self._call()
        assert "mean_words_per_sentence" in prompt

    def test_contains_sample_doc_title(self):
        prompt = self._call()
        assert "Post One" in prompt

    def test_contains_typical_openings(self):
        prompt = self._call()
        assert "Every system is a bet." in prompt

    def test_contains_typical_endings(self):
        prompt = self._call()
        assert "Start there." in prompt

    def test_requests_json_output(self):
        prompt = self._call()
        assert "voice_summary" in prompt

    def test_mentions_british_english(self):
        prompt = self._call()
        assert "British English" in prompt

    def test_truncates_long_doc_excerpts(self):
        long_doc = {
            "kind": "blog",
            "content": "x" * 10000,
            "date": "2024-01-01",
            "year": 2024,
            "title": "Long Doc",
            "categories": [],
            "topics": [],
            "word_count": 2000,
        }
        prompt = self._call(docs=[long_doc])
        # Excerpt is capped at 5000 chars; the full 10000 should NOT appear
        assert "x" * 5001 not in prompt

