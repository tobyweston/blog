from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from openai import OpenAI

from config import (
    CORPUS_CACHE,
    DEFAULT_AUDIENCE,
    DEFAULT_MODEL,
    OUTPUT_DIR,
    STYLE_PROFILE_JSON,
)
from extract_corpus import build_corpus, save_corpus


BASE_DIR = Path(__file__).resolve().parent
FRAMEWORKS_DIR = BASE_DIR / "frameworks"
PLANS_DIR = BASE_DIR / "output" / "plans"
PLANS_DIR.mkdir(parents=True, exist_ok=True)


def ensure_corpus() -> list[dict[str, Any]]:
    if not CORPUS_CACHE.exists():
        docs = build_corpus()
        save_corpus(docs)
    return json.loads(CORPUS_CACHE.read_text(encoding="utf-8"))


def load_style_profile() -> dict[str, Any]:
    if not STYLE_PROFILE_JSON.exists():
        raise SystemExit("Missing style profile. Run style_profile.py first.")
    return json.loads(STYLE_PROFILE_JSON.read_text(encoding="utf-8"))


def load_frameworks() -> list[dict[str, Any]]:
    frameworks: list[dict[str, Any]] = []

    if not FRAMEWORKS_DIR.exists():
        return frameworks

    for path in sorted(FRAMEWORKS_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, flags=re.DOTALL)
        if not match:
            continue

        frontmatter = yaml.safe_load(match.group(1)) or {}
        body = match.group(2).strip()

        if not isinstance(frontmatter, dict):
            continue

        frameworks.append(
            {
                "path": str(path),
                "name": frontmatter.get("name", path.stem),
                "slug": frontmatter.get("slug", path.stem),
                "topics": frontmatter.get("topics", []) or [],
                "when_to_use": frontmatter.get("when_to_use", []) or [],
                "summary": frontmatter.get("summary", ""),
                "key_claims": frontmatter.get("key_claims", []) or [],
                "argument_patterns": frontmatter.get("argument_patterns", []) or [],
                "example_phrasing": frontmatter.get("example_phrasing", []) or [],
                "guardrails": frontmatter.get("guardrails", []) or [],
                "body": body,
            }
        )

    return frameworks


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{2,}", text.lower()))


def score_framework(framework: dict[str, Any], query: str) -> int:
    q = tokenize(query)
    blob = " ".join(
        [
            framework.get("name", ""),
            framework.get("summary", ""),
            " ".join(framework.get("topics", [])),
            " ".join(framework.get("when_to_use", [])),
            " ".join(framework.get("key_claims", [])),
            " ".join(framework.get("argument_patterns", [])),
        ]
    )
    return len(q & tokenize(blob))


def pick_frameworks(
    frameworks: list[dict[str, Any]],
    query: str,
    limit: int = 3,
) -> list[dict[str, Any]]:
    ranked = sorted(
        frameworks,
        key=lambda fw: score_framework(fw, query),
        reverse=True,
    )
    chosen = [fw for fw in ranked if score_framework(fw, query) > 0]
    return chosen[:limit] if chosen else ranked[:limit]


def pick_topic_samples(
    corpus: list[dict[str, Any]],
    query: str,
    limit: int = 5,
) -> list[dict[str, Any]]:
    q = tokenize(query)

    scored = []
    for doc in corpus:
        blob = " ".join(
            [
                doc.get("title", ""),
                doc.get("description", ""),
                " ".join(doc.get("categories", [])),
                " ".join(doc.get("topics", [])),
                doc.get("content", "")[:3000],
            ]
        )
        score = len(q & tokenize(blob))
        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda item: (item[0], item[1].get("date", "")), reverse=True)
    return [doc for _, doc in scored[:limit]]


def slugify(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def build_prompt(
    *,
    topic: str,
    angle: str | None,
    notes: str | None,
    audience: str,
    style_profile: dict[str, Any],
    frameworks: list[dict[str, Any]],
    samples: list[dict[str, Any]],
) -> str:
    framework_block = "\n\n---\n\n".join(
        "\n".join(
            [
                f"FRAMEWORK: {fw.get('name', '')}",
                f"SUMMARY: {fw.get('summary', '')}",
                f"KEY CLAIMS: {', '.join(fw.get('key_claims', []))}",
                f"ARGUMENT PATTERNS: {', '.join(fw.get('argument_patterns', []))}",
                f"EXAMPLE PHRASING: {', '.join(fw.get('example_phrasing', []))}",
                f"GUARDRAILS: {', '.join(fw.get('guardrails', []))}",
            ]
        )
        for fw in frameworks
    )

    sample_block = "\n\n---\n\n".join(
        "\n".join(
            [
                f"TITLE: {doc.get('title', '')}",
                f"DATE: {doc.get('date', '')}",
                f"CATEGORIES: {', '.join(doc.get('categories', []))}",
                f"TOPICS: {', '.join(doc.get('topics', []))}",
                "EXCERPT:",
                doc.get("content", "")[:2500].strip(),
            ]
        )
        for doc in samples
    )

    return f"""
You are planning a blog post for Toby Weston.

You are not writing the post yet.
You are producing the argument and structure for the post.

Audience:
{audience}

Requested topic:
{topic}

Requested angle:
{angle or "Choose the strongest angle implied by the topic."}

Additional notes:
{notes or "None"}

Style profile:
{json.dumps(style_profile, ensure_ascii=False, indent=2)}

Candidate frameworks:
{framework_block}

Relevant blog samples:
{sample_block}

Return valid markdown with these sections:

# Post Plan

## Recommended title
(single best title)

## Alternative titles
(bullet list)

## Reader
(one short paragraph)

## Central insight
(one paragraph)

## Why this matters
(one paragraph)

## Recommended framework
(name of framework or 'None')

## Opening options
(3 bullets)

## Outline
(numbered list with 5-7 sections)

## Key arguments
(bullet list)

## Things to avoid
(bullet list)

## Suggested categories
(bullet list)

## Suggested topics
(bullet list)

Important constraints:
- Choose one central idea only
- Prefer Toby's reflective, slightly contrarian, first-principles style
- Do not make it sound like a sales page
- Do not drift into generic AI explanation tone
- Use British English
""".strip()


def write_plan(topic: str, content: str) -> Path:
    today = date.today().isoformat()
    slug = slugify(topic) or "untitled-plan"
    path = PLANS_DIR / f"{today}-{slug}.plan.md"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create a blog post plan. Planning comes first: "
            "review the plan before drafting."
        ),
        epilog=(
            "Recommended workflow:\\n"
            "  1. python plan_post.py --topic \"...\" --angle \"...\"\\n"
            "  2. review output/plans/<generated>.plan.md\\n"
            "  3. python generate_post.py --plan output/plans/<generated>.plan.md"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--topic", required=True)
    parser.add_argument("--angle")
    parser.add_argument("--notes")
    parser.add_argument("--audience", default=DEFAULT_AUDIENCE)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    corpus = ensure_corpus()
    style_profile = load_style_profile()
    frameworks = load_frameworks()

    query = " ".join(
        part for part in [args.topic, args.angle or "", args.notes or ""] if part
    ).strip()

    chosen_frameworks = pick_frameworks(frameworks, query, limit=3)
    chosen_samples = pick_topic_samples(corpus, query, limit=5)

    prompt = build_prompt(
        topic=args.topic,
        angle=args.angle,
        notes=args.notes,
        audience=args.audience,
        style_profile=style_profile,
        frameworks=chosen_frameworks,
        samples=chosen_samples,
    )

    if args.dry_run:
        print("DRY RUN")
        print("\nFrameworks:")
        for fw in chosen_frameworks:
            print(f" - {fw.get('name', '')}")
        print("\nSamples:")
        for doc in chosen_samples:
            print(f" - {doc.get('date', '')} | {doc.get('title', '')}")
        print("\nPrompt preview:\n")
        print(prompt[:3000])
        if len(prompt) > 3000:
            print("\n... [truncated]")
        return

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.responses.create(
        model=args.model,
        input=prompt,
    )

    content = response.output_text.strip()
    output_path = write_plan(args.topic, content)

    print(f"Plan written to: {output_path}")
    print("Frameworks used:")
    for fw in chosen_frameworks:
        print(f" - {fw.get('name', '')}")
    print("Samples used:")
    for doc in chosen_samples:
        print(f" - {doc.get('date', '')} | {doc.get('title', '')}")


if __name__ == "__main__":
    main()