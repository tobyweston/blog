# Baking in Evidence — hero prompt

- **Post:** `astro/src/content/blog/2026-10-02-rego-bakery-release-policy.mdx`
- **Style:** `bold-outline-cartoon`
- **Series:** follows `2026-10-02-attestations-and-evidence` — attach that post's
  hero (`astro/public/images/heroes/2026-10-02-attestations-and-evidence-hero.jpg`)
  as a style reference
- **Written:** 2026-10-02

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about software governance. Output a single flat image, no borders, no
frame, no watermark, no signature.

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
The baker is proudly holding up ONE large printed document toward the viewer,
like a certificate. The document is the focus of the image and must be clearly
readable. It is a clean white printed page with:
  - a bright green shield badge with a white tick in its top-left corner
  - three horizontal bands of printed content separated by thin rules, each band
    suggesting a small table of rows (grey placeholder lines, not real text)
  - a strip of small monospace-looking characters along the top, suggesting a
    hash

SUPPORTING DETAIL
Behind the baker, on the countertop, a neat row of three or four IDENTICAL
copies of the same document, slightly overlapping, each with the same green
shield badge. The point being made visually: every document has the same shape.

To one side, a single sheet of paper showing a few lines of code in a monospace
font on a pale background, with simple syntax colouring.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Across the document the baker is holding: the single word "EVIDENCE"
  - On the sheet of code, exactly two lines:
        package bakery
        default compliant := false
  - On the green shield badge: no text, just a white tick
Everything else must be abstract placeholder lines, not legible lettering.

COLOUR
Warm, domestic palette: cream, golden brown, wood tones, soft reds, with a
single saturated accent colour used sparingly for the thing that matters most.
Backgrounds warm and slightly muted so foreground objects separate cleanly.
The green shield and the white document should be the highest-contrast elements
so the eye lands on them first.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the baker's face, the held document and all text inside
that central band; the top 20% and the bottom 20% may be cut away entirely, so
put nothing there but background. Keep text away from the left and right edges
too. The image must still read at roughly 550 x 190 pixels, so favour large
shapes and strong contrast over fine detail. Balanced composition, not centred
symmetrically.
```

## Notes

The two lines of Rego are the most likely thing to come out mangled. If the
generator fumbles them, drop the `SUPPORTING DETAIL` code sheet and the second
text bullet and regenerate — the Rego is in the post itself, so the hero doesn't
need to carry it. The green shield and the row of identical documents are the
parts doing the real work.
