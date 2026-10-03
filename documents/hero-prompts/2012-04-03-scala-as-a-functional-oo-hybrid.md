# Scala as a Functional OO Hybrid — hero prompt

- **Post:** `astro/src/content/blog/2012-04-03-scala-as-a-functional-oo-hybrid.md`
- **Style:** `technical-blueprint`
- **Series:** standalone
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/build-tools.jpg`, which is a 29-byte HTML 404 page
  saved with a `.jpg` extension

## Why this image

The post has almost no physical nouns in it — it argues that Scala is both
object-oriented and functional, and that you should know which style you are
writing in. The drawable mechanism is the blend itself: one machine assembled
from two visibly different kinds of part, joined at a coupling. The secondary
detail is referential transparency, drawn literally as the post describes it:
a sub-assembly and a plain block of the same shape, interchangeable.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about a programming language that is object-oriented and functional at
the same time. Output a single flat image, no borders, no frame, no watermark,
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
ONE single machine, drawn in isometric projection, running left to right across
the middle of the image. It is clearly built from two different kinds of part,
meeting at a coupling in the centre:

  - The LEFT half is built from solid rectangular blocks stacked and nested
    inside one another, like a cutaway of boxes within boxes. Each block is a
    closed container with a visible shell. This half looks SOLID and layered.
  - The RIGHT half is built from a straight chain of open inline units, like
    pipe sections bolted end to end, with a clear arrow entering the first unit
    on the right-hand side and a clear arrow leaving the last. Nothing branches
    off this chain and nothing connects it back to the left half except the
    central coupling. This half looks LINEAR and open.
  - Where the two halves meet, a single prominent flanged coupling joins them,
    bolted on both sides. This coupling is the focal point of the whole image.

The reader should understand at a glance: one machine, two kinds of engineering,
bolted together on purpose.

SUPPORTING DETAIL
Below the machine and slightly to the right, a small inset study drawn in the
same isometric style: a short sub-assembly of three chained units, an equals
sign, and then a single plain block of exactly the same outline as that whole
sub-assembly. Thin construction lines connect the inset to the right half of the
main machine. This shows that the assembly and the plain block are
interchangeable.

A few faint callout leader lines point at the coupling and at the stacked blocks,
ending in small empty circles with no text in them.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Above the left half of the machine: the single word "OO"
  - Above the right half of the machine: the single word "FUNCTIONAL"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. Do not put any text on the coupling or in the inset
study.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the central coupling only — it must be the
highest-contrast element in the image. Keep both halves of the machine in navy
and slate so the coupling is the thing the eye lands on.

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

- **"FUNCTIONAL" is the fragile string.** Ten characters is past where these
  models stay reliable. If it comes back misspelled, ask for "FP" instead, or
  drop both words — the two halves read as different without labels.
- **The inset study** is the first thing to cut if the image comes back
  cluttered. It is the nicest idea in the prompt and the least necessary; at
  192px tall it may be mush anyway.
- **Watch the bottom fifth.** Generators like to drop the inset study low in the
  frame, which is exactly the band the card crop throws away. If that happens,
  regenerate asking for the inset raised into the central band.
- **Text-free fallback:** drop the TEXT IN THE IMAGE section entirely. The two
  halves plus the amber coupling carry the idea on their own.
