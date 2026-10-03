# Catching Multiple Exceptions — hero prompt

- **Post:** `astro/src/content/blog/2011-08-29-catching-multiple-exceptions-and.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, exceptions group — all carry the Java cup in its
  series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` at all today.
- **Video:** none

## Why this image

The post's question is what to do when more than one thing fails: you do not want
to pick one and discard the rest, so you collect them and rethrow them all
together.

So the image is a collector. Several different items arrive from several places,
gather in one tray, and leave as a single bound bundle through one outlet. The
items stay visibly different inside the bundle — none of them was thrown away.

## Reference images

None. These posts illustrate themselves with code listings, which must not be
drawn — see the standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about collecting several failures during a batch and rethrowing them together. Output a single flat image, no borders, no frame, no
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
A wide collecting tray drawn in isometric projection, centred in the image, with
a single outlet chute leaving it on the RIGHT.

FOUR items of clearly different shapes — a cube, a cylinder, a wedge and a
hexagonal block — descend into the tray from above along separate dashed paths,
arriving from four different directions.

Leaving through the outlet, a single bundle: the same four shapes held together
by two straps around them. Each shape is still individually visible within the
bundle, not merged into one mass.

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
One faint callout leader line points at the straps around the bundle, ending in a
small empty circle. Nothing remains in the tray and nothing has fallen beside it.

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
The amber accent belongs to the two straps binding the bundle, and to nothing
else. The tray, the chute and all four shapes stay navy and slate.

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

- **The bundle becoming one blob.** The four shapes must stay distinguishable
  inside it. If they merge, the image says the failures were collapsed into one,
  which is exactly what the post rejects.
- **Items left behind.** Nothing in the tray, nothing on the floor.
- **Fewer than four inputs.** Several, from several directions, is the point.
- **The Java mark growing, or its orange drifting towards the amber.** It is
  small, in the lower-left corner, and well away from the accent. Of all three
  series marks this is the one most likely to muddy a card, because its steam is
  close in hue to the accent.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2011-08-29-catching-multiple-exceptions-and --install ~/Downloads/<your-file>.jpg
```
