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

BRAND MARK
On the RIGHT of the image, clear of the main subject and above the lower third, a
Git mark: a diamond standing on one point, drawn in a strong orange-red, with a
simple branch diagram inside it — a straight line running through the diamond
with a small filled node at each end, and a short branch curving up from the
middle of that line to a third node. Flat shapes, no outline around the diamond,
no text beside it.
The whole mark, including the lowest point of the diamond, must sit above the
lower third of the image and must not touch any edge.

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
There is NO amber accent in this image. The orange-red Git mark is the only warm
element anywhere, and nothing else may be warm — Git's orange and the usual amber
are too close in hue to coexist.
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
- **The diamond rendered as a square.** It stands on one point.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2013-01-23-useful-git-commands --install ~/Downloads/<your-file>.jpg
```
