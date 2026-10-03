# Implicit Parameters in Scala — hero prompt

- **Post:** `astro/src/content/blog/2015-07-03-scala-implicit-parameters.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-functional-programming.jpg`, a generic hero shared by six posts, which keep it.
- **Video:** none

## Why this image

The post's idea is that you leave a parameter off and the compiler finds a value
marked `implicit` and fills it in for you.

So the image is a machine with one empty socket, and a part arriving into it on
its own from a store off to the side — nobody is holding it. The first of a pair
with the implicit functions post, which uses the same machine and the same
store.

## Reference images

None. The post's only figures are code listings, which must not be drawn — see the
standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about the compiler supplying an argument you did not pass. Output a single flat image, no borders, no frame, no
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
A horizontal machine body drawn in isometric projection, occupying the RIGHT two
thirds of the image. Along its upper face are FOUR identical round sockets in a
row. Three of them are filled with seated plugs. The FOURTH, second from the
right, is empty and visibly open.

To the LEFT, a small open rack holds three spare plugs standing upright in
slots.

One plug is in mid-air between the rack and the empty socket, travelling along a
dashed construction line that curves from the rack to that socket, with a small
arrowhead showing its direction. Nothing and nobody is carrying it.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the empty socket, ending in a small empty
circle.

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
The amber accent belongs to the plug in mid-air and the empty socket it is
heading for, and to nothing else. The machine body, the three seated plugs and
the rack stay navy and slate.

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

- **A hand or a figure placing the plug.** The entire point is that nobody does
  it. If an arm appears, regenerate.
- **"implicit" is lowercase** and is a Scala keyword. Generators capitalise short
  strings by habit; this is the one to check. Eight characters, so also check the
  spelling.
- **All four sockets filled.** One must be visibly empty.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2015-07-03-scala-implicit-parameters --install ~/Downloads/<your-file>.jpg
```
