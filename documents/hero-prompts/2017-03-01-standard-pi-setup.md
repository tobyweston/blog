# Standard Raspberry Pi Setup — hero prompt

- **Post:** `astro/src/content/blog/2017-03-01-standard-pi-setup.md`
- **Style:** `technical-blueprint`
- **Series:** the `raspberry-pi` series — all six carry the berry, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-raspberry-pi.jpg`
- **Video:** none

## Why this image

This is the post you read when a Pi comes out of the box: burn an image to an SD
card, enable SSH, turn the GUI off and run it headless. The moment that
represents all of it is the card going into the slot — nothing happens before it
and everything follows from it.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about standard raspberry pi setup on a Raspberry Pi. Output a single flat
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
A Raspberry Pi board drawn flat in three-quarter view, centred in the image, seen
from slightly above.

A microSD card floats just clear of its slot at the edge of the board, aligned to
slide in, drawn as in an exploded diagram with a dashed construction line and a
small arrow showing the direction of insertion. The card is drawn large and
clearly, at the same scale as the board rather than realistically small.

Behind the board and well separated from it, the flat outline of a computer
monitor drawn in thin dashed line only, unfilled and ghosted, with a diagonal
line struck through it — indicating a screen that is deliberately not there.

RECURRING MOTIF
In the lower-right corner of the board, a small raspberry emblem etched into the
silkscreen: a cluster of seven or eight rounded drupelets packed into a rough
heart shape, with two pointed leaves angled up from the top. Drawn flat in the
same uniform line weight as the rest of the illustration, as a mark etched on the
board rather than a sticker, a badge or a photograph. No text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the SD card slot, ending in a small empty
circle.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - On the face of the microSD card: "OS"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the raspberry emblem, and no code,
terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the microSD card and the arrow showing it sliding in,
and to nothing else. The board, the ghosted monitor and the strike-through stay
navy and slate — the ghosted monitor lighter still, so it reads as absent.
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

- **The ghosted monitor reading as a real one.** It must be obviously absent:
  thin dashed outline, no fill, struck through. If it comes back solid the image
  says the opposite of headless.
- **The monitor drifting into the top band** that the card crop removes. It can
  sit behind and to one side rather than above.
- **"OS" is a safe string**, but watch it is not expanded to "OS CARD" or similar.
- **Text-free fallback:** drop the label. A card entering a slot beside a
  struck-through screen still reads.
- **The berry turning into fruit.** It is a small etched mark in a corner, not a
  photograph of a raspberry and not a sticker. If it arrives rendered, shaded or
  oversized, regenerate — and never let it take the amber.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2017-03-01-standard-pi-setup --install ~/Downloads/<your-file>.jpg
```
