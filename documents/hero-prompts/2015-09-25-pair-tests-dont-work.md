# Pair Testing Doesn't Work — hero prompt

- **Post:** `astro/src/content/blog/2015-09-25-pair-tests-dont-work.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

After years on both sides of pair-programming interviews the author concludes they
do not reliably tell you anything — a contrived exercise under observation is not
the work.

So the image is the gap between the two: a small staged platform with someone
performing on it while being watched, and beyond it the much larger untidy place
where the actual work happens.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about why a staged interview exercise is a poor proxy for real work. Output a single flat image, no borders, no frame, no watermark,
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
On the LEFT, a small raised platform, neat and brightly lit, with ONE stylised
faceless figure standing on it working at a tiny desk. Two further figures stand
below the platform watching, arms folded.

On the RIGHT, taking up considerably more of the image, a large untidy workspace:
several desks at different angles, stacks of paper, a long table with four
figures working together around it, none of them watching anyone.

A clear empty gap separates the two, with no path, bridge or arrow crossing it.
The platform is small and tidy; the workspace is large and busy, and the
difference in scale is the point.

SUPPORTING DETAIL
Nothing else. No scoreboard, no clipboard, no clock.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the small staged platform and the single
figure on it, and to nothing else — so the eye lands on the artificial thing
first and then finds the real work beside it.

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

- **The two halves at equal size.** The disproportion carries the argument.
- **A bridge or arrow between them.** The absence of a connection is the point.
- **The watchers reading as hostile.** They are observers, not judges.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2015-09-25-pair-tests-dont-work --install ~/Downloads/<your-file>.jpg
```
