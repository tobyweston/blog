# Daily Standups Don't Work — hero prompt

- **Post:** `astro/src/content/blog/2012-09-15-daily-standups-dont-work.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The post's complaint is that standups drift from collaboration into reporting —
people take turns addressing one listener rather than talking to each other.

So the image is a circle that has stopped being a circle: figures still standing
in a ring, but every one of them turned to face the same single point.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a daily meeting that has decayed into a status report. Output a single flat image, no borders, no frame, no watermark,
no signature.

STYLE
Flat editorial illustration in a mid-century printed style, as though screen
printed in a small number of inks. Bold simplified geometric shapes, strong
silhouettes, minimal interior detail, no outlines or only occasional rough ones.
Visible paper grain and light halftone or misregistration texture. Figures
stylised and faceless or near-faceless. Confident and graphic. Not
photorealistic, not a 3D render, not a cartoon with thick outlines, not flat
corporate vector art with gradient blobs.

SUBJECT
A ring of SIX stylised faceless figures standing in a circle, drawn from slightly
above, occupying the middle of the image.

Every one of them is turned to face the SAME single figure standing at one side
of the ring, who holds a flat board. None of the six is facing any of the others.

Thin lines run from each of the six to that one figure, all converging on it —
and there are no lines at all between any of the six themselves. The ring shape
survives; the connections that would make it a circle do not.

SUPPORTING DETAIL
Nothing else. No table, no room, no clock on a wall.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the converging lines and the board held by the
listening figure, and to nothing else. All seven figures stay in the deep ink and
the mid tone.

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

- **Lines between the ring members.** There must be none; their absence is the
  whole diagnosis.
- **A conference table.** They are standing, and furniture clutters the ring.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-09-15-daily-standups-dont-work --install ~/Downloads/<your-file>.jpg
```
