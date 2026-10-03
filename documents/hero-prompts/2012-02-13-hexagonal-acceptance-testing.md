# Hexagonal Acceptance Testing — hero prompt

- **Post:** `astro/src/content/blog/2012-02-13-hexagonal-acceptance-testing.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post's claim is that a unit test can also be an acceptance test: prove the unit
behaves a certain way, and that it behaves the same way in production, and the
intersection gives you both.

So the image is a hexagonal core with ports around its edge, and a single probe
coupled to one port — the same connection serving both purposes, rather than two
separate rigs.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about testing at an application's boundary so one test proves two things. Output a single flat image, no borders, no frame, no watermark,
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
A hexagonal block drawn in isometric projection, centred, with a port set into
each of its six faces. The hexagon is solid and plainly the core of the thing.

Coupled firmly to ONE of those ports, a single probe assembly reaching away to
the RIGHT, ending in a plain connector.

From that one probe, TWO separate dashed construction lines run outward to two
small identical recording plates standing apart from each other — one above the
probe and one below. The same single connection feeds both.

The other five ports are open and empty.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the coupling where the probe meets the
hexagon, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons,
terminal output, version numbers, brand names or filenames. Nothing may be
numbered or named, and any marking that would read as writing must be left out
rather than rendered as placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the single coupling where the probe meets the port,
and to nothing else — it is the one connection doing both jobs.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-02-13-hexagonal-acceptance-testing --install ~/Downloads/<your-file>.jpg
```
