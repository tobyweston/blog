# HTTP Encoding Schemes — hero prompt

- **Post:** `astro/src/content/blog/2012-06-11-http-encoding-schemes.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

URL encoding and form encoding are not the same thing, and the post exists because
people treat them as interchangeable.

So the image takes the slip from the companion HTTP post and runs it through two
different stencil plates, producing two visibly different results from the same
input. Same source, two schemes, two outputs.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about two different ways of escaping the same characters for the web. Output a single flat image, no borders, no frame, no watermark,
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
One small flat slip — the same slip as in the companion HTTP image — mounted at
the LEFT of the frame on a feed arm, with a row of plain identical marks on its
face.

From it, the feed splits into TWO parallel paths running to the RIGHT. Each path
passes through its own stencil plate, and the two plates have visibly different
cut patterns: one cut with narrow slots, the other with wide square apertures.

Beyond each plate, the resulting slip. The upper one now carries a dense run of
narrow marks; the lower carries fewer, wider, differently spaced marks. The two
results must be obviously unalike.

The two paths never cross and never rejoin.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
Two faint callout leader lines, one to each stencil plate, ending in small empty
circles.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the two stencil plates, and to nothing else. The
source slip, both feed paths and both resulting slips stay navy and slate.

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

- **The two results looking alike.** Their difference is the entire post.
- **The paths rejoining.** They are alternatives, not stages.
- **Real characters or text on the slips.** Abstract marks only.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-06-11-http-encoding-schemes --install ~/Downloads/<your-file>.jpg
```
