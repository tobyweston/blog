# Getting Things Done (Part I) — hero prompt

- **Post:** `astro/src/content/blog/2012-07-20-getting-things-done-i.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

Part one introduces the core GTD move: get it all out of your head and into a
system you trust, so you stop holding it.

So the image is exactly that transfer — a figure with a dense cloud of small
shapes above their head, streaming down into a single large in-tray. Part II
picks up the same tray and the same small shapes, so the pair read as a set.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about emptying everything you are carrying in your head into one trusted place. Output a single flat image, no borders, no frame, no watermark,
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
A single stylised faceless figure standing on the LEFT of the image, seen in
profile.

Above and around their head, a dense irregular cluster of perhaps twenty small
shapes — squares, triangles, circles, all different sizes, jumbled and
overlapping, clearly a burden being carried.

From that cluster, a broad stream of the same small shapes curves down and to the
RIGHT, landing in a single large open in-tray standing on a plain surface. The
tray is substantial and obviously built for the purpose.

The cluster above the head is visibly thinning where the stream leaves it.

SUPPORTING DETAIL
Nothing else. No desk, no office, no computer, no lists.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the in-tray alone, and to nothing else. The
figure and every one of the small shapes stay in the deep ink and the mid tone.

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

- **The tray being small or incidental.** It is the destination and the accent; it
  should look able to hold everything.
- **A tidy cluster.** The jumble above the head is the problem being solved.
- **Any text, list or label.**

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-07-20-getting-things-done-i --install ~/Downloads/<your-file>.jpg
```
