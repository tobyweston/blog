# Getting Things Done (Part II) — hero prompt

- **Post:** `astro/src/content/blog/2012-07-22-getting-things-done-ii.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

Part two is the workflow — collecting, processing, organising, reviewing, doing.
The heart of it is that each item is handled once and routed somewhere definite.

So the image continues Part I: the same in-tray, now feeding a single processing
point that sends each shape down one of several distinct chutes. The tray and the
small shapes are drawn as in Part I, which is what ties the pair together.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about processing a pile of collected items into the right places one at a time. Output a single flat image, no borders, no frame, no watermark,
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
The same large open in-tray as in the companion image, standing on the LEFT,
still holding a pile of small mixed shapes.

A single shape is leaving the tray and passing through a processing point: a
simple angled deflector drawn just to the right of the tray, with one shape
resting against it.

From that deflector, FOUR separate chutes fan out to the RIGHT at different
angles, each ending in its own small open container. The containers are different
shapes from one another.

Shapes already sorted sit in the containers — and each container holds only one
kind of shape, so the sorting has plainly been deliberate.

SUPPORTING DETAIL
Nothing else. No arrows beyond the chutes themselves, no labels, no calendar.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the angled deflector — the point where each
item is handled — and to nothing else. The tray, the chutes, the containers and
every shape stay in the deep ink and the mid tone.

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

- **The tray looking different from Part I.** Same tray, same shapes; that is what
  makes them a pair.
- **Containers holding mixed shapes.** Each gets one kind, or the sorting means
  nothing.
- **Fewer than four destinations.**

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-07-22-getting-things-done-ii --install ~/Downloads/<your-file>.jpg
```
