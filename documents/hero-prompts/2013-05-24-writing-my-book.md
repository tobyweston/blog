# Writing my Book — hero prompt

- **Post:** `astro/src/content/blog/2013-05-24-writing-my-book.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

A personal post about writing "Effective Acceptance Testing" on Leanpub —
published incrementally while still being written, which is the interesting part.

So the image is a book being assembled in public: finished signatures already
bound, the next one still on the bench, and readers already holding copies of
what exists so far.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about self-publishing a technical book in the open, a chapter at a time. Output a single flat image, no borders, no frame, no watermark,
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
A workbench drawn in three-quarter view across the middle of the image.

On the bench, a part-bound book: a block of stitched pages already bound into
covers on the LEFT, with THREE further loose gatherings of pages laid out beside
it to the RIGHT, waiting to be added. The binding thread is still attached.

Standing in front of and below the bench, THREE stylised faceless figures, each
already holding an open copy of the same part-bound book, reading it.

The book being incomplete and already in people's hands at the same time is the
point.

SUPPORTING DETAIL
Nothing else. No shop, no shelves, no e-reader.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the three loose gatherings still waiting to be
bound, and to nothing else. The bound block, the bench and all three figures stay
in the deep ink and the mid tone.

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

- **A finished book.** Its incompleteness is the subject.
- **The readers waiting empty-handed.** They already have it; that is the
  Leanpub idea.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2013-05-24-writing-my-book --install ~/Downloads/<your-file>.jpg
```
