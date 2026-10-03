# Yet Another TeamCity Build Monitor — hero prompt

- **Post:** `astro/src/content/blog/2014-01-01-another-teamcity-build-monitor.mdx`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** the video keyframe installed earlier, which was not good enough —
  see below
- **Video:** the post embeds one, but a keyframe was tried and rejected

## Why this image

Replaces the video keyframe, which is a GitHub screenshot — dated, and unreadable
at card size.

Radiate's whole idea is that it aggregates *all* builds into one indicator, with
no cherry-picking which failures to ignore. So the image is many inputs and
exactly one lamp, with no bypass path anywhere.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about reducing every build's status to one single pass or fail. Output a single flat image, no borders, no frame, no
watermark, no signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
A single large indicator lamp drawn in isometric projection on the RIGHT of the
image: a round lens in a substantial housing mounted on a bracket, plainly the one
output of the whole arrangement.

Feeding it from the LEFT, TWELVE thin lines, each beginning at its own small
square terminal arranged in a grid of three rows by four. Every line runs right
and gathers into a single trunk, and that trunk enters the lamp housing.

Every one of the twelve is connected. None bypasses the trunk, none stops short,
and there is no second lamp and no switch anywhere on the run.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth. Treat the lower fifth of the frame as unusable: a mark placed
there loses its cup to the card crop and survives only as a stray orange squiggle.

SUPPORTING DETAIL
One faint callout leader line points at the point where the twelve lines gather
into the single trunk, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers, branding or filenames. Any marking that would read as
writing must be left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and well
clear of the amber element — its orange steam is close in hue to the accent, so
the two must never sit near each other or at similar sizes.
The amber accent belongs to the lamp's lens and the single trunk feeding it, and
to nothing else. All twelve terminals, their lines and the housing stay navy and
slate.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject and all text inside that central
band; the top 20% and the bottom 20% may be cut away entirely, so put nothing
there but background. Keep text away from the left and right edges too. The
image must still read at roughly 550 x 190 pixels, so favour large shapes and
strong contrast over fine detail. Balanced composition, not centred
symmetrically.
```

## What is most likely to go wrong

- **A second lamp, or a switch on the run.** Both would imply you can select which
  failures count, which is the thing Radiate refuses to do.
- **Any line bypassing the trunk.** All twelve go in.
- **A screen or dashboard.** It is a physical lamp; see the standing rule about
  dashboards.
- **The Java mark sinking into the bottom fifth**, where the card crop removes
  the cup and leaves only its steam. This is the failure that spoiled the first
  pass of this batch.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2014-01-01-another-teamcity-build-monitor --install ~/Downloads/<your-file>.jpg
```
