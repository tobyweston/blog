# Play it Next — hero prompt

- **Post:** `astro/src/content/blog/2012-08-28-play-it-next.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

A small practical post about queueing a track to play next without wrecking the
playlist you are already listening to.

So the image is a queue on a rail with one item being inserted at the second
position, and everything behind it keeping its order.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about slotting one item into the front of a queue without disturbing the rest. Output a single flat image, no borders, no frame, no watermark,
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
A horizontal rail drawn in isometric projection, centred, carrying a queue of SIX
identical flat discs standing on edge in a row, evenly spaced, like records in a
rack.

A GAP has opened between the FIRST and SECOND disc, and a seventh disc is
descending into that gap along a dashed construction line with a small arrow.

All the discs behind the gap stay in their original order and spacing — nothing
else has shifted or been disturbed.

A simple pickup head sits at the front of the rail, at the first disc.

SUPPORTING DETAIL
One faint callout leader line points at the gap being filled, ending in a small
empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the descending disc and the gap it is dropping into,
and to nothing else. The rail, the pickup head and the six queued discs stay navy
and slate.

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

- **The queue being disturbed.** Everything behind the insertion keeps its place;
  that is the entire feature.
- **Insertion at the front or the back.** Second position, just after the one
  playing.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-08-28-play-it-next --install ~/Downloads/<your-file>.jpg
```
