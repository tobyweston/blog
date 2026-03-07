from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from statistics import mean, median
from typing import Any

from openai import OpenAI

from config import CORPUS_CACHE, DEFAULT_MODEL, STYLE_PROFILE_JSON, STYLE_PROFILE_MD
from extract_corpus import build_corpus, save_corpus


def ensure_corpus() -> list[dict[str, Any]]:
    if not CORPUS_CACHE.exists():
        docs = build_corpus()
        save_corpus(docs)
    return json.loads(CORPUS_CACHE.read_text(encoding="utf-8"))


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def split_paragraphs(text: str) -> list[str]:
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def tokenise_words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z'\-]+", text.lower())


def stopwords() -> set[str]:
    return {
        "the", "and", "for", "that", "with", "this", "you", "are", "but", "not",
        "have", "was", "from", "they", "your", "all", "can", "has", "had", "his",
        "her", "its", "our", "out", "too", "into", "than", "then", "their", "there",
        "what", "when", "where", "why", "how", "who", "will", "would", "could",
        "should", "about", "because", "just", "more", "some", "very", "much", "like",
        "over", "under", "also", "only", "really", "being", "been", "were", "them",
        "those", "these", "such", "each", "any", "may", "might", "one", "two",
        "three", "first", "second", "new", "old", "make", "made", "using", "use",
        "used", "get", "got", "getting", "say", "says", "said", "way", "ways",
        "thing", "things", "part", "parts", "much", "many", "still", "even",
        "it", "is", "to", "of", "in", "on", "a", "an", "as", "at", "by", "or", "if",
        "be", "do", "does", "did", "so", "we", "i", "he", "she", "my", "me"
    }


def sentence_stats(docs: list[dict[str, Any]]) -> dict[str, float]:
    lengths: list[int] = []

    for doc in docs:
        for sentence in split_sentences(doc.get("content", "")):
            lengths.append(len(tokenise_words(sentence)))

    if not lengths:
        return {
            "mean_words_per_sentence": 0.0,
            "median_words_per_sentence": 0.0,
            "min_words_per_sentence": 0.0,
            "max_words_per_sentence": 0.0,
        }

    return {
        "mean_words_per_sentence": round(mean(lengths), 2),
        "median_words_per_sentence": round(median(lengths), 2),
        "min_words_per_sentence": min(lengths),
        "max_words_per_sentence": max(lengths),
    }


def paragraph_stats(docs: list[dict[str, Any]]) -> dict[str, float]:
    lengths: list[int] = []

    for doc in docs:
        for para in split_paragraphs(doc.get("content", "")):
            lengths.append(len(split_sentences(para)))

    if not lengths:
        return {
            "mean_sentences_per_paragraph": 0.0,
            "median_sentences_per_paragraph": 0.0,
        }

    return {
        "mean_sentences_per_paragraph": round(mean(lengths), 2),
        "median_sentences_per_paragraph": round(median(lengths), 2),
    }


def opening_lines(docs: list[dict[str, Any]], limit: int = 12) -> list[str]:
    openings = []
    for doc in docs:
        paragraphs = split_paragraphs(doc.get("content", ""))
        if paragraphs:
            openings.append(paragraphs[0])
    return openings[:limit]


def ending_lines(docs: list[dict[str, Any]], limit: int = 12) -> list[str]:
    endings = []
    for doc in docs:
        paragraphs = split_paragraphs(doc.get("content", ""))
        if paragraphs:
            endings.append(paragraphs[-1])
    return endings[:limit]


def top_terms(docs: list[dict[str, Any]], limit: int = 40) -> list[tuple[str, int]]:
    counts: Counter[str] = Counter()
    stops = stopwords()

    for doc in docs:
        words = tokenise_words(doc.get("content", ""))
        for word in words:
            if word in stops:
                continue
            if len(word) < 4:
                continue
            counts[word] += 1

    return counts.most_common(limit)


def metadata_counts(docs: list[dict[str, Any]], field: str, limit: int = 20) -> list[tuple[str, int]]:
    counts: Counter[str] = Counter()
    for doc in docs:
        for item in doc.get(field, []):
            counts[item] += 1
    return counts.most_common(limit)


def choose_analysis_docs(
    corpus: list[dict[str, Any]],
    max_docs: int,
    max_age_years: int | None = None,
) -> list[dict[str, Any]]:
    filtered = [doc for doc in corpus if doc.get("kind") == "blog" and doc.get("content", "").strip()]

    if max_age_years is not None:
        current_year = 2026
        pruned = []
        for doc in filtered:
            year = doc.get("year")
            if year is None:
                pruned.append(doc)
                continue
            if current_year - int(year) <= max_age_years:
                pruned.append(doc)
        filtered = pruned or filtered

    filtered = sorted(
        filtered,
        key=lambda d: (d.get("date", ""), d.get("word_count", 0)),
        reverse=True,
    )

    return filtered[:max_docs]


def build_analysis_prompt(
    docs: list[dict[str, Any]],
    sentence_metrics: dict[str, float],
    paragraph_metrics: dict[str, float],
    top_words: list[tuple[str, int]],
    categories: list[tuple[str, int]],
    topics: list[tuple[str, int]],
    openings: list[str],
    endings: list[str],
) -> str:
    samples = []

    for doc in docs[:10]:
        excerpt = doc.get("content", "")[:5000].strip()
        samples.append(
            "\n".join(
                [
                    f"TITLE: {doc.get('title', '')}",
                    f"DATE: {doc.get('date', '')}",
                    f"CATEGORIES: {', '.join(doc.get('categories', []))}",
                    f"TOPICS: {', '.join(doc.get('topics', []))}",
                    "EXCERPT:",
                    excerpt,
                ]
            )
        )

    joined_samples = "\n\n---\n\n".join(samples)

    return f"""
You are analysing the writing voice of Toby Weston based on his published blog posts.

Your job is to extract a practical ghostwriting style guide that can later be used to write authentic blog posts in his voice.

Be specific and grounded in the examples. Avoid generic writing-advice filler.
Use British English.

Quantitative signals:
- sentence metrics: {json.dumps(sentence_metrics)}
- paragraph metrics: {json.dumps(paragraph_metrics)}
- common terms: {json.dumps(top_words)}
- common categories: {json.dumps(categories)}
- common topics: {json.dumps(topics)}

Typical openings:
{json.dumps(openings, ensure_ascii=False, indent=2)}

Typical endings:
{json.dumps(endings, ensure_ascii=False, indent=2)}

Writing samples:
{joined_samples}

Return valid JSON with this structure:
{{
  "voice_summary": "...",
  "tone": {{
    "overall": "...",
    "traits": ["...", "..."]
  }},
  "rhythm": {{
    "sentence_style": "...",
    "paragraph_style": "...",
    "pace": "..."
  }},
  "structure": {{
    "typical_openings": ["...", "..."],
    "typical_flow": ["...", "...", "..."],
    "typical_endings": ["...", "..."]
  }},
  "rhetorical_patterns": ["...", "..."],
  "signature_moves": ["...", "..."],
  "favourite_themes": ["...", "..."],
  "vocabulary": {{
    "common_terms": ["...", "..."],
    "preferred_register": "...",
    "technical_density": "..."
  }},
  "humour": {{
    "present": true,
    "style": "..."
  }},
  "dos": ["...", "..."],
  "donts": ["...", "..."],
  "prompt_instructions": [
    "...",
    "..."
  ]
}}
""".strip()


def heuristic_profile(docs: list[dict[str, Any]]) -> dict[str, Any]:
    sentence_metrics = sentence_stats(docs)
    paragraph_metrics = paragraph_stats(docs)
    top_words = [word for word, _ in top_terms(docs, limit=20)]
    top_categories = [name for name, _ in metadata_counts(docs, "categories", limit=10)]
    top_topics = [name for name, _ in metadata_counts(docs, "topics", limit=15)]

    return {
        "voice_summary": (
            "Thoughtful technical writing with clear argument, practical engineering focus, "
            "measured confidence, and occasional dry wit."
        ),
        "tone": {
            "overall": "Conversational but authoritative",
            "traits": [
                "reflective",
                "precise",
                "practical",
                "technically credible",
            ],
        },
        "rhythm": {
            "sentence_style": f"Average sentence length around {sentence_metrics['mean_words_per_sentence']} words.",
            "paragraph_style": f"Average paragraph length around {paragraph_metrics['mean_sentences_per_paragraph']} sentences.",
            "pace": "Usually steady, occasionally punchier for emphasis.",
        },
        "structure": {
            "typical_openings": [
                "Starts with an assertion, observation, or problem framing.",
                "Sometimes opens from lived engineering experience rather than theory.",
            ],
            "typical_flow": [
                "introduce the problem",
                "explain why the common view is incomplete",
                "offer a clearer mental model",
                "land on practical implications",
            ],
            "typical_endings": [
                "Ends on a takeaway, principle, or challenge to the reader.",
                "Avoids overblown summary language.",
            ],
        },
        "rhetorical_patterns": [
            "contrast between what people think and what is actually happening",
            "moving from concrete engineering detail to broader principle",
        ],
        "signature_moves": [
            "reframing a technical issue as an organisational or design issue",
            "using precise examples to expose a weak assumption",
        ],
        "favourite_themes": top_topics[:10] or top_categories[:10],
        "vocabulary": {
            "common_terms": top_words,
            "preferred_register": "plain-spoken technical English",
            "technical_density": "moderate to high",
        },
        "humour": {
            "present": True,
            "style": "dry, understated, used sparingly",
        },
        "dos": [
            "Be clear and direct.",
            "Prefer substance over flourish.",
            "Use concrete examples when making abstract points.",
            "Sound like an experienced engineer thinking out loud.",
        ],
        "donts": [
            "Do not sound like marketing copy.",
            "Do not use generic AI optimism or hype.",
            "Do not over-explain simple technical concepts to expert readers.",
        ],
        "prompt_instructions": [
            "Use British English.",
            "Write with measured authority and practical engineering judgement.",
            "Prefer clear framing, concrete examples, and useful takeaways.",
            "Avoid sales language, empty transitions, and exaggerated enthusiasm.",
        ],
    }


def render_markdown(profile: dict[str, Any], docs: list[dict[str, Any]]) -> str:
    def bullets(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- None"

    return f"""# Toby Weston Style Profile

## Voice summary
{profile.get("voice_summary", "")}

## Tone
**Overall:** {profile.get("tone", {}).get("overall", "")}

{bullets(profile.get("tone", {}).get("traits", []))}

## Rhythm
- Sentence style: {profile.get("rhythm", {}).get("sentence_style", "")}
- Paragraph style: {profile.get("rhythm", {}).get("paragraph_style", "")}
- Pace: {profile.get("rhythm", {}).get("pace", "")}

## Structure
### Typical openings
{bullets(profile.get("structure", {}).get("typical_openings", []))}

### Typical flow
{bullets(profile.get("structure", {}).get("typical_flow", []))}

### Typical endings
{bullets(profile.get("structure", {}).get("typical_endings", []))}

## Rhetorical patterns
{bullets(profile.get("rhetorical_patterns", []))}

## Signature moves
{bullets(profile.get("signature_moves", []))}

## Favourite themes
{bullets(profile.get("favourite_themes", []))}

## Vocabulary
- Preferred register: {profile.get("vocabulary", {}).get("preferred_register", "")}
- Technical density: {profile.get("vocabulary", {}).get("technical_density", "")}

### Common terms
{bullets(profile.get("vocabulary", {}).get("common_terms", []))}

## Humour
- Present: {profile.get("humour", {}).get("present", False)}
- Style: {profile.get("humour", {}).get("style", "")}

## Dos
{bullets(profile.get("dos", []))}

## Don'ts
{bullets(profile.get("donts", []))}

## Prompt instructions
{bullets(profile.get("prompt_instructions", []))}

## Source posts analysed
{bullets([f"{d.get('date', '')} — {d.get('title', '')}" for d in docs])}
"""


def save_profile(profile: dict[str, Any], docs: list[dict[str, Any]]) -> None:
    STYLE_PROFILE_JSON.write_text(
        json.dumps(profile, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    STYLE_PROFILE_MD.write_text(
        render_markdown(profile, docs),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-docs", type=int, default=20)
    parser.add_argument("--max-age-years", type=int, default=12)
    parser.add_argument(
        "--heuristic-only",
        action="store_true",
        help="Skip API analysis and build a local profile only",
    )
    args = parser.parse_args()

    corpus = ensure_corpus()
    docs = choose_analysis_docs(
        corpus=corpus,
        max_docs=args.max_docs,
        max_age_years=args.max_age_years,
    )

    if not docs:
        raise SystemExit("No blog posts found to analyse.")

    if args.heuristic_only:
        profile = heuristic_profile(docs)
        save_profile(profile, docs)
        print(f"Wrote {STYLE_PROFILE_JSON}")
        print(f"Wrote {STYLE_PROFILE_MD}")
        return

    sentence_metrics = sentence_stats(docs)
    paragraph_metrics = paragraph_stats(docs)
    words = top_terms(docs, limit=30)
    categories = metadata_counts(docs, "categories", limit=15)
    topics = metadata_counts(docs, "topics", limit=20)
    openings = opening_lines(docs, limit=10)
    endings = ending_lines(docs, limit=10)

    prompt = build_analysis_prompt(
        docs=docs,
        sentence_metrics=sentence_metrics,
        paragraph_metrics=paragraph_metrics,
        top_words=words,
        categories=categories,
        topics=topics,
        openings=openings,
        endings=endings,
    )

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.responses.create(
        model=args.model,
        input=prompt,
    )

    raw = response.output_text.strip()

    try:
        profile = json.loads(raw)
    except json.JSONDecodeError:
        print("Model did not return valid JSON. Falling back to heuristic profile.")
        profile = heuristic_profile(docs)

    save_profile(profile, docs)

    print(f"Wrote {STYLE_PROFILE_JSON}")
    print(f"Wrote {STYLE_PROFILE_MD}")


if __name__ == "__main__":
    main()