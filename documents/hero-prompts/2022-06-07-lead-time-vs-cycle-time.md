# Lead Time vs Cycle Time — hero prompt

- **Post:** `astro/src/content/blog/2022-06-07-lead-time-vs-cycle-time.md`
- **Style:** `flat-editorial` — first use of this style
- **Series:** standalone
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-agile.jpg`, a generic hero shared
  with `2012-09-15-daily-standups-dont-work`. That post keeps it, so nothing is
  orphaned.
- **Video:** none

## Why this image, and why this style

The post's whole argument is a containment relationship: lead time runs from the
customer's order to delivery, and cycle time is the shorter span *inside* it
covering only the making. Its own diagrams draw exactly that — a long measured
span with a shorter one nested within. That nesting is the hero; nothing else in
the post competes with it.

`flat-editorial` rather than `technical-blueprint`, despite the diagrams: there
is no mechanism here, only a measurement, and an isometric drawing of a duration
would be nice lines around nothing. The style also happens to fit the subject —
the post traces these terms back to lean manufacturing, and a mid-century printed
look is the period those ideas come from.

The accent goes on the *cycle time* span, because the post's practical point is
that it is the part you can actually manage: "companies can significantly reduce
their lead time by more effectively managing their cycle time".

## Reference images

The post has four diagrams — `leadtime_1.svg` through `leadtime_4.svg`, Excalidraw
exports in black on white. **They cannot be attached directly**: the API wants a
raster image, and these fail to rasterise locally because of the webfonts they
embed. `generate_hero.py --reference` will say so rather than failing obscurely.

Take from them only what this style wants, which per `flat-editorial` is
composition and nothing else: the long span with the shorter one nested inside,
and the left-to-right direction of travel. Ignore their hand-drawn line quality
and their labels entirely. That arrangement is written into the prompt below, so
no attachment is needed.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about the difference between two measured durations in software
delivery. Output a single flat image, no borders, no frame, no watermark, no
signature.

STYLE
Flat editorial illustration in a mid-century printed style, as though screen
printed in a small number of inks. Bold simplified geometric shapes, strong
silhouettes, minimal interior detail, no outlines or only occasional rough ones.
Visible paper grain and light halftone or misregistration texture. Figures
stylised and faceless or near-faceless. Confident and graphic. Not
photorealistic, not a 3D render, not a cartoon with thick outlines, not flat
corporate vector art with gradient blobs.

SUBJECT
A single production line running left to right across the middle of the image,
drawn as one long horizontal belt or bench with simple geometric shapes sitting
on it. The shapes progress along the belt: a plain rectangle at the left becomes
more assembled towards the right, ending as one finished solid block.

At the far LEFT of the belt, a stylised faceless figure hands a small square over
to it. At the far RIGHT, a second stylised faceless figure receives the finished
block. Both figures are simple silhouettes, flat and without features.

Above the belt, TWO horizontal measuring spans drawn as plain bracket lines with
a short vertical tick at each end, like dimension lines on a drawing:

  - The UPPER, LONGER span reaches all the way from the figure on the left to the
    figure on the right, covering the entire scene end to end.
  - The LOWER, SHORTER span sits beneath it and covers only the middle portion of
    the belt — where the shapes are being assembled. It begins well after the
    left-hand figure and ends well before the right-hand one, so it is clearly
    contained within the longer span above it.

The containment is the entire point: a reader must see at a glance that the
shorter measurement sits inside the longer one.

SUPPORTING DETAIL
Nothing else. No machinery, no clocks, no gauges, no arrows beyond the two
measuring spans. Empty paper around the composition is correct.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Along the upper, longer span: "LEAD TIME"
  - Along the lower, shorter span: "CYCLE TIME"
Everything else must be abstract placeholder lines, not legible lettering. No
labels on the figures, the belt or the shapes.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the shorter "CYCLE TIME" span and its end
ticks, and to nothing else. The longer span, the belt and both figures stay in
the deep ink and the mid tone, so the shorter span is what the eye lands on.

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

- **The spans stacked instead of nested.** This is the one that matters. If the
  two brackets come back the same length, or side by side, or the shorter one
  extending past the longer, the image states the opposite of the post. Check
  this before anything else and regenerate if it is wrong.
- **Both spans drifting into the top band**, which the card crop removes. They
  need to sit just above the belt, well inside the central 60%, not floating near
  the top edge. This is the likeliest reason to need a second attempt.
- **"LEAD TIME" and "CYCLE TIME" are low-risk strings** — short, uppercase, no
  punctuation — but they must not be swapped. The long one is LEAD.
- **Clocks and stopwatches.** Generators reach for them whenever "time" appears.
  The prompt forbids them because a clock face at 192px is a grey circle. If they
  appear, regenerate.
- **Text-free fallback:** drop the TEXT IN THE IMAGE section. A long span over a
  shorter nested one still reads, though it loses which is which — so prefer one
  more regeneration over going text-free here.
