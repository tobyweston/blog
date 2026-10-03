# Be Explicit About the UI Thread in SWT — hero prompt

- **Post:** `astro/src/content/blog/2008-12-30-be-explicit-about-ui-thread-in-swt.md`
- **Style:** `technical-blueprint`
- **Series:** the `java` posts, SWT and UI testing group — all carry the Java
  cup in its series variant, see the Recurring motif section of the style file
- **Written:** 2026-10-03
- **Replaces:** nothing — this post has no `heroImage` today
- **Video:** none

## Why this image

In SWT almost everything on screen may only be touched from the UI thread, and the
post argues for being explicit about which thread you are on rather than
discovering it by crashing.

The image is a single gated walkway into a glass case: one lane in, everything
else blocked out.

## Reference images

None worth attaching — these posts illustrate themselves with code listings,
which must not be drawn.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about only one thread being allowed to touch the user interface. Output a single flat image, no borders, no frame, no
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
A sealed glass display case drawn in isometric projection on the RIGHT of the
image, its interior holding three simple panel shapes arranged like a laid-out
screen.

A single narrow walkway leads into the case through one gate in its side. The
gate is open and the walkway is clear.

THREE identical small carriages approach from the LEFT. ONE of them is on the
walkway, passing through the gate. The other TWO have been stopped short by a
plain barrier across their path, well before the case, and sit waiting behind
it.

The case has no other opening anywhere.

BRAND MARK
In the lower-left corner of the image, clear of the main subject, a Java mark: a
plain cup seen from the side, drawn in a mid steel blue, with two curling wisps
of steam rising from it in a warm orange-red. Flat shapes, no outline, no saucer,
no circle or roundel around it and no text beside it.

SUPPORTING DETAIL
One faint callout leader line points at the single gate, ending in a small empty
circle.

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
The amber accent belongs to the walkway and its gate — the one permitted route —
and to nothing else. The case, the panels, all three carriages and the barrier
stay navy and slate.

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

- **A second way in.** One gate. Any other opening undoes the point.
- **The stopped carriages looking broken.** They are waiting, not crashed.
- **The Java mark growing, or its orange drifting towards the amber.** Small,
  lower-left, well clear of the accent.
- **The mark landing in the bottom fifth**, which the card crop removes.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2008-12-30-be-explicit-about-ui-thread-in-swt --install ~/Downloads/<your-file>.jpg
```
