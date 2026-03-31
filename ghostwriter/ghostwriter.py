from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PLANS_DIR = BASE_DIR / "output" / "plans"

PLAN_RE = re.compile(r"Plan written to:\s*(.+)")
DRAFT_RE = re.compile(r"Draft written to:\s*(.+)")
REVISED_RE = re.compile(r"Revised draft written to:\s*(.+)")

DEFAULT_PLAN_MODEL = "gpt-5-mini"
DEFAULT_DRAFT_MODEL = "gpt-5"
DEFAULT_REVISION_MODEL = "gpt-5-mini"
DEFAULT_EVAL_MODEL = "gpt-5-mini"


def slugify(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def print_banner(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80 + "\n")


def print_step(step: str, detail: str | None = None) -> None:
    print(f"\n>>> {step}")
    if detail:
        print(detail)


def prompt_continue(message: str, auto: bool) -> None:
    if auto:
        print(f"[auto] {message}")
        return

    try:
        input(f"\n{message}\nPress Enter to continue...")
    except KeyboardInterrupt:
        print("\nStopped.")
        raise SystemExit(1)


def prompt_choice(message: str, choices: list[str], default: str, auto: bool) -> str:
    if auto:
        print(f"[auto] {message} -> {default}")
        return default

    print(f"\n{message}")
    print(f"Choices: {', '.join(choices)}")
    raw = input(f"Enter choice [{default}]: ").strip().lower()

    if not raw:
        return default
    if raw not in choices:
        print(f"Unknown choice '{raw}', using default '{default}'.")
        return default
    return raw


def run_python_script(script_name: str, args: list[str]) -> str:
    cmd = [sys.executable, str(BASE_DIR / script_name), *args]

    print("\n$ " + " ".join(cmd) + "\n")

    result = subprocess.run(
        cmd,
        cwd=BASE_DIR,
        text=True,
        capture_output=True,
    )

    if result.stdout:
        print(result.stdout)

    if result.returncode != 0:
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)

    return result.stdout


def parse_output_path(pattern: re.Pattern[str], output: str, label: str) -> Path:
    match = pattern.search(output)
    if not match:
        raise RuntimeError(f"Could not find {label} in command output.")
    return Path(match.group(1).strip())


def expected_plan_path(topic: str) -> Path:
    today = date.today().isoformat()
    slug = slugify(topic) or "untitled-plan"
    return PLANS_DIR / f"{today}-{slug}.plan.md"


def resolve_model(stage_model: str | None, global_model: str | None, default_model: str) -> str:
    if stage_model:
        return stage_model
    if global_model:
        return global_model
    return default_model


def build_plan_args(args: argparse.Namespace) -> list[str]:
    cmd = [
        "--topic", args.topic,
        "--audience", args.audience,
        "--model", resolve_model(args.plan_model, args.model, DEFAULT_PLAN_MODEL),
    ]

    if args.angle:
        cmd.extend(["--angle", args.angle])

    if args.notes:
        cmd.extend(["--notes", args.notes])

    if args.research:
        cmd.append("--research")
        cmd.extend(args.research)

    if args.notes_file:
        cmd.append("--notes-file")
        cmd.extend(args.notes_file)

    if args.plan_dry_run:
        cmd.append("--dry-run")

    return cmd


def build_generate_args(plan_path: Path, args: argparse.Namespace) -> list[str]:
    cmd = [
        "--plan", str(plan_path),
        "--model", resolve_model(args.draft_model, args.model, DEFAULT_DRAFT_MODEL),
    ]

    if args.draft_dry_run:
        cmd.append("--dry-run")

    return cmd


def build_revise_args(draft_path: Path, mode: str, model: str, in_place: bool = True) -> list[str]:
    cmd = [
        "--input", str(draft_path),
        "--mode", mode,
        "--model", model,
    ]
    if in_place:
        cmd.append("--in-place")
    return cmd


def build_evaluate_args(draft_path: Path, model: str) -> list[str]:
    return [
        "--input", str(draft_path),
        "--model", model,
    ]


def maybe_run_revision(draft_path: Path, args: argparse.Namespace, auto: bool) -> Path:
    if args.skip_revision:
        print_step("Skipping revision", "You asked to skip the revision step.")
        return draft_path

    print_banner("REVISION")
    print("A first draft exists. You can optionally run a focused revision pass.")
    print("Common good defaults are:")
    print("  - tighten")
    print("  - sharpen-argument")
    print("  - stronger-hook")
    print("  - more-like-me")
    print("  - less-tutorial")

    choice = prompt_choice(
        "Would you like to run a revision pass?",
        choices=["none", "tighten", "stronger-hook", "more-like-me", "less-tutorial", "more-opinionated", "add-framework"],
        default=args.revision_mode or "tighten",
        auto=auto if args.auto_revision else False,
    )

    if choice == "none":
        print_step("No revision selected", "Keeping the freshly generated draft.")
        return draft_path

    print_step(
        "Running revision",
        f"Mode: {choice}\nThis will overwrite the current draft in place.",
    )

    output = run_python_script(
        "revise_post.py",
        build_revise_args(
            draft_path,
            choice,
            resolve_model(args.revision_model, args.model, DEFAULT_REVISION_MODEL),
            in_place=True,
        ),
    )

    revised_path = parse_output_path(REVISED_RE, output, "revised draft path")
    print_step("Revision complete", f"Revised draft: {revised_path}")
    return revised_path


def maybe_run_evaluation(draft_path: Path, args: argparse.Namespace, auto: bool) -> None:
    if args.skip_evaluation:
        print_step("Skipping evaluation", "You asked to skip the evaluation step.")
        return

    print_banner("EVALUATION")
    print("Next step is evaluation.")
    print("This checks voice fidelity, central idea, originality, clarity, AI smell, and publishability.")

    choice = prompt_choice(
        "Run evaluation now?",
        choices=["yes", "no"],
        default="yes",
        auto=auto,
    )

    if choice == "no":
        print_step("Evaluation skipped", "You can run evaluate_post.py manually later.")
        return

    print_step("Running evaluation", f"Draft: {draft_path}")
    run_python_script(
        "evaluate_post.py",
        build_evaluate_args(draft_path, resolve_model(args.eval_model, args.model, DEFAULT_EVAL_MODEL)),
    )


def new_workflow(args: argparse.Namespace) -> None:
    print_banner("👻 Ghostwriter")
    print("This command will guide you through the full writing pipeline:")
    print("  1. create a plan")
    print("  2. pause for plan review")
    print("  3. generate a draft from the approved plan")
    print("  4. optionally revise")
    print("  5. evaluate the result")

    print_step(
        "Brief",
        "\n".join(
            [
                f"Topic:   {args.topic}",
                f"Angle:   {args.angle or '(none)'}",
                f"Notes:   {args.notes or '(none)'}",
                f"Research:{' ' + ', '.join(args.research) if args.research else ' (auto/common + post-specific only)'}",
                f"Notes file:{' ' + ', '.join(args.notes_file) if args.notes_file else ' (auto/common + post-specific only)'}",
            ]
        ),
    )

    prompt_continue("About to create a plan.", auto=args.auto)

    print_banner("PLAN")
    plan_output = run_python_script("plan_post.py", build_plan_args(args))

    if args.plan_dry_run:
        print_step("Plan dry-run complete", "No plan file was created because --plan-dry-run was used.")
        return

    plan_path = parse_output_path(PLAN_RE, plan_output, "plan path")
    if not plan_path.exists():
        # fallback for safety
        guess = expected_plan_path(args.topic)
        if guess.exists():
            plan_path = guess

    print_step("Plan created", f"Plan file: {plan_path}")
    print("Open the plan and read it before drafting.")
    print("You are checking for:")
    print("  - one strong central idea")
    print("  - a good title")
    print("  - a framework that makes sense")
    print("  - an outline worth writing")

    prompt_continue(
        f"Review this plan now:\n{plan_path}\n\nWhen happy, continue to draft generation.",
        auto=args.auto,
    )

    print_banner("DRAFT")
    draft_output = run_python_script("generate_post.py", build_generate_args(plan_path, args))

    if args.draft_dry_run:
        print_step("Draft dry-run complete", "No draft file was created because --draft-dry-run was used.")
        return

    draft_path = parse_output_path(DRAFT_RE, draft_output, "draft path")
    print_step("Draft created", f"Draft file: {draft_path}")

    revised_path = maybe_run_revision(draft_path, args, auto=args.auto)
    maybe_run_evaluation(revised_path, args, auto=args.auto)

    print_banner("DONE")
    print("Pipeline complete.")
    print(f"Plan:  {plan_path}")
    print(f"Draft: {revised_path}")
    print("\nSuggested next action:")
    print("Read the draft in your editor and make any final human edits before publishing.")


def rebuild_index_workflow(args: argparse.Namespace) -> None:
    print_banner("REBUILD SEMANTIC INDEX")
    print("This will rebuild the FAISS index from:")
    print("  - blog corpus")
    print("  - frameworks")
    print("  - research/common and research/posts/<slug>")
    print("  - notes/common and notes/posts/<slug>")
    print("\nUse this after adding or changing posts, frameworks, research, or notes.")

    prompt_continue("About to rebuild the semantic index.", auto=args.auto)
    run_python_script("build_index.py", [])
    print_step("Index rebuild complete", "Your retrieval layer is now up to date.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="👻 Ghostwriter CLI: guided plan → draft → revise → evaluate workflow.",
        epilog=(
            "Examples:\n"
            "  python ghostwriter.py new \"Why compliance fails developers\"\n"
            "  python ghostwriter.py new \"Code review as an evidence system\" --angle \"review is really an assurance mechanism\"\n"
            "  python ghostwriter.py new \"Trust in software delivery\" --auto\n"
            "  python ghostwriter.py reindex\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser(
        "new",
        help="Guided workflow: create plan, pause for review, generate draft, optionally revise and evaluate.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    new_parser.add_argument("topic", help="The blog topic or working title")
    new_parser.add_argument("--angle", help="Optional angle or thesis")
    new_parser.add_argument("--notes", help="Inline notes for the planner")
    new_parser.add_argument("--research", nargs="+", help="Research file paths (space or comma separated)")
    new_parser.add_argument("--notes-file", nargs="+", help="Note file paths (space or comma separated)")
    new_parser.add_argument("--audience", default="Senior engineers and engineering leaders")

    new_parser.add_argument("--model", help="Fallback model for all stages unless a stage-specific model is provided")
    new_parser.add_argument("--plan-model", help=f"Model used for planning (default: {DEFAULT_PLAN_MODEL})")
    new_parser.add_argument("--draft-model", help=f"Model used for drafting (default: {DEFAULT_DRAFT_MODEL})")
    new_parser.add_argument("--revision-model", help=f"Model used for revision (default: {DEFAULT_REVISION_MODEL})")
    new_parser.add_argument("--eval-model", help=f"Model used for evaluation (default: {DEFAULT_EVAL_MODEL})")

    new_parser.add_argument("--plan-dry-run", action="store_true", help="Run planning in dry-run mode only")
    new_parser.add_argument("--draft-dry-run", action="store_true", help="Run drafting in dry-run mode only")

    new_parser.add_argument("--skip-revision", action="store_true", help="Skip the revision step")
    new_parser.add_argument("--skip-evaluation", action="store_true", help="Skip the evaluation step")

    new_parser.add_argument(
        "--revision-mode",
        choices=["tighten", "stronger-hook", "more-like-me", "less-tutorial", "more-opinionated", "add-framework", "sharpen-argument"],
        help="Default suggested revision mode",
    )
    new_parser.add_argument(
        "--auto-revision",
        action="store_true",
        help="Automatically run the default revision mode without prompting",
    )
    new_parser.add_argument(
        "--auto",
        action="store_true",
        help="Run non-interactively where possible, with sensible defaults",
    )

    reindex_parser = subparsers.add_parser(
        "reindex",
        help="Rebuild the semantic FAISS index",
    )
    reindex_parser.add_argument(
        "--auto",
        action="store_true",
        help="Run without confirmation prompts",
    )

    args = parser.parse_args()

    if args.command == "new":
        new_workflow(args)
    elif args.command == "reindex":
        rebuild_index_workflow(args)


if __name__ == "__main__":
    main()