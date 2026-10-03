# Easily Deploy Java to Debian — hero prompt

- **Post:** `astro/src/content/blog/2019-09-02-deploy-java-to-debian.md`
- **Style:** `technical-blueprint`
- **Series:** `Deploying to Debian` (first of two), declared in both posts'
  frontmatter. Both carry the Debian swirl — see the Recurring motif section of
  the style file.
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-devops.jpg`, also used by
  `2014-01-01-another-teamcity-build-monitor`, which keeps it. Nothing is
  orphaned.
- **Video:** none

## Why this image

The post does one thing: take a built Java, Scala or Kotlin application and wrap
it as a `.deb` with `sbt-native-packager`. The image is that wrapping — loose
parts going into one sealed crate — and the crate carries the swirl, because the
package format is what the post is about.

The second post in the series publishes a repository full of these crates, so
this one shows exactly one, being closed.

## Two marks, one accent

The cup marks what goes in; the swirl marks where it lands. That is the post in
one picture — a Java application becoming a Debian package — and it is why only
one of the two is warm.

## The swirl takes the accent

Unlike the raspberry series, where the berry is a small corner mark in the line
colour, the swirl here sits centrally and holds the warm accent. That does not
break the one-accent rule: in both these posts the swirl is stamped on the very
thing the post is about, so marking the brand and marking the subject are the
same act.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about packaging a Java application as a Debian package. Output a single flat image, no borders, no frame, no
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
A single sturdy shipping crate drawn in isometric projection, centred in the
image and large enough to dominate it. Its lid is open and tilted back.

Floating above the open crate, as in an exploded diagram, THREE simple objects
descending into it in a line: a cylindrical canister drawn largest and nearest
the crate's mouth, a flat rectangular plate, and a small folded sheet. Dashed construction lines run from each down into the
crate, showing them being packed.

The crate's front face is clean and unobstructed, because the swirl is stamped
across it.

BRAND MARKS
Two marks appear in this image, on different objects.

On the face of the cylindrical canister, a Java mark: a plain cup seen from the
side with three short curling wisps of steam rising from it, drawn as one simple
flat silhouette in the line colour. No saucer, no handle detail, no text beside
it, and no circle or roundel around it.

Stamped across the centre of the main object, a Debian swirl mark: a single
tapering spiral stroke, broad where it begins at the upper right and narrowing
smoothly to a fine point as it coils inward and down, like a curl of smoke. One
unbroken stroke, no outline around it, no text beside it, drawn flat as a mark
stencilled onto the surface rather than a sticker or a rendered logo.

SUPPORTING DETAIL
Two faint callout leader lines point at the crate's lid hinge and at one of the
descending objects, ending in small empty circles. No conveyor, no forklift, no
warehouse.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - On the front face of the crate, beneath the swirl: ".deb"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text beside the swirl, and no code, terminal
output or filenames anywhere in the image.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the swirl stamped on the crate's front face, and to
nothing else. The crate, the lid, all three descending objects and the Java cup
mark on the canister stay navy and slate, so the swirl is the highest-contrast
thing in the image.

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

- **`.deb` and its leading dot.** The dot is the fragile part — it gets dropped,
  doubled or turned into a comma. If it will not come out, "DEB" in capitals is
  a clean fallback and still reads.
- **A warehouse appearing.** One crate, three objects, nothing else. Forklifts
  and shelving belong to the companion post, not this one.
- **The swirl drawn as a circular badge.** It is one tapering stroke, not a roundel
  and not a logo in a ring. If it arrives inside a circle, regenerate.
- **The cup competing with the swirl.** Two marks in one image is one more than
  these prompts usually risk. The cup stays small, cool and on the canister; if
  it comes back warm, large, or stamped on the crate alongside the swirl, the
  image loses its direction of travel. Regenerate rather than accept it.
- **A steaming cup turning into a coffee scene.** No saucer, no table, no beans.
  It is a flat mark on the side of a canister.
- **The swirl drifting out of the centre.** It is deliberately central here, not
  tucked in a corner, and the card crop keeps the middle band — so a swirl placed
  high or low may vanish from the card entirely while looking fine in the full
  image. Check the card render.

## Install

```bash
cd /Users/toby/dev/code/github/active/blog && .claude/skills/hero-image/scripts/generate_hero.py 2019-09-02-deploy-java-to-debian --install ~/Downloads/<your-file>.jpg
```
