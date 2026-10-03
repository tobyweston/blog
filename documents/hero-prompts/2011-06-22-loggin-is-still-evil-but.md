# Logging is Still Evil, But... — hero prompt

- **Post:** `astro/src/content/blog/2011-06-22-loggin-is-still-evil-but.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, logging group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

The follow-up: if you are going to log, be honest about it and test it. The post
asserts against Log4J in tests using a custom appender.

So the image is the companion to the first: the same machine, the same taps — but
now the drain pipe runs into a measuring vessel with a gauge on it, instead of
leaving the frame. The clutter has become something you can check.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about testing what your code logs instead of pretending it does not matter. Output a single flat image, no borders, no frame, no
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
The same clean mechanical assembly as in the companion image, drawn in isometric
projection: three connected components in a row joined by proper couplings, with a
small tap clamped onto each and a thin pipe running from every tap.

Here the three thin pipes converge into one larger pipe that no longer leaves the
frame. Instead it runs down into a closed measuring vessel standing on the RIGHT:
a cylindrical body with a graduated sight window up one side and a round dial
mounted on its front.

The vessel is clearly a measuring instrument, not a bucket.

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
One faint callout leader line points at the sight window on the vessel, ending in
a small empty circle. The dial carries tick marks but no numbers.

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
The amber accent belongs to the measuring vessel, its sight window and its dial,
and to nothing else. The machine, the taps and all the pipework stay navy and
slate — the reverse of the companion image, where the taps held the accent.

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

- **A bucket or an open tank.** It is a sealed instrument with a gauge; that is
  what makes this post about testing rather than draining.
- **Numbers on the dial.** Ticks only.
- **Losing the match with the companion image.** Same machine, same taps, same
  layout — only the far end changes.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2011-06-22-loggin-is-still-evil-but --install ~/Downloads/<your-file>.jpg
```
