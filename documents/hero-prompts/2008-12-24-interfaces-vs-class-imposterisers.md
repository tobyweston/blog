# Interfaces vs Class Imposterisers — hero prompt

- **Post:** `astro/src/content/blog/2008-12-24-interfaces-vs-class-imposterisers.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

Mocking against an interface gives you a stand-in that only has to match a
defined shape. A class imposturiser copies the real thing itself — more faithful,
and more tightly bound to it.

So the image shows a socket with two different stand-ins offered up: a plain
plate cut to the socket's profile, and a full duplicate of the real component.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about standing in for a real thing by its shape, or by copying it whole. Output a single flat image, no borders, no frame, no watermark,
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
A mounting plate drawn in isometric projection, centred, with a single shaped
socket in its face. Seated in the socket, the real component: a detailed body
with ribs, a port and a bolt flange.

Floating ABOVE the plate on a dashed construction line, a plain flat plate cut to
exactly the socket's outline and nothing more — no ribs, no port, no detail at
all. Just the matching profile.

Floating BELOW the plate on its own dashed line, a complete duplicate of the real
component — same ribs, same port, same flange, indistinguishable from the one in
the socket.

Both are aligned to the same socket. One matches only its shape; the other copies
everything.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
Two faint callout leader lines, one to the plain profile above and one to the full
duplicate below, ending in small empty circles.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the plain flat profile plate above, and to nothing
else — the stand-in that only has to match a shape.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## What is most likely to go wrong

- **The duplicate differing from the real component.** It is a copy; any
  difference loses the point.
- **The plain plate gaining detail.** Its emptiness is what distinguishes it.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2008-12-24-interfaces-vs-class-imposterisers --install ~/Downloads/<your-file>.jpg
```
