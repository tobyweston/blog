# Sending Messages vs Method Invocation — hero prompt

- **Post:** `astro/src/content/blog/2012-10-06-sending-messages-vs-method-invocation.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

Alan Kay's original idea of OO was message passing, not method calls, and the post
explores why the difference matters. It already illustrates itself with a
photograph of a letter — that is the author's own metaphor, so the hero takes it.

Two objects, a posted message travelling between them, and no rigid linkage
anywhere.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about objects sending messages to each other rather than calling each other's methods. Output a single flat image, no borders, no frame, no watermark,
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
TWO separate closed housings drawn in isometric projection, one on the LEFT and
one on the RIGHT, with a wide empty gap between them. Neither is connected to the
other by any shaft, rod, pipe or cable — the gap is completely clear.

Each housing has a slot in its side, like a letter box.

In the gap, a single flat sealed envelope is in mid-travel from the left housing's
slot towards the right one's, drawn flat-on so its shape is unmistakable, with a
dashed path behind it showing where it has come from.

Below, drawn faint and secondary, a short length of rigid coupling lies
disconnected on the ground, plainly not in use.

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
One faint callout leader line points at the receiving slot on the right-hand
housing, ending in a small empty circle.

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
The amber accent belongs to the envelope in flight, and to nothing else. Both
housings, both slots and the discarded coupling stay navy and slate.

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

- **Any rigid connection between the housings.** The gap must be empty; that is
  the distinction from a method call.
- **The envelope reading as a parcel or a data packet.** A flat sealed envelope,
  drawn plainly.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-10-06-sending-messages-vs-method-invocation --install ~/Downloads/<your-file>.jpg
```
