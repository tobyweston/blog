# Pi Console Lead — hero prompt

- **Post:** `astro/src/content/blog/2015-12-28-pi-console-lead.md`
- **Style:** `technical-blueprint`
- **Series:** the `raspberry-pi` series — all six carry the berry, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-raspberry-pi-alt.jpg`
- **Video:** none

## Why this image

The Pi Zero has no ethernet port, so the post sets one up headless over a
USB-to-serial console lead wired to GPIO pins 8 and 10. The image is that
connection: four coloured jumper wires landing on named pins of the header, with
the cable running off to a laptop. The pins are the whole subject — the post is
specific about which ones.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about pi console lead on a Raspberry Pi. Output a single flat
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
A Raspberry Pi Zero board drawn flat in three-quarter view, filling the LEFT
two-thirds of the image, with its long double row of GPIO header pins clearly
drawn along the top edge.

FOUR separate jumper wires run from that header off towards the RIGHT, gathering
into a single cable that ends in a USB connector lying at the right edge of the
image. The four wires are drawn as smooth curves, well separated, not a bundle.

Only two of the header pins are connected, near the middle of the row, and those
two pins are drawn slightly enlarged with a small ring around each.

RECURRING MOTIF
In the lower-right corner of the board, a small raspberry emblem etched into the
silkscreen: a cluster of seven or eight rounded drupelets packed into a rough
heart shape, with two pointed leaves angled up from the top. Drawn flat in the
same uniform line weight as the rest of the illustration, as a mark etched on the
board rather than a sticker, a badge or a photograph. No text beside it.

SUPPORTING DETAIL
Two faint callout leader lines point at the two connected pins, ending in small
empty circles. Nothing else on the board is called out.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beside the USB connector at the right: "USB"
  - Along the body of the cable: "SERIAL"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the raspberry emblem, and no code,
terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the four jumper wires and the two connected pins,
and to nothing else. The board, the header and the USB connector stay navy and
slate.
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

- **A full-size Pi instead of a Zero.** The Zero is a long narrow board; a
  generator will reach for the familiar larger one with its four USB sockets. It
  does not matter enormously at card size, but a board covered in ports clutters
  the strip.
- **All forty pins connected.** Two, in the middle. If every pin sprouts a wire
  the specificity is lost.
- **"SERIAL" is the fragile string** at six characters. "USB" will be fine.
- **Text-free fallback:** drop both labels. Four wires from two pins to a USB
  plug still reads.
- **The berry turning into fruit.** It is a small etched mark in a corner, not a
  photograph of a raspberry and not a sticker. If it arrives rendered, shaded or
  oversized, regenerate — and never let it take the amber.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2015-12-28-pi-console-lead --install ~/Downloads/<your-file>.jpg
```
