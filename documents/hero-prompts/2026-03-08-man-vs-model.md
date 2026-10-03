# Man vs Model — hero prompt

- **Post:** `astro/src/content/blog/2026-03-08-man-vs-model.mdx`
- **Style:** `data-infographic` — this post is the style's reference image
- **Series:** standalone
- **Written:** 2026-10-03, reconstructed from the existing hero
- **Reference images:** attach the post's own charts, see below

```bash
.claude/skills/hero-image/scripts/generate_hero.py 2026-03-08-man-vs-model \
  --reference astro/src/content/images/man-vs-model/fvi_bar_chart.png \
              astro/src/content/images/man-vs-model/feature_points_publish_chart.png
```

## Where the numbers come from

Every figure is quoted from the post. Checked before writing:

| Figure | Source in the post |
|---|---|
| four weeks | "a concentrated four-week window" |
| 2x | "roughly **2x higher engineering throughput**" |
| 2.8x | "roughly **2.8x larger initiatives shipped**" |
| 5.8x | `DLI = 2.05 x 2.84 ≈ 5.82`, "**~5.8x vs historical baseline**" |

## One deliberate change from the existing hero

The hero on the post today shows 2x and 2.8x. The post's actual punchline is the
third number: those two measure different axes, and combining them gives a
Delivery Leverage Index of ~5.8x — the whole "Something Surprising" section. A
card that stops at 2.8x reports the inputs and withholds the finding.

So this prompt lays the three out as the multiplication the post actually
performs: 2x times 2.8x equals 5.8x. It is the same arithmetic, it reads in one
glance at card size, and it puts the headline result on the card, which is the
entire point of this style.

To reproduce the current image instead, drop the third card and the operators.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post summarising measured results from a four-week AI-assisted development
experiment. Output a single flat image, no borders, no frame, no watermark, no
signature.

STYLE
Flat vector infographic in a clean modern editorial style, laid out on a dark
ground. Solid shapes with no outlines, simple pictogram icons with no interior
detail, rounded-corner panels each with a thin luminous border. Typography does
the work: very large condensed bold numerals paired with short uppercase
captions beneath them. Generous spacing, thin horizontal rules separating bands,
everything aligned to a grid. Calm, precise and uncluttered, like a well-made
conference slide. Not photorealistic, not a 3D render, not a cartoon, not
hand-drawn, no gradients behind the type, no glowing neon, no busy dashboard
chrome, no fake charts with unreadable axes.

REFERENCE IMAGES
The attached images are charts from the post itself. Take two things from them
and nothing else: the specific mid blue used in their bars, and the sense of a
descending series of values. Do NOT reproduce these charts, their axes, their
tick marks, their gridlines or any of their labels, and do NOT carry over their
white background — this image is on a dark ground.

SUBJECT
A single horizontal row across the middle of the image, reading as one equation,
on a dark near-black navy ground.

  - At the far LEFT, a narrow column of two conditions stacked vertically, each
    a simple white pictogram with a short label beside it: a calendar icon, and
    below it a single person icon. No panel or border around these.
  - A thin vertical rule separates that column from the rest.
  - Then THREE rounded-corner stat panels in a row, each containing a small
    pictogram at the top, one very large condensed numeral below it, and a short
    uppercase caption under the numeral.
  - Between the first and second panel, a large multiplication symbol. Between
    the second and third, a large equals symbol. Both symbols plain white and
    clearly larger than the captions, so the row reads as an equation.
  - The THIRD panel is noticeably larger than the first two — taller, wider, and
    with the heaviest numeral in the image. It is the result and must dominate.

The reader should understand at a glance: two measured effects multiplied
together give a much bigger third one.

SUPPORTING DETAIL
The pictograms, in order: a small upward bar-chart glyph on the first panel, a
set of three nested rectangles on the second, and an upward arrow on the third.
Flat white silhouettes, no detail, no outlines.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words, labels, axis titles or units. Every numeral below must
be exact — do not round them or change them.
  - Beside the calendar icon: "4 WEEKS"
  - Beside the person icon: "1 CODER"
  - First panel, numeral then caption: "2x" and "THROUGHPUT"
  - Second panel, numeral then caption: "2.8x" and "LARGER FEATURES"
  - Third panel, numeral then caption: "5.8x" and "DELIVERY LEVERAGE"
Everything else must be abstract placeholder lines, not legible lettering. No
title, no heading and no footer line anywhere in the image.

COLOUR
Dark near-black navy ground throughout. White for headline type and for the
pictogram icons, with one clear mid blue and one warm amber as the only accents.
Each accent owns exactly one stat and the border of its panel, so the two
headline numbers are told apart by colour. Panels sit one shade lighter than the
ground, never a different hue. Four values in total and no more.
The first panel and its border are amber, the second blue. The third panel —
the result — takes the amber, at the highest contrast in the image, so the eye
lands on it first.

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

## A note on the file format

The hero on the post today is a PNG. `output-spec.md` reserves PNG for images
with flat areas and hard edges, which a card of large flat numerals looks like
it ought to be — so this was worth checking rather than assuming. Re-encoding the
current hero at JPEG q86 shows no ringing around the numerals and comes in at
135KB against 551KB for the PNG, so JPEG is the right choice here and the
script's default needs no override.

One consequence: regenerating writes `...-hero.jpg` and repoints the
frontmatter, leaving the old `...-hero.png` orphaned in
`astro/public/images/heroes/`. Delete it once the new image is accepted.

## What is most likely to go wrong

- **Check all three numerals before installing.** `2.8x` and `5.8x` are the
  risky ones: the decimal point gets dropped or the digits swapped, and in the
  existing hero the `8` in `2.8x` collides with the caption beneath it. A wrong
  number here is a correctness bug — the card is making a factual claim about
  the author's own work. Reject and regenerate rather than accepting a near miss.
- **The equation may come back as three unrelated cards.** The multiplication and
  equals symbols are what turn this from a dashboard into an argument. If they
  are missing or tiny, regenerate.
- **The third panel may not dominate.** Generators tend to make a row of panels
  uniform. If all three come out the same size, the finding is buried — say so
  more forcefully and ask for the result panel at roughly 1.5x the others.
- **A title may appear anyway.** The prompt forbids one because the card crop
  cuts the top band off, as measured on the current hero. A title that appears
  is harmless but wasted; it is not worth a regeneration on its own.
- **Reduced fallback:** drop the left-hand conditions column first — "4 WEEKS"
  and "1 CODER" are context, not findings. That takes the text budget from eight
  strings to six. Drop the captions next, leaving three numerals and the
  operators, which still carries the whole argument.
