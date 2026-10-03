# Convert a Callable to a Runnable — hero prompt

- **Post:** `astro/src/content/blog/2009-05-29-convert-callable-to-runnable.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, concurrency and tempus-fugit group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

`Executors` will turn a `Runnable` into a `Callable` but offers nothing going the
other way, so the post writes the missing adapter.

The image is that asymmetry: a conversion bench with a working path in one
direction and a blocked one coming back, and a hand-made part filling the gap.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about adapting one task interface into another the standard library will not. Output a single flat image, no borders, no frame, no
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
A low bench drawn in isometric projection, centred, with a fitting mounted at each
end: a SQUARE socket on the LEFT and a ROUND socket on the RIGHT.

Between them, TWO parallel guide rails. Along the UPPER rail an adapter sits
seated and complete, carrying a part from left to right. The LOWER rail, running
right to left, has an obvious empty gap in the middle of it, with the rail ends
unfinished on either side.

Bridging that gap, a single adapter drawn slightly differently from the upper
one — visibly made rather than supplied, with exposed bolts and a plainer finish
— lowering into place along a dashed construction line.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth. Treat the lower fifth of the frame as unusable: a mark placed
there loses its cup to the card crop and survives only as a stray orange squiggle.

SUPPORTING DETAIL
One faint callout leader line points at the gap in the lower rail, ending in a
small empty circle.

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
The amber accent belongs to the hand-made adapter dropping into the lower rail,
and to nothing else.

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

- **Both rails looking equally equipped.** The asymmetry is the post.
- **The two adapters looking identical.** One is supplied, one is made.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-05-29-convert-callable-to-runnable --install ~/Downloads/<your-file>.jpg
```
