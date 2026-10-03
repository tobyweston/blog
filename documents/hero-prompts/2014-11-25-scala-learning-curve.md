# Scala Learning Curve — hero prompt

- **Post:** `astro/src/content/blog/2014-11-25-scala-learning-curve.md`
- **Style:** `technical-blueprint`
- **Series:** the `scala` posts — all carry the crimson Scala mark, see the
  Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-functional-programming.jpg`, a generic hero shared by six posts, which keep it.
- **Video:** none

## Why this image

The post is built around one chart of its own: a quick early ramp, then a long
slower climb into the harder functional features, with milestones along the way.

The hero is that curve made physical — a ramp you walk up, steep at first then
flattening into a long haul. Attach the post's chart so the shape of the hero
matches the shape of the curve the post actually plots.

## Reference images

Attach the post's own chart, which is the thing the hero is a physical version of:

```bash
.claude/skills/hero-image/scripts/generate_hero.py 2014-11-25-scala-learning-curve \
  --reference astro/src/content/images/learning_curve.png
```

Take the *shape of the curve* from it — where it rises steeply and where it
flattens — and nothing else. Do not reproduce its axes, its labels or its
gridlines; the hero is a ramp, not a chart.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about what learning the language actually feels like over time. Output a single flat image, no borders, no frame, no
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
A single continuous ramp or incline drawn in three-quarter view, running from the
lower LEFT to the upper RIGHT across the middle of the image.

Its profile is specific and is the whole subject: it rises STEEPLY for the first
third, then bends and continues as a much shallower, much longer climb for the
remaining two thirds. The bend between the two is clearly visible.

THREE small flag markers are planted along the ramp: one near the top of the
steep section, and two spaced widely apart along the long shallow section, so the
spacing itself shows the slowing down.

A single small stylised figure, drawn simply and without features, is walking up
the shallow section between the second and third flags.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.

SUPPORTING DETAIL
Thin horizontal construction lines run from each flag to the left edge, ending
without labels. No axis, no numbers, no gridlines — this is a ramp, not a chart.

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
The amber accent belongs to the bend where the steep section meets the shallow
one — the short stretch of ramp either side of it — and to nothing else. The
rest of the ramp, the flags and the figure stay navy and slate.

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

- **It turning back into a chart.** Axes, ticks and gridlines are exactly what the
  standing rule forbids, and the post already has the real chart in its body. If
  axes appear, regenerate.
- **A smooth curve.** The bend is the finding. An even arc says nothing.
- **Evenly spaced flags.** The widening gaps are the point.
- **The Scala mark growing or turning navy.** It is small, crimson, in the
  lower-left corner, and it never competes with the amber. A large red emblem
  will take over the card; a navy one reads as a mistake.
- **The mark landing in the bottom fifth**, which the card crop removes. Lower
  left means low, not at the very edge — keep it inside the central band.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2014-11-25-scala-learning-curve --install ~/Downloads/<your-file>.jpg
```
