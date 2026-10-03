# Inheritance vs Composition — hero prompt

- **Post:** `astro/src/content/blog/2009-01-24-inheritance-vs-composition.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post's example is `Stack extends Vector` — inheriting an entire API when you
wanted four operations.

Its companion, `2013-01-10-stack-vs-deque`, draws the *symptom* as a tube with
side hatches. This one draws the *cause*, so it must not repeat that: a small
part bolted onto a far larger assembly and dragging all of it along, against the
same part holding one chosen component inside itself.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about taking everything from a parent versus holding only what you need. Output a single flat image, no borders, no frame, no watermark,
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
TWO arrangements side by side on a common base, drawn in isometric projection.

On the LEFT, a small neat housing is bolted rigidly to the side of a vast slab of
unrelated machinery — gears, pipes, brackets, four or five times its size. The
small housing is plainly the thing of interest, and it cannot be moved without
taking the whole slab with it. A single rigid bracket joins them.

On the RIGHT, the SAME small neat housing stands alone, open on one side, with
ONE chosen component seated inside it. Nothing else is attached. Beside it, the
rest of that vast machinery sits separately on the base, unconnected.

The small housing must be recognisably identical in both.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the rigid bracket on the left, ending in a
small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the single chosen component seated inside the
right-hand housing, and to nothing else.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## What is most likely to go wrong

- **The small housing differing between the two.** Same object, two ways of
  getting what it needs.
- **The slab looking small.** Its bulk is the cost of inheriting.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-01-24-inheritance-vs-composition --install ~/Downloads/<your-file>.jpg
```
