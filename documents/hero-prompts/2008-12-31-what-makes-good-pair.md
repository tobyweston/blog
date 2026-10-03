# What Makes a Good Pair — hero prompt

- **Post:** `astro/src/content/blog/2008-12-31-what-makes-good-pair.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post is about communication, engagement and listening, and it illustrates
itself with cookies and milk — things that are fine apart and better together.
The rules say use the author's metaphor, so that is the image.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about what two people need from each other to work well together. Output a single flat image, no borders, no frame, no watermark,
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
A plain table seen side on across the middle of the image.

On it, close together and plainly a pair: a tall glass of milk and a small stack
of round cookies on a plate. They are drawn as two distinct objects, touching but
separate.

At each end of the table, ONE stylised faceless figure sits leaning in towards
the centre, so the two of them and the pair of objects form a single close group.
Both figures lean the same amount — neither dominates.

Nothing stands between the figures: no screen, no monitor, no partition.

SUPPORTING DETAIL
Nothing else. No room, no window, no keyboard.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the glass of milk and the stack of cookies
together, as one pair, and to nothing else. Both figures and the table stay in
the deep ink and the mid tone.

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

- **A screen between them.** The post is about the people, not the setup.
- **One figure leaning more than the other.** Equal.
- **Separating the milk and the cookies.** They touch; they are the pair.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2008-12-31-what-makes-good-pair --install ~/Downloads/<your-file>.jpg
```
