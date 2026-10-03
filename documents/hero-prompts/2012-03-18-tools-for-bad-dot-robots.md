# Tools for bad.robots — hero prompt

- **Post:** `astro/src/content/blog/2012-03-18-tools-for-bad-dot-robots.md`
- **Style:** `technical-blueprint`, with the mascot composited in
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image, and why the robot

This is the post that introduces `robotooling` — four of the author's own Java
libraries collected under the bad.robot banner. It is his project, his name on
it, and an announcement rather than an explanation, which is exactly the case the
robot note in `SKILL.md` describes as earning the mascot. If the robot appears on
one hero in ten, this is the one.

So the image is a tool rack with four distinct tools in it, one for each library,
and the robot standing beside it as its proprietor.

## The robot is composited, not drawn

The mascot goes in from `documents/brand/robot-mascot.png`, which is the site's
own artwork extracted from `robot-cane-og.png` and given an alpha channel. It is
not described to the generator and not redrawn — the same principle as the
FreeAgent and OAuth marks, and for the same reason: a generated approximation of
a logo is a worse logo.

The prompt therefore keeps the left of the frame clear, as composition rather
than as a reserved box — asking for an empty rectangle makes these models draw a
rectangle.

```bash
# after generating, from the repo root
H=astro/public/images/heroes/2012-03-18-tools-for-bad-dot-robots-hero.jpg
magick $H \
  \( documents/brand/robot-mascot.png -resize x300 \) \
  -gravity west -geometry +110-20 -composite -quality 86 $H
```

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
introducing a small collection of a developer's own open-source tools. Output a
single flat image, no borders, no frame, no watermark, no signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
An open wall-mounted tool rack drawn in isometric projection, with FOUR bays
side by side, each holding one tool. The four tools are clearly different from
one another and each sits in a shaped cradle made for it:

  - a short spigot or tap fitting with a stub of hose attached
  - a flat rectangular plate ruled into a regular grid of small empty squares
  - a bound sheaf of plain sheets, clipped along one edge
  - a set of four small identical stamped blocks, nested together in their bay

The rack is a single piece of furniture, plainly built to hold these things
together rather than four separate shelves.

MARGINS
The entire composition must sit within the RIGHT 72% of the image width. The
leftmost 28% is empty background — nothing whatsoever extends into it: no part
of the rack, no tool, no callout line, no shadow and no marking. The background
there is the same plain ground and grid as everywhere else, with no panel, box,
border, frame or change of tone to indicate it.
Do not draw any robot, character, figure, mascot, logo, badge or emblem anywhere
in this image.

SUPPORTING DETAIL
One faint callout leader line points at one of the shaped cradles, ending in a
small empty circle. Nothing else — no workshop, no walls, no other furniture.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, filenames,
URLs or project names, and nothing numbered or named. The ruled grid plate holds
empty squares only. Any marking that would read as writing must be left out
rather than rendered as placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand, not warm off-white. Deep navy and slate line work. One warm
accent (amber or rust), used sparingly, for the single component the post is
about. No gradients beyond flat tonal steps.
The amber belongs ONLY to the rack's frame rails — the two uprights and the top
rail — and to nothing else. The four shaped cradles stay navy and slate like the
tools, so the amber is a thin structural outline holding everything together
rather than a large coloured mass. Most of this image is cool: if more than
roughly a tenth of it is warm, there is too much amber.

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

- **Anything intruding into the left 28%.** The robot goes there. A callout line
  or the end of the rack straying across will end up behind him.
- **A drawn robot or figure appearing.** The prompt forbids it. The real one is
  composited; a generated one would clash with it and with the mascot everywhere
  else on the site.
- **The four tools not reading as different.** Four of the same thing says
  nothing about a collection of four libraries.
- **The ground drifting warm.** Cool blue-grey. A cream or sand ground puts this
  card between the two house families and belonging to neither.
- **Too much amber.** The frame rails only, not the cradles. A rack rendered
  orange all over stops being an accent and becomes the whole picture.
- **The robot sized wrong at the composite step.** At 300px tall he stands about
  a third of the frame height, which keeps him a presence without becoming the
  subject. Check he is inside the card crop, not below it.
