# Disable Edimax Wifi Dongle's LED — hero prompt

- **Post:** `astro/src/content/blog/2016-01-06-disable-led-for-edimax.md`
- **Style:** `technical-blueprint`
- **Series:** the `raspberry-pi` series — all six carry the berry, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-raspberry-pi.jpg`
- **Video:** none

## Why this image

The post recompiles a kernel module for one reason: to stop a USB wi-fi dongle's
LED blinking. The subject is a single tiny light being put out, which is a gift
for this palette — one amber point in an otherwise cool drawing, and the post is
about removing it.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about disable edimax wifi dongle's led on a Raspberry Pi. Output a single flat
image, no borders, no frame, no watermark, no signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
A Raspberry Pi board drawn flat in three-quarter view, occupying the LEFT half of
the image. A small USB wi-fi dongle is plugged into one of its USB sockets,
drawn considerably larger than scale so it reads clearly — roughly a third of the
width of the board.

The dongle has one small round indicator LED on its upper face. That LED is the
focal point of the whole image and everything else is arranged to lead to it.

To the RIGHT of the board, floating clear of it as in an exploded diagram, the
same dongle drawn a second time at a larger size and cut away, so its interior is
visible: a simple rectangular chip on a small circuit board, with a short track
running from the chip to the LED. A dashed construction line links the cutaway to
the dongle on the board.

RECURRING MOTIF
In the lower-right corner of the board, a small raspberry emblem etched into the
silkscreen: a cluster of seven or eight rounded drupelets packed into a rough
heart shape, with two pointed leaves angled up from the top. Drawn flat in the
same uniform line weight as the rest of the illustration, as a mark etched on the
board rather than a sticker, a badge or a photograph. No text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the LED on the cutaway, ending in a small
empty circle.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beside the cutaway dongle: "LED"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the raspberry emblem, and no code,
terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the single LED and the short track feeding it, on
both the plugged-in dongle and the cutaway. Nothing else in the image is warm.
The board, both dongle bodies and the chip stay navy and slate.
The raspberry emblem stays in the line colour and never takes the accent.

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

- **The LED getting lost.** It is one small dot and it is the subject. If the
  cutaway is cluttered with components the eye has nothing to land on.
- **Light rays or a glow.** The style forbids glowing effects, and a starburst
  around the LED will wreck it. A solid amber dot is correct.
- **"LED" is about as safe a string as exists.** No excuse for it being wrong.
- **Text-free fallback:** drop the label entirely; the cutaway and the amber dot
  carry it.
- **The berry turning into fruit.** It is a small etched mark in a corner, not a
  photograph of a raspberry and not a sticker. If it arrives rendered, shaded or
  oversized, regenerate — and never let it take the amber.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2016-01-06-disable-led-for-edimax --install ~/Downloads/<your-file>.jpg
```
