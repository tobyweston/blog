# Baking in Evidence — hero prompt

- **Post:** `astro/src/content/blog/2026-10-02-baking-in-evidence.mdx`
- **Style:** `bold-outline-cartoon`, with the baker
- **Series:** the bakery / controls-engineering series
- **Written:** 2026-10-03 — a fresh pass against the current skill, for comparison
  with the hero already in place
- **Video:** none

## Why this image

This post's complaint is specific: evidence comes out in whatever shape the tool
that produced it happened to emit — a JSON blob here, a PDF there, a spreadsheet
somewhere else. The fix is that every control emits the same shape.

So a fresh pass makes the image about sameness of output from difference of
input, which the current hero only implies by showing copies. Several visibly
different machines, one identical document shape coming out of each.

## Reference image

```bash
--reference astro/src/content/images/unified-evidence-bakery.png
```

Per the style's rule: take the objects and the arrangement, drop the rendering.
The attached figure is a diagram and a rendered document — neither should be
reproduced, and the attached layout must be redrawn with thick outlines and flat
fills, not pasted in.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about making every control produce a record of the same shape. Output a single flat image, no borders, no frame, no watermark,
no signature.

STYLE
Bold-outline vector cartoon illustration, in the style of a modern comic or
children's-book spread. Thick black outlines on every object, clean flat colour
fills with soft gradient shading, gentle highlights. Cheerful, warm and slightly
exaggerated, with friendly rounded shapes. Not photorealistic, not a 3D render,
not watercolour, not flat minimalist corporate vector art, not line art.

RECURRING CHARACTER (continue an existing series)
A friendly cartoon baker: dark hair tied back, broad happy grin, white
double-breasted chef's jacket with black round buttons, red cuffs, red
neckerchief tied at the throat, white chef's hat. Warm bakery setting: wooden
shelves of bread loaves loosely blurred behind, copper mixing bowls, a light
stone countertop across the lower third.

SUBJECT
THREE clearly different machines standing in a row along the countertop, each
obviously a different piece of equipment: a tall oven with a round door on the
LEFT, a squat mixing machine with a bowl in the MIDDLE, and a narrow proving
cabinet with slatted shelves on the RIGHT.

From the front of each, one printed document is emerging through a slot. All
THREE documents are identical: the same size, the same proportions, the same
layout — a bright green shield badge with a white tick in the upper corner, and
three horizontal bands of grey placeholder lines below it.

The machines could not look more different from one another; the documents could
not look more alike. That contrast is the subject.

The baker stands at the RIGHT end of the row, holding one of the three documents
up and looking at it with approval.

SUPPORTING DETAIL
On the counter in front of the middle machine, a single iced cake on a plate.
Nothing else.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Across the face of the document the baker is holding: "EVIDENCE"
Everything else must be abstract placeholder lines, not legible lettering. No
text on the green shield badges, just a white tick. No code, no terminal output,
no filenames and no numbers anywhere.

COLOUR
Warm, domestic palette: cream, golden brown, wood tones, soft reds, with a
single saturated accent colour used sparingly for the thing that matters most.
Backgrounds warm and slightly muted so foreground objects separate cleanly.
The saturated accent belongs to the three identical documents, and to nothing
else — all three share it, because their sameness is the point. The three
machines, the counter, the baker and the cake stay in the warm domestic palette.
The green shields keep their own green.

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

- **The three documents differing.** Identical in size, shape and layout. If they
  vary at all the image argues against the post.
- **The three machines looking similar.** Their variety is the other half of the
  contrast.
- **Code or a terminal appearing.** The post contains Rego, but a code wall reads
  as grey mush at card size — see the standing rule.
- **The baker losing her look.** Same jacket, same red cuffs and neckerchief,
  same hat as the rest of the series — she is a recurring character, not a
  generic chef.
- **The counter filling with clutter.** One cake. The bakery behind stays loosely
  blurred.
