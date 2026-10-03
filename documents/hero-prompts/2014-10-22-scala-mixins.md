# Scala Mixins: The Right Way — hero prompt

- **Post:** `astro/src/content/blog/2014-10-22-scala-mixins.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-functional-programming.jpg`, a generic hero shared by six posts, which keep it.
- **Video:** none

## Why this image

The post's tension is that a Scala trait can be used two ways — for polymorphism,
which is inheritance, and for mixing in behaviour, which is reuse — and that
conflating them causes trouble.

The image takes the second, which is the one the post argues for: sleeves sliding
onto a shaft. Each adds something; none of them is the shaft's parent. Stacking
is visibly not the same operation as descending from something.

## Reference images

None. The post's only figures are code listings, which must not be drawn — see the
standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about layering reusable behaviour onto a class without inheriting from it. Output a single flat image, no borders, no frame, no
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
A single vertical shaft or spindle drawn in isometric projection, standing on a
small base, centred in the image.

THREE open rings or sleeves float above and around it, as in an exploded diagram,
each aligned to slide down onto the shaft, each at a different height, with
dashed construction lines showing their path down. The sleeves are different
thicknesses and each carries a different simple surface pattern — one ribbed, one
notched, one plain — so they are clearly distinct parts doing different jobs.

One sleeve is already seated on the shaft near its base.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the seated sleeve, ending in a small empty
circle. No tree diagram, no arrows pointing upward to a parent, nothing
suggesting a hierarchy.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beside the shaft: "WITH"
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
The amber accent belongs to the three floating sleeves, and to nothing else. The
shaft, its base and the seated sleeve stay navy and slate.

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

- **An inheritance tree creeping in.** Boxes joined by arrows to a parent is the
  thing this post warns against. Sleeves on a shaft, nothing above them.
- **"WITH" is a safe string** — it is the Scala keyword for mixing in — but it
  must not become "WITH:" or be repeated on each sleeve.
- **Identical sleeves.** They do different jobs; they should look different.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2014-10-22-scala-mixins --install ~/Downloads/<your-file>.jpg
```
