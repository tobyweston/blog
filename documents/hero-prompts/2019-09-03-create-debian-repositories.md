# Creating Debian Repositories — hero prompt

- **Post:** `astro/src/content/blog/2019-09-03-create-debian-repositories.md`
- **Style:** `technical-blueprint`
- **Series:** `Deploying to Debian` (second of two), declared in both posts'
  frontmatter. Both carry the Debian swirl — see the Recurring motif section of
  the style file.
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-devops.jpg`, also used by
  `2014-01-01-another-teamcity-build-monitor`, which keeps it. Nothing is
  orphaned.
- **Video:** none

## Why this image

Where the previous post makes one package, this one builds the place those
packages live: an `aptly` repository, cryptographically signed, served over HTTP
so `apt` can reach it.

So the image is the companion to that one — many crates rather than one, held in
a structure, with a seal on it. The signing matters enough to the post to earn
the one supporting detail: "Archives should also be cryptographically signed to
prove that the software was published by who they say they were."

The swirl moves from the crate to the structure itself, which is what makes the
two cards read as a before and after.

## The swirl takes the accent

Unlike the raspberry series, where the berry is a small corner mark in the line
colour, the swirl here sits centrally and holds the warm accent. That does not
break the one-accent rule: in both these posts the swirl is stamped on the very
thing the post is about, so marking the brand and marking the subject are the
same act.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about publishing your own signed Debian package repository. Output a single flat image, no borders, no frame, no
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
A tall open shelving rack drawn in isometric projection, centred in the image,
holding NINE identical small crates in three rows of three. The crates are the
same shape as the single large crate in the companion image, drawn small here.

The rack's solid side panel faces the viewer at an angle and is clean and
unobstructed, because the swirl is stamped across it.

Running from the right-hand edge of the rack, a single pipe or duct curves away
to the RIGHT and ends at a plain open flange at the edge of the image, as though
feeding something out. One small crate sits inside the mouth of that pipe, part
way along, in transit.

BRAND MARK
Stamped across the centre of the main object, a Debian swirl mark: a single
tapering spiral stroke, broad where it begins at the upper right and narrowing
smoothly to a fine point as it coils inward and down, like a curl of smoke. One
unbroken stroke, no outline around it, no text beside it, drawn flat as a mark
stencilled onto the surface rather than a sticker or a rendered logo.

SUPPORTING DETAIL
Fixed to the front of the rack, a round seal the size of one crate face: a plain
disc with a notched edge and a small closed padlock shape pressed into its
centre. One faint callout leader line points at it, ending in a small empty
circle.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beside the open flange at the right: "apt"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the swirl, and no code, terminal
output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the swirl stamped on the rack's side panel, and to
nothing else — not the seal, not the pipe, not the crate in transit. The rack,
all nine crates, the pipe and the padlock seal stay navy and slate.

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

- **Nine crates is a texture, not an inventory.** Any number that reads as "a
  shelf full" is fine. Do not regenerate over a miscount.
- **"apt" is lowercase and must stay lowercase** — it is a command name.
  Generators capitalise short strings by habit. This is the one to check.
- **The seal stealing the accent.** The swirl holds it; the padlock seal stays
  cool. If the seal comes back warm the image has two focal points and neither
  wins at card size.
- **The pipe reading as plumbing.** It is a delivery route. If it sprouts valves
  and joints it stops meaning distribution.
- **Losing the family resemblance.** These crates must look like the one in the
  companion post. If they come back as boxes, barrels or parcels, the pair stop
  reading as a series.
- **The swirl drifting out of the centre.** It is deliberately central here, not
  tucked in a corner, and the card crop keeps the middle band — so a swirl placed
  high or low may vanish from the card entirely while looking fine in the full
  image. Check the card render.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2019-09-03-create-debian-repositories --install ~/Downloads/<your-file>.jpg
```
