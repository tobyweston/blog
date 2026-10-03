# Objectives — hero prompt

- **Post:** `astro/src/content/blog/2010-06-17-objectives.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post's argument is that a good objective sits where what is good for you and
what is good for the company actually overlap — SMART plus a Y for *you*.

So the image is two circles overlapping, with the one thing worth having sitting
in the overlap and nowhere else.

## Reference images

None worth attaching.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about setting goals that serve you as well as the organisation. Output a single flat image, no borders, no frame, no watermark,
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
TWO large overlapping circles drawn flat, side by side across the middle of the
image, their overlap a clear lens shape in the centre. Where the two inks cross,
the colours multiply, as the printed style does.

Inside the LEFT circle, away from the overlap, a scatter of small plain shapes.
Inside the RIGHT circle, away from the overlap, another scatter of different
small shapes.

In the overlap itself, ONE larger solid shape sits alone — bigger than anything
in either circle, and clearly the only thing in that space.

A single stylised faceless figure stands beside the overlap, reaching in to take
the shape from it.

SUPPORTING DETAIL
Nothing else. No labels, no arrows, no ticks.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the single shape in the overlap, and to nothing
else. Both circles, both scatters and the figure stay in the deep ink and the mid
tone.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## What is most likely to go wrong

- **Letters in the circles.** No lettering anywhere; this is not a labelled Venn
  diagram.
- **Several shapes in the overlap.** One.
- **The circles not actually overlapping.** The lens is the subject.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-06-17-objectives --install ~/Downloads/<your-file>.jpg
```
