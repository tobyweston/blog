# SWTBot vs Window Licker — hero prompt

- **Post:** `astro/src/content/blog/2009-03-15-swtbot-vs-window-licker.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, SWT and UI testing group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

An experience report comparing two frameworks, and the post is explicit that they
are not squaring off — they are built differently and suit different things.

So the image avoids a versus framing. It shows two harnesses of visibly different
internal construction, both connected to the same application window: same job,
different machines.

## Reference images

```bash
--reference astro/src/content/images/window-licker.png
```

Take only the arrangement from it. Do not reproduce any screenshot content; see
the standing rule against UI screenshots.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about comparing two GUI testing frameworks and how differently they are built. Output a single flat image, no borders, no frame, no
watermark, no signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
One application window drawn as a plain outline — a rectangle with a title bar —
standing upright in the CENTRE of the image, in light line only.

A harness is connected to it from each side, and the two are built differently:

  - The LEFT harness is a compact solid block with a single short arm reaching to
    the window, its internals hidden.
  - The RIGHT harness is open-framed, built of visible struts, with three thinner
    arms reaching to the window at different heights.

Both connect to the same window. Neither is larger or more prominent than the
other, and there is nothing between them suggesting conflict — no arrows facing
off, no dividing line down the middle.

BRAND MARK
On the LEFT of the image, clear of the main subject, a Java mark: a plain cup
seen from the side, drawn in a mid steel blue, with two curling wisps of steam
rising from it in a warm orange-red. Flat shapes, no outline, no saucer, no
circle or roundel around it and no text beside it.
Position it so the WHOLE mark — the base of the cup included — sits above the
lower third of the image. It must not touch the bottom edge and must not sit in
the bottom fifth. Treat the lower fifth of the frame as unusable: a mark placed
there loses its cup to the card crop and survives only as a stray orange squiggle.

SUPPORTING DETAIL
Two faint callout leader lines, one into each harness, ending in small empty
circles.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames, and no text beside the Java mark. Any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The small blue-and-orange Java mark in the corner is the only exception. Keep it
small and well clear of the amber element — its orange steam is close in hue to
the accent, so the two must never sit near each other or at similar sizes.
The amber accent belongs to the arms where both harnesses meet the window — the
point of contact they share — and to nothing else. Both harness bodies and the
window outline stay navy and slate.

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

- **A versus composition.** No central divide, no facing arrows, no scoreboard.
  The post explicitly rejects that framing.
- **One harness dominating.** Equal weight.
- **A real screenshot.** The window stays an empty outline.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-03-15-swtbot-vs-window-licker --install ~/Downloads/<your-file>.jpg
```
