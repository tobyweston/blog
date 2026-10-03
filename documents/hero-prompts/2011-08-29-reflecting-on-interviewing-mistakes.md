# Reflecting on Interviewing Mistakes — hero prompt

- **Post:** `astro/src/content/blog/2011-08-29-reflecting-on-interviewing-mistakes.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post looks hard at techniques the author helped champion — pair tests among
them — and concludes that even progressive interviewing fools itself.

So the image is a careful measurement being taken of the wrong thing: an
elaborate apparatus trained precisely on a shape, while the shape it is supposed
to be measuring stands just outside its reach.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about how a hiring process can look rigorous while measuring the wrong thing. Output a single flat image, no borders, no frame, no watermark,
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
A stylised faceless figure on the RIGHT, standing upright and clearly the
subject of attention.

On the LEFT, an elaborate measuring apparatus on a tripod — calipers, a sighting
arm, a graduated scale — aimed with evident precision. But it is trained on a
plain flat cut-out silhouette of a person standing just in front of the real
figure: a board, propped up, obviously not the person.

The real figure stands behind and slightly to one side of the cut-out, unmeasured
and unattended.

The apparatus is detailed and careful; what it is pointed at is not the person.

SUPPORTING DETAIL
Nothing else. No room, no desk, no clipboard.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons,
terminal output, version numbers, brand names or filenames. Nothing may be
numbered or named, and any marking that would read as writing must be left out
rather than rendered as placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the flat cut-out silhouette being measured,
and to nothing else. The apparatus and the real figure stay in the deep ink and
the mid tone.

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
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2011-08-29-reflecting-on-interviewing-mistakes --install ~/Downloads/<your-file>.jpg
```
