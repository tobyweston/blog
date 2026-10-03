# Wrapping Exceptions is Dull — hero prompt

- **Post:** `astro/src/content/blog/2010-04-25-wrapping-exceptions-is-dull.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, exceptions group — all carry the Java cup in its
  series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` at all today.
- **Video:** none

## Why this image

The post opens "I'm totally bored of wrapping exceptions in Java" and shows the
same verbose try/catch written again and again. The fix is a helper that does the
wrapping for you.

So the image is a wrapping machine: identical parts going in one end, identical
sleeved parts coming out the other, and a tall stack of the sleeves beside it.
The repetition is the subject, and the machine is the relief.

## Reference images

None. These posts illustrate themselves with code listings, which must not be
drawn — see the standing rule against code walls.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about removing the boilerplate of wrapping and rethrowing checked exceptions. Output a single flat image, no borders, no frame, no
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
A compact wrapping machine drawn in isometric projection, centred in the image: a
rectangular body with an open infeed on the LEFT and an open outfeed on the
RIGHT, with a simple roller visible inside.

Approaching the infeed in a line, THREE identical bare cylinders, evenly spaced.

Leaving the outfeed in a line, THREE identical cylinders of the same size, each
now enclosed in a close-fitting sleeve with a visible seam. They are otherwise
unchanged.

Beside the machine, a tall neat stack of flat unused sleeves waiting to be used,
drawn as a simple column of identical thin rectangles.

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
One faint callout leader line points at the roller inside the machine, ending in a
small empty circle.

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
The amber accent belongs to the three sleeves on the cylinders leaving the
machine, and to nothing else. The machine body, the bare cylinders and the stack
of unused sleeves stay navy and slate.

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

- **The input and output differing in anything but the sleeve.** The cylinders are
  unchanged; only the wrapping is added. That is the complaint.
- **A production line sprawling across the frame.** One machine, three in, three
  out.
- **The stack of sleeves dominating.** It is context for how dull this is, not
  the subject.
- **The Java mark growing, or its orange drifting towards the amber.** It is
  small, in the lower-left corner, and well away from the accent. Of all three
  series marks this is the one most likely to muddy a card, because its steam is
  close in hue to the accent.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-04-25-wrapping-exceptions-is-dull --install ~/Downloads/<your-file>.jpg
```
