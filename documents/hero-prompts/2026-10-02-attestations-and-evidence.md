# Attestations and Evidence — hero prompt

- **Post:** `astro/src/content/blog/2026-10-02-attestations-and-evidence.mdx`
- **Style:** `bold-outline-cartoon`, with the baker
- **Series:** the bakery / controls-engineering series
- **Written:** 2026-10-03 — a fresh pass against the current skill, for comparison
  with the hero already in place
- **Video:** none

## Why this image

The post's own diagram lays the chain out and gives it the bakery reading:
attestations (what happened — the ingredients) plus policy (what should have
happened — allergen-free) go into an evaluation (the testing laboratory) and come
out as evidence (a nut-free certificate).

A fresh pass takes that chain rather than arranging the terms side by side,
because the post's argument is that the two inputs are *not interchangeable* and
the order matters. Two distinct things in, one thing out.

## Reference image

```bash
--reference astro/src/content/images/attestation_and_cakes_summary.png
```

Per the style's rule: take the objects and the arrangement, drop the rendering.
The attached figure is a diagram and a rendered document — neither should be
reproduced, and the attached layout must be redrawn with thick outlines and flat
fills, not pasted in.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about two different kinds of record that together let a control be proved. Output a single flat image, no borders, no frame, no watermark,
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
The baker stands behind the countertop on the LEFT, both hands resting on it,
watching what is happening in front of her.

On the counter, running left to right, a simple three-stage bench device:

  - At its left end, TWO separate hoppers side by side feeding in. The NEAR
    hopper holds a loose heap of baking ingredients — flour, eggs, butter. The
    FAR hopper holds a small neat stack of printed cards. They are obviously
    different in kind, not two of the same thing.
  - In the middle, a glass-fronted cabinet with a simple mechanism visible
    inside, plainly where the two are brought together and checked.
  - At its right end, a slot from which ONE finished printed certificate is
    emerging, held in a little tray.

That certificate is clean and formal, with a bright green shield badge carrying a
white tick in its upper corner, and three horizontal bands of grey placeholder
lines below it.

SUPPORTING DETAIL
On the counter beside the device, a single small iced cake on a plate, finished
and waiting. Nothing else.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Across the face of the emerging certificate: "EVIDENCE"
Everything else must be abstract placeholder lines, not legible lettering. No
text on the green shield badges, just a white tick. No code, no terminal output,
no filenames and no numbers anywhere.

COLOUR
Warm, domestic palette: cream, golden brown, wood tones, soft reds, with a
single saturated accent colour used sparingly for the thing that matters most.
Backgrounds warm and slightly muted so foreground objects separate cleanly.
The saturated accent belongs to the emerging certificate alone — the thing the
whole bench produces — and to nothing else. The two hoppers, the cabinet, the
baker and the cake stay in the warm domestic palette. The green shield keeps its
own green.

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

- **The two hoppers looking alike.** One holds ingredients, one holds printed
  cards. Their difference is the post's entire point.
- **More than one certificate.** One out. The companion post is the one about
  many.
- **"EVIDENCE" is a safe string** but must not gain a second word.
- **The baker losing her look.** Same jacket, same red cuffs and neckerchief,
  same hat as the rest of the series — she is a recurring character, not a
  generic chef.
- **The counter filling with clutter.** One cake. The bakery behind stays loosely
  blurred.
