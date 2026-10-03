# Upgrade Raspbian — Jessie to Stretch — hero prompt

- **Post:** `astro/src/content/blog/2017-10-26-upgrade-raspian-jessie-to-stretch.md`
- **Style:** `technical-blueprint`
- **Series:** the `raspberry-pi` series — all six carry the berry, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-raspberry-pi-alt.jpg`
- **Video:** none

## Why this image

A short, practical post: `apt-get dist-upgrade` from one Raspbian release to the
next. The image is a version plate being swapped on the board — one coming off,
one going on.

This post and the Stretch-to-Buster one are explicitly a pair; that post links
back to this one. They are drawn to the same composition on purpose, and told
apart by their plates. See that post's prompt, which shows three plates rather
than two, so a reader can see where in the sequence they have landed.

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
bolts — like a machine's rating plate. TWO such plates are shown: one currently
bolted to the board, and a second floating directly above it as in an exploded
diagram, aligned to take its place, with a dashed construction line and a short
curved arrow showing the swap.

The plate on the board is the old one. The plate above it is the new one and is
drawn slightly larger and more prominently.

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
  - On the plate currently bolted to the board: "JESSIE"
  - On the plate floating above it: "STRETCH"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the raspberry emblem, and no code,
terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the upper, incoming plate and the curved arrow
showing the swap, and to nothing else. The board and the old plate stay navy and
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

- **The two plates reading as equals.** The incoming one should clearly be
  arriving: larger, amber, with the arrow. If they sit side by side like a
  comparison the sense of upgrading is lost.
- **"JESSIE" and "STRETCH" must not be swapped.** Jessie is the one on the board,
  being replaced. Getting these the wrong way round inverts the post.
- **Text-free fallback:** there isn't a useful one — the plates are blank
  rectangles without their names. Regenerate rather than ship it mute.
- **The berry turning into fruit.** It is a small etched mark in a corner, not a
  photograph of a raspberry and not a sticker. If it arrives rendered, shaded or
  oversized, regenerate — and never let it take the amber.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2017-10-26-upgrade-raspian-jessie-to-stretch --install ~/Downloads/<your-file>.jpg
```
