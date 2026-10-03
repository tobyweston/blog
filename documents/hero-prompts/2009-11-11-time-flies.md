# tempus-fugit 1.0 Released — hero prompt

- **Post:** `astro/src/content/blog/2009-11-11-time-flies.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, concurrency and tempus-fugit group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

The release announcement for the author's own library. A release post has no
mechanism of its own, so the image is the library as a thing you take off a
shelf: one sealed component, complete and ready, with its parts visible.

It opens the tempus-fugit group — the deadlock, atomicity and 1.1 posts all draw
from the same vocabulary of clocks and threads.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a library for testing concurrent and time-sensitive code. Output a single flat image, no borders, no frame, no
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
A single sealed module drawn large in isometric projection, centred, resting on a
plain plinth. Its casing is cut away on one side to show the interior: a simple
clock escapement — a toothed wheel and a pivoting anchor — meshed with TWO
parallel shafts running the length of the module.

The casing is clean and unmarked apart from a single raised band around its
middle.

To one side, slightly behind, two further identical modules stand closed and
stacked, suggesting more of the same ready to use.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Java mark: a
plain cup seen from the side, drawn in a mid steel blue, with two curling wisps
of steam rising from it in a warm orange-red. Flat shapes, no outline, no saucer,
no circle or roundel around it and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the escapement wheel, ending in a small
empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames, and no text beside the Java mark. Any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark in the corner is the only exception. Keep it
small and well clear of the amber element — its orange steam is close in hue to
the accent, so the two must never sit near each other or at similar sizes.
The amber accent belongs to the escapement wheel and its anchor, and to nothing
else.

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

- **A literal clock face.** An escapement is a mechanism; a clock face at 192px
  is a grey circle.
- **Version numbers appearing.** No text in this image at all.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-11-11-time-flies --install ~/Downloads/<your-file>.jpg
```
