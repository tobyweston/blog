# Output spec

Facts about this site. Verify rather than assume if the layout has changed.

## Size and format

- **1600 x 900** (16:9). Matches the most recent heroes; older stock images in
  `public/images/heroes/` vary (1200x800, 1920x1080) and are not the standard.
- **JPEG** for illustrations and photographs. PNG only where the image has flat
  areas and hard edges that JPEG artefacts would spoil. SVG is supported
  (`trust-voice-autonomy.svg`) but generators don't produce usable SVG.
- **Under ~400KB.** The attestations hero is 319KB. `bank-on-tech.jpg` is 3MB,
  which is a mistake, not a precedent.

## Naming and location

```
astro/public/images/heroes/<post-filename-without-extension>-hero.jpg
```

For example `2026-10-02-attestations-and-evidence.mdx` →
`2026-10-02-attestations-and-evidence-hero.jpg`.

Older posts share generic stock heroes (`java-code.jpg`, `agile.jpg`) — reuse
those for incidental posts rather than generating something bespoke.

## Frontmatter

`heroImage` is an optional string in `astro/src/content.config.ts`, a path from
the site root:

```yaml
heroImage: "/images/heroes/2026-10-02-attestations-and-evidence-hero.jpg"
```

Place it after `pubDate`, matching the other posts.

## Installing a generated image

```bash
# from the repo root
sips -g pixelWidth -g pixelHeight ~/Downloads/<generated>.jpg
```

If it isn't 1600x900, resize and crop centrally rather than squashing:

```bash
magick ~/Downloads/<generated>.jpg -resize 1600x900^ -gravity center \
  -extent 1600x900 -quality 86 \
  astro/public/images/heroes/<slug>-hero.jpg
```

Then add `heroImage` to the frontmatter and confirm the build resolves it:

```bash
cd astro && npx astro build
```

## Checking the crop

Cards render the hero at `h-48` with `object-cover`. Measured at a 1440px
viewport the card image is 546 x 192, about 2.8:1, so only the middle 63% of a
1600x900 hero is visible — the top and bottom fifth are cropped away. On mobile
the grid is one column and the crop is far gentler, so desktop is the case to
check. Before calling it done:

```bash
magick astro/public/images/heroes/<slug>-hero.jpg \
  -gravity center -crop 1600x563+0+0 +repage -resize 546x /tmp/card-check.png
```

Look at `/tmp/card-check.png`. If the focal object is clipped or unreadable,
the prompt's composition section needs tightening, not the image cropping.

## Alt text

The hero is decorative on cards but is also the social preview, so give it a
descriptive `alt` if it is ever rendered inline. The in-post hero markup in
`astro/src/layouts/BlogPost.astro` is currently commented out.
