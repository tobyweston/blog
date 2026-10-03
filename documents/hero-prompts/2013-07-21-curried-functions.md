# Currying Functions in Java & Scala — hero prompt

- **Post:** `astro/src/content/blog/2013-07-21-curried-functions.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

Currying takes a function of several arguments and turns it into a chain, each
link taking one argument and handing back the next.

So the image is exactly that transformation: one wide block with several inlets
on the left, and beside it the same work done by a row of single-inlet units
feeding one into the next.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about turning one many-argument operation into a chain of single-argument ones. Output a single flat image, no borders, no frame, no watermark,
no signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
TWO arrangements side by side, drawn in isometric projection on a common base.

On the LEFT, ONE wide block with THREE separate inlet ports along its upper face,
all feeding into the single body, and one outlet at its right end.

On the RIGHT, THREE small units in a row, each the same height as the other two.
Each has exactly ONE inlet on its upper face and one outlet on its right side,
and each unit's outlet feeds directly into the next unit's body. The last one's
outlet leaves to the right.

A single dashed construction line runs from the left arrangement to the right,
with a small arrowhead, showing one becoming the other.

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
One faint callout leader line points at the join between the first and second
small units, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark in the corner is the only exception. Keep it
small and well clear of the amber element — its orange steam is close in hue to
the accent, so the two must never sit near each other or at similar sizes.
The amber accent belongs to the three single inlets on the right-hand row, and to
nothing else. The wide block, its three inlets and the unit bodies stay navy and
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

- **The right-hand units not feeding each other.** The chain is the whole idea;
  three units in a row not connected says nothing.
- **Different numbers of inlets between the two sides.** Three and three.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2013-07-21-curried-functions --install ~/Downloads/<your-file>.jpg
```
