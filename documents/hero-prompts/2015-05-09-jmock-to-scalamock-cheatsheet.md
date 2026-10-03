# JMock to Scalamock Cheat Sheet — hero prompt

- **Post:** `astro/src/content/blog/2015-05-09-jmock-to-scalamock-cheatsheet.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` at all today.
- **Video:** none

## Why this image

The post is a lookup table: a JMock idiom on the left, its Scalamock equivalent on
the right, over and over. There is no mechanism and no argument — it is a
reference you keep open in a tab.

So the image is a conversion plate: paired fittings, each left-hand one matched
to exactly one right-hand one. It says "these two things mean the same" without
needing a single word of either library.

## Reference images

None. The post's only figures are code listings, which must not be drawn — see the
standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about translating one mocking library's idioms into another's. Output a single flat image, no borders, no frame, no
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
A flat rectangular plate drawn in three-quarter view, centred and filling most of
the image, like a machinist's conversion chart mounted on a wall.

The plate is divided down the middle by a single vertical rule into a LEFT column
and a RIGHT column.

FOUR rows run across it. In each row sits a pair of small fittings: a shape in
the left column, and a different shape in the right column that is clearly its
counterpart — a square peg beside a square socket, a hexagonal nut beside a
hexagonal driver, and so on. A short horizontal connector joins each pair across
the central rule.

The pairs must be visibly matched: each left shape obviously belongs to the right
shape on its own row and to no other.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
Small empty callout circles sit at the head of each column, with no text in them.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - No text labels anywhere in this image.
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the Scala mark, and no code, braces,
semicolons, terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The crimson Scala mark in the corner is the only exception to that palette. It
stays crimson, stays small, and stays clear of the amber, which is always the
larger warm shape in the image.
The amber accent belongs to the four short horizontal connectors crossing the
central rule, and to nothing else. The plate, the rule and all eight fittings
stay navy and slate.

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

- **Real text appearing in the rows.** It is a cheat sheet, so a generator will
  want to fill it with code. The standing rule against code walls applies — any
  lettering means a regeneration.
- **Mismatched pairs.** If the left and right shapes do not obviously correspond,
  the image says nothing.
- **A spreadsheet.** No gridlines beyond the single central rule and the row
  separations.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2015-05-09-jmock-to-scalamock-cheatsheet --install ~/Downloads/<your-file>.jpg
```
