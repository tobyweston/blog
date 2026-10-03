# Building Better Exceptions — hero prompt

- **Post:** `astro/src/content/blog/2012-03-29-building-better-exceptions.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, exceptions group — all carry the Java cup in its
  series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-exception-handling.jpg`, a generic shared hero, which other posts keep.
- **Video:** none

## Why this image

The follow-up to the boundaries post. Its argument is that an exception should be
a proper object with behaviour — "tell don't ask" — rather than a bag you
interrogate from outside.

So the image compares two carriers: a flat inert tag that tells you nothing until
you examine it, and beside it a solid component with its own working fittings.
The second is the one the post wants.

## Reference images

None. These posts illustrate themselves with code listings, which must not be
drawn — see the standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about designing exceptions as real objects with behaviour rather than empty carriers. Output a single flat image, no borders, no frame, no
watermark, no signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
Two objects side by side on a plain surface, drawn in isometric projection, both
the same overall size so the comparison is about what they are rather than how
big.

On the LEFT, a flat blank tag or luggage label lying face-up, with a small hole
at one end and a plain unmarked face. It has no moving parts and nothing on it.

On the RIGHT, a solid rectangular component with real fittings built into it: a
small lever on its upper face, a round port on its near side, and two bolt heads.
It plainly does something on its own.

A short dashed construction line runs between them at the midpoint, with a small
arrowhead pointing from the flat tag towards the component, showing the direction
of travel.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Java mark: a
plain cup seen from the side, drawn in a mid steel blue, with two curling wisps
of steam rising from it in a warm orange-red. Flat shapes, no outline, no saucer,
no circle or roundel around it and no text beside it.

SUPPORTING DETAIL
Two faint callout leader lines point at the lever and at the port on the
right-hand component, ending in small empty circles. Nothing is called out on the
flat tag — there is nothing to call out.

TEXT IN THE IMAGE
  - No text labels anywhere in this image.
No code, braces, semicolons, terminal output or filenames anywhere in the image,
and no text beside the Java mark. Any marking that would read as writing must be
left out rather than rendered as placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark in the corner is the only exception. Keep it
small and well clear of the amber element — its orange steam is close in hue to
the accent, so the two must never sit near each other or at similar sizes.
The amber accent belongs to the lever and the port on the right-hand component —
its working parts — and to nothing else. Both bodies, the flat tag and the arrow
stay navy and slate.

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

- **The two objects reading as unrelated.** They are the same thing done badly
  and well. Same size, same surface, same projection.
- **The flat tag gaining detail.** Its blankness is half the argument.
- **A tick and a cross appearing.** No judgement symbols; the fittings make the
  point.
- **The Java mark growing, or its orange drifting towards the amber.** It is
  small, in the lower-left corner, and well away from the accent. Of all three
  series marks this is the one most likely to muddy a card, because its steam is
  close in hue to the accent.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-03-29-building-better-exceptions --install ~/Downloads/<your-file>.jpg
```
