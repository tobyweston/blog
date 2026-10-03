# A Simple Introduction to HTTP — hero prompt

- **Post:** `astro/src/content/blog/2012-06-10-http-simple.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The post's complaint is concrete: Apache's client needs a great deal of setup and
boilerplate to make one simple GET.

So the image compares two rigs that emit the identical slip — one a sprawling
assembly, the other a single small handheld unit. The companion post on encoding
reuses the same slip, so the pair read together.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about making a plain web request without a pile of configuration around it. Output a single flat image, no borders, no frame, no watermark,
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
TWO arrangements on a common base, drawn in isometric projection.

Filling the LEFT two thirds, a sprawling assembly: a large frame carrying eight
or nine separate components — tanks, valves, a pump, brackets — joined by a
tangle of pipes, with one output nozzle at its right-hand end.

On the RIGHT, standing alone and taking very little space, a single small
handheld unit: a compact body with a grip and one output nozzle.

Each emits an IDENTICAL small flat slip, drawn the same size and shape in both
cases, leaving the nozzle on a short dashed path. The two slips must be plainly
the same thing.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the small handheld unit, ending in a small
empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the small handheld unit and the slip it emits, and to
nothing else. The sprawling assembly, all its components and its own slip stay
navy and slate.

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

- **The two slips differing.** Same output, wildly different apparatus — that is
  the argument.
- **The small unit being hard to spot.** It is the accent and the point.
- **The large assembly looking broken.** It works; it is just enormous.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-06-10-http-simple --install ~/Downloads/<your-file>.jpg
```
