# Automatically rebase on git pull — hero prompt

- **Post:** `astro/src/content/blog/2013-07-09-automatically-rebase-on-git-pull.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

One git config setting, and the post explains what it changes: pulls rebase rather
than merge, so history stays a single line.

So the image is two assembly lines, one of which forks and rejoins while the
other is lifted and set back down on the end of the incoming run.

## The Git mark is composited, not drawn

Jason Long's mark goes in from `documents/brand/git.png` after generation,
unmodified. Sourced from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Git-logo.svg),
**CC BY 3.0, attribution required** — see `documents/brand/README.md`.

```bash
H=astro/public/images/heroes/2013-07-09-automatically-rebase-on-git-pull-hero.jpg
magick $H \( documents/brand/git.png -resize x95 \) \
  -gravity east -geometry +120-20 -composite -quality 86 $H
```

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about replaying your work on top of incoming changes instead of merging it in. Output a single flat image, no borders, no frame, no watermark,
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
TWO horizontal tracks drawn in isometric projection, one above the other, each
carrying a row of identical blocks.

The UPPER track shows a merge: the main run of blocks continues straight, while a
short branch of two blocks leaves it, runs parallel for a while, and rejoins
further along, producing a visible loop in the line.

The LOWER track shows a rebase: the same two blocks have been lifted clear of the
line — drawn above it on dashed construction lines with a small arrow — and set
back down at the END of the main run, so the lower track is one unbroken straight
line of blocks with no branch and no loop at all.

The contrast between a line with a loop in it and a line without is the subject.

MARGINS
The entire composition must fit within the LEFT 72% of the image width. The
rightmost 28% is empty background — nothing whatsoever extends into it: no
object, no track, no carriage, no callout line, no shadow and no marking. The
background there is the same plain ground and grid as everywhere else, with no
panel, box, border, frame or change of tone to indicate it.
Do not draw any logo, badge, emblem, roundel or icon anywhere in this image.

SUPPORTING DETAIL
One faint callout leader line points at the point on the lower track where the
lifted blocks have been set back down, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the two lifted blocks on the lower track, and to
nothing else. Both tracks and all the other blocks stay navy and slate.

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

- **Both tracks looking the same.** One has a loop, one does not.
- **Branching on the lower track.** It must be perfectly straight.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2013-07-09-automatically-rebase-on-git-pull --install ~/Downloads/<your-file>.jpg
```
