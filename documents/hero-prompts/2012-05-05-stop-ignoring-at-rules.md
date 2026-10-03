# Stop Ignoring @Rules — hero prompt

- **Post:** `astro/src/content/blog/2012-05-05-stop-ignoring-at-rules.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The post's danger is specific and nasty: an older JMock runner silently ignores
your `@Rules`, so tests report green when the check never ran. False positives.

So the image is an inspection rig where the checking arm is mounted but its
linkage is missing — the gauge reads pass because nothing is driving it. The
disconnection is small, deliberate and easy to miss, which is the point.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a safety check that is fitted but not connected, so everything appears to pass. Output a single flat image, no borders, no frame, no watermark,
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
An inspection rig drawn in isometric projection, centred: a frame over a belt
carrying three identical parts left to right.

Mounted on the frame above the belt, a checking arm with a probe at its lower
end. The arm is properly bolted to the frame and looks entirely correct.

But the short linkage between the arm and the drive shaft above it is ABSENT:
there is a clear gap with a mounting pin exposed at each end and nothing joining
them. The probe hangs clear of the parts below and touches nothing.

At the end of the belt, a simple round gauge with its needle resting firmly at
one end of its travel, as though everything has passed.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the gap where the linkage should be,
ending in a small empty circle. The gauge face carries tick marks but no numbers.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the gap in the linkage and the two exposed mounting
pins either side of it, and to nothing else. The rig, the arm, the probe, the
belt, the parts and the gauge stay navy and slate.

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

- **The gap being obvious at a glance.** It should be small and easy to overlook —
  that is why the bug bites — but the amber must still find it.
- **The probe touching a part.** It hangs clear; nothing is being checked.
- **The gauge showing a failure.** It reads pass. That is the danger.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-05-05-stop-ignoring-at-rules --install ~/Downloads/<your-file>.jpg
```
