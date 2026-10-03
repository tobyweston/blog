# Java Source on Mac OS X — hero prompt

- **Post:** `astro/src/content/blog/2009-08-01-java-source-for-mac-osx.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

Short and exasperated: the source is in there somewhere, behind Apple's
distribution arrangements, and getting at it is the whole problem.

So the image is a sealed cabinet with a viewing window — the thing you want is
plainly visible inside, and the hatch is locked. It carries the command glyph, as
the Mac Tips hero does, so the two Mac posts read together.

## The mark is composited

The command glyph goes in from `documents/brand/command-key.png` after
generation, as on the Mac Tips hero, so the two Mac posts read together. U+2318
is a standard interface symbol and not a trademark.

```bash
H=astro/public/images/heroes/2009-08-01-java-source-for-mac-osx-hero.jpg
magick $H \( documents/brand/command-key.png -resize x150 \) \
  -gravity east -geometry +150-20 -composite -quality 86 $H
```

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about source code you can see but cannot get at. Output a single flat image, no borders, no frame, no watermark,
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
A display case drawn in isometric projection, centred: a plain rectangular
cabinet whose front face is one large clear panel, with no door, hatch or opening
of any kind anywhere on it. It is a solid sealed case.

Standing inside the case, clearly visible through the panel, a neatly wound spool
of ribbon on a spindle — plainly the thing worth having.

In front of the case, outside it, a small empty display stand with a shaped
cradle moulded to fit that very spool. The cradle sits waiting and unoccupied,
and its shape plainly matches the spool behind the glass.

Nothing in the image connects the two: no opening, no chute, no handle.

MARGINS
The entire composition must fit within the LEFT 72% of the image width. The
rightmost 28% is empty background — nothing whatsoever extends into it: no
object, no callout line, no shadow and no marking. The background there is the
same plain ground and grid as everywhere else, with no panel, box, border, frame
or change of tone to indicate it.
Do not draw any logo, badge, emblem, roundel or icon anywhere in this image.

SUPPORTING DETAIL
One faint callout leader line points at the empty shaped cradle on the stand,
ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The amber accent belongs to the empty shaped cradle waiting outside the case, and
to nothing else. The case, its panel and the spool inside stay navy and slate.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## What is most likely to go wrong

- **The case gaining a door or hatch.** It is sealed on every face; that is why
  the spool cannot be had.
- **The spool hidden.** It must be clearly visible through the panel — seeing it
  and not reaching it is the frustration.
- **The cradle occupied.** It stays empty.

An earlier version of this prompt used a padlock, a hasp and a missing key. The
model returned text instead of an image, twice — most likely reading "something
visible, locked away, and no key" as circumventing a lock. Reframed as a sealed
case and a waiting cradle, it generates fine. Worth remembering: a refusal here
arrives as a completed response with output tokens in the text modality and no
image, not as an HTTP error.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2009-08-01-java-source-for-mac-osx --install ~/Downloads/<your-file>.jpg
```
