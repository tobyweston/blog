# Type Safe Annotation — hero prompt

- **Post:** `astro/src/content/blog/2010-01-04-type-safe-annotation.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

Java insists an annotation's enum values be enum constants, which stops you
checking them usefully at runtime. Filed under concurrency because the author hit
it implementing Goetz's annotations, but the concurrency is the setting, not the
subject — so this stays in the blueprint family rather than the concurrency one.

The image is a label plate with a slot that takes only one profile, and the richer
fitting you actually wanted sitting beside it, unable to go in.

## Reference images

None worth attaching.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a label that will only accept one narrow kind of value. Output a single flat image, no borders, no frame, no watermark,
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
A label plate drawn in isometric projection, centred, mounted on the face of a
plain block. Set into the plate is a single narrow slot of a very specific shape —
a thin rectangular keyway.

Seated in that slot, one thin flat key, plainly the only profile that fits.

Floating beside the plate on a dashed construction line, a second, far richer
fitting: a shaped component with a toothed edge and two side lugs, aligned to the
slot but obviously unable to enter it. A short gap is left between the fitting
and the slot, and the mismatch of profiles is clear.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the narrow keyway, ending in a small empty
circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the richer fitting that cannot go in, and to nothing
else.

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

- **The rich fitting seated.** It must be held outside, not entering.
- **The two profiles looking compatible.** The mismatch is the whole post.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-01-04-type-safe-annotation --install ~/Downloads/<your-file>.jpg
```
