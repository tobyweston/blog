# Scala Exception Handling — hero prompt

- **Post:** `astro/src/content/blog/2012-03-30-scala-exception-handling.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` at all today.
- **Video:** none

## Why this image

The post moves from Java's checked exceptions, which a developer can swallow or
rethrow, to Scala's functional alternatives where a failure is a value you must
open: `Either`, `Option`, `Try`.

So the image is a sorter. One thing goes in, and it can only come out of one of
two labelled chutes — there is no third path and nothing falls on the floor. That
is what "handled as a value" looks like as a mechanism.

## Reference images

None. The post's only figures are code listings, which must not be drawn — see the
standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about handling failure as a value rather than by throwing. Output a single flat image, no borders, no frame, no
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
A single sorting chute drawn in isometric projection, centred in the image. One
wide inlet at the TOP narrows to a junction in the middle, where it divides into
exactly TWO outlets angling down to the LEFT and to the RIGHT.

A small cube is entering the inlet at the top. A second, identical cube has
already travelled down the RIGHT outlet and rests at its mouth.

The junction itself contains a simple pivoting flap, drawn clearly, showing that
everything arriving must be sent down one side or the other.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the pivoting flap, ending in a small empty
circle. The floor beneath the chute is clean and empty — nothing has escaped.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beside the left outlet: "LEFT"
  - Beside the right outlet: "RIGHT"
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
The amber accent belongs to the pivoting flap at the junction, and to nothing
else. Both chutes, both cubes and the frame stay navy and slate.

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

- **A third outlet.** Two, exactly. A chute with three ways out destroys the
  point.
- **"LEFT" and "RIGHT" must sit on the correct sides** and are otherwise safe
  strings.
- **Spillage.** Nothing on the floor, nothing in mid-air outside the chute.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-03-30-scala-exception-handling --install ~/Downloads/<your-file>.jpg
```
