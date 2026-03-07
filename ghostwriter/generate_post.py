from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from openai import OpenAI

from config import (
    CORPUS_CACHE,
    DEFAULT_AUDIENCE,
    DEFAULT_DRAFT,
    DEFAULT_MAX_AGE_YEARS,
    DEFAULT_MODEL,
    DEFAULT_STRICT_MAX_AGE,
    MAX_SAMPLE_CHARS,
    MAX_STYLE_SAMPLES,
    MODEL_PRICING,
    OUTPUT_DIR,
    RECENCY_HALF_LIFE_YEARS,
)
from extract_corpus import build_corpus, save_corpus


CURRENT_YEAR = datetime.now().year


@dataclass
class ScoredDoc:
    doc: dict[str, Any]
    score: float


def ensure_corpus() -> list[dict[str, Any]]:
    if not CORPUS_CACHE.exists():
        docs = build_corpus()
        save_corpus(docs)
    return json.loads(CORPUS_CACHE.read_text(encoding="utf-8"))


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{2,}", text.lower()))


def slugify(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def years_old(doc: dict[str, Any]) -> int | None:
    year = doc.get("year")
    if year is None:
        date_text = doc.get("date", "")
        match = re.match(r"^(\d{4})-\d{2}-\d{2}$", date_text)
        if not match:
            return None
        year = int(match.group(1))
    return CURRENT_YEAR - int(year)


def recency_multiplier(age: int | None) -> float:
    if age is None:
        return 0.9
    return max(0.35, 0.5 ** (age / RECENCY_HALF_LIFE_YEARS))


def metadata_text(doc: dict[str, Any]) -> str:
    return " ".join(
        [
            doc.get("title", ""),
            doc.get("description", ""),
            " ".join(doc.get("categories", [])),
            " ".join(doc.get("topics", [])),
        ]
    )


def content_preview(doc: dict[str, Any], max_chars: int = 5000) -> str:
    return (doc.get("content", "") or "")[:max_chars]


def score_doc(
    doc: dict[str, Any],
    query: str,
    max_age_years: int,
    strict_max_age: bool,
) -> float:
    age = years_old(doc)

    if strict_max_age and age is not None and age > max_age_years:
        return -1.0

    q = tokenize(query)
    meta = tokenize(metadata_text(doc))
    body = tokenize(content_preview(doc))

    title_overlap = len(q & tokenize(doc.get("title", "")))
    meta_overlap = len(q & meta)
    body_overlap = len(q & body)

    published_bonus = 8 if doc.get("kind") == "blog" else 2
    metadata_bonus = (meta_overlap * 8) + (title_overlap * 10)
    body_bonus = body_overlap * 3

    category_topic_bonus = 0
    for field in ("categories", "topics"):
        for item in doc.get(field, []):
            if tokenize(item) & q:
                category_topic_bonus += 6

    length_penalty = -10 if doc.get("word_count", 0) < 250 else 0
    age_mult = recency_multiplier(age)

    if age is not None and age > max_age_years and not strict_max_age:
        age_mult *= 0.55

    return (
        published_bonus
        + metadata_bonus
        + body_bonus
        + category_topic_bonus
        + length_penalty
    ) * age_mult


def pick_style_samples(
    corpus: list[dict[str, Any]],
    query: str,
    max_age_years: int,
    strict_max_age: bool,
) -> list[dict[str, Any]]:
    scored = [
        ScoredDoc(
            doc=doc,
            score=score_doc(
                doc=doc,
                query=query,
                max_age_years=max_age_years,
                strict_max_age=strict_max_age,
            ),
        )
        for doc in corpus
    ]

    ranked = sorted(scored, key=lambda item: item.score, reverse=True)

    chosen: list[dict[str, Any]] = []
    seen_titles: set[str] = set()

    for item in ranked:
        if len(chosen) >= MAX_STYLE_SAMPLES:
            break
        if item.score <= 0:
            continue

        title = item.doc.get("title", "").strip().lower()
        if not item.doc.get("content", "").strip():
            continue
        if title in seen_titles:
            continue

        chosen.append(item.doc)
        seen_titles.add(title)

    return chosen


def infer_categories_and_topics(
    samples: list[dict[str, Any]],
    requested_categories: list[str],
    requested_topics: list[str],
) -> tuple[list[str], list[str]]:
    if requested_categories or requested_topics:
        return requested_categories, requested_topics

    category_counts: dict[str, int] = {}
    topic_counts: dict[str, int] = {}

    for sample in samples:
        for cat in sample.get("categories", []):
            category_counts[cat] = category_counts.get(cat, 0) + 1
        for topic in sample.get("topics", []):
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

    best_categories = [
        k for k, _ in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    ]
    best_topics = [
        k for k, _ in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    ]

    return best_categories, best_topics


def build_prompt(
    *,
    topic: str,
    angle: str | None,
    audience: str,
    notes: str | None,
    samples: list[dict[str, Any]],
    categories: list[str],
    topics: list[str],
    explicit_title: str | None,
) -> str:
    excerpts = []

    for sample in samples:
        excerpt = content_preview(sample, MAX_SAMPLE_CHARS).strip()
        excerpts.append(
            "\n".join(
                [
                    f"TITLE: {sample.get('title', '')}",
                    f"DATE: {sample.get('date', '')}",
                    f"KIND: {sample.get('kind', '')}",
                    f"CATEGORIES: {', '.join(sample.get('categories', []))}",
                    f"TOPICS: {', '.join(sample.get('topics', []))}",
                    "EXCERPT:",
                    excerpt,
                ]
            )
        )

    sample_block = "\n\n---\n\n".join(excerpts)
    today = date.today().isoformat()

    return f"""
You are ghostwriting a blog post for Toby Weston.

Write in Toby's voice based on the supplied samples.
Do not mention the samples.
Use British English.
Avoid generic AI phrasing, filler, hype, emojis, and marketing language.
Prefer crisp argument, practical insight, lived engineering judgement, and occasional dry wit where natural.

Audience:
{audience}

Requested topic:
{topic}

Requested angle:
{angle or "Choose the strongest angle implied by the topic."}

Additional notes:
{notes or "None"}

Requested title:
{explicit_title or "No fixed title; choose the best one."}

Frontmatter categories to use:
{categories or "Infer sensible ones from the brief."}

Frontmatter topics to use:
{topics or "Infer sensible ones from the brief."}

Style samples:
{sample_block}

Return only a complete Astro-ready MDX document.

Requirements:
- Include valid YAML frontmatter at the top
- Frontmatter keys must include:
  title
  description
  date
  draft
  categories
  topics
- Set date to {today}
- Set draft to {str(DEFAULT_DRAFT).lower()}
- categories and topics must be YAML lists
- Write a strong description, not a placeholder
- The body should be engaging, readable, and substantive
- Do not include a closing "in summary" style wrap-up unless it feels natural
- Do not sound like a sales page
""".strip()


def extract_frontmatter_block(text: str) -> tuple[str | None, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end():]


def parse_title_from_frontmatter(frontmatter: str | None) -> str | None:
    if not frontmatter:
        return None
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', frontmatter, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def frontmatter_list_yaml(items: list[str]) -> str:
    if not items:
        return "[]"
    return "\n".join(f"  - {json.dumps(item)}" for item in items)


def normalise_generated_document(
    generated: str,
    *,
    fallback_title: str,
    categories: list[str],
    topics: list[str],
) -> str:
    frontmatter, body = extract_frontmatter_block(generated)
    today = date.today().isoformat()

    title = parse_title_from_frontmatter(frontmatter) or fallback_title or "Untitled Draft"
    description = ""

    if frontmatter:
        match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', frontmatter, flags=re.MULTILINE)
        if match:
            description = match.group(1).strip()

    if not description:
        body_text = re.sub(r"^#\s+.*?$", "", body, flags=re.MULTILINE).strip()
        first_para = body_text.split("\n\n", 1)[0].strip()
        description = first_para[:180].rstrip(".") + "." if first_para else "Draft post."

    clean_frontmatter = "\n".join(
        [
            "---",
            f"title: {json.dumps(title)}",
            f"description: {json.dumps(description)}",
            f"date: {today}",
            f"draft: {str(DEFAULT_DRAFT).lower()}",
            "categories:",
            frontmatter_list_yaml(categories) if categories else "  []",
            "topics:",
            frontmatter_list_yaml(topics) if topics else "  []",
            "---",
            "",
        ]
    )

    body = body.strip() + "\n"
    return clean_frontmatter + body


def write_output(content: str, title: str) -> Path:
    today = date.today().isoformat()
    slug = slugify(title or "untitled-draft")
    path = OUTPUT_DIR / f"{today}-{slug}.mdx"
    path.write_text(content, encoding="utf-8")
    return path


def csv_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def estimate_tokens_from_text(text: str) -> int:
    # Rough planning heuristic only
    return max(1, round(len(text) / 4))


def estimate_cost_usd(model: str, input_tokens: int, output_tokens: int) -> float | None:
    pricing = MODEL_PRICING.get(model)
    if not pricing:
        return None

    input_cost = (input_tokens / 1_000_000) * pricing["input_per_million"]
    output_cost = (output_tokens / 1_000_000) * pricing["output_per_million"]
    return input_cost + output_cost


def print_dry_run(
    *,
    model: str,
    prompt: str,
    samples: list[dict[str, Any]],
    categories: list[str],
    topics: list[str],
    estimated_output_tokens: int,
) -> None:
    input_tokens = estimate_tokens_from_text(prompt)
    estimated_cost = estimate_cost_usd(model, input_tokens, estimated_output_tokens)

    print("DRY RUN")
    print(f"Model: {model}")
    print(f"Estimated input tokens:  {input_tokens:,}")
    print(f"Estimated output tokens: {estimated_output_tokens:,}")
    if estimated_cost is not None:
        print(f"Estimated API cost:     ${estimated_cost:.4f}")
    else:
        print("Estimated API cost:     unknown (model not in MODEL_PRICING)")

    print("\nInferred frontmatter")
    print(f"  categories: {categories}")
    print(f"  topics:     {topics}")

    print("\nStyle samples selected")
    for idx, sample in enumerate(samples, start=1):
        print(
            f"  {idx}. {sample.get('date', '')} | {sample.get('kind', '')} | "
            f"{sample.get('title', '')}"
        )
        if sample.get("categories"):
            print(f"     categories: {', '.join(sample.get('categories', []))}")
        if sample.get("topics"):
            print(f"     topics:     {', '.join(sample.get('topics', []))}")

    print("\nPrompt preview")
    preview = prompt[:2000]
    print(preview)
    if len(prompt) > len(preview):
        print("\n... [truncated]")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--angle")
    parser.add_argument("--audience", default=DEFAULT_AUDIENCE)
    parser.add_argument("--notes")
    parser.add_argument("--title")
    parser.add_argument("--categories", help="Comma-separated categories")
    parser.add_argument("--topics", help="Comma-separated topics")
    parser.add_argument("--max-age-years", type=int, default=DEFAULT_MAX_AGE_YEARS)
    parser.add_argument(
        "--strict-max-age",
        action="store_true",
        default=DEFAULT_STRICT_MAX_AGE,
        help="Hard-exclude posts older than --max-age-years",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--estimated-output-tokens",
        type=int,
        default=1800,
        help="Used for dry-run cost estimation only",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show chosen samples and estimated cost without calling the API",
    )
    args = parser.parse_args()

    corpus = ensure_corpus()

    query = " ".join(
        part
        for part in [
            args.topic,
            args.angle or "",
            args.notes or "",
            args.categories or "",
            args.topics or "",
        ]
        if part
    ).strip()

    samples = pick_style_samples(
        corpus=corpus,
        query=query,
        max_age_years=args.max_age_years,
        strict_max_age=args.strict_max_age,
    )

    if not samples:
        raise SystemExit("No suitable style samples found. Try increasing --max-age-years.")

    requested_categories = csv_list(args.categories)
    requested_topics = csv_list(args.topics)

    categories, topics = infer_categories_and_topics(
        samples=samples,
        requested_categories=requested_categories,
        requested_topics=requested_topics,
    )

    prompt = build_prompt(
        topic=args.topic,
        angle=args.angle,
        audience=args.audience,
        notes=args.notes,
        samples=samples,
        categories=categories,
        topics=topics,
        explicit_title=args.title,
    )

    if args.dry_run:
        print_dry_run(
            model=args.model,
            prompt=prompt,
            samples=samples,
            categories=categories,
            topics=topics,
            estimated_output_tokens=args.estimated_output_tokens,
        )
        return

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.responses.create(
        model=args.model,
        input=prompt,
    )

    generated = response.output_text.strip()
    fallback_title = args.title or "Untitled Draft"
    content = normalise_generated_document(
        generated,
        fallback_title=fallback_title,
        categories=categories,
        topics=topics,
    )

    final_title = parse_title_from_frontmatter(extract_frontmatter_block(content)[0]) or fallback_title
    output_path = write_output(content, final_title)

    print(f"Draft written to: {output_path}")
    print("Style samples used:")
    for sample in samples:
        print(f" - {sample.get('date', '')} | {sample.get('title', '')}")


if __name__ == "__main__":
    main()