# Evidencing Source Code Reviews — hero prompt

- **Post:** `astro/src/content/blog/2019-10-30-evidencing-source-code-reviews.md`
- **Style:** `bold-outline-cartoon`, **without the baker**
- **Series:** standalone — see the note below
- **Written:** 2026-10-03
- **Replaces:** `/images/heroes/multiple-usages-security.jpg`, shared with several
  other posts, which keep it. Nothing is orphaned.
- **Video:** none

## Why this style, and why no baker

The post is filed `agile` but it is a governance piece: the MAS regulator, the
TRM guidelines, and how to prove a code review happened without drowning in
paperwork. That is squarely `bold-outline-cartoon`'s territory — compliance and
audit, with the warm look deliberately at odds with the dryness of the subject.

**The baker is deliberately left out.** She belongs to the 2026 bakery series,
and putting her on a 2019 post about GPG keys would imply a continuity that does
not exist. The style's recurring-character block is optional and this is a case
for omitting it — but keep the green shield with a white tick, which the style
defines as a passing evaluation and which carries across posts.

## Why this image

The post's trick is that a Git commit can carry two different people's marks: an
*author*, and a *signatory* who is provably someone else. "Cryptographically
provable that two developers worked on the code."

So the hero is one document bearing two different seals. Not a screen, not a
terminal — the post is about producing something you can hand to a regulator, and
a sealed document is what that looks like.

The accent goes on the second seal, the signatory's, because the entire argument
rests on it differing from the first.

Worth knowing when judging the result: the post concludes the technique *doesn't*
work, because rebasing overwrites signatures. The hero deliberately shows the
idea rather than its failure — one focal idea, and a hero illustrating a caveat
would be unreadable at 192px.

## Reference images

None. The post's only figures are terminal transcripts of `git log` output, and
the standing rule forbids drawing code or screens — they render as grey mush on a
card. Do not attach them.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
about proving that two different developers worked on the same piece of code.
Output a single flat image, no borders, no frame, no watermark, no signature.

STYLE
Bold-outline vector cartoon illustration, in the style of a modern comic or
children's-book spread. Thick black outlines on every object, clean flat colour
fills with soft gradient shading, gentle highlights. Cheerful, warm and slightly
exaggerated, with friendly rounded shapes. Not photorealistic, not a 3D render,
not watercolour, not flat minimalist corporate vector art, not line art.

SUBJECT
One large printed document lying on a wooden desk, tilted towards the viewer so
its face fills the middle of the image and is clearly readable as a document. It
is a clean cream page carrying a few bands of grey placeholder lines, suggesting
printed content without any real words.

Along the BOTTOM edge of that document, side by side, TWO round wax seals pressed
into the page. They are obviously made by different stamps:

  - The LEFT seal is plain, with a simple ring border and a smooth centre.
  - The RIGHT seal is distinctly different: a notched, cog-like outer edge, and a
    small closed padlock shape pressed into its centre.

Both seals are the same size and sit at the same height, so they read as a
matching pair of signatures on one page rather than one seal and a decoration.

In the TOP-RIGHT corner of the document, a bright green shield badge with a white
tick in it.

SUPPORTING DETAIL
Resting on the desk beside the document, one old-fashioned brass stamp or seal
press, lying on its side, its handle towards the viewer. Nothing else on the desk.

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - Beneath the left seal: "AUTHOR"
  - Beneath the right seal: "SIGNER"
Everything else must be abstract placeholder lines, not legible lettering. No
text on the shield badge, just a white tick. No text on the seals themselves, no
code, no terminal output and no filenames anywhere in the image.

COLOUR
Warm, domestic palette: cream, golden brown, wood tones, soft reds, with a
single saturated accent colour used sparingly for the thing that matters most.
Backgrounds warm and slightly muted so foreground objects separate cleanly.
The saturated accent belongs to the RIGHT seal — the notched one with the
padlock — so that the second signature is the highest-contrast thing on the page.
The left seal stays a muted wax red. The green shield keeps its own green.

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

- **The two seals coming back identical.** Their difference is the entire point —
  two different people signed one page. If they match, the image says the
  opposite. Check this first.
- **The seals sitting in the bottom fifth**, which the card crop removes. A
  document's seals naturally belong at its foot, and that is exactly the band
  that disappears. If the card render loses them, raise the whole document rather
  than re-cropping.
- **"AUTHOR" and "SIGNER" are low-risk** — short, uppercase, no punctuation — but
  check they are not swapped, and that the generator has not expanded "SIGNER"
  into "SIGNATORY" or "SIGNED BY".
- **No baker.** If a chef or any mascot appears, regenerate. This post is not part
  of that series.
- **Text-free fallback:** drop the two labels. Two visibly different seals on one
  page still reads as two signatories, and the padlock carries the cryptographic
  sense on its own.
