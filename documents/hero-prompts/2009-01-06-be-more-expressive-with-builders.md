# Be More Expressive with Builders — hero prompt

- **Post:** `astro/src/content/blog/2009-01-06-be-more-expressive-with-builders.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, micro-DSLs group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

The post builds a fluent micro-DSL using `CountDownLatch` as its example, where
method chaining makes the call read like a phrase.

The image is that chain made physical: separate shaped links, each only fitting
the next, assembling into one continuous run. It opens the micro-DSL group.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about chaining small pieces together so code reads as a sentence. Output a single flat image, no borders, no frame, no
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
FOUR separate link pieces drawn in isometric projection, arranged left to right
across the middle of the image with small gaps between them.

Each link is a short bar with a differently shaped end: a tongue, a slot, a hook,
a ring. The shapes are cut so that each link's right-hand end plainly matches
only the left-hand end of the link beside it — the order is forced by the shapes.

The leftmost two are already joined. The remaining two are still separated, with
dashed construction lines showing them closing up.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Java mark: a
plain cup seen from the side, drawn in a mid steel blue, with two curling wisps
of steam rising from it in a warm orange-red. Flat shapes, no outline, no saucer,
no circle or roundel around it and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the joint between the two already-joined
links, ending in a small empty circle.

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
The amber accent belongs to the matched end faces where links meet — the joints —
and to nothing else. The link bodies stay navy and slate.

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

- **Identical links.** If any link could follow any other, the ordering idea is
  lost.
- **A literal chain of oval loops.** These are engineered couplings, not chain.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-01-06-be-more-expressive-with-builders --install ~/Downloads/<your-file>.jpg
```
