# Pair Tests: What Candidates Can Expect — hero prompt

- **Post:** `astro/src/content/blog/2012-07-04-pair-tests-what-candidates-can-expect.md`
- **Style:** `flat-editorial`
- **Written:** 2026-10-03
- **Replaces:** nothing bespoke — this post has no hero of its own today
- **Video:** none

## Why this image

The companion to `2015-09-25-pair-tests-dont-work`, written three years earlier
and from the other side: not whether the exercise works, but what to expect if
you are the one being tested.

So it reuses that hero's staged platform deliberately — but where the later post
views it from outside, small against a large real workplace, this one is up on
the platform with the candidate. Same stage, different seat.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about what a pair programming interview is actually like from the candidate's side. Output a single flat image, no borders, no frame, no watermark,
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
A raised platform occupying most of the image, viewed close and from slightly
above, so the viewer is on it rather than looking at it from a distance.

On the platform, TWO stylised faceless figures sit side by side at one small
desk, close together. Between them sits ONE keyboard, and both of them have a
hand resting on it — the sharing must be unmistakable.

At the very edge of the platform, cropped by the frame, the shoulders and backs
of TWO further figures standing and watching. They are partial, at the margin,
and clearly not part of the pair.

Nothing exists beyond the platform's edge — the background is plain paper.

SUPPORTING DETAIL
Nothing else. No screen content, no clock, no clipboard.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, terminal
output, version numbers or filenames. Any marking that would read as writing must
be left out rather than rendered as placeholder lettering, and nothing in the
image may be numbered or named.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the platform itself, as in the companion
image, and to nothing else. All four figures, the desk and the keyboard stay in
the deep ink and the mid tone.

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

- **The two seated figures not sharing the keyboard.** One keyboard, two hands.
  That is the whole subject.
- **The watchers taking up space.** They are cropped at the margin.
- **A wide view of the room.** The later post owns that composition; this one is
  close in.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-07-04-pair-tests-what-candidates-can-expect --install ~/Downloads/<your-file>.jpg
```
