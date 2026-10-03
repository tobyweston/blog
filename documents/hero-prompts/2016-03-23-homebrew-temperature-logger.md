# Home Brew Temperature Logger — hero prompt

- **Post:** `astro/src/content/blog/2016-03-23-homebrew-temperature-logger.mdx`
- **Style:** `technical-blueprint`
- **Series:** the `raspberry-pi` series — all six carry the berry, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/2016-03-23-homebrew-temperature-logger-hero.png`
- **Video:** none

## Why this image

A Pi Zero plus a DS18B20 probe for about a tenner, logging room temperature and
serving charts. The image is the sensor on the end of its lead reaching away from
the board — the one part of this build that touches the real world.

Note this post's current hero is a screenshot of the project's own web UI. The
standing rule against UI screenshots applies: they date badly and read as nothing
at 192px. The existing `temperature-machine.png` is still used inside the post
body via an import, so **do not delete it** after installing.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about home brew temperature logger on a Raspberry Pi. Output a single flat
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
A Raspberry Pi Zero board drawn flat in three-quarter view, occupying the LEFT
third of the image.

From its GPIO header, three wires run RIGHT in a gentle curve, ending in a small
cylindrical metal probe — a sealed stainless steel tube with a rounded tip, drawn
large enough to read clearly, suspended in open space at the right of the image.

Around the probe, three or four short curved lines radiating outwards, in the
manner of a diagram indicating something being sensed. No glow and no rays.

RECURRING MOTIF
In the lower-right corner of the board, a small raspberry emblem etched into the
silkscreen: a cluster of seven or eight rounded drupelets packed into a rough
heart shape, with two pointed leaves angled up from the top. Drawn flat in the
same uniform line weight as the rest of the illustration, as a mark etched on the
board rather than a sticker, a badge or a photograph. No text beside it.

SUPPORTING DETAIL
Below the wires, a simple flat line graph drawn small and wide: a single
horizontal axis with one gently undulating line tracing across it, no tick marks,
no numbers and no axis labels. It sits low and does not compete with the probe.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beside the probe: "DS18B20"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the raspberry emblem, and no code,
terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the probe tip and the short radiating lines around
it, and to nothing else. The board, the three wires and the small graph stay navy
and slate.
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

- **"DS18B20" is a hard string** — eight characters mixing letters and digits, and
  exactly the kind of part number a generator garbles into "DS1820" or "D518B20".
  It is also the one genuinely useful label here. Check it character by
  character; if it will not come, drop it rather than ship a wrong part number.
- **The graph taking over.** It is a supporting detail and belongs small and low.
  If it comes back as a full chart with axes, regenerate — see the standing rule
  against invented charts.
- **A glowing probe.** Short radiating lines, not light rays.
- **Text-free fallback:** drop the part number. A probe on a lead with a trace
  beneath it reads fine.
- **The berry turning into fruit.** It is a small etched mark in a corner, not a
  photograph of a raspberry and not a sticker. If it arrives rendered, shaded or
  oversized, regenerate — and never let it take the amber.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2016-03-23-homebrew-temperature-logger --install ~/Downloads/<your-file>.jpg
```
