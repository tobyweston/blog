from __future__ import annotations

import argparse
import json
import os
from datetime import date
from pathlib import Path
from typing import Any

from openai import OpenAI

from config import DEFAULT_AUDIENCE, DEFAULT_MODEL, STYLE_PROFILE_JSON
from retrieve import pick_frameworks, pick_notes, pick_research, pick_topic_samples, slugify


BASE_DIR = Path(__file__).resolve().parent
PLANS_DIR = BASE_DIR / "output" / "plans"
PLANS_DIR.mkdir(parents=True, exist_ok=True)


def load_style_profile() -> dict[str, Any]:
    if not STYLE_PROFILE_JSON.exists():
        raise SystemExit("Missing style profile. Run style_profile.py first.")
    return json.loads(STYLE_PROFILE_JSON.read_text(encoding="utf-8"))


def csv_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def build_prompt(
        *,
        topic: str,
        angle: str | None,
        notes: str | None,
        audience: str,
        style_profile: dict[str, Any],
        frameworks: list[dict[str, Any]],
        samples: list[dict[str, Any]],
        research: list[dict[str, Any]],
        notes_files: list[dict[str, Any]],
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
    ) or "None"

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
    ) or "None"

    research_block = "\n\n---\n\n".join(
        "\n".join(
            [
                f"RESEARCH FILE: {item.get('name', '')}",
                item.get("content", "")[:4000].strip(),
            ]
        )
        for item in research
    ) or "None"

    notes_block = "\n\n---\n\n".join(
        "\n".join(
            [
                f"NOTES FILE: {item.get('name', '')}",
                item.get("content", "")[:2500].strip(),
            ]
        )
        for item in notes_files
    ) or "None"

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

Inline notes from user:
{notes or "None"}

Style profile:
{json.dumps(style_profile, ensure_ascii=False, indent=2)}

Candidate frameworks:
{framework_block}

Relevant blog samples:
{sample_block}

Research material:
{research_block}

Author notes:
{notes_block}

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
            "Recommended workflow:\n"
            "  1. python plan_post.py --topic \"...\" --angle \"...\"\n"
            "  2. review output/plans/<generated>.plan.md\n"
            "  3. python generate_post.py --plan output/plans/<generated>.plan.md\n\n"
            "Optional grounding:\n"
            "  --research research/common/doc.md,research/post/<slug>/doc.md\n"
            "  --notes-file notes/common/note.md,notes/post/<slug>/note.md"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--topic", required=True)
    parser.add_argument("--angle")
    parser.add_argument("--notes")
    parser.add_argument("--audience", default=DEFAULT_AUDIENCE)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--research", help="Comma-separated research file paths to ground the plan",)
    parser.add_argument("--notes-file", help="Comma-separated note file paths containing rough ideas or story fragments",)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    style_profile = load_style_profile()

    query = " ".join(
        part
        for part in [
            args.topic,
            args.angle or "",
            args.notes or "",
            ]
        if part
    ).strip()

    research_paths = csv_list(args.research)
    notes_paths = csv_list(args.notes_file)

    chosen_frameworks = pick_frameworks(query, limit=3)
    chosen_samples = pick_topic_samples(query, limit=5)
    chosen_research = pick_research(
        query,
        paths=research_paths,
        topic_or_query=args.topic,
        limit=3,
    )
    chosen_notes = pick_notes(
        query,
        paths=notes_paths,
        topic_or_query=args.topic,
        limit=3,
    )

    prompt = build_prompt(
        topic=args.topic,
        angle=args.angle,
        notes=args.notes,
        audience=args.audience,
        style_profile=style_profile,
        frameworks=chosen_frameworks,
        samples=chosen_samples,
        research=chosen_research,
        notes_files=chosen_notes,
    )

    if args.dry_run:
        print("DRY RUN")
        print("\nFrameworks:")
        for fw in chosen_frameworks:
            print(f" - {fw.get('name', '')}")

        print("\nSamples:")
        for doc in chosen_samples:
            print(f" - {doc.get('date', '')} | {doc.get('title', '')}")

        print("\nResearch:")
        for item in chosen_research:
            print(f" - {item.get('path', '')}")

        print("\nNotes files:")
        for item in chosen_notes:
            print(f" - {item.get('path', '')}")

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

    if chosen_research:
        print("Research used:")
        for item in chosen_research:
            print(f" - {item.get('path', '')}")

    if chosen_notes:
        print("Notes used:")
        for item in chosen_notes:
            print(f" - {item.get('path', '')}")


if __name__ == "__main__":
    main()