# Inferring Type in a Micro DSL — hero prompt

- **Post:** `astro/src/content/blog/2009-02-23-infering-type-in-micro-dsl.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, micro-DSLs group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

The third micro-DSL post, and the one where it gets hard: Java struggles to infer
types once multiple generics are involved, so the API has to be shaped around the
limitation.

The image is a coupling with its mating profile left undetermined — a socket whose
shape has not been decided, with candidate profiles waiting beside it.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a compiler failing to work out types when several generics are in play. Output a single flat image, no borders, no frame, no
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
A single coupling drawn large in isometric projection, centred: a solid body whose
far end carries a finished connector, and whose near end is an open socket drawn
with a DASHED outline only, its shape plainly not yet determined.

Floating to the LEFT of that open socket, THREE candidate plugs of different
profiles — square, round, hexagonal — each on its own dashed construction line
converging on the socket. None of them is seated.

The dashed socket outline and the three candidates make clear that the shape is
still being worked out.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Java mark: a
plain cup seen from the side, drawn in a mid steel blue, with two curling wisps
of steam rising from it in a warm orange-red. Flat shapes, no outline, no saucer,
no circle or roundel around it and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the dashed socket outline, ending in a
small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames, and no text beside the Java mark. Any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark in the corner is the only exception. Keep it
small and well clear of the amber element — its orange steam is close in hue to
the accent, so the two must never sit near each other or at similar sizes.
The amber accent belongs to the dashed outline of the undetermined socket, and to
nothing else. The coupling body, the finished connector and all three candidate
plugs stay navy and slate.

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

- **The socket drawn solid.** Its being undecided is the subject; a dashed outline
  is how that reads.
- **One of the plugs seated.** None of them is chosen yet.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-02-23-infering-type-in-micro-dsl --install ~/Downloads/<your-file>.jpg
```
