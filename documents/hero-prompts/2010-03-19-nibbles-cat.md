# A Concrete Deadlock Example — hero prompt

- **Post:** `astro/src/content/blog/2010-03-19-nibbles-cat.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, concurrency and tempus-fugit group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

The author's own deadlock, introduced into a statistics daemon by a
synchronisation policy spread across two classes. The companion to the detector
post, and deliberately the same jam drawn without the probe — here the point is
how it happened, not how to find it.

So this image shows the ordering: two sequences taking the same two locks in
opposite directions.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a real deadlock caused by two classes locking in opposite orders. Output a single flat image, no borders, no frame, no
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
TWO horizontal tracks drawn in isometric projection, one above the other, each
running the full width of the image.

Two upright posts stand in the middle of the image, passing through both tracks —
the SAME two posts serve both tracks, which must be unmistakable.

On the UPPER track, a carriage travels left to right and has already latched onto
the LEFT post, with its forward latch reaching towards the RIGHT post.
On the LOWER track, an identical carriage travels right to left and has already
latched onto the RIGHT post, with its forward latch reaching towards the LEFT
post.

Neither reaching latch can close, because each target post is already held.

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
Two faint callout leader lines point at the two reaching latches, ending in small
empty circles.

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
The amber accent belongs to the two reaching latches that cannot close, and to
nothing else. The posts, both carriages and both tracks stay navy and slate.

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

- **Four posts instead of two.** The same two, taken in opposite orders, is the
  whole cause.
- **A cat.** The slug is a joke about the author's cat; the post is not about one.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-03-19-nibbles-cat --install ~/Downloads/<your-file>.jpg
```
