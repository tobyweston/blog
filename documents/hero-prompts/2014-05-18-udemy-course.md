# Udemy Java 8 Course — hero prompt

- **Post:** `astro/src/content/blog/2014-05-18-udemy-course.mdx`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** the video keyframe installed earlier, which was not good enough —
  see below
- **Video:** the post embeds one, but a keyframe was tried and rejected

## Why this image

Replaces the video keyframe, which is a mid-lecture slide reading "PART 2:
everything else" — a real frame, but it says nothing about the subject and
carries text the card cannot use.

The course covers what Java 8 added, so the image is a fitted toolkit case: older
tools already seated in their cut-outs, a group of new ones newly placed, and one
cut-out still empty.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a set of new language features taught as a course. Output a single flat image, no borders, no frame, no
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
An open fitted toolkit case drawn in isometric projection, centred, its lid
hinged back. The base is a shaped tray with SEVEN tool-shaped cut-outs.

FOUR cut-outs hold older tools, seated flush and plainly long in use: a spanner, a
driver, a small clamp, a gauge.

THREE further cut-outs hold newly added tools of distinctly different design —
slimmer, simpler, fewer parts — sitting slightly proud as though just placed.

One cut-out at the end of the row is empty.

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
One faint callout leader line points at one of the three newer tools, ending in a
small empty circle.

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
The amber accent belongs to the three newer tools sitting proud in their cut-outs,
and to nothing else. The case, the tray, the four older tools and the empty
cut-out stay navy and slate.

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

- **The new tools looking like the old ones.** Their different design is what
  makes them read as additions.
- **A full case.** The empty cut-out matters — more is coming.
- **Any lettering.** No course name, no version number, no branding.
- **The Java mark sinking into the bottom fifth**, where the card crop removes
  the cup and leaves only its steam. This is the failure that spoiled the first
  pass of this batch.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2014-05-18-udemy-course --install ~/Downloads/<your-file>.jpg
```
