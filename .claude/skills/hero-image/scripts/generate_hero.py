#!/usr/bin/env python3
"""
Generate a hero image from a saved prompt and install it.

Takes the prompt this skill already wrote under documents/hero-prompts/, sends it
to the Gemini image API, and does every step reference/output-spec.md asks for:
normalise to 1600x900, keep it under the size budget, write it to the right
path, set heroImage in the post's frontmatter, and render the card crop so the
result can be checked at the size it actually ships at.

Deliberately stdlib only — urllib and subprocess out to ImageMagick, which the
machine already has. Nothing to pip install.

    export GEMINI_API_KEY=...        # https://aistudio.google.com/apikey
    generate_hero.py 2011-10-29-java-source-on-mac
    generate_hero.py <slug> --variants 3     # pick from three, install none
    generate_hero.py <slug> --dry-run        # everything but the API call
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PROMPTS = REPO / "documents/hero-prompts"
HEROES = REPO / "astro/public/images/heroes"
POSTS = [REPO / "astro/src/content/blog", REPO / "astro/src/content/unpublished"]

ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/interactions"
MODEL = "gemini-3.1-flash-image"
# Free-tier keys are gated per model: the workhorse above is paid-only and
# answers 429 "limit: 0 input tokens per minute". --model switches to another.
MODELS = ["gemini-3.1-flash-image", "gemini-3.1-flash-lite-image",
          "gemini-3-pro-image", "gemini-2.5-flash-image"]

# YouTube keyframes, best first. maxres is 1280x720 and often absent; hq always
# exists but is 480x360 and 4:3, so it needs cropping to 16:9.
THUMBS = ["maxresdefault", "sddefault", "hqdefault"]

# reference/output-spec.md
WIDTH, HEIGHT = 1600, 900
MAX_BYTES = 400 * 1024
QUALITY_STEPS = [86, 80, 74, 68, 62]
CARD_W, CARD_H = 546, 192


def fail(msg: str, hint: str = "") -> None:
    print(f"error: {msg}", file=sys.stderr)
    if hint:
        print(f"       {hint}", file=sys.stderr)
    sys.exit(1)


def find_post(slug: str) -> Path:
    """Accept a slug, filename or path and return the post."""
    candidate = Path(slug)
    if candidate.is_file():
        return candidate.resolve()
    stem = candidate.name.removesuffix(".md").removesuffix(".mdx")
    hits = [p for d in POSTS if d.is_dir() for p in d.iterdir()
            if p.suffix in {".md", ".mdx"} and p.stem == stem]
    if not hits:
        hits = [p for d in POSTS if d.is_dir() for p in d.iterdir()
                if p.suffix in {".md", ".mdx"} and stem in p.stem]
    if not hits:
        fail(f"no post matching {slug!r}", f"looked in {', '.join(str(d) for d in POSTS)}")
    if len(hits) > 1:
        fail(f"{slug!r} matches several posts: " + ", ".join(p.name for p in hits))
    return hits[0]


def read_prompt(post: Path) -> str:
    """Pull the ```text fenced block out of the saved prompt file."""
    path = PROMPTS / f"{post.stem}.md"
    if not path.is_file():
        fail(f"no prompt at {path.relative_to(REPO)}",
             "run the hero-image skill first — it writes the prompt this reads")
    blocks = re.findall(r"```text\n(.*?)```", path.read_text(), re.S)
    if not blocks:
        fail(f"no ```text block in {path.name}")
    return max(blocks, key=len).strip()


def find_image(node) -> bytes | None:
    """
    Walk the response for base64 image data.

    The REST docs don't pin the response shape down, so rather than hardcode one
    path this looks for any dict carrying a plausible base64 payload, preferring
    one that declares an image mime type.
    """
    found: list[tuple[int, str]] = []

    def walk(n, image_hint: bool):
        if isinstance(n, dict):
            hint = image_hint or "image" in str(n.get("mime_type", "")) or n.get("type") == "image"
            blob = n.get("data")
            if isinstance(blob, str) and len(blob) > 2048:
                found.append((0 if hint else 1, blob))
            for k, v in n.items():
                walk(v, hint or "image" in k.lower())
        elif isinstance(n, list):
            for v in n:
                walk(v, image_hint)

    walk(node, False)
    if not found:
        return None
    found.sort(key=lambda t: t[0])
    try:
        return base64.b64decode(found[0][1], validate=True)
    except Exception:
        return None


def call_gemini(prompt: str, key: str, model: str = MODEL,
                references: list[Path] | None = None) -> bytes:
    inputs: list[dict] = [{"type": "text", "text": prompt}]
    for ref in references or []:
        mime = "image/png" if ref.suffix.lower() == ".png" else "image/jpeg"
        inputs.append({
            "type": "image",
            "mime_type": mime,
            "data": base64.b64encode(ref.read_bytes()).decode(),
        })

    body = json.dumps({
        "model": model,
        "input": inputs,
        "response_format": {
            "type": "image",
            "mime_type": "image/jpeg",
            "aspect_ratio": "16:9",
            "image_size": "2K",
        },
    }).encode()

    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:600]
        hint = detail
        if e.code == 429 and "limit: 0" in detail:
            hint = (f"{model} is not available on this key's tier. Every image model\n"
                    f"       is gated to zero on the free tier, so this needs billing\n"
                    f"       enabled: https://ai.dev/rate-limit\n"
                    f"       Or generate in the Gemini app and install it with:\n"
                    f"         generate_hero.py <slug> --install ~/Downloads/<file>.jpg")
        fail(f"Gemini returned HTTP {e.code}", hint)
    except urllib.error.URLError as e:
        fail(f"could not reach Gemini: {e.reason}")

    data = find_image(payload)
    if data is None:
        fail("no image in the response",
             "response keys: " + ", ".join(sorted(payload)[:12]))
    return data


IMG_RE = re.compile(
    r"""(?:^import\s+\w+\s+from\s+['"]([^'"]+\.(?:png|jpe?g|gif|webp|svg))['"]"""
    r"""|!\[[^\]]*\]\(([^)]+\.(?:png|jpe?g|gif|webp|svg))\))""",
    re.M | re.I | re.X)


def find_post_images(post: Path) -> list[Path]:
    """
    Images the post already uses — its own charts, diagrams and screenshots.

    These are the best reference material a hero prompt has: they are already in
    the post's visual language, and for a data infographic they carry the actual
    numbers. Both import and markdown forms resolve relative to the post.
    """
    out: list[Path] = []
    for m in IMG_RE.finditer(post.read_text()):
        ref = m.group(1) or m.group(2)
        path = (post.parent / ref).resolve()
        if path.is_file() and path not in out:
            out.append(path)
    return out


def find_youtube_id(post: Path) -> str | None:
    """A <YouTubeEmbed youtubeId="..."> in the body, or youtubeId in frontmatter."""
    text = post.read_text()
    m = re.search(r'youtubeId=["\']([A-Za-z0-9_-]{6,})["\']', text)
    if m:
        return m.group(1)
    m = re.search(r'^youtubeId:\s*["\']?([A-Za-z0-9_-]{6,})["\']?\s*$', text, re.M)
    return m.group(1) if m else None


def fetch_keyframe(video_id: str) -> tuple[bytes, str]:
    """Pull the largest keyframe YouTube has for this video."""
    for name in THUMBS:
        url = f"https://img.youtube.com/vi/{video_id}/{name}.jpg"
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = r.read()
        except urllib.error.HTTPError:
            continue
        except urllib.error.URLError as e:
            fail(f"could not reach YouTube: {e.reason}")
        # A missing thumbnail 302s to a 120x90 placeholder rather than 404ing.
        if len(data) > 8000:
            return data, name
    fail(f"no usable keyframe for video {video_id}")


def normalise(raw: Path, dest: Path) -> int:
    """Centre-crop to 1600x900 and step quality down until under budget."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    for q in QUALITY_STEPS:
        subprocess.run([
            "magick", str(raw),
            "-resize", f"{WIDTH}x{HEIGHT}^",
            "-gravity", "center", "-extent", f"{WIDTH}x{HEIGHT}",
            "-quality", str(q), str(dest),
        ], check=True)
        if dest.stat().st_size <= MAX_BYTES:
            return q
    return QUALITY_STEPS[-1]


def card_check(hero: Path) -> Path:
    """Render the hero as the card actually crops it, for eyeballing."""
    out = Path(tempfile.gettempdir()) / f"card-check-{hero.stem}.png"
    crop_h = round(WIDTH / (CARD_W / CARD_H))
    subprocess.run([
        "magick", str(hero),
        "-gravity", "center", "-crop", f"{WIDTH}x{crop_h}+0+0", "+repage",
        "-resize", f"{CARD_W}x", str(out),
    ], check=True)
    return out


def set_hero(post: Path, ref: str) -> str:
    """Replace heroImage, or insert it after pubDate as the spec asks."""
    text = post.read_text()
    m = re.match(r"(---\n)(.*?)(\n---\n)", text, re.S)
    if not m:
        fail(f"no frontmatter in {post.name}")
    head, fm, tail = m.groups()
    line = f'heroImage: "{ref}"'

    if re.search(r"^heroImage:", fm, re.M):
        was = re.search(r"^heroImage:\s*(.*)$", fm, re.M).group(1).strip()
        fm = re.sub(r"^heroImage:.*$", line, fm, count=1, flags=re.M)
        action = f"replaced {was}"
    else:
        lines = fm.split("\n")
        at = next((i for i, l in enumerate(lines) if l.startswith("pubDate:")), len(lines) - 1)
        lines.insert(at + 1, line)
        fm = "\n".join(lines)
        action = "added"

    post.write_text(head + fm + tail + text[m.end():])
    return action


def already_has_bespoke_hero(post: Path) -> bool:
    """
    True only if this post's own hero exists on disk.

    Checking the frontmatter path is not enough: a rename can point heroImage at
    the convention path before any image is there, and skipping on that basis
    silently leaves the post with a broken hero.
    """
    return any((HEROES / f"{post.stem}-hero{ext}").is_file()
               for ext in (".jpg", ".jpeg", ".png", ".svg", ".webp"))


def run_all(args) -> None:
    """
    Work through every saved prompt in one go.

    The per-post command is fine for one hero; it does not scale to a backlog of
    forty. This runs the lot, skips what is already done, keeps going past
    failures and prints a summary at the end, so a batch can be left alone.
    """
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        fail("GEMINI_API_KEY is not set",
             "create one at https://aistudio.google.com/apikey, then: export GEMINI_API_KEY=...")

    prompts = sorted(PROMPTS.glob("*.md"))
    if not prompts:
        fail(f"no prompts in {PROMPTS.relative_to(REPO)}")

    todo, skipped = [], []
    for path in prompts:
        try:
            post = find_post(path.stem)
        except SystemExit:
            skipped.append((path.stem, "no matching post"))
            continue
        if already_has_bespoke_hero(post) and not args.force:
            skipped.append((path.stem, "already has its own hero"))
            continue
        todo.append(post)

    print(f"{len(todo)} to generate, {len(skipped)} skipped")
    for slug, reason in skipped:
        print(f"  skip  {slug}  ({reason})")
    if not todo:
        return
    est = len(todo) * (0.034 if "lite" in args.model else 0.101)
    print(f"\nmodel {args.model}, roughly ${est:.2f} for {len(todo)} images")
    if args.dry_run:
        for post in todo:
            print(f"  would generate  {post.stem}")
        return

    done, failed = [], []
    for i, post in enumerate(todo, 1):
        print(f"\n[{i}/{len(todo)}] {post.stem}")
        try:
            prompt = read_prompt(post)
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                raw = Path(tmp.name)
            raw.write_bytes(call_gemini(prompt, key, args.model))
            dest = HEROES / f"{post.stem}-hero.jpg"
            quality = normalise(raw, dest)
            raw.unlink(missing_ok=True)
            set_hero(post, f"/images/heroes/{post.stem}-hero.jpg")
            print(f"        {dest.stat().st_size / 1024:.0f} KB, q{quality}  "
                  f"card: {card_check(dest)}")
            done.append(post.stem)
        except SystemExit as e:
            # fail() exits; in batch we note it and carry on to the next post.
            print(f"        FAILED ({e.code})")
            failed.append(post.stem)
        except Exception as e:
            print(f"        FAILED ({e})")
            failed.append(post.stem)
        if i < len(todo):
            time.sleep(args.delay)

    print(f"\n{len(done)} generated, {len(failed)} failed")
    for slug in failed:
        print(f"  failed  {slug}")

    if done and not args.no_build:
        r = subprocess.run(["npx", "astro", "build"], cwd=REPO / "astro",
                           capture_output=True, text=True)
        print(f"build: {'ok' if r.returncode == 0 else 'FAILED'}")
    print("\nLook at every card check before pushing. This script does not judge "
          "images,\nand a wrong number or a mangled label is not something it can see.")


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate and install a post's hero image.")
    ap.add_argument("post", nargs="?", help="slug, filename or path")
    ap.add_argument("--all", action="store_true",
                    help="work through every saved prompt, skipping posts that "
                         "already have their own hero")
    ap.add_argument("--force", action="store_true",
                    help="with --all, regenerate even where a hero exists")
    ap.add_argument("--delay", type=float, default=2.0,
                    help="seconds between requests in --all (default 2)")
    ap.add_argument("--variants", type=int, default=1,
                    help="generate N candidates and install none; pick one yourself")
    ap.add_argument("--install", metavar="FILE",
                    help="install an image you generated elsewhere (e.g. in the "
                         "Gemini app) instead of calling the API")
    ap.add_argument("--keyframe", nargs="?", const=True, metavar="VIDEO_ID",
                    help="use the post's YouTube keyframe instead of generating. "
                         "The id is found in the post if you don't give one.")
    ap.add_argument("--dry-run", action="store_true",
                    help="resolve the post and prompt, then stop before calling the API")
    ap.add_argument("--reference", nargs="*", metavar="FILE",
                    help="images to send with the prompt as reference. With no "
                         "values, uses the post's own images (up to 4).")
    ap.add_argument("--model", default=MODEL, choices=MODELS,
                    help=f"image model (default {MODEL})")
    ap.add_argument("--no-build", action="store_true", help="skip the astro build")
    args = ap.parse_args()

    if args.all:
        run_all(args)
        return
    if not args.post:
        ap.error("give a post, or --all")

    post = find_post(args.post)
    ref = f"/images/heroes/{post.stem}-hero.jpg"
    dest = HEROES / f"{post.stem}-hero.jpg"
    video_id = args.keyframe if isinstance(args.keyframe, str) else find_youtube_id(post)

    print(f"post   {post.relative_to(REPO)}")

    # Report what the post offers before anything can fail: --dry-run is the
    # documented way to find out which of its own images are worth attaching.
    post_images = find_post_images(post)
    references: list[Path] = []
    if args.reference is not None:
        references = [Path(f).expanduser() for f in args.reference] or post_images[:4]
        missing = [r for r in references if not r.is_file()]
        if missing:
            fail("reference image not found: " + ", ".join(str(m) for m in missing))
        vector = [r for r in references if r.suffix.lower() == ".svg"]
        if vector:
            fail("can't send SVG as a reference: " + ", ".join(v.name for v in vector),
                 "the API wants a raster image. Open it in a browser and screenshot\n"
                 "       it, or export a PNG, then pass that instead.")
        for r in references:
            print(f"ref    {r.name}")
    elif post_images:
        print(f"images this post already uses ({len(post_images)}): "
              f"{', '.join(i.name for i in post_images[:4])}"
              f"{' ...' if len(post_images) > 4 else ''}")
        print("       pass --reference to send them with the prompt")

    if args.keyframe:
        if not video_id:
            fail("no youtubeId in the post", "pass one: --keyframe <VIDEO_ID>")
        print(f"source keyframe from youtube video {video_id}")
        prompt = None
    else:
        if video_id:
            print(f"note   this post embeds youtube video {video_id} — a keyframe is")
            print(f"       usually the better hero. Re-run with --keyframe to use it.")
        prompt = None if args.install else read_prompt(post)
        if prompt is None:
            print("source installing a file you generated elsewhere")
        else:
            print(f"prompt {len(prompt)} chars, first line: {prompt.splitlines()[0][:70]}...")
    print(f"hero   {ref}")

    if args.dry_run:
        print("\ndry run — stopping before fetching anything")
        return

    if args.install:
        src = Path(args.install).expanduser()
        if not src.is_file():
            fail(f"no such file: {src}")
        quality = normalise(src, dest)
        size_kb = dest.stat().st_size / 1024
        print(f"\nwrote  {dest.relative_to(REPO)}  from {src.name}, "
              f"{WIDTH}x{HEIGHT}, {size_kb:.0f} KB, q{quality}")
        print(f"       frontmatter: {set_hero(post, ref)}")
        print(f"       card check:  {card_check(dest)}")
        if not args.no_build:
            r = subprocess.run(["npx", "astro", "build"], cwd=REPO / "astro",
                               capture_output=True, text=True)
            print(f"       build:       {'ok' if r.returncode == 0 else 'FAILED'}")
            if r.returncode:
                sys.exit(1)
        print("\nLook at the card check before calling it done.")
        return

    if args.keyframe:
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            raw = Path(tmp.name)
        data, which = fetch_keyframe(video_id)
        raw.write_bytes(data)
        # maxresdefault is 1280x720, so this is a 1.25x upscale — invisible at
        # the 546px the card renders, and it keeps every hero the same size.
        # Don't be tempted to skip the upscale: -extent then letterboxes it.
        quality = normalise(raw, dest)
        raw.unlink(missing_ok=True)
        size_kb = dest.stat().st_size / 1024
        print(f"\nwrote  {dest.relative_to(REPO)}  from {which}, {size_kb:.0f} KB, q{quality}")
        print(f"       frontmatter: {set_hero(post, ref)}")
        print(f"       card check:  {card_check(dest)}")
        if not args.no_build:
            r = subprocess.run(["npx", "astro", "build"], cwd=REPO / "astro",
                               capture_output=True, text=True)
            print(f"       build:       {'ok' if r.returncode == 0 else 'FAILED'}")
            if r.returncode:
                sys.exit(1)
        return

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        fail("GEMINI_API_KEY is not set",
             "create one at https://aistudio.google.com/apikey, then: export GEMINI_API_KEY=...")

    if args.variants > 1:
        out = Path(tempfile.mkdtemp(prefix="hero-variants-"))
        for i in range(1, args.variants + 1):
            raw = out / f"raw-{i}.jpg"
            raw.write_bytes(call_gemini(prompt, key, args.model, references))
            q = normalise(raw, out / f"{post.stem}-hero-{i}.jpg")
            print(f"  variant {i}: {out / f'{post.stem}-hero-{i}.jpg'} (q{q})")
        print(f"\n{args.variants} candidates in {out} — nothing installed.")
        print(f"Install one with:  cp <chosen> {dest}")
        return

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        raw = Path(tmp.name)
    raw.write_bytes(call_gemini(prompt, key, args.model, references))
    quality = normalise(raw, dest)
    raw.unlink(missing_ok=True)

    size_kb = dest.stat().st_size / 1024
    print(f"\nwrote  {dest.relative_to(REPO)}  {WIDTH}x{HEIGHT}, {size_kb:.0f} KB, q{quality}")
    print(f"       frontmatter: {set_hero(post, ref)}")
    print(f"       card check:  {card_check(dest)}")

    if not args.no_build:
        r = subprocess.run(["npx", "astro", "build"], cwd=REPO / "astro",
                           capture_output=True, text=True)
        tail = (r.stdout or r.stderr).strip().splitlines()[-1:] or [""]
        print(f"       build:       {'ok' if r.returncode == 0 else 'FAILED'} — {tail[0].strip()}")
        if r.returncode:
            sys.exit(1)

    print("\nLook at the card check before calling it done — if the focal subject")
    print("is clipped, tighten the prompt's composition section, not the crop.")


if __name__ == "__main__":
    main()
