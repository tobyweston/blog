# Setter vs Constructor Injection — hero prompt

- **Post:** `astro/src/content/blog/2010-05-01-setter-vs-constructor-injection.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

Constructor injection forces dependencies to be set explicitly and up front;
setter injection leaves the object open to being assembled, or half assembled,
later.

So the image compares two housings: one that cannot be closed until every socket
is filled, and one that closes regardless and has openings reachable afterwards.

## Reference images

None worth attaching.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about supplying a thing's dependencies when it is built, or afterwards. Output a single flat image, no borders, no frame, no watermark,
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
TWO housings drawn in isometric projection, side by side and the same size.

The LEFT housing is open, with THREE sockets in its base, all three filled with
seated plugs. Its lid is lowering into place on a dashed construction line, and a
simple interlock is visible: a catch on the lid that lines up only because all
three sockets are occupied.

The RIGHT housing is closed, but has THREE hatches cut into its outer wall, two
of them standing open. Through one open hatch an empty socket is visible inside.
A plug is being pushed in through that hatch from outside.

Both housings are otherwise identical.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the interlock catch on the left-hand lid,
ending in a small empty circle.

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
The amber accent belongs to the interlock catch on the left-hand housing, and to
nothing else — the thing that will not let it close half assembled.

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

- **The right-hand housing having no empty socket.** Its openness is the point.
- **The two housings differing in size or shape.** Same object, two ways of
  filling it.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-05-01-setter-vs-constructor-injection --install ~/Downloads/<your-file>.jpg
```
