# Running JUnit Tests in Parallel — hero prompt

- **Post:** `astro/src/content/blog/2009-12-29-running-junit-tests-in-parallel.md`
- **Style:** `concurrency-schematic`
- **Series:** the concurrency / tempus-fugit family. Sand ground, teal accent and
  the hourglass mark set this family apart from the blueprint posts on the index
- **Written:** 2026-10-03
- **Replaces:** nothing of its own — generic or absent today
- **Video:** none

## Why this image

A runner that puts each test in its own thread, so a suite finishes in a fraction
of the time.

So the image is the two arrangements compared by length: one long single file,
and the same parts spread across several lanes covering a fraction of the
distance. This is where the family's braid motif belongs, as the feed splitting
into lanes.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about running a suite of tests at the same time instead of one after another. Output a single flat image, no borders, no frame, no
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
TWO arrangements stacked one above the other, drawn in isometric projection,
sharing a common start line at the LEFT.

The UPPER arrangement is a single lane with TWELVE identical small parts in one
long queue, stretching all the way to the right edge of the composition.

The LOWER arrangement takes the same twelve parts and spreads them across FOUR
parallel lanes, three to a lane. It reaches only about a quarter as far to the
right, and its right-hand end is clearly marked by a short vertical rule.

At the start line, the single feed divides into the four lanes as a two-strand
braid, the strands crossing over and under each other before fanning out.

RECURRING MOTIF
On the LEFT of the image, clear of the main subject, a small hourglass: two
rounded glass bulbs meeting at a narrow waist, held in a slim frame of two end
plates joined by three slender posts. A fine stream of sand falls from the upper
bulb into a small conical heap in the lower one. Drawn flat in the same charcoal
line work as the rest, no colour fill, no text beside it.
Position it so the whole hourglass, base included, sits above the lower third of
the image. It must not touch any edge and must not sit in the bottom fifth.

SUPPORTING DETAIL
One faint callout leader line points at the short vertical rule marking where the
lower arrangement ends, ending in a small empty circle.

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
The teal accent belongs to the short vertical rule where the four-lane
arrangement finishes, and to nothing else — it marks how much sooner it is
done.

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
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-12-29-running-junit-tests-in-parallel --install ~/Downloads/<your-file>.jpg
```
