# Logging is Evil, But... — hero prompt

- **Post:** `astro/src/content/blog/2010-10-18-logging-is-evil-but.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, logging group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

The post's complaint is that logging clutters code and couples concerns —
"we've all seen too much of" a logger declared and called throughout a class that
is trying to do something else.

So the image is a clean mechanism with a parasitic second system threaded through
it: taps spliced into every part, all draining to one pipe.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## The Log4j mark is composited, not drawn

Both posts are specifically about Log4j, so the real mark goes in from
`documents/brand/log4j.png` after generation, unmodified. The prompt reserves the
right of the frame as composition, not as a boxed area.

```bash
H=astro/public/images/heroes/2010-10-18-logging-is-evil-but-hero.jpg
magick $H \( documents/brand/log4j.png -resize x110 \) \
  -gravity east -geometry +110-20 -composite -quality 86 $H
```

Sourced from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Apache_Log4j_Logo.png),
where the file is tagged Apache License 2.0 with the Apache Software Foundation
as author. The ASF treats project logos as trademarks regardless, and its policy
is aimed at stopping a logo being used to denote someone else's product or
service; a hero on a post *about* Log4j is editorial use of the mark to refer to
the thing itself. Recorded in `documents/brand/README.md`.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about logging statements tangled through code that has nothing to do with them. Output a single flat image, no borders, no frame, no
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
A clean mechanical assembly drawn in isometric projection, centred: three
connected components in a row, joined by proper couplings, plainly one working
machine.

Spliced into that assembly, a second and quite separate system: a small tap
clamped onto EACH of the three components, and a thin pipe running from every tap,
all of them converging into one larger pipe that leaves the frame at the RIGHT.

The taps are obviously additions — clamped on from outside, not part of any
component — and the thin pipes cut across the clean lines of the machine.

MARGINS
The entire composition must fit within the LEFT 72% of the image width. The
rightmost 28% is empty background — nothing whatsoever extends into it: no
object, no pipe, no tap, no callout line, no shadow and no marking. The
background there is the same plain ground and grid as everywhere else, with no
panel, box, border, frame or change of tone to indicate it.
Do not draw any logo, badge, emblem, roundel or icon anywhere in this image.

SUPPORTING DETAIL
One faint callout leader line points at one of the clamped taps, ending in a small
empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the three clamped taps and their thin pipes, and to
nothing else. The three components and their couplings stay navy and slate.

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

- **The taps looking original.** They must read as clamped on afterwards; that is
  the complaint.
- **Liquid or drips.** No fluid, no spills — this is a diagram.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-10-18-logging-is-evil-but --install ~/Downloads/<your-file>.jpg
```

## One mark, not two

These posts carried the Java cup before Log4j was added. It has been dropped
rather than kept alongside: Log4j's mark is strongly red, the Java cup's steam is
orange, and the amber accent is warm too. Three warm things in one card leaves it
without a focal point, and of the two marks Log4j is both the more specific and
the one the post is actually about.
