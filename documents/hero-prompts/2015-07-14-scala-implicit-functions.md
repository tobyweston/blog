# Implicit Functions in Scala — hero prompt

- **Post:** `astro/src/content/blog/2015-07-14-scala-implicit-functions.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-functional-programming.jpg`, a generic hero shared by six posts, which keep it.
- **Video:** none

## Why this image

The companion to the implicit parameters post, which it links back to. Here the
compiler does not supply a missing value — it converts something of one type into
something of another so that two things fit.

So the same visual family, one step on: an adapter appearing of its own accord
between two fittings that cannot otherwise mate. The machine and the store are
drawn as in the previous post, so the pair read as a series.

## Reference images

None. The post's only figures are code listings, which must not be drawn — see the
standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about the compiler converting one type into another so code compiles. Output a single flat image, no borders, no frame, no
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
Two separate machine bodies drawn in isometric projection, facing each other
across the middle of the image with a gap between them.

The LEFT body ends in a SQUARE connector. The RIGHT body ends in a ROUND
connector. They plainly cannot join — the mismatch must be obvious at a glance.

In the gap between them floats a single adapter: a short component that is SQUARE
at its left face and ROUND at its right face, aligned to bridge the two, with
dashed construction lines running from it to each connector.

Behind and to the LEFT, the same small open rack as in the companion image holds
two more adapters upright in slots. A dashed line curves from the rack to the
floating adapter, showing where it came from. Nothing and nobody is carrying it.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
Two faint callout leader lines point at the square face and the round face of the
adapter, ending in small empty circles.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - On the front of the rack: "implicit"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the Scala mark, and no code, braces,
semicolons, terminal output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The crimson Scala mark in the corner is the only exception to that palette. It
stays crimson, stays small, and stays clear of the amber, which is always the
larger warm shape in the image.
The amber accent belongs to the floating adapter alone, and to nothing else. Both
machine bodies, both connectors and the rack stay navy and slate.

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

- **The mismatch not being obvious.** Square against round, clearly. If both ends
  look alike there is nothing for the adapter to solve.
- **"implicit" is lowercase**, as in the companion post. Keep the rack identical
  to that image — it is what makes the two read as a pair.
- **A hand fitting the adapter.** Same as the companion post: nobody does it.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2015-07-14-scala-implicit-functions --install ~/Downloads/<your-file>.jpg
```
