# Performance Monitoring Basics — hero prompt

- **Post:** `astro/src/content/blog/2009-10-31-performance-monitoring-part-1.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post argues for setting monitoring up early — response times, throughput,
resource use — rather than bolting it on when something is already wrong.

So the image is a machine with its instruments fitted as part of the build:
tapping points designed into the run, gauges mounted on proper brackets, all of
it looking original rather than added.

## Reference images

None worth attaching.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about instrumenting a system before you need the numbers. Output a single flat image, no borders, no frame, no watermark,
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
A horizontal machine run drawn in isometric projection: three connected sections
joined end to end, spanning the middle of the image.

At the junction between each pair of sections, a tapping point is built into the
pipework itself — a flanged branch that is plainly part of the casting, not
clamped on from outside.

Rising from each tapping point on a short rigid stem, a round gauge mounted on a
proper bracket. THREE gauges in all, evenly spaced, each with tick marks on its
face and no numbers.

Everything is drawn as a single designed assembly: no clamps, no straps, no
tape.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at one of the flanged tapping points where it
joins the main run, ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The small blue-and-orange Java mark is the only exception. Keep it small and
well clear of the amber element.
The amber accent belongs to the three built-in tapping points, and to nothing
else — the gauges themselves stay navy and slate, because the post is about
designing the taps in rather than about the dials.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## What is most likely to go wrong

- **Gauges clamped or strapped on.** They must look original to the machine; that
  is the argument.
- **Numbers on the dials.** Ticks only.
- **A dashboard or screen.** Physical gauges; see the standing rule.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-10-31-performance-monitoring-part-1 --install ~/Downloads/<your-file>.jpg
```
