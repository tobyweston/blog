# Functional Interfaces in Java 8 — hero prompt

- **Post:** `astro/src/content/blog/2014-04-07-functional-interfaces-in-java8.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The post's definition is simple: a functional interface is an interface with a
single method, and anywhere you use a lambda you are using one.

So the image is a mounting plate with exactly one socket — not two, not three —
and a small plain part dropping into it. It opens the Java 8 group with
`classes-vs-functions` and `method-references`.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about an interface with exactly one method, which a lambda satisfies. Output a single flat image, no borders, no frame, no watermark,
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
A mounting plate drawn in isometric projection, standing upright and centred,
with exactly ONE socket cut into its face. The plate is large and the single
socket is small, so the emptiness around it is obvious.

Descending into that socket along a dashed construction line, one small plain
part with no features other than the connector that matches.

To the LEFT, a second plate of the same size lies discarded flat on the ground,
face up, with THREE sockets in it — plainly not the one in use.

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
One faint callout leader line points at the single socket on the upright plate,
ending in a small empty circle.

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
The amber accent belongs to the single socket and the part descending into it,
and to nothing else. Both plates and the discarded three-socket one stay navy and
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

- **More than one socket on the upright plate.** Exactly one. That is the
  definition.
- **The discarded plate dominating.** It is context, lying flat and plainly out
  of use.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2014-04-07-functional-interfaces-in-java8 --install ~/Downloads/<your-file>.jpg
```
