# Type Classes in Scala — hero prompt

- **Post:** `astro/src/content/blog/2016-08-13-type-classes.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-functional-programming.jpg`, a generic hero shared by six posts, which keep it.
- **Video:** none

## Why this image

Type classes give several unrelated types the same capability without any of them
extending a shared parent — "ad-hoc polymorphism".

So the image is three objects of genuinely different shapes, each wearing its own
clip-on collar, and all three collars presenting the same fitting. The absence of
anything above them is as important as the collars: no parent, no tree.

## Reference images

None. The post's only figures are code listings, which must not be drawn — see the
standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about giving unrelated types common behaviour without inheritance. Output a single flat image, no borders, no frame, no
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
THREE objects of clearly different shapes standing in a row across the middle of
the image, drawn in isometric projection: a cube, a cylinder and a hexagonal
prism. They are plainly unrelated to one another.

Each one wears a collar clipped around its upper part. The three collars are
shaped differently from each other below, where each grips its own object, but
every one of them presents an IDENTICAL round fitting on top — the same size, the
same shape, at the same height across all three.

A single long horizontal bar hovers above the row, with three identical round
sockets along its underside, aligned to drop onto the three fittings. Dashed
construction lines run from each socket to the fitting below it.

The space above the bar is empty. There is no parent box, no tree, no arrows
pointing upward.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at one of the collars where it grips its
object, ending in a small empty circle.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - No text labels anywhere in this image.
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
The amber accent belongs to the three collars and their identical round fittings,
and to nothing else. The cube, the cylinder, the prism and the bar above stay
navy and slate.

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

- **The three fittings not matching.** They must be identical — that is the whole
  idea. Different collars, same interface.
- **An inheritance tree.** Nothing above the bar. If a parent box appears with
  arrows down to the three objects, the image says the opposite of the post.
- **The three objects looking like a family.** They should be obviously unrelated
  shapes, not three sizes of the same thing.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2016-08-13-type-classes --install ~/Downloads/<your-file>.jpg
```
