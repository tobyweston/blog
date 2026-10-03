---
name: hero-image
description: Write an image-generation prompt for a named blog post's hero image in one of the site's house styles, then wire the generated image into the post. Use when asked to create, generate, redo or restyle a hero image, hero banner, card image or social/OG image for a post in astro/src/content/blog.
---

# Hero images

Produces a prompt to paste into an external image generator (Gemini, Midjourney,
whatever is to hand), then installs the result. Claude writes the prompt, not the
image.

## Where the hero actually shows up

Check this before composing, because it drives the composition rules:

- **Post cards** on `/blog` and in `PreviewBlog` — rendered at `h-48`
  (192px tall) with `object-cover` across a two-column grid. Measured at a
  1440px viewport that is 546 x 192, so a 1600x900 hero is centre-cropped to
  about 2.8:1 and loses the top and bottom fifth.
- **Social and search previews** — `BlogPost.astro` passes `heroImage` to
  `SiteLayout` as the OG image and into the schema.org `image` field.
- **Not** as a banner at the top of the post. That markup is commented out in
  `astro/src/layouts/BlogPost.astro`.

So the hero is a thumbnail and a social card. It has to survive a hard centre
crop and still read at roughly 550x190. Fine detail and small text are wasted.

## Workflow

### 1. Resolve the post

Accept a slug, filename, title or path. Find it under
`astro/src/content/blog/`. If more than one matches, ask. If the post is in
`astro/src/content/unpublished/`, that's fine — treat it the same.

### 2. Check for a video first

If the post embeds a YouTube video (`<YouTubeEmbed youtubeId="..." />` in the
body, or `youtubeId` in frontmatter for the video collection), **prefer a
keyframe from that video over a generated image.** It is the real thing, it is
free, and a post whose centrepiece is a talk should show the talk.

```bash
.claude/skills/hero-image/scripts/generate_hero.py <slug> --keyframe
```

That pulls the largest keyframe YouTube holds, crops it to 1600x900 and wires it
in. Generate instead when the video is incidental to the post, or when the
keyframe is a title card or a face filling the frame — both read as nothing at
192px. Look at the card check before deciding.

### 3. Read the post and pull out the visual material

Read the whole post, not just the frontmatter. Extract:

- `title`, `subTitle`, `description`, `categories`, `keywords`
- the central argument in one sentence — the thing the image should make a
  reader curious about
- **three to six concrete nouns that can be drawn.** This is the part that
  matters. Abstractions ("governance", "trust", "latency") produce generic
  stock-art slop. Hunt for the physical objects the post already uses: a
  printed document, a train ticket, an oven, a shield, a filing cabinet, a
  conveyor belt. Most posts contain their own metaphor — use the author's,
  don't invent a new one.
- any recurring character or motif from earlier posts in the same series. If the
  post links to a previous post, read that post's `heroImage` and look at it, so
  the new one continues rather than resets.
- **the images the post already contains.** Look at every one of them before
  composing — its charts, diagrams, screenshots and photographs are the post's
  existing visual language, and the hero should look like it belongs to the same
  article rather than arriving from a stock library. Take the real shapes from
  them: the actual shape of a curve, the arrangement of a diagram, the objects
  in a photograph, the colours already in use.

  ```bash
  .claude/skills/hero-image/scripts/generate_hero.py <slug> --dry-run
  ```

  lists what the post has. Attach the two or three most useful to the generator
  with `--reference`, and name them in the prompt's `REFERENCE IMAGES` block so
  it is on record which ones shaped the result. A post with no images of its own
  simply skips this.

If the post is one of a series, say so in the prompt explicitly — continuity is
the main reason this skill exists.

### 4. Pick a style

Explicit instruction wins. Otherwise work down this table:

| The post | Style |
|---|---|
| **Reports figures it measured** — two or three headline numbers you can quote straight out of it | `data-infographic` |
| Categories contain `compliance`, `governance`, `controls-engineering`, `policy-as-code` | `bold-outline-cartoon` |
| Categories contain `raspberry-pi`, `debian`, `tooling`, `build`, `java`, `scala`, `rego` | `technical-blueprint` |
| Categories contain `culture`, `teams`, `process`, `metrics`, `opinion` | `flat-editorial` |

Check the first row before the category rows: it is about what the post contains,
not how it is filed, and it wins when it applies. A post categorised `metrics`
that argues about measurement is `flat-editorial`; one that reports what the
author actually measured is `data-infographic`.

If nothing fits cleanly, offer the four and ask. Never silently mix two styles —
the point is a consistent look across the site.

Read the chosen file in `styles/` and `reference/output-spec.md` before writing
anything.

### 5. Compose the prompt

Fill the skeleton below. Paste the style file's **Style block** and **Palette**
sections in verbatim — they are the shared part, and editing them per post is how
a house style drifts.

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a technical
blog post about <one-line subject>. Output a single flat image, no borders, no
frame, no watermark, no signature.

STYLE
<verbatim Style block from the chosen style file>

<RECURRING CHARACTER — only if the style defines one and the series uses it>

<REFERENCE IMAGES — only if images are attached. Name each one and say what to
take from it and what to ignore, e.g. "The attached bar chart is from the post
itself: match its proportions and its blue/amber pairing, but do not reproduce
its axes or labels." Always say what NOT to copy, or the generator will trace
the whole thing.>

SUBJECT
<the scene: one clear focal object or action, drawn from the concrete nouns.
Say what the reader should understand at a glance.>

<SUPPORTING DETAIL — one or two secondary elements, placed and described>

TEXT IN THE IMAGE
Use very little text, rendered large and spelled exactly as written. Do not
invent additional words or labels.
  - <exact string 1>
  - <exact string 2>
Everything else must be abstract placeholder lines, not legible lettering.

COLOUR
<verbatim Palette block from the chosen style file, plus one line saying which
element should be the highest-contrast focal point>

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

### 6. Hand it over

- Save the finished prompt to `documents/hero-prompts/<post-filename>.md`, with
  the post title, the chosen style and the date at the top. These are kept so a
  hero can be regenerated or restyled later without re-deriving it.
- Print the prompt in the reply inside a ```text fence so it can be copied.
- Name the previous post's hero file as a style reference to attach, if the post
  is part of a series.
- List the post's own images that should be attached, with the exact
  `--reference` invocation, so the generation can be repeated identically.
- Call out which parts are most likely to be mangled — any literal text — and
  what to drop if the generator fumbles it.

### 7. Wire the image in

```bash
export GEMINI_API_KEY=...    # once per shell; get one at https://aistudio.google.com/apikey
.claude/skills/hero-image/scripts/generate_hero.py <slug>
```

The script reads the prompt you just saved, calls the Gemini image API, and does
everything `reference/output-spec.md` asks for: 1600x900, under 400KB, written to
`astro/public/images/heroes/<slug>-hero.jpg`, `heroImage` set in the post's
frontmatter, `npx astro build` to confirm it resolves, and a card-crop render to
check. Useful flags:

| Flag | Why |
|---|---|
| `--keyframe [ID]` | Use the post's YouTube keyframe instead of generating |
| `--install FILE` | Install an image generated elsewhere — see the note below |
| `--reference [FILE...]` | Send images with the prompt; bare, it uses the post's own |
| `--variants 3` | Generate three candidates, install none, pick one yourself |
| `--model NAME` | Switch image model |
| `--dry-run` | Resolve post and prompt, stop before spending anything |
| `--no-build` | Skip the astro build |

**The API needs billing enabled.** Every Gemini image model is capped at zero on
the free tier — a key without billing answers `429 ... limit: 0` for all four,
and a Gemini app subscription is a different product that does not grant API
access. Without billing, generate in the Gemini app as before and hand the file
to the script, which still does every other step:

```bash
.claude/skills/hero-image/scripts/generate_hero.py <slug> --install ~/Downloads/<file>.jpg
```

**Always look at the card check it prints.** If the focal subject is clipped,
the prompt's composition section needs tightening — don't fix it by re-cropping.

Doing it by hand instead: follow `reference/output-spec.md`, which carries the
same steps as `magick` invocations.

## Rules that apply to every prompt

**Keep literal text to three strings at most.** Image models mangle lettering.
Anything longer than two or three words should be specified as abstract
placeholder lines. Always state the exact spelling of the strings you do ask for,
and always offer a text-free fallback.

`data-infographic` is the one exception — it is built out of labelled numbers and
needs six to eight strings. Its style file sets out what it does to earn that,
and the exception applies to that style only.

**One focal idea.** A hero that tries to illustrate the whole argument reads as
clutter at 192px. Pick the single image the post turns on.

`data-infographic` reads as the exception and isn't: its two or three stat cards
are one idea — the finding — stated in parts, on a strict grid that keeps them
legible. Three *unrelated* ideas are clutter in any style, that one included.

**Use the post's own metaphor.** If the author compared something to a bakery,
a train ticket or CCTV, that is the image. Don't substitute a better one.

**No UI screenshots, no code walls, no floating holographic dashboards.** They
date badly and read as nothing at thumbnail size. A `data-infographic` hero is
not an exception to this: it is flat type and pictograms on a plain ground, with
no window chrome, no perspective and no invented charts.

**State the negatives.** Every prompt should say what the style is *not*
(not photorealistic, not 3D render, and so on) — the style files carry this.

**Reach for the technology the post is actually about.** If a post names a
language, product or tool — Scala, Java, Debian, Log4j, a Raspberry Pi — work its
mark or its idioms into the image rather than drawing a generic computer. It
anchors the hero to the subject at a glance, which is most of the job at 192px.

Prefer an idiom to a logo. Image models reliably draw a *glyph* and reliably
mangle a *logo*, and a mangled trademark looks worse than none:

| Reliable | Risky |
|---|---|
| A single large glyph: `=>`, `λ`, `;`, `#!`, `{}` | An accurate corporate wordmark |
| The mark described as shapes and colours — "a red-to-orange double spiral", "a raspberry in outline", "a red swirl" | "the Scala logo", "the Debian logo" |
| The product's colours applied to an object already in the scene | Small lettering anywhere |

So: name the mark by its **shape and palette**, keep it to one secondary element
away from the focal point, and ask for it **redrawn in the chosen house style** —
a photoreal logo dropped into a blueprint or a cartoon wrecks both. Count any
mark against the three-string text budget.

Always give a fallback line for when it comes back wrong: the image has to work
with the mark removed. If the generator fumbles it twice, drop it — a clean hero
beats a recognisable-but-wrong trademark.

Using a product's mark to illustrate a post about that product is ordinary
editorial use. Don't imply endorsement, don't rework a mark into a joke, and
don't put a company's mark on something the post is criticising.

**Favour a real keyframe over a drawing.** See step 2 — if the post has a video,
that footage is more honest than anything a generator will produce.
