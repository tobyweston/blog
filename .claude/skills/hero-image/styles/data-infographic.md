# Data infographic

For posts that measured something and have numbers to show for it. The hero is a
summary of the findings rather than a picture of the subject — a reader should be
able to take the headline result off the card without opening the post.

Derived from `2026-03-08-man-vs-model`, which is the reference image for this
style. Look at it before writing a prompt.

## Style block

```text
Flat vector infographic in a clean modern editorial style, laid out on a dark
ground. Solid shapes with no outlines, simple pictogram icons with no interior
detail, rounded-corner panels each with a thin luminous border. Typography does
the work: very large condensed bold numerals paired with short uppercase
captions beneath them. Generous spacing, thin horizontal rules separating bands,
everything aligned to a grid. Calm, precise and uncluttered, like a well-made
conference slide. Not photorealistic, not a 3D render, not a cartoon, not
hand-drawn, no gradients behind the type, no glowing neon, no busy dashboard
chrome, no fake charts with unreadable axes.
```

## Palette

```text
Dark near-black navy ground throughout. White for headline type and for the
pictogram icons, with one clear mid blue and one warm amber as the only accents.
Each accent owns exactly one stat and the border of its panel, so the two
headline numbers are told apart by colour. Panels sit one shade lighter than the
ground, never a different hue. Four values in total and no more.
```

## Recurring component

**The stat card.** The unit this style is built from: a rounded panel with a thin
accent border, a small pictogram at the top, one very large numeral below it, and
a caption of at most two short uppercase words under that. Two or three of them
in a row is the whole composition. A left-hand column of plain icon-and-label
pairs — "4 WEEKS", "1 CODER" — sets up the conditions the numbers were measured
under.

Keep the card shape identical between posts. It is the thing that will make a
series of these look like a set.

## The two rules that matter most

**Never invent a number.** Every figure in the image must appear in the post,
copied exactly. This style's whole value is that the card states a real finding,
and a hero that rounds 2.8x to 3x or illustrates a number the post never
measured is worse than having no hero. Quote the post, and if the post has no
numbers then this is the wrong style.

**The card crop eats the headline.** Measured on the reference image: at the
2.8:1 card crop, the top headline and the closing line at the bottom are both cut
away entirely, and only the middle band survives. That turned out fine because
the stats live in the middle — but it is luck unless you plan for it. Put the
stat cards in the central 60% and treat any headline or closing question as
something only the social preview will ever show.

## Text budget

This style deliberately breaks the three-string rule in `SKILL.md`. An infographic
with two labelled stats needs six to eight strings, and there is no way round it.
Buy that back by making every string trivially easy to render:

- Numerals are the most reliable glyphs these models draw. Lead with them.
- Captions in CAPITALS, two words maximum, no punctuation, no hyphens.
- Never put a sentence inside a panel.
- Spell every string out in the prompt exactly, and check each one before
  installing — a wrong number is a correctness bug, not a cosmetic one.
- Expect to regenerate more often than with the other styles. Budget for it.

## Reference images from the post

This style gains the most from attachments, because the post's charts hold the
very numbers the hero is summarising. Attach the two or three charts the findings
rest on and ask for their palette and their proportions to carry over, so the
card and the post read as one piece of work.

Do not ask for a chart to be redrawn. Generated axes, ticks and legends come back
as unreadable noise at card size, and a fake chart implies data that was never
plotted. Take the colours and the shape of the result; state the finding as a
numeral on a stat card instead.

## Works well for

Posts reporting something the author measured: productivity and delivery
studies, benchmark results, cost or pricing comparisons, before-and-after
numbers. The test is whether you can pull two or three headline figures straight
out of the post.

## Avoid

Posts that argue rather than measure — use `flat-editorial`. Posts explaining a
mechanism — use `technical-blueprint`. Above all, avoid it for any post where you
would have to make a number up to fill the second panel; that is the signal the
post wants a different style, not that it wants fewer stats.

## Used by

- `2026-03-08-man-vs-model` — four weeks, one coder, 2x more code shipped,
  2.8x larger features. The reference image for the style.
