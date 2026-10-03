# Java source on Mac — hero prompt

- **Post:** `astro/src/content/blog/2011-10-29-java-source-on-mac.md`
- **Style:** `technical-blueprint`
- **Series:** standalone
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/mac-tools.jpg`, which does not exist
- **Video:** none, so this is generated rather than a keyframe

## Why this image

The post is a recipe for attaching JDK source in an IDE, and the thing it
actually turns on is `ln -s` — two symlinks, one to `src.jar` and one to
`docs.jar`. So the image is the link itself: an archive, two labelled canisters,
and the links drawn as real couplings rather than arrows.

For the technology mark it takes the idiom rather than the logo, per the skill's
rule: Java's steaming cup, which also lands the post's own closing joke, "Have a
cup of tea." A plain mug of steam is the one warm thing in a cold blueprint, so
it carries the amber accent.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about linking Java source and documentation archives into a developer's
toolchain. Output a single flat image, no borders, no frame, no watermark, no
signature.

STYLE
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.

SUBJECT
An isometric scene running left to right across the middle of the image:

  - On the LEFT, a heavy closed cabinet or vault drawn in isometric projection,
    with a thick hinged door standing slightly ajar. This is an archive. Its
    front face is plain — no text on it.
  - In the CENTRE, TWO cylindrical canisters sitting side by side on a low
    plinth, like sealed sample jars with bolted lids and a band around the
    middle. They are identical in shape and clearly a matching pair.
  - Running from the cabinet to each canister, TWO separate rigid link rods,
    each ending in a small bolted collar clamped onto the canister. Draw these
    as real mechanical couplings, not as arrows. The two rods are the focus of
    the image: they are what connects the archive to the pair of canisters.

The reader should understand at a glance: something sealed has been linked to
something that can now be opened and read.

SUPPORTING DETAIL
On the RIGHT, standing on the same surface, a simple wide mug seen in
three-quarter view with three curling wisps of steam rising from it. Drawn in
the same clean line style as everything else, slightly smaller than the
canisters. It is the only warm object in the picture.

A few faint callout leader lines point at the two link rods and at the cabinet
door, ending in small empty circles with no text in them.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Across the band of the left-hand canister: "src.jar"
  - Across the band of the right-hand canister: "docs.jar"
Everything else must be abstract placeholder lines, not legible lettering. The
callout circles stay empty. No text on the cabinet, the mug or the link rods.

COLOUR
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
The amber accent belongs to the mug and its steam, and to the bolted collars
where the two link rods clamp on — nothing else. Keep the cabinet and the
canisters in navy and slate so those warm points are what the eye lands on.

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

- **`src.jar` and `docs.jar` are the fragile part.** Both contain a full stop,
  which models often drop or turn into a comma, and they are the smallest text
  in the frame. Check the spelling before installing. If either comes back
  wrong, ask for "SRC" and "DOCS" in capitals instead — shorter and far more
  reliable — and if that fumbles too, drop the text entirely: the paired
  canisters and the two link rods carry the idea without labels.
- **The mug may drift towards a logo.** It is deliberately described as a plain
  mug with steam, not as any product's mark. If it comes back looking like a
  trademark, regenerate — the skill's rule is that a mangled mark is worse than
  none.
- **Arrows instead of couplings.** Generators like turning "link" into an arrow.
  The prompt says rigid rods with bolted collars twice for that reason; if it
  still produces arrows, it is worth one regeneration, because arrows make it
  look like a generic data-flow diagram.
- **Text-free fallback:** drop the TEXT IN THE IMAGE section. The archive, the
  matched pair and the two couplings survive on their own.
