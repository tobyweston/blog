# Pairing Honestly — hero prompt

- **Post:** `astro/src/content/blog/2010-08-15-pairing-honestly.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

A retrospective where the team were honest that, despite all having "done
pairing", they had each done wildly different amounts of it.

So the image is the admission made visible: a row of figures each standing on a
block of a different height, all facing one another, none hidden. The unevenness
is the honesty, not the failure.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a team admitting openly how differently each of them has paired. Output a single flat image, no borders, no frame, no watermark,
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
FIVE stylised faceless figures standing in a row across the middle of the image,
each on their own solid rectangular block.

The five blocks are all different heights, and markedly so — one very tall, one
very low, three at varying heights between. The figures stand level on top of
their own blocks, so their heads sit at five different levels.

All five are turned to face inward towards one another, and none is turned away
or hidden behind another. A single continuous line runs along the row connecting
all five at chest height, like a shared rail they are all holding.

SUPPORTING DETAIL
Nothing else. No room, no chart, no podium.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons,
terminal output, version numbers, brand names or filenames. Nothing may be
numbered or named, and any marking that would read as writing must be left out
rather than rendered as placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the single continuous line connecting all five
figures, and to nothing else. All five figures and all five blocks stay in the
deep ink and the mid tone.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-08-15-pairing-honestly --install ~/Downloads/<your-file>.jpg
```
