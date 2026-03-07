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
    DEFAULT_MODEL,
    DEFAULT_DRAFT,
    MAX_SAMPLE_CHARS,
    MAX_STYLE_SAMPLES,
    OUTPUT_DIR,
    STYLE_PROFILE_JSON,
)
from retrieve import (
    pick_frameworks,
    pick_notes,
    pick_research,
    pick_topic_samples,
    pick_voice_anchors,
    slugify,
)


def load_style_profile() -> dict[str, Any]:
    if not STYLE_PROFILE_JSON.exists():
        raise SystemExit("Missing style profile. Run style_profile.py first.")

    return json.loads(STYLE_PROFILE_JSON.read_text(encoding="utf-8"))


def parse_plan(plan_path: Path) -> dict[str, Any]:
    raw = plan_path.read_text(encoding="utf-8")

    def section(name: str) -> str:
        pattern = rf"^##\s+{re.escape(name)}\s*\n(.*?)(?=^##\s+|\Z)"
        match = re.search(pattern, raw, flags=re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""

    def bullets(text: str) -> list[str]:
        return [
            re.sub(r"^[-*]\s+", "", line).strip()
            for line in text.splitlines()
            if re.match(r"^[-*]\s+", line.strip())
        ]

    def numbered(text: str) -> list[str]:
        return [
            re.sub(r"^\d+[.)]\s+", "", line).strip()
            for line in text.splitlines()
            if re.match(r"^\d+[.)]\s+", line.strip())
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


def frontmatter_list_yaml(items: list[str]) -> str:
    if not items:
        return "  []"
    return "\n".join(f"  - {json.dumps(item)}" for item in items)


def extract_frontmatter_block(text: str) -> tuple[str | None, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end():]


def parse_title_from_frontmatter(frontmatter: str | None) -> str | None:
    if not frontmatter:
        return None

    match = re.search(
        r'^title:\s*["\']?(.*?)["\']?\s*$',
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

    title = parse_title_from_frontmatter(frontmatter) or fallback_title
    description = ""

    if frontmatter:
        match = re.search(
            r'^description:\s*["\']?(.*?)["\']?\s*$',
            frontmatter,
            flags=re.MULTILINE,
        )
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
            frontmatter_list_yaml(categories),
            "topics:",
            frontmatter_list_yaml(topics),
            "---",
            "",
        ]
    )

    return clean_frontmatter + body.strip() + "\n"


def build_prompt(
        *,
        plan: dict[str, Any],
        style_profile: dict[str, Any],
        voice_samples: list[dict[str, Any]],
        topic_samples: list[dict[str, Any]],
        frameworks: list[dict[str, Any]],
        research: list[dict[str, Any]],
        notes: list[dict[str, Any]],
) -> str:
    def block_docs(label: str, docs: list[dict[str, Any]], chars: int) -> str:
        return "\n\n---\n\n".join(
            "\n".join(
                [
                    f"{label}: {doc.get('title', doc.get('name', ''))}",
                    doc.get("content", "")[:chars],
                ]
            )
            for doc in docs
        ) or "None"

    voice_block = block_docs("VOICE SAMPLE", voice_samples, MAX_SAMPLE_CHARS)
    topic_block = block_docs("RELATED POST", topic_samples, MAX_SAMPLE_CHARS)
    research_block = block_docs("RESEARCH", research, 4000)
    notes_block = block_docs("NOTES", notes, 2500)

    framework_block = "\n\n---\n\n".join(
        "\n".join(
            [
                f"FRAMEWORK: {fw.get('name')}",
                fw.get("summary", ""),
                ", ".join(fw.get("key_claims", [])),
            ]
        )
        for fw in frameworks
    ) or "None"

    return f"""
You are ghostwriting a blog post for Toby Weston.

Follow the supplied plan exactly.

Style profile:
{json.dumps(style_profile, indent=2)}

Approved plan:
{plan["raw"]}

Frameworks:
{framework_block}

Voice samples:
{voice_block}

Related posts:
{topic_block}

Research material:
{research_block}

Author notes:
{notes_block}

Return a complete Astro-ready MDX post.

Rules:
- Use British English
- Preserve the plan's central insight
- Prefer short paragraphs
- Avoid generic AI explanation tone
- Avoid startup marketing tone
- Avoid developer evangelism style
""".strip()


def write_output(content: str, title: str) -> Path:
    today = date.today().isoformat()
    slug = slugify(title or "untitled")
    path = OUTPUT_DIR / f"{today}-{slug}.mdx"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Draft a blog post from an approved plan.",
        epilog=(
            "Workflow:\n"
            "  python plan_post.py --topic \"...\"\n"
            "  review the plan\n"
            "  python generate_post.py --plan output/plans/<plan>.plan.md"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--plan",
        required=True,
        help="Plan file created by plan_post.py",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    plan_path = Path(args.plan)

    if not plan_path.exists():
        raise SystemExit(f"Plan not found: {plan_path}")

    plan = parse_plan(plan_path)
    style_profile = load_style_profile()

    query = " ".join(
        [
            plan.get("recommended_title", ""),
            plan.get("central_insight", ""),
            plan.get("why_this_matters", ""),
            plan.get("recommended_framework", ""),
            " ".join(plan.get("key_arguments", [])),
            " ".join(plan.get("suggested_topics", [])),
        ]
    ).strip()

    voice_samples = pick_voice_anchors(MAX_STYLE_SAMPLES)
    topic_samples = pick_topic_samples(query)
    frameworks = pick_frameworks(query)
    research = pick_research(query)
    notes = pick_notes(query)

    prompt = build_prompt(
        plan=plan,
        style_profile=style_profile,
        voice_samples=voice_samples,
        topic_samples=topic_samples,
        frameworks=frameworks,
        research=research,
        notes=notes,
    )

    if args.dry_run:
        print("DRY RUN\n")
        print(f"Plan: {plan_path}")
        print(f"Recommended title: {plan.get('recommended_title', '')}")
        print(f"Recommended framework: {plan.get('recommended_framework', '')}")

        print("\nVoice samples:")
        for doc in voice_samples:
            print(f" - {doc.get('date', '')} | {doc.get('title', '')}")

        print("\nTopic samples:")
        for doc in topic_samples:
            print(f" - {doc.get('date', '')} | {doc.get('title', '')}")

        print("\nFrameworks:")
        for fw in frameworks:
            print(f" - {fw.get('name', '')}")

        if research:
            print("\nResearch:")
            for item in research:
                print(f" - {item.get('path', '')}")

        if notes:
            print("\nNotes:")
            for item in notes:
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

    final_title = parse_title_from_frontmatter(
        extract_frontmatter_block(content)[0]
    ) or fallback_title

    output_path = write_output(content, final_title)

    print(f"Draft written to: {output_path}")
    print(f"Plan used: {plan_path}")


if __name__ == "__main__":
    main()