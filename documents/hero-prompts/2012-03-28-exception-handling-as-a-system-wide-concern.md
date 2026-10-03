# Exception Handling as a System Wide Concern — hero prompt

- **Post:** `astro/src/content/blog/2012-03-28-exception-handling-as-a-system-wide-concern.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, exceptions group — all carry the Java cup in its
  series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` at all today.
- **Video:** none

## Why this image

The post argues against ad-hoc catching — "catching an exception, arbitrarily
logging it before rethrowing isn't a good idea" — and for identifying the
boundaries of a system and handling failure at those few places.

So the image is an enclosure with a small number of gates. Everything inside
flows outward, and all of it must leave through one of three marked openings. The
wall is unbroken everywhere else, which is the argument.

## Reference images

None. These posts illustrate themselves with code listings, which must not be
drawn — see the standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about handling failures at a system's boundaries rather than everywhere. Output a single flat image, no borders, no frame, no
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
A closed rectangular enclosure drawn in isometric projection, centred in the
image, like a walled compound seen from above and to one side. Its wall is
continuous and unbroken except in exactly THREE places, where a gate is set into
it.

Inside the enclosure, six or seven small cubes are scattered, each with a short
dashed path curving away from it. Every one of those paths converges on one of
the three gates — none of them crosses the wall anywhere else.

Each gate is drawn as a distinct framed opening with a shaped surround, clearly a
deliberate structure rather than a gap.

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
One faint callout leader line points at one of the gates, ending in a small empty
circle. The ground outside the enclosure is empty.

TEXT IN THE IMAGE
  - No text labels anywhere in this image.
No code, braces, semicolons, terminal output or filenames anywhere in the image,
and no text beside the Java mark. Any marking that would read as writing must be
left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark in the corner is the only exception. Keep it
small and well clear of the amber element — its orange steam is close in hue to
the accent, so the two must never sit near each other or at similar sizes.
The amber accent belongs to the three gates and their surrounds, and to nothing
else. The wall, the cubes and all the dashed paths stay navy and slate.

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

- **Paths leaking through the wall.** Every route must reach a gate. A single
  dashed line crossing the wall elsewhere contradicts the post.
- **Too many gates.** Three. A wall with ten openings is not a boundary.
- **It reading as a maze.** The enclosure is simple and rectangular; the interior
  has no internal walls.
- **The Java mark growing, or its orange drifting towards the amber.** It is
  small, in the lower-left corner, and well away from the accent. Of all three
  series marks this is the one most likely to muddy a card, because its steam is
  close in hue to the accent.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-03-28-exception-handling-as-a-system-wide-concern --install ~/Downloads/<your-file>.jpg
```
