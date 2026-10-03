# The @Deprecated Annotation — hero prompt

- **Post:** `astro/src/content/blog/2009-01-22-deprecated-annotation.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post's gripe: `@Deprecated` takes no value, so you can mark something as
obsolete but not record what replaces it.

So the image is a sign bracket with two plate positions — the upper one fitted
with a plain hatched warning plate, the lower one an empty frame with its
fixings waiting and nothing to put in them.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a warning label with nowhere to say what to use instead. Output a single flat image, no borders, no frame, no watermark,
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
A sign bracket drawn in isometric projection, centred, mounted on a post and
designed to carry TWO plates one above the other.

The UPPER position holds a plate: plain, with bold diagonal hatching across its
face and no lettering.

The LOWER position is an empty frame — the mounting rails, two bolt holes and a
pair of retaining clips, all clearly made to hold a second plate, and nothing in
them. The empty frame is as large as the plate above it.

Fixed to the post itself, the machine the sign refers to: a plain fitting with a
cap over it.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the empty lower frame, ending in a small
empty circle.

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
The amber accent belongs to the empty lower frame and its waiting fixings, and to
nothing else — the absence is the subject, not the warning above it.

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

- **Anything in the lower frame.** It stays empty. That is the complaint.
- **Lettering on the upper plate.** Diagonal hatching only.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-01-22-deprecated-annotation --install ~/Downloads/<your-file>.jpg
```
