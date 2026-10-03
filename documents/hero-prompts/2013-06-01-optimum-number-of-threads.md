# Calculate the Optimum Number of Threads — hero prompt

- **Post:** `astro/src/content/blog/2013-06-01-optimum-number-of-threads.md`
- **Style:** `technical-blueprint`
- **Series:** standalone
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/performance.jpg`, which does not exist
- **Video:** none, so this is generated rather than a keyframe

## Why this image

The post answers one question twice: how many threads keep a fixed set of cores
busy. For CPU-bound work it is `cores + 1`; for IO-bound work it is many more,
because a thread waiting on IO leaves its core idle. That contrast is the image
— the same bank of cores fed by few lanes or by many — and it reads as a
silhouette at thumbnail size, which a formula never would.

The amber accent goes on the single extra lane in the CPU panel. That one spare
lane *is* the post's headline fact, so it should be the thing the eye lands on.

No Java mug here, despite the `java` category. The previous post in the queue
uses one, and the formulas in this post are not Java-specific — the cores and
lanes are the real subject, so they carry it.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about how many worker threads it takes to keep a fixed number of CPU
cores busy. Output a single flat image, no borders, no frame, no watermark, no
signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
One image divided into two halves by a single thin vertical rule down the centre.
Both halves show THE SAME machine, drawn identically in isometric projection: a
row of FOUR identical square processor blocks sitting flat on a base plate, like
four chips mounted in a row. The four blocks must look the same on both sides.

What differs is how many supply lanes feed them:

  - LEFT HALF: FIVE narrow lanes run into the four blocks — straight, solid,
    unbroken channels, packed close together. Four lanes feed the four blocks
    directly and ONE additional lane runs alongside them into the row. The
    arrangement looks tight and efficient, barely more lanes than blocks.
  - RIGHT HALF: the same four blocks, but roughly TWELVE lanes feed them,
    fanning in from the right edge. Most of these lanes are drawn as broken,
    hollow or dashed channels with visible gaps along their length, as though
    stalled. Only two or three are solid and unbroken. The arrangement looks
    crowded, with far more lanes than blocks.

The reader should understand at a glance: the same four blocks, fed by a few
clean lanes on one side and by a crowd of mostly-stalled lanes on the other.

SUPPORTING DETAIL
A few faint callout leader lines point at the single additional lane on the left
and at one of the broken lanes on the right, ending in small empty circles with
no text in them.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Above the left half: "CPU"
  - Above the right half: "IO"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No formulas and no numbers anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to exactly one thing: the single additional lane on the
LEFT half — the one extra beyond the four blocks. Everything else, including
every lane on the right half, stays navy and slate, so that one amber lane is
the highest-contrast element in the picture.

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

- **The two halves drifting apart.** The whole point is that the four blocks are
  identical on both sides and only the lanes differ. Generators like to make the
  two halves different machines entirely. If that happens, regenerate — a
  before/after of two unrelated things says nothing.
- **Lane counts won't be exact.** Five versus twelve is a ratio, not an
  inventory; as long as one side is visibly sparse and the other visibly
  crowded, it works. Don't regenerate over a miscount.
- **"CPU" and "IO" are safe strings** — short, capitalised, no punctuation. This
  is the low-risk one of the three prompts.
- **Resist adding the formula.** `threads = cores / (1 - blocking coefficient)`
  is the post's payload and it is exactly the kind of string that comes back as
  nonsense, at a size nobody can read on a card. It stays in the post.
- **Text-free fallback:** drop the TEXT IN THE IMAGE section. Sparse lanes
  versus crowded broken lanes carries the idea unlabelled.
