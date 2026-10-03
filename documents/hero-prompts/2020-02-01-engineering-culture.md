# Establishing an Engineering Culture — hero prompt

- **Post:** `astro/src/content/blog/2020-02-01-engineering-culture.mdx`
- **Style:** `flat-editorial`
- **Series:** standalone
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/2020-02-01-engineering-culture-hero.svg`
- **Video:** none

## Read this before installing

This post's hero is **also used inside the post body**. The `ImgTag` in the "Big
3 Levers" section points at `/images/heroes/2020-02-01-engineering-culture-hero.svg`
by path, the same file the frontmatter uses.

Installing a new hero writes `...-hero.jpg` and repoints the frontmatter only, so
the body keeps rendering the SVG and nothing breaks — but **do not delete the
SVG afterwards**, unlike the orphans left by the other prompts in this folder.
It is still the post's own diagram, and it explains Trust → Voice → Autonomy far
better in the body than a hero ever will.

## Why this image

The post supplies its own mechanical vocabulary and uses it throughout: "The Big
3 Levers", "Autonomy Fulcrums", "Trust Fulcrums". Levers on fulcrums, in that
order, is the author's metaphor and the rules say to use it rather than invent
one.

The order matters and is the argument: trust is the one you pull, voice is what
it raises, autonomy is what that in turn makes possible. Three levers in a
cascade says that in a single glance.

`flat-editorial` rather than `technical-blueprint`, despite levers being
machinery. This post is about fear, psychological safety and whether people feel
heard; blueprint explicitly has no warmth to spend on human subjects. The three
labels are plain words, not the "legible technical detail" flat-editorial warns
against.

The accent goes on the first lever, TRUST, because that is the one a leader
actually pulls — the post's whole practical claim is that the other two follow
from it.

## Reference images

None to attach. The post's only diagram is the SVG hero above, and SVGs cannot be
sent to the generator. Its arrangement — three stages reading left to right — is
written into the prompt instead.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about the three things that shape an engineering team's culture. Output a single
flat image, no borders, no frame, no watermark, no signature.

STYLE
Flat editorial illustration in a mid-century printed style, as though screen
printed in a small number of inks. Bold simplified geometric shapes, strong
silhouettes, minimal interior detail, no outlines or only occasional rough ones.
Visible paper grain and light halftone or misregistration texture. Figures
stylised and faceless or near-faceless. Confident and graphic. Not
photorealistic, not a 3D render, not a cartoon with thick outlines, not flat
corporate vector art with gradient blobs.

SUBJECT
THREE simple levers arranged in a row across the middle of the image, reading
left to right as one connected mechanism.

Each lever is drawn the same way: a straight beam resting on a solid triangular
fulcrum, tilted so one end is low and the other is raised.

They are linked in a rising cascade. The raised end of the FIRST lever presses
down on the low end of the SECOND. The raised end of the SECOND presses down on
the low end of the THIRD. Each fulcrum sits slightly higher than the one before,
so the whole row climbs gently from left to right.

At the far LEFT, a single stylised faceless figure stands with both hands on the
low end of the first lever, pushing down on it. This figure is the only person in
the image.

At the far RIGHT, balanced on the raised end of the third lever, a simple solid
shape rises clear of the ground — a plain circle or sphere, lifted free.

The reader should understand at a glance: one person pushes the first lever, and
the motion carries along the row until something is lifted at the end.

SUPPORTING DETAIL
Nothing else. No gears, no ropes, no pulleys, no buildings, no crowd.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Along the beam of the first lever: "TRUST"
  - Along the beam of the second lever: "VOICE"
  - Along the beam of the third lever: "AUTONOMY"
Everything else must be abstract placeholder lines, not legible lettering. No
labels on the figure, the fulcrums or the lifted shape.

COLOUR
Three or four inks only, printed on warm off-white paper: a deep ink (near-black
or dark teal), one mid tone, and one saturated accent (burnt orange or mustard).
Colours overlap and multiply where shapes cross. No photographic colour range.
The burnt orange accent belongs to the FIRST lever — the one marked "TRUST" —
and its fulcrum, and to nothing else. The other two levers, the figure and the
lifted shape stay in the deep ink and the mid tone, so the eye lands on the lever
being pushed.

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

- **The cascade coming back as three unconnected levers.** The linkage is the
  argument — trust produces voice produces autonomy. Three see-saws in a row
  side by side says nothing. This is the thing to check first.
- **The climb pushing the third lever out of the central band.** A row that rises
  left to right wants to escape the top of the frame, and the card crop will take
  "AUTONOMY" with it. Keep the rise gentle; check the card render.
- **"AUTONOMY" is the fragile string** at eight characters. "TRUST" and "VOICE"
  will be fine. If it will not come out, it is better to drop all three labels
  than to ship two correct ones and one mangled.
- **Text-free fallback:** the cascade and the single figure still read as cause
  and effect, though the image loses which lever is which.
