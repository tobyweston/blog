from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

from openai import OpenAI

from config import DEFAULT_MODEL, STYLE_PROFILE_JSON


REVISION_MODES = {
    "tighten": "Tighten the draft. Remove flab, repetition, and generic transitions while preserving meaning and voice.",
    "stronger-hook": "Rewrite the opening to create a stronger hook while staying true to the argument and Toby's style.",
    "more-like-me": "Make the draft sound more like Toby Weston based on the supplied style profile. Increase voice fidelity without becoming theatrical.",
    "less-tutorial": "Reduce tutorial tone. Make it more reflective, analytical, and blog-like.",
    "more-opinionated": "Make the draft a little more opinionated and slightly more contrarian, while staying grounded and credible.",
    "add-framework": "Strengthen or add a framework section if the argument would benefit from one.",
    "sharpen-argument": "Dramatically improve the central idea of the article. Clarify the core thesis, remove anything that dilutes it, and ensure every section serves the main argument.",
}


def load_style_profile_text() -> str:
    path = Path(STYLE_PROFILE_JSON)
    if not path.exists():
        raise SystemExit("Missing style profile. Run style_profile.py first.")
    return path.read_text(encoding="utf-8")


def slug_suffix(mode: str) -> str:
    return re.sub(r"[^a-z0-9\-]+", "-", mode.lower()).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Revise an existing draft intentionally.",
        epilog=(
            "Examples:\n"
            "  python revise_post.py --input path/to/draft.mdx --mode tighten\n"
            "  python revise_post.py --input path/to/draft.mdx --mode stronger-hook\n"
            "  python revise_post.py --input path/to/draft.mdx --mode more-like-me"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--input", required=True, help="Path to the draft .md/.mdx file")
    parser.add_argument(
        "--mode",
        required=True,
        choices=sorted(REVISION_MODES.keys()),
        help="Revision mode",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the input file instead of writing a sibling revised file",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Draft not found: {input_path}")

    draft = input_path.read_text(encoding="utf-8")
    style_profile = load_style_profile_text()
    revision_instruction = REVISION_MODES[args.mode]

    prompt = f"""
You are revising a blog post draft for Toby Weston.

Use British English.
Preserve the core meaning and central argument unless the instruction explicitly implies otherwise.
Do not add marketing tone, generic AI explanation tone, startup language, or developer evangelism.
Return only the revised full document.

Style profile:
{style_profile}

Revision instruction:
{revision_instruction}

Draft:
{draft}
""".strip()

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.responses.create(
        model=args.model,
        input=prompt,
    )

    revised = response.output_text.strip() + "\n"

    if args.in_place:
        output_path = input_path
    else:
        output_path = input_path.with_name(
            f"{input_path.stem}.{slug_suffix(args.mode)}{input_path.suffix}"
        )

    output_path.write_text(revised, encoding="utf-8")
    print(f"Revised draft written to: {output_path}")


if __name__ == "__main__":
    main()