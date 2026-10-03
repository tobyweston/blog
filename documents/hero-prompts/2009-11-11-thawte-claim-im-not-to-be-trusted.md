# Thawte Discontinue Free Certificates — hero prompt

- **Post:** `astro/src/content/blog/2009-11-11-thawte-claim-im-not-to-be-trusted.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

Thawte withdrew free personal certificates and the web of trust, which the author
had been using to sign JARs for WebStart.

So the image is the moment the authority goes away: a sealed artifact and the
press that validated it, with the press's die now removed and its mount empty.

## Reference images

None worth attaching.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a free certificate service being withdrawn and leaving signed work unverifiable. Output a single flat image, no borders, no frame, no watermark,
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
A sealing press drawn in isometric projection on the RIGHT: a heavy frame with a
descending arm, and a mount at the arm's foot where a die should sit.

That mount is EMPTY. The die has been removed and lies to one side, detached, with
a dashed construction line showing it has been lifted away rather than being on
its way in — the line runs outward, with a small arrowhead pointing away from the
press.

On the bed beneath the press sits one flat package already carrying a pressed
seal, finished before the die was taken. Behind it, a short queue of THREE further
packages waits, none of them sealed.

The three waiting packages cannot be sealed, and nothing in the image is going to
seal them.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the empty mount, ending in a small empty
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
The amber accent belongs to the empty mount and the detached die lying beside it,
and to nothing else.

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

- **The die on its way in.** The arrow points away; it is being removed.
- **The waiting packages being sealed.** They are blank and stay blank.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-11-11-thawte-claim-im-not-to-be-trusted --install ~/Downloads/<your-file>.jpg
```
