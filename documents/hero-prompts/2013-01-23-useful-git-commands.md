# Useful Git Commands — hero prompt

- **Post:** `astro/src/content/blog/2013-01-23-useful-git-commands.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The post opens "more as a reminder to myself than anything" — it is a reference
list, not an argument.

So the image is a tool board: a row of distinct hand tools hung in their outlines
on a wall, each in its own silhouette, one missing from its place because it is
in use.

## The Git mark is composited, not drawn

Jason Long's mark goes in from `documents/brand/git.png` after generation,
unmodified. Sourced from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Git-logo.svg),
**CC BY 3.0, attribution required** — see `documents/brand/README.md`.

```bash
H=astro/public/images/heroes/2013-01-23-useful-git-commands-hero.jpg
magick $H \( documents/brand/git.png -resize x95 \) \
  -gravity east -geometry +120-20 -composite -quality 86 $H
```

This post previously had the diamond *drawn* by the generator. It came back well,
but a drawn trademark is still a drawn trademark, and the companion rebase post
now carries the real mark — two Git posts with different-looking Git marks is a
defect. Both use the real file.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a personal collection of commands kept as a reminder. Output a single flat image, no borders, no frame, no watermark,
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
A flat tool board drawn in three-quarter view, filling the middle of the image,
with SIX tool silhouettes painted onto it in a row.

FIVE of the silhouettes have their tool hanging in place — a spanner, pliers, a
driver, a small saw, a mallet — each sitting neatly within its own painted
outline.

The SIXTH outline is empty, and its tool lies on a small shelf beneath the board,
clearly the one currently in use.


MARGINS
The entire composition must fit within the LEFT 72% of the image width. The
rightmost 28% is empty background — nothing whatsoever extends into it: no
object, no track, no carriage, no callout line, no shadow and no marking. The
background there is the same plain ground and grid as everywhere else, with no
panel, box, border, frame or change of tone to indicate it.
Do not draw any logo, badge, emblem, roundel or icon anywhere in this image.

SUPPORTING DETAIL
One faint callout leader line points at the empty outline on the board, ending in
a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
There is NO amber accent in this image. The real Git mark composited in afterwards
is the only warm element, and nothing in the drawing may be warm — Git's orange
and the usual amber are too close in hue to coexist.
The empty painted outline is distinguished by being empty, not by colour: the
board, all six outlines and all six tools stay entirely navy and slate.

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

- **Text on the board.** No labels anywhere; a tool board reads without them.
- **A cluttered workshop.** One flat board, six outlines, one shelf.
- **Anything else coming back warm.** The Git diamond is the only orange in the
  frame. An amber tool or outline would give the card two focal points.
- **Anything intruding into the right 28%.** The real mark goes there.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2013-01-23-useful-git-commands --install ~/Downloads/<your-file>.jpg
```
