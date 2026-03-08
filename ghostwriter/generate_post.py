from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus, urlparse
from urllib.request import Request, urlopen

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

HERO_IMAGES_DIR = (OUTPUT_DIR.parent.parent.parent / "public" / "images" / "heroes").resolve()
DEFAULT_HERO_IMAGE = "/images/heroes/generic.jpg"


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


def parse_frontmatter_value(frontmatter: str | None, keys: list[str]) -> str:
    if not frontmatter:
        return ""

    for key in keys:
        match = re.search(
            rf"^{re.escape(key)}:\s*(.*?)\s*$",
            frontmatter,
            flags=re.MULTILINE,
        )
        if not match:
            continue
        value = match.group(1).strip().strip("'\"")
        if value:
            return value
    return ""


def trim_text(text: str, max_chars: int) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= max_chars:
        return clean
    trimmed = clean[:max_chars].rsplit(" ", 1)[0].strip()
    return trimmed or clean[:max_chars].strip()


def categories_to_string(categories: list[str]) -> str:
    cleaned: list[str] = []
    seen: set[str] = set()

    for category in categories:
        value = slugify(str(category))
        if not value or value in seen:
            continue
        cleaned.append(value)
        seen.add(value)

    return " ".join(cleaned) if cleaned else "engineering"


def keywords_to_string(categories: list[str], topics: list[str]) -> str:
    keywords: list[str] = []
    seen: set[str] = set()

    for item in [*categories, *topics]:
        key = re.sub(r"\s+", " ", str(item)).strip()
        if not key:
            continue
        dedupe_key = key.lower()
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        keywords.append(key)

    return ", ".join(keywords[:12])


def _extension_for(content_type: str, final_url: str) -> str:
    content_type = content_type.lower().split(";", 1)[0].strip()
    if content_type == "image/jpeg":
        return ".jpg"
    if content_type == "image/png":
        return ".png"
    if content_type == "image/webp":
        return ".webp"

    path = Path(urlparse(final_url).path)
    ext = path.suffix.lower()
    if ext == ".jpeg":
        return ".jpg"
    if ext in {".jpg", ".png", ".webp"}:
        return ext
    return ".jpg"


def download_hero_image(*, search_query: str, slug: str) -> str:
    HERO_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    query = re.sub(r"\s+", " ", search_query).strip() or "software engineering"
    encoded_query = quote_plus(query)
    sources = [
        f"https://source.unsplash.com/1600x900/?{encoded_query}",
        f"https://loremflickr.com/1600/900/{encoded_query}",
    ]

    for url in sources:
        try:
            request = Request(url, headers={"User-Agent": "ghostwriter/1.0"})
            with urlopen(request, timeout=20) as response:
                image = response.read()
                if len(image) < 1024:
                    continue

                content_type = response.headers.get("Content-Type", "")
                final_url = response.geturl()
                extension = _extension_for(content_type, final_url)

            filename = f"{date.today().isoformat()}-{slug}-hero{extension}"
            destination = HERO_IMAGES_DIR / filename
            destination.write_bytes(image)
            return f"/images/heroes/{filename}"
        except Exception:
            continue

    return DEFAULT_HERO_IMAGE


def normalise_generated_document(
        generated: str,
        *,
        fallback_title: str,
        categories: list[str],
        topics: list[str],
        subtitle_hint: str,
        hero_image: str,
) -> str:
    frontmatter, body = extract_frontmatter_block(generated)

    today = date.today().isoformat()

    title = parse_title_from_frontmatter(frontmatter) or fallback_title
    description = parse_frontmatter_value(frontmatter, ["description"])

    if not description:
        body_text = re.sub(r"^#\s+.*?$", "", body, flags=re.MULTILINE).strip()
        first_para = body_text.split("\n\n", 1)[0].strip()
        description = first_para[:180].rstrip(".") + "." if first_para else "Draft post."

    subtitle = parse_frontmatter_value(frontmatter, ["subTitle", "subtitle"])
    if not subtitle:
        subtitle = trim_text(subtitle_hint or description, 110).rstrip(".")

    category_string = categories_to_string(categories)
    keywords = keywords_to_string(categories, topics)
    hero = hero_image or parse_frontmatter_value(frontmatter, ["heroImage"]) or DEFAULT_HERO_IMAGE

    clean_frontmatter = "\n".join(
        [
            "---",
            f"title: {json.dumps(title)}",
            f"subTitle: {json.dumps(subtitle)}",
            f"description: {json.dumps(description)}",
            f"pubDate: {json.dumps(today)}",
            f"draft: {str(DEFAULT_DRAFT).lower()}",
            f"categories: {json.dumps(category_string)}",
            f"keywords: {json.dumps(keywords)}",
            f"heroImage: {json.dumps(hero)}",
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
- Start with frontmatter that includes title, subTitle and description
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

    topic_hint = plan.get("recommended_title") or query

    voice_samples = pick_voice_anchors(MAX_STYLE_SAMPLES)
    topic_samples = pick_topic_samples(query)
    frameworks = pick_frameworks(query)
    research = pick_research(query, topic_or_query=topic_hint)
    notes = pick_notes(query, topic_or_query=topic_hint)

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
    hero_query = " ".join(
        [
            fallback_title,
            plan.get("central_insight", ""),
            "software engineering",
        ]
    ).strip()
    hero_image = download_hero_image(
        search_query=hero_query,
        slug=slugify(fallback_title or "untitled"),
    )

    content = normalise_generated_document(
        generated,
        fallback_title=fallback_title,
        categories=categories,
        topics=topics,
        subtitle_hint=plan.get("central_insight", ""),
        hero_image=hero_image,
    )

    final_title = parse_title_from_frontmatter(
        extract_frontmatter_block(content)[0]
    ) or fallback_title

    output_path = write_output(content, final_title)

    print(f"Draft written to: {output_path}")
    print(f"Hero image: {hero_image}")
    print(f"Plan used: {plan_path}")


if __name__ == "__main__":
    main()
