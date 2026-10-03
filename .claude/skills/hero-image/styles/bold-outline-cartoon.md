# Bold outline cartoon

The governance and compliance series look. Warm, friendly, a little wry —
deliberately at odds with the dryness of the subject, which is the joke.

## Style block

```text
Bold-outline vector cartoon illustration, in the style of a modern comic or
children's-book spread. Thick black outlines on every object, clean flat colour
fills with soft gradient shading, gentle highlights. Cheerful, warm and slightly
exaggerated, with friendly rounded shapes. Not photorealistic, not a 3D render,
not watercolour, not flat minimalist corporate vector art, not line art.
```

## Palette

```text
Warm, domestic palette: cream, golden brown, wood tones, soft reds, with a
single saturated accent colour used sparingly for the thing that matters most.
Backgrounds warm and slightly muted so foreground objects separate cleanly.
```

## Recurring characters

**The baker.** The series mascot, also used in `ExampleCallout` via
`ChefMascot.astro` (`astro/src/assets/chef-mascot.png`). Describe her as:

```text
A friendly cartoon baker: dark hair tied back, broad happy grin, white
double-breasted chef's jacket with black round buttons, red cuffs, red
neckerchief tied at the throat, white chef's hat. Warm bakery setting: wooden
shelves of bread loaves loosely blurred behind, copper mixing bowls, a light
stone countertop across the lower third.
```

She stands in for the first-line engineering team: the person operating the
control, not the person auditing it. Keep her cheerful and competent — the
series never makes her the butt of the joke.

**The cake or batch** is the artifact under control. **A green shield with a
white tick** is a passing evaluation; **a red shield with a white cross** is a
failing one. These map to the rendered evidence documents in the posts, so keep
them consistent.

## Reference images from the post

Take the *objects* and leave the rendering. A post's screenshots of a rendered
evidence document, a certificate or a form tell you what the baker should be
holding and roughly how it is laid out — the badge in the corner, the bands of
content, the proportions. Say explicitly that the attached image is a reference
for content and layout only and must be redrawn with thick outlines and flat
fills, or you will get a photorealistic document pasted into a cartoon.

## Works well for

Governance, compliance, controls, audit, policy-as-code, anything where a
concrete physical metaphor is already doing the explaining.

## Avoid

Hardware, build tooling and anything where the subject is genuinely a machine —
the cartoon warmth fights it. Use `technical-blueprint` instead.

## Used by

- `2026-10-02-attestations-and-evidence` — the baker presenting attestations,
  policy and evidence as three labelled groups on a counter.
- `2019-10-30-evidencing-source-code-reviews` — one document bearing two
  different wax seals, an author's and a signatory's. **The first use of this
  style without the baker**: the post is governance, but it predates the bakery
  series by seven years and borrowing her would imply a continuity that does not
  exist. The green shield with the tick still carries across. Omitting the
  recurring character is a legitimate choice when a post shares the subject
  matter but not the series.
