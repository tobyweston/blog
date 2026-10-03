# JUnit and Threaded Tests — hero prompt

- **Post:** `astro/src/content/blog/2008-12-17-junit-and-threaded-tests-i-recently.md`
- **Style:** `concurrency-schematic`
- **Series:** the concurrency / tempus-fugit family. Sand ground, teal accent and
  the hourglass mark set this family apart from the blueprint posts on the index
- **Written:** 2026-10-03
- **Replaces:** nothing of its own — generic or absent today
- **Video:** none

## Why this image

The runner calls `System.exit()` while the threads are still going, so the suite
reports green on work that never completed. A false positive.

So the image is a race that has been stopped early: a finish gate already closed
and showing a result, while two runners are still mid-track behind it.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a test runner that finishes before the threads it started have. Output a single flat image, no borders, no frame, no
watermark, no signature.

STYLE
Clean technical schematic in the manner of a timing diagram crossed with an
exploded isometric drawing. Crisp uniform-weight line work in a deep charcoal
ink, restrained flat fills, drawn on a warm pale sand-coloured ground carrying a
faint regular pattern of fine vertical rules, like timing gridlines. Objects in
isometric or three-quarter projection with visible construction lines and small
callout leaders ending in empty circles. Precise and deliberate, not sketchy.
Not photorealistic, not a 3D render, not a cartoon, not a glossy marketing
render, no glowing neon or holographic effects.

SUBJECT
TWO parallel horizontal tracks drawn in isometric projection, running left to
right across the middle of the image.

At the RIGHT end of both tracks stands a single finish gate — a substantial frame
with a barrier already lowered across both lanes, and a small indicator plate on
its side showing a raised flag, as though a result has been recorded.

On the tracks BEHIND that closed barrier, two carriages are still travelling,
clearly short of the gate, each with a short motion trail behind it. Neither has
arrived.

The barrier being down while both carriages are still moving is the entire
subject and must be unmistakable.

RECURRING MOTIF
On the LEFT of the image, clear of the main subject, a small hourglass: two
rounded glass bulbs meeting at a narrow waist, held in a slim frame of two end
plates joined by three slender posts. A fine stream of sand falls from the upper
bulb into a small conical heap in the lower one. Drawn flat in the same charcoal
line work as the rest, no colour fill, no text beside it.
Position it so the whole hourglass, base included, sits above the lower third of
the image. It must not touch any edge and must not sit in the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the raised indicator flag on the gate,
ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, thread dumps,
stack traces, version numbers or filenames. Nothing may be numbered or named, and
any marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Warm pale sand ground throughout, with its faint vertical timing rules a shade
deeper. Deep charcoal ink for all line work and a mid warm grey for flat fills.
One strong teal accent, reserved for the single component the post is about. No
other colour.
The hourglass mark stays in the charcoal line work and never takes the teal.
The teal accent belongs to the lowered barrier and the raised indicator flag —
the result declared too early — and to nothing else.

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

- **The ground coming back blue.** Warm sand is what separates this family from
  the blueprint posts at thumbnail size. A cool grey-blue ground means
  regenerate.
- **The hourglass mark growing, or taking the teal.** Small, left, above the
  lower third, always in the line colour.
- **A clock face.** An hourglass reads as a silhouette at 192px; a clock face is
  a grey circle.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2008-12-17-junit-and-threaded-tests-i-recently --install ~/Downloads/<your-file>.jpg
```
