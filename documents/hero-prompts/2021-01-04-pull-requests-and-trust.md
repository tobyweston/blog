# Pull Requests and Trust — hero prompt

- **Post:** `astro/src/content/blog/2021-01-04-pull-requests-and-trust.mdx`
- **Style:** `flat-editorial`
- **Series:** standalone
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-git-collaboration.jpg`, shared with
  `2013-01-23-useful-git-commands`, which keeps it. Nothing is orphaned.
- **Video:** none

## Why this image

The post hands over its own metaphor, and the skill's rule is to use the
author's rather than invent a better one. It is the Kief Morris pullquote, which
sits at the emotional centre of the piece:

> Using pull requests for code changes by your own team members is like having
> your family members go through an airport security checkpoint to enter your
> home. It's a costly solution to a different problem.

So the hero is exactly that, drawn straight: a family queueing at airport
security to get into their own front door. It carries the argument — that the
ceremony is aimed at strangers and is absurd when pointed at people you already
trust — without needing a word of explanation.

`flat-editorial` because this post argues rather than demonstrates, and because
the style's faceless stylised figures are what let a domestic scene read as a
point rather than as a cartoon.

## A deliberate choice: no text at all

The other prompts in this folder spend their text budget on labels. This one
spends none. The visual joke is self-explanatory, and every string omitted is a
failure mode removed — no misspellings to check, nothing to mangle, and nothing
competing with the silhouettes at 192px. If a generated version comes back with
invented signage, reject it.

## Reference images

The post has one image, `git-request-pull.png`, a screenshot of the native Git
command's documentation. Ignore it. Per `flat-editorial`'s rule, only composition
is worth lifting from a post's images, and a terminal screenshot has none to
give. Do not attach it.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about how code review ceremony aimed at strangers becomes absurd when pointed at
your own team. Output a single flat image, no borders, no frame, no watermark,
no signature.

STYLE
Flat editorial illustration in a mid-century printed style, as though screen
printed in a small number of inks. Bold simplified geometric shapes, strong
silhouettes, minimal interior detail, no outlines or only occasional rough ones.
Visible paper grain and light halftone or misregistration texture. Figures
stylised and faceless or near-faceless. Confident and graphic. Not
photorealistic, not a 3D render, not a cartoon with thick outlines, not flat
corporate vector art with gradient blobs.

SUBJECT
An ordinary domestic front door, set in the wall of a house, on the RIGHT of the
image. It is clearly a home: a simple pitched roofline above it, a window with
curtains beside it, a doormat in front of it.

Directly in front of that door stands an airport security checkpoint, completely
out of place: a tall rectangular walk-through scanner arch, and beside it a low
conveyor belt carrying two shallow trays.

Queueing to pass through the arch, a line of THREE stylised faceless figures of
different heights, reading as a family — a tall adult, a second adult, and a
small child. The nearest adult is placing ordinary domestic belongings into a
tray on the conveyor: a set of house keys and a potted plant. The child holds a
teddy bear and waits.

A fourth faceless figure in a flat peaked cap stands beside the arch in the
posture of a guard, arms folded, watching them.

The reader should understand at a glance: these people live here, and they are
being screened to get in.

SUPPORTING DETAIL
Nothing further. No signage, no queue barriers, no aeroplanes, no luggage
carousel. The incongruity of a security arch on a doorstep is the whole joke and
extra scenery dilutes it.

TEXT IN THE IMAGE
No text anywhere in this image. No signs, no labels, no lettering on the arch,
the trays, the door or the conveyor, and no watermark. Any marking that would
read as writing must be left out entirely rather than rendered as placeholder
lines.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the security arch and the conveyor trays, and
to nothing else. The house, the door and all four figures stay in the deep ink
and the mid tone, so the checkpoint is the thing that looks wrong in the picture.

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

- **The house stops reading as a home.** If the door ends up looking like an
  office entrance or a terminal gate, the joke collapses into a picture of an
  airport. The roofline, the curtained window and the doormat are what carry it —
  if they are missing, regenerate.
- **The roofline sitting in the top band**, which the card crop removes. If the
  only cue that this is a house is cropped away, the card fails even though the
  full image works. Check the card render, not just the image.
- **Invented signage.** Generators like to letter an "EXIT" or a "SECURITY" onto
  an arch. The prompt forbids all text for this reason; a stray word is grounds
  for a regeneration here, since there is no label to check it against.
- **Too much airport.** Watch for carousels, departure boards and suitcases
  creeping in. One arch, one conveyor, two trays.
