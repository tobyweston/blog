# Force IE8 to Display JSON — hero prompt

- **Post:** `astro/src/content/blog/2012-02-21-jersey-and-ie8.md`
- **Style:** `technical-blueprint`
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

IE8 gets a mime type it does not expect and offers the response as a file to save
instead of displaying it. The fix is to declare the right content type.

So the image is a sorting gate reading a label on an arriving parcel and sending
it down the wrong chute — into a storage bin rather than on to the viewing
window. One label, two destinations.

## The logo is composited, not drawn

The real mark goes in from `documents/brand/internet-explorer.png` after generation, unmodified.
The prompt reserves the right of the frame as composition rather than as a boxed
area — asking these models to "leave a clear rectangle" makes them draw one.

```bash
H=astro/public/images/heroes/2012-02-21-jersey-and-ie8-hero.jpg
magick $H \( documents/brand/internet-explorer.png -resize x170 \) \
  -gravity east -geometry +120-20 -composite -quality 86 $H
```

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about a browser downloading a response instead of showing it. Output a single flat image, no borders, no frame, no watermark,
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
A sorting gate drawn in isometric projection: a short belt arriving from the LEFT
carrying one flat parcel, meeting a pivoting diverter.

Beyond the diverter, TWO destinations. Straight ahead sits an open viewing frame
— an empty rectangular aperture on a stand, plainly where the parcel should go.
Branching down and away sits a closed storage bin with a hinged lid.

The diverter is thrown towards the BIN, and the parcel is already travelling that
way, past the turning for the viewing frame. The viewing frame stands empty.

On the leading face of the parcel, a small blank plate is fixed — a label holder
with nothing written on it.

MARGINS
The entire composition must fit within the LEFT 72% of the image width. The
rightmost 28% is empty background — nothing whatsoever extends into it: no
object, no callout line, no shadow and no marking. The background there is the
same plain ground and grid as everywhere else, with no panel, box, border, frame
or change of tone to indicate it.
Do not draw any logo, badge, emblem, roundel or icon anywhere in this image.

SUPPORTING DETAIL
One faint callout leader line points at the blank label plate on the parcel,
ending in a small empty circle.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons,
terminal output, version numbers, brand names or filenames. Nothing may be
numbered or named, and any marking that would read as writing must be left out
rather than rendered as placeholder lettering.

COLOUR
Restrained and COOL: the ground is a pale blue-grey, definitely cool in cast —
not cream, not sand. Deep navy and slate line work, with one warm accent (amber
or rust) used sparingly for the single component the post is about. No gradients
beyond flat tonal steps.
The amber accent belongs to the blank label plate and the pivoting diverter it
has set the wrong way, and to nothing else.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep the focal subject inside that central band; the top 20%
and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2012-02-21-jersey-and-ie8 --install ~/Downloads/<your-file>.jpg
```
