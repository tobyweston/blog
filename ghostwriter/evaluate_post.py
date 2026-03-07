from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from openai import OpenAI

from config import DEFAULT_MODEL, STYLE_PROFILE_JSON


def load_style_profile() -> dict:
    if not STYLE_PROFILE_JSON.exists():
        raise SystemExit("Missing style profile. Run style_profile.py first.")

    return json.loads(STYLE_PROFILE_JSON.read_text(encoding="utf-8"))


def load_draft(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Draft not found: {path}")

    return path.read_text(encoding="utf-8")


def build_prompt(style_profile: dict, draft: str) -> str:

    return f"""
You are reviewing a blog post written for Toby Weston.

Your job is to evaluate the draft and score its quality.

Use the author's style profile as the standard.

STYLE PROFILE:
{json.dumps(style_profile, indent=2)}

DRAFT:
{draft}

Evaluate the post against the following rubric.

Return valid markdown.

# Blog Evaluation

## Overall score
(0–10)

## Voice fidelity
Does it sound like Toby Weston?

Score: X/10

Explanation.

## Central idea
Is there a single clear insight?

Score: X/10

Explanation.

## Originality
Is the thinking interesting or insightful?

Score: X/10

Explanation.

## Clarity
Is the argument easy to follow?

Score: X/10

Explanation.

## Generic AI signals
Does the text show signs of generic AI writing?

Examples:
- overly neutral tone
- filler transitions
- generic explanations

Score: X/10 (10 = no AI smell)

Explanation.

## Publishability
Could this be published with only light editing?

Score: X/10

Explanation.

## Major weaknesses
List the 3 most important problems.

## Suggested improvements
Concrete revisions that would strengthen the article.
""".strip()


def main() -> None:

    parser = argparse.ArgumentParser(
        description="Evaluate a blog draft against the Toby Weston style profile."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the draft post (.md or .mdx)",
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
    )

    args = parser.parse_args()

    draft_path = Path(args.input)

    style_profile = load_style_profile()

    draft = load_draft(draft_path)

    prompt = build_prompt(style_profile, draft)

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.responses.create(
        model=args.model,
        input=prompt,
    )

    evaluation = response.output_text.strip()

    print("\n")
    print("=" * 80)
    print("BLOG POST EVALUATION")
    print("=" * 80)
    print("\n")

    print(evaluation)

    print("\n")
    print("=" * 80)


if __name__ == "__main__":
    main()