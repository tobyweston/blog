# Upgrade Raspbian — Stretch to Buster — hero prompt

- **Post:** `astro/src/content/blog/2019-08-29-upgrade-raspian-stretch-to-buster.md`
- **Style:** `technical-blueprint`
- **Series:** the `raspberry-pi` series — all six carry the berry, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-raspberry-pi.jpg`
- **Video:** none

## Why this image

The same operation as the Jessie-to-Stretch post, two years later, and the post
says so and links back to it.

Two nearly identical cards sitting on the blog index would be a defect, so this
one deliberately shows THREE plates rather than two: the sequence so far, with
the newest arriving. A reader can tell at a glance which upgrade they are looking
at, and the pair still read as a set.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about upgrade raspbian on a Raspberry Pi. Output a single flat
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
A Raspberry Pi board drawn flat in three-quarter view, occupying the lower
two-thirds of the image.

Mounted on the face of the board, a rectangular name plate held by four small
bolts — like a machine's rating plate. THREE such plates are shown in a rising
diagonal line from lower-left to upper-right, as in an exploded diagram, each
aligned to the same bolt holes on the board, with dashed construction lines
linking them.

The LOWEST plate is drawn faded and thin, clearly already superseded. The MIDDLE
plate is the one currently bolted to the board, drawn normally. The HIGHEST plate
is the newest, drawn largest and most prominently, with a short curved arrow
showing it coming in to replace the middle one.

RECURRING MOTIF
In the lower-right corner of the board, a small raspberry emblem etched into the
silkscreen: a cluster of seven or eight rounded drupelets packed into a rough
heart shape, with two pointed leaves angled up from the top. Drawn flat in the
same uniform line weight as the rest of the illustration, as a mark etched on the
board rather than a sticker, a badge or a photograph. No text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the bolt holes on the board, ending in a
small empty circle.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - On the lowest, faded plate: "JESSIE"
  - On the middle plate: "STRETCH"
  - On the highest, incoming plate: "BUSTER"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the raspberry emblem, and no code,
terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the highest, incoming plate and the curved arrow
showing it arriving, and to nothing else. The board and the two older plates stay
navy and slate, the lowest one faded almost to the background.
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

- **The rising diagonal escaping the central band.** Three stacked plates climbing
  to the right is exactly the composition the card crop punishes. Keep the rise
  shallow, and check the card render before accepting.
- **Three strings is the budget, and all three are version names.** Check all of
  them, and check the order: JESSIE faded at the bottom, BUSTER arriving at the
  top.
- **Both upgrade posts coming out identical.** If this one ends up showing two
  plates, it is indistinguishable from the Jessie post on the index. Regenerate.
- **Text-free fallback:** none — see the companion post.
- **The berry turning into fruit.** It is a small etched mark in a corner, not a
  photograph of a raspberry and not a sticker. If it arrives rendered, shaded or
  oversized, regenerate — and never let it take the amber.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2019-08-29-upgrade-raspian-stretch-to-buster --install ~/Downloads/<your-file>.jpg
```
