# Is instanceof Really a Smell? — hero prompt

- **Post:** `astro/src/content/blog/2009-07-29-isnotinstanceofsmell.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post's line is that `instanceof` "fell in with a bad crowd and isn't really as
bad as it's cracked up to be".

So the image is guilt by association, drawn literally: a row of components on a
shelf, most of them visibly crude and damaged, one among them clean and
well-machined — and a single sweep arm about to clear the whole shelf without
distinguishing.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a sound tool judged by the company it keeps. Output a single flat image, no borders, no frame, no watermark,
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
A shelf drawn in isometric projection, spanning the middle of the image, holding
FIVE components in a row.

FOUR of them are visibly poor: burred edges, a cracked face, a bent lug, a
mismatched bolt. They look like things that deserve to be thrown out.

The FIFTH, standing among them and not at either end, is clean and precisely
machined, with true edges and a proper finish. It plainly does not belong with
the others.

Above the shelf, a single wide sweep arm on a pivot is poised to travel the full
length of the row in one motion, with a short dashed arc showing its path. It
covers all five.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the clean component, ending in a small
empty circle.

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
The amber accent belongs to the one clean, well-machined component, and to nothing
else. The four poor ones, the shelf and the sweep arm stay navy and slate.

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

- **The clean one at the end of the row.** It sits among them; that is the
  association.
- **The sweep arm missing some.** It covers all five indiscriminately.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-07-29-isnotinstanceofsmell --install ~/Downloads/<your-file>.jpg
```
