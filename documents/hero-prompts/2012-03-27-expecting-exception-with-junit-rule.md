# Expecting Exceptions JUnit Rule — hero prompt

- **Post:** `astro/src/content/blog/2012-03-27-expecting-exception-with-junit-rule.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, exceptions group — all carry the Java cup in its
  series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` at all today.
- **Video:** none

## Why this image

The post replaces the try/fail/catch idiom — an improvised scaffold around the
thing you are testing — with JUnit's `ExpectedException` rule, a fixture built
for the job that can also inspect what it caught.

So the image is a purpose-made cradle positioned under a test rig: a shaped
receiver that catches exactly one falling part and holds it for inspection,
rather than a net strung up by hand.

## Reference images

None. These posts illustrate themselves with code listings, which must not be
drawn — see the standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a purpose-built test fixture for asserting that something failed. Output a single flat image, no borders, no frame, no
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
A test rig drawn in isometric projection: a simple upright frame holding a small
component at its top, centred in the image.

Directly below, mounted to the frame on proper brackets, a shaped cradle — a
receiver moulded to exactly fit the component, with a clamp arm on one side and a
small inspection window in its base.

One component is in mid-fall between the rig and the cradle, drawn with a short
dashed path showing it dropping straight into the receiver. A second, identical
component already sits seated in the cradle, held by the clamp.

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
One faint callout leader line points at the inspection window in the base of the
cradle, ending in a small empty circle. No loose netting, no rope, no improvised
scaffolding anywhere.

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
The amber accent belongs to the cradle, its clamp arm and its inspection window,
and to nothing else. The frame, both components and the brackets stay navy and
slate.

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

- **A net or a basket.** The whole point is that it is purpose-built and fitted.
  A sagging net says the opposite.
- **The component missing the cradle.** It falls straight in.
- **The rig stealing focus.** The cradle is the subject; the frame above should
  be plain and unremarkable.
- **The Java mark growing, or its orange drifting towards the amber.** It is
  small, in the lower-left corner, and well away from the accent. Of all three
  series marks this is the one most likely to muddy a card, because its steam is
  close in hue to the accent.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-03-27-expecting-exception-with-junit-rule --install ~/Downloads/<your-file>.jpg
```
