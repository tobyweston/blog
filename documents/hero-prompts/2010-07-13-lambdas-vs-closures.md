# Lambdas vs. Closures — hero prompt

- **Post:** `astro/src/content/blog/2010-07-13-lambdas-vs-closures.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post separates two things that get conflated: a lambda is an anonymous
function; a closure is one that closes over state from the scope around it.

So the image puts two otherwise identical units side by side — one sealed and
self-contained, one with a tube reaching out and drawing something in from
beyond its own body. The Greek lambda is cut into both, as the author asked, so
the comparison is plainly between two of the same kind of thing.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about the difference between an anonymous function and one that captures its surroundings. Output a single flat image, no borders, no frame, no watermark,
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
TWO identical rectangular units drawn in isometric projection, side by side and
exactly the same size, each standing on the same plain base.

The LEFT unit is completely sealed: a smooth closed body with one inlet at the
front and one outlet at the back, and nothing else attached to it.

The RIGHT unit is the same body with one addition: a flexible tube leaves its
side, reaches out beyond the unit's own footprint, and ends in a small cup that
is drawing from a separate reservoir standing apart on the base. The unit cannot
work without what the tube brings in.

Cut cleanly into the front face of EACH unit, as an engraved recess rather than
a printed mark, the Greek letter lambda — the capital Λ form, a simple two-stroke
inverted V. It appears once on each unit, the same size on both, and is the only
lettering in the image.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the small cup where the tube draws from
the separate reservoir, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image, apart from the two engraved lambdas described above. No code, braces, semicolons,
terminal output, version numbers, brand names or filenames. Nothing may be
numbered or named, and any marking that would read as writing must be left out
rather than rendered as placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the flexible tube, its cup and the separate reservoir
it draws from — everything the right-hand unit reaches outside itself for — and
to nothing else. Both unit bodies, both engraved lambdas and the base stay navy
and slate.

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
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-07-13-lambdas-vs-closures --install ~/Downloads/<your-file>.jpg
```
