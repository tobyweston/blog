# Changing Test Gears — hero prompt

- **Post:** `astro/src/content/blog/2010-07-09-changing-test-gears.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post's own metaphor is poker: good players change gears, reading how the odds
shift as the game goes on and altering their style to match. The rules say to use
the author's metaphor rather than invent one, so the image is a card table at the
moment of that switch.

## Reference images

None worth attaching.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about knowing when to switch the kind of testing you are doing. Output a single flat image, no borders, no frame, no watermark,
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
A card table seen from above and slightly to one side, filling the middle of the
image.

On the felt, THREE face-up cards are laid in a row, and a fourth is being turned
over — caught mid-turn, half showing. The cards carry plain geometric pips, not
real suits or numbers.

In front of the cards, a stack of chips that has plainly just been pushed
forward: it sits well ahead of two other, untouched stacks further back, with a
short motion mark behind it.

A single stylised faceless figure's hands are at the table edge, one resting, one
having just pushed the stack.

SUPPORTING DETAIL
Nothing else. No room, no other players, no faces, no money.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Nothing may be numbered or named, and any
marking that would read as writing must be left out rather than rendered as
placeholder lettering.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the pushed-forward stack of chips and the card
caught mid-turn — the moment of changing gear — and to nothing else.

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

- **Real suits, numbers or court cards.** Plain geometric pips only.
- **A casino scene.** One table, some cards, three stacks, a pair of hands.
- **The pushed stack not reading as moved.** It must sit clearly ahead of the
  others.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2010-07-09-changing-test-gears --install ~/Downloads/<your-file>.jpg
```
