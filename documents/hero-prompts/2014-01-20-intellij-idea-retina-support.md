# IntelliJ IDEA Retina Support — hero prompt

- **Post:** `astro/src/content/blog/2014-01-20-intellij-idea-retina-support.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

A short practical post: IDEA 13's retina support is broken on JDK 7 and 8, so the
author stays on 1.6 for crisp rendering.

So the image is the same test pattern rendered through two different cartridges —
one crisp, one visibly coarse — which is a comparison that survives being shrunk
to card size.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about rendering that is sharp on one runtime and soft on the next. Output a single flat image, no borders, no frame, no watermark,
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
TWO identical projection units drawn in isometric projection, side by side, each
with a cartridge seated in its base and a flat panel standing in front of it
showing what it produces.

The LEFT unit's panel carries a crisp pattern: fine, evenly spaced parallel lines
and a small circle with a clean edge.

The RIGHT unit's panel carries the SAME pattern rendered coarsely: the lines are
thick and stepped, and the circle's edge is visibly built from square steps.

The two units are otherwise identical, including their panels' size and frame.

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
One faint callout leader line points at the stepped edge of the circle on the
right-hand panel, ending in a small empty circle.

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
The amber accent belongs to the crisp pattern on the LEFT panel, and to nothing
else. Both units, both cartridges and the coarse right-hand pattern stay navy and
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

- **The difference being too subtle.** It must read at 192px: fine lines against
  obviously chunky stepped ones.
- **A real screenshot or any UI chrome.** Abstract test patterns only.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2014-01-20-intellij-idea-retina-support --install ~/Downloads/<your-file>.jpg
```
