# Mountain Lion Carnage — hero prompt

- **Post:** `astro/src/content/blog/2012-07-28-mountain-lion-carnage.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The upgrade took Java, Subversion and Git away and left Python half broken, and
the post is the recovery.

So the image is a mounting rail with bays emptied: the modules are not destroyed,
they are on the floor, and one is being put back. Missing rather than broken is
the whole character of the problem.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about an operating system upgrade that quietly removed the tools you depend on. Output a single flat image, no borders, no frame, no watermark,
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
A horizontal mounting rail drawn in isometric projection, spanning the middle of
the image, with SIX bays along it.

THREE bays still hold their modules, seated and bolted. THREE are empty, their
mounting points bare and their retaining clips hanging open.

On the ground below the rail, lying on their sides, the three missing modules —
undamaged, plainly just removed rather than broken.

One of those three is in mid-air on a dashed construction line, rising back
towards its empty bay, with a small arrowhead showing the direction.

SUPPORTING DETAIL
One faint callout leader line points at an open retaining clip on an empty bay,
ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the single module being lifted back into place and the
bay it is heading for, and to nothing else.

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

- **The missing modules looking broken.** They are intact and on the floor. Damage
  would tell a different story.
- **All six bays empty.** Three and three.
- **An Apple logo or any OS branding.**

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-07-28-mountain-lion-carnage --install ~/Downloads/<your-file>.jpg
```
