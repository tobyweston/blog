# Growing Team Skills — hero prompt

- **Post:** `astro/src/content/blog/2010-07-11-growing-team-skills.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post uses a competency depth chart to make a team's skill distribution visible
— where you are strong, and where only one person knows something.

So the image is that depth made physical: a row of columns of different heights,
with the shortest one obviously the exposure. The post's own chart is attached for
its shape; this is not a redrawing of it.

## Reference image

```bash
--reference astro/src/content/images/depth-chart.png
```

Take the shape of the distribution from it and nothing else. Do not reproduce its
axes, labels or gridlines — the hero is a row of columns, not a chart.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about seeing where a team's skills are deep and where they are thin. Output a single flat image, no borders, no frame, no watermark,
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
A row of SEVEN upright columns standing side by side across the middle of the
image, each built of stacked identical blocks so its height is countable at a
glance.

The columns are of markedly different heights. Most are three or four blocks
tall. ONE near the centre is a single block high and plainly the shortest — the
gap between it and its neighbours is the most noticeable thing in the row.

A single horizontal line runs across the whole row at the height of the second
block, like a minimum level, and the short column is the only one that falls
below it.

SUPPORTING DETAIL
Nothing else. No axes, no gridlines, no scale markings — this is a row of columns,
not a chart.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the single short column and the stretch of the
horizontal line that passes above it, and to nothing else.

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

- **It turning back into a bar chart.** No axes or ticks; the post already has the
  real chart in its body.
- **More than one short column.** One gap, clearly.
- **Even heights.** The unevenness is the finding.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-07-11-growing-team-skills --install ~/Downloads/<your-file>.jpg
```
