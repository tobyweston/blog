# Refactoring in 10 Minutes — hero prompt

- **Post:** `astro/src/content/blog/2019-08-09-refactoring-in-10-minutes.mdx`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** the video keyframe installed earlier, which was not good enough —
  see below
- **Video:** the post embeds one, but a keyframe was tried and rejected

## Why this image

Replaces the video keyframe, which is a title card — the skill's own rule says to
generate rather than use one, because a slide of lettering reads as nothing at
192px.

Refactoring changes structure, not behaviour, so the image is one mechanism shown
twice: the same parts, the same connectors at each end, tangled in the first and
orderly in the second. If the ends did not match it would be a rewrite.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about improving the structure of code without changing what it does. Output a single flat image, no borders, no frame, no
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
TWO housings drawn in isometric projection, side by side and the same size, each
open at the top so the linkage inside is visible. Both have an IDENTICAL input
connector on the far left and an IDENTICAL output connector on the far right.

The LEFT housing's interior is a tangle: five rods crossing each other at
irregular angles, two of them doubling back, with the path from input to output
hard to follow.

The RIGHT housing holds exactly the SAME five rods — recognisably the same parts,
same lengths — but arranged in a clean orderly run, parallel and evenly spaced,
with the path from input to output immediately readable.

A single dashed construction line with a small arrowhead runs from the left
housing to the right.

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
Two faint callout leader lines point at the two output connectors, one on each
housing, ending in small empty circles — showing that the ends are unchanged.

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
The amber accent belongs to the two identical output connectors, one on each
housing, and to nothing else. Both shells and all the rods stay navy and slate.

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

- **The two housings holding different parts.** Same rods, rearranged. Different
  parts would mean a rewrite, not a refactoring.
- **The connectors differing.** Identical at both ends is the entire definition.
- **The tangle being too tidy.** The left side must be visibly hard to follow.
- **The Java mark sinking into the bottom fifth**, where the card crop removes
  the cup and leaves only its steam. This is the failure that spoiled the first
  pass of this batch.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2019-08-09-refactoring-in-10-minutes --install ~/Downloads/<your-file>.jpg
```
