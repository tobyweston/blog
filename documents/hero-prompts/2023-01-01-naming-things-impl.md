# Don't name classes 'Impl' — hero prompt

- **Post:** `astro/src/content/blog/2023-01-01-naming-things-impl.md`
- **Style:** `technical-blueprint`
- **Series:** part of the author's "5 Coding Habits that are Hurting you" series
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-code-quality.jpg`, shared with
  `2019-08-09-refactoring-in-10-minutes`, which keeps it. Nothing is orphaned.
- **Video:** none

## Why this image

The post's argument is that `StackImpl` tells a reader nothing, where
`ArrayStack` tells them what they need to know — "What would you name another
implementation? `Stack2Impl`? How do they differ? I should be able to tell from
the name."

So the image is two interchangeable modules that fit the same socket: one whose
form shows what it is, and one that is a featureless blank. The socket is the
interface, the modules are implementations, and the blank one is the habit the
post is calling out.

`technical-blueprint` because the point depends on reading labels, and
`flat-editorial` explicitly avoids anything needing legible technical detail.
The category table sends `java` here anyway, and unusually for an opinion piece
there is a real mechanism to draw: a contract and the things that satisfy it.

## The accent is on the thing the post is against

In the other blueprint prompts the amber marks the good part. Here it marks the
blank `Impl` module, because that is "the single component the post is about" —
the habit being called out. Deliberate, not a slip.

## Reference images

The post has none of its own — only fenced Java snippets, which must not be drawn.
See the standing rule against code walls: a block of code renders as grey mush at
card size.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about naming implementation classes so that their names say what they
actually are. Output a single flat image, no borders, no frame, no watermark, no
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
An isometric scene with one receiving socket and two modules that fit it.

  - On the LEFT, a heavy mounting plate standing upright, with a single
    rectangular recessed socket cut into it. Bolt holes around the socket. This
    is the fitting that both modules plug into, and it is drawn once.
  - Floating to the RIGHT of the plate, as in an exploded diagram, TWO
    rectangular modules of identical outline and identical connector, clearly
    interchangeable, each with a dashed construction line showing it aligning
    with the same socket.
  - The UPPER module is visibly structured: its face is divided into a row of
    six equal compartments, like a tray of cells, so you can see at a glance
    what it is made of.
  - The LOWER module is completely featureless: the same outline, same
    connector, but a blank unbroken face with no detail of any kind on it.

The reader should understand at a glance: both fit the same socket, but only one
of them tells you anything about itself.

SUPPORTING DETAIL
Two faint callout leader lines, one from the upper module and one from the lower,
each ending in a small empty circle. No other scenery.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels. Capitalisation must be exactly as given.
  - On the mounting plate, beside the socket: "Stack"
  - On the face of the upper, compartmented module: "ArrayStack"
  - On the face of the lower, blank module: "Impl"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No code, no braces, no semicolons and no syntax
anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the LOWER, blank module only — the one marked
"Impl" — so that the featureless one is what the eye lands on. The mounting
plate and the compartmented module stay entirely in navy and slate.

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

- **"ArrayStack" is the fragile string.** Ten characters, mixed case, and a
  compound word generators like to split into "Array Stack" or capitalise as
  "ARRAYSTACK". Mixed case is the point — these are class names. Check it
  closely; if it will not come out, fall back to "Array" and "Impl", which still
  makes the contrast.
- **The two modules stacked vertically may both drift out of the central band.**
  They need to sit side by side or close together vertically, well inside the
  middle 60%. This is the likeliest reason for a second attempt.
- **The blank module coming back not blank.** Generators dislike empty surfaces
  and will decorate it. Its blankness *is* the argument — if it arrives with
  panel lines, vents or texture, regenerate.
- **Code creeping in.** Any braces, semicolons or syntax means a regeneration;
  see the standing rule about code walls.
- **Text-free fallback:** there isn't a good one. Without the three labels this
  image is just two blocks and a plate. If the lettering will not come out after
  a few attempts, the post is better served by a different composition than by a
  text-free version of this one.
