# Diff Excel with Java and Hamcrest — hero prompt

- **Post:** `astro/src/content/blog/2012-09-14-diff-excel-with-java-and-hamcrest.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The post uses Hamcrest matchers and Apache POI to assert that two spreadsheets
match, and to report where they do not.

So the image is two grids held one above the other in a comparator frame, with
light passing through and a single cell standing proud where they disagree.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about comparing two spreadsheets cell by cell in a test. Output a single flat image, no borders, no frame, no watermark,
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
A comparator frame drawn in isometric projection, centred: two flat grid plates
held parallel one above the other on four corner posts, each plate ruled into a
regular grid of small squares.

The two grids are aligned exactly. In ONE position, a single small square block
stands proud between the plates, holding them minutely apart at that point — the
one cell where the two do not agree.

Everywhere else the plates sit flush.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth. Treat the lower fifth of the frame as unusable: a mark placed
there loses its cup to the card crop and survives only as a stray orange squiggle.

SECOND BRAND MARK
On the RIGHT of the image, clear of the main subject and above the lower third, an
Excel mark: a rounded square tile drawn in a deep green, with a bold white X
spanning most of its face, and one corner of the tile folded over to suggest a
document. Flat shapes, no outline, no text beside it.
The whole mark must sit above the lower third of the image and must not touch any
edge.

SUPPORTING DETAIL
One faint callout leader line points at the single proud block, ending in a small
empty circle.

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
The amber accent belongs to the one proud block, and to nothing else. Both grid
plates and the four posts stay navy and slate.
Three coloured things appear in this image and no more: the blue-and-orange Java
cup on the left, the green Excel tile on the right, and the amber block between
them. Keep all three well apart from one another.

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

- **More than one mismatch.** One. A field of differences is noise at card size.
- **The two marks crowding each other.** Java cup on the left, Excel tile on the
  right, the amber block between them. If either mark drifts towards the middle
  the card has no focal point.
- **Numbers or letters in the grid cells.** Empty ruled squares only — see the
  rule against drawing spreadsheets.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-09-14-diff-excel-with-java-and-hamcrest --install ~/Downloads/<your-file>.jpg
```
