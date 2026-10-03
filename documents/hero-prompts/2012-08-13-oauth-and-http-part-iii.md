# FreeAgent, OAuth & HTTP (Part III) — hero prompt

- **Post:** `astro/src/content/blog/2012-08-13-oauth-and-http-part-iii.md`
- **Style:** `technical-blueprint`
- **Series:** `FreeAgent, OAuth & HTTP`, part III of three. The hexagonal
  token appears in all three — carried in I, received in II, used as a die in III
- **Written:** 2026-10-03
- **Replaces:** a generic shared hero, which other posts keep
- **Video:** none

## Why this image

Part III is the practical end: every request is signed before it goes out, so the
API can verify it.

So the image closes the series — the hexagonal token is now mounted in a press
that stamps each outgoing envelope as it passes. The token has gone from being
carried, to being received, to being used.

## Logos are composited, not generated

This series carries two **real** logos rather than described ones, because both
rights holders effectively require it. FreeAgent's brand guidelines say "Don't
modify the FreeAgent logos in any way" and "Don't change the colour or dimensions"
— a generator redrawing it would breach that outright. The OAuth logo is Chris
Messina's, CC BY-SA 3.0, with attribution required.

So the prompt reserves two empty rectangles and forbids drawing any emblem, and
the real files are composited in afterwards, unmodified and at their original
aspect ratio:

```bash
# after generating, from the repo root
S=documents/brand            # OAuth (CC BY-SA 3.0) and FreeAgent official mark
H=astro/public/images/heroes/2012-08-13-oauth-and-http-part-iii-hero.jpg
magick $H \
  \( $S/oauth.png -resize 150x \) -gravity west -geometry +90+0 -composite \
  \( $S/freeagent.png -resize 150x \) -gravity east -geometry +90+0 -composite \
  -quality 86 $H
```

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about signing each outgoing request so the receiver can prove who sent it. Output a single flat image, no borders, no frame, no
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
A stamping press drawn in isometric projection, centred: a sturdy frame with a
vertical ram, and a horizontal belt running left to right beneath it.

Mounted in the head of the ram, facing down, the same small hexagonal token from
the earlier parts — it is the die.

Travelling along the belt, THREE flat sealed envelopes. The FIRST, on the right,
is blank and approaching. The SECOND is directly beneath the ram, being stamped.
The THIRD, on the left, has passed through and now carries a small hexagonal
impression on its face.

The progression left to right must be readable: blank, stamped, marked.

MARGINS
The entire composition must fit within the middle 68% of the image width. The
leftmost 16% and the rightmost 16% of the image are empty background — nothing
whatsoever extends into them: no object, no leg, no belt, no dashed path, no
callout line, no shadow and no marking. The background there is simply the same
plain ground and grid as everywhere else, with no panel, box, border, frame or
change of tone to indicate it.
Do not draw any logo, badge, emblem, roundel or icon anywhere in this image.
SUPPORTING DETAIL
One faint callout leader line points at the hexagonal impression on the envelope
that has passed through, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, URLs or filenames. Any marking that would read as writing must be left
out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
No other colour anywhere — the two composited logos bring their own, and a third
hue would leave the card without a focal point.
The amber accent belongs to the hexagonal die in the ram head and the matching
impression on the third envelope, and to nothing else. The press, the belt and
all three envelopes stay navy and slate.

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

- **The reserved areas not being left clear.** This is the one that matters: a
  callout line or a corner of the subject straying into either zone will end up
  underneath a logo. Check both areas before compositing.
- **A drawn logo appearing anyway.** Generators like to decorate. Any badge,
  roundel or emblem means regenerate — it will clash with the real mark.
- **The hexagonal token changing shape between parts.** The three cards are a
  series and the token is what ties them together.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-08-13-oauth-and-http-part-iii --install ~/Downloads/<your-file>.jpg
```
