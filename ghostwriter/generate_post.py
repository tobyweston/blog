from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path
from typing import Any

from openai import OpenAI

from config import (
    CORPUS_CACHE,
    DEFAULT_DRAFT,
    DEFAULT_MODEL,
    MAX_SAMPLE_CHARS,
    MAX_STYLE_SAMPLES,
    OUTPUT_DIR,
    STYLE_PROFILE_JSON,
)
from extract_corpus import build_corpus, save_corpus


def ensure_corpus() -> list[dict[str, Any]]:
    if not CORPUS_CACHE.exists():
        docs = build_corpus()
        save_corpus(docs)
    return json.loads(CORPUS_CACHE.read_text(encoding="utf-8"))


def load_style_profile() -> dict[str, Any]:
    if not STYLE_PROFILE_JSON.exists():
        raise SystemExit(
            "Missing style profile. Run style_profile.py first."
        )
    return json.loads(STYLE_PROFILE_JSON.read_text(encoding="utf-8"))


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z][a-zA-Z0-9\\-]{2,}", text.lower()))


def slugify(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^a-z0-9\\s-]", "", value)
    value = re.sub(r"\\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def parse_plan(plan_path: Path) -> dict[str, Any]:
    if not plan_path.exists():
        raise SystemExit(f"Plan file not found: {plan_path}")

    raw = plan_path.read_text(encoding="utf-8")

    def section(name: str) -> str:
        pattern = rf"^##\\s+{re.escape(name)}\\s*\\n(.*?)(?=^##\\s+|\\Z)"
        match = re.search(pattern, raw, flags=re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""

    def bullets(text: str) -> list[str]:
        return [
            re.sub(r"^[-*]\\s+", "", line).strip()
            for line in text.splitlines()
            if re.match(r"^[-*]\\s+", line.strip())
        ]

    def numbered(text: str) -> list[str]:
        return [
            re.sub(r"^\\d+[.)]\\s+", "", line).strip()
            for line in text.splitlines()
            if re.match(r"^\\d+[.)]\\s+", line.strip())
        ]

    return {
        "raw": raw,
        "recommended_title": section("Recommended title"),
        "alternative_titles": bullets(section("Alternative titles")),
        "reader": section("Reader"),
        "central_insight": section("Central insight"),
        "why_this_matters": section("Why this matters"),
        "recommended_framework": section("Recommended framework"),
        "opening_options": bullets(section("Opening options")),
        "outline": numbered(section("Outline")),
        "key_arguments": bullets(section("Key arguments")),
        "things_to_avoid": bullets(section("Things to avoid")),
        "suggested_categories": bullets(section("Suggested categories")),
        "suggested_topics": bullets(section("Suggested topics")),
    }


def score_doc(doc: dict[str, Any], query: str) -> int:
    q = tokenize(query)
    blob = " ".join(
        [
            doc.get("title", ""),
            doc.get("description", ""),
            " ".join(doc.get("categories", [])),
            " ".join(doc.get("topics", [])),
            doc.get("content", "")[:5000],
        ]
    )
    return len(q & tokenize(blob))


def pick_style_samples(
    corpus: list[dict[str, Any]],
    query: str,
    limit: int = MAX_STYLE_SAMPLES,
) -> list[dict[str, Any]]:
    scored = []
    for doc in corpus:
        if not doc.get("content", "").strip():
            continue
        score = score_doc(doc, query)
        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda item: (item[0], item[1].get("date", "")), reverse=True)

    chosen: list[dict[str, Any]] = []
    seen_titles: set[str] = set()

    for _, doc in scored:
        if len(chosen) >= limit:
            break
        title = doc.get("title", "").strip().lower()
        if title in seen_titles:
            continue
        chosen.append(doc)
        seen_titles.add(title)

    if not chosen:
        fallback = sorted(
            [d for d in corpus if d.get("content", "").strip()],
            key=lambda d: d.get("date", ""),
            reverse=True,
        )
        chosen = fallback[:limit]

    return chosen


def frontmatter_list_yaml(items: list[str]) -> str:
    if not items:
        return "  []"
    return "\\n".join(f"  - {json.dumps(item)}" for item in items)


def extract_frontmatter_block(text: str) -> tuple[str | None, str]:
    match = re.match(r"^---\\s*\\n(.*?)\\n---\\s*\\n?", text, flags=re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end():]


def parse_title_from_frontmatter(frontmatter: str | None) -> str | None:
    if not frontmatter:
        return None
    match = re.search(
        r'^title:\\s*["\\\']?(.*?)["\\\']?\\s*$',
        frontmatter,
        flags=re.MULTILINE,
    )
    return match.group(1).strip() if match else None


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
        match = re.search(
            r'^description:\\s*["\\\']?(.*?)["\\\']?\\s*$',
            frontmatter,
            flags=re.MULTILINE,
        )
        if match:
            description = match.group(1).strip()

    if not description:
        body_text = re.sub(r"^#\\s+.*?$", "", body, flags=re.MULTILINE).strip()
        first_para = body_text.split("\\n\\n", 1)[0].strip()
        description = first_para[:180].rstrip(".") + "." if first_para else "Draft post."

    clean_frontmatter = "\\n".join(
        [
            "---",
            f"title: {json.dumps(title)}",
            f"description: {json.dumps(description)}",
            f"date: {today}",
            f"draft: {str(DEFAULT_DRAFT).lower()}",
            "categories:",
            frontmatter_list_yaml(categories),
            "topics:",
            frontmatter_list_yaml(topics),
            "---",
            "",
        ]
    )

    body = body.strip() + "\\n"
    return clean_frontmatter + body


def build_prompt(
    *,
    plan: dict[str, Any],
    style_profile: dict[str, Any],
    samples: list[dict[str, Any]],
) -> str:
    sample_block = "\\n\\n---\\n\\n".join(
        "\\n".join(
            [
                f"TITLE: {doc.get('title', '')}",
                f"DATE: {doc.get('date', '')}",
                f"CATEGORIES: {', '.join(doc.get('categories', []))}",
                f"TOPICS: {', '.join(doc.get('topics', []))}",
                "EXCERPT:",
                doc.get("content", "")[:MAX_SAMPLE_CHARS].strip(),
            ]
        )
        for doc in samples
    )

    return f"""
You are ghostwriting a blog post for Toby Weston.

You must write from the supplied plan.
Do not invent a different central argument.
Use British English.
Avoid generic AI explanation tone, filler, hype, startup marketing tone, and generic developer evangelism.

Style profile:
{json.dumps(style_profile, ensure_ascii=False, indent=2)}

Approved post plan:
{plan["raw"]}

Relevant voice and topic samples:
{sample_block}

Return only a complete Astro-ready MDX document.

Requirements:
- Follow the approved plan
- Preserve one clear central idea
- Include valid YAML frontmatter at the top
- Frontmatter keys must include:
  title
  description
  date
  draft
  categories
  topics
- Use the recommended title unless there is a very strong reason not to
- categories and topics must be YAML lists
- Keep the writing in Toby's voice: reflective, analytical, pragmatic, slightly contrarian where appropriate
- Prefer short paragraphs
- Avoid sounding like a sales page
""".strip()


def write_output(content: str, title: str) -> Path:
    today = date.today().isoformat()
    slug = slugify(title or "untitled-draft")
    path = OUTPUT_DIR / f"{today}-{slug}.mdx"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Draft a blog post from an approved plan. "
            "Planning is mandatory: run plan_post.py first, then pass --plan."
        ),
        epilog=(
            "Recommended workflow:\\n"
            "  1. python plan_post.py --topic \"...\" --angle \"...\"\\n"
            "  2. review the generated plan\\n"
            "  3. python generate_post.py --plan output/plans/<your-plan>.plan.md"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--plan",
        required=True,
        help=(
            "Path to an approved .plan.md file created by plan_post.py. "
            "Topic-only drafting is intentionally not supported."
        ),
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model to use for drafting. Use a plan first; this command only drafts from plans.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the selected samples and prompt preview without calling the API.",
    )
    args = parser.parse_args()

    corpus = ensure_corpus()
    style_profile = load_style_profile()

    plan_path = Path(args.plan)
    plan = parse_plan(plan_path)

    retrieval_query = " ".join(
        [
            plan.get("recommended_title", ""),
            plan.get("central_insight", ""),
            plan.get("why_this_matters", ""),
            plan.get("recommended_framework", ""),
            " ".join(plan.get("key_arguments", [])),
            " ".join(plan.get("suggested_categories", [])),
            " ".join(plan.get("suggested_topics", [])),
        ]
    ).strip()

    samples = pick_style_samples(corpus, retrieval_query, limit=MAX_STYLE_SAMPLES)

    prompt = build_prompt(
        plan=plan,
        style_profile=style_profile,
        samples=samples,
    )

    if args.dry_run:
        print("DRY RUN")
        print(f"Plan: {plan_path}")
        print(f"Recommended title: {plan.get('recommended_title', '')}")
        print(f"Recommended framework: {plan.get('recommended_framework', '')}")
        print("\\nSamples:")
        for doc in samples:
            print(f" - {doc.get('date', '')} | {doc.get('title', '')}")
        print("\\nPrompt preview:\\n")
        print(prompt[:3000])
        if len(prompt) > 3000:
            print("\\n... [truncated]")
        return

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.responses.create(
        model=args.model,
        input=prompt,
    )

    generated = response.output_text.strip()

    fallback_title = plan.get("recommended_title") or "Untitled Draft"
    categories = plan.get("suggested_categories", [])
    topics = plan.get("suggested_topics", [])

    content = normalise_generated_document(
        generated,
        fallback_title=fallback_title,
        categories=categories,
        topics=topics,
    )

    final_title = parse_title_from_frontmatter(extract_frontmatter_block(content)[0]) or fallback_title
    output_path = write_output(content, final_title)

    print(f"Draft written to: {output_path}")
    print(f"Plan used: {plan_path}")
    print("Samples used:")
    for doc in samples:
        print(f" - {doc.get('date', '')} | {doc.get('title', '')}")


if __name__ == "__main__":
    main()