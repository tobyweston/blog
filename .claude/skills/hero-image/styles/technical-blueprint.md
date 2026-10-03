# Technical blueprint

For posts where the subject really is a machine, a pipeline or a piece of
tooling. Precise and diagrammatic rather than warm. Reads as "someone drew this
on purpose" rather than as decoration.

## Style block

```text
Clean technical illustration in the manner of an exploded isometric diagram or
a draughtsman's blueprint. Crisp uniform-weight line work, restrained flat fills,
subtle paper or grid texture in the background. Objects drawn in isometric or
three-quarter projection with visible construction lines and small callout
leaders pointing at components. Precise and deliberate, not sketchy. Not
photorealistic, not a 3D render, not a cartoon, not a glossy marketing render,
no glowing neon or holographic effects.
```

## Palette

```text
Restrained and cool: off-white or pale blue-grey ground, deep navy and slate
line work, with one warm accent (amber or rust) reserved for the single
component the post is about. No gradients beyond flat tonal steps.
```

## Recurring motif

**The raspberry.** Every post in the `raspberry-pi` series carries the berry, so
the cards read as a set on the index. Paste this block verbatim, the same way as
the Style block — describing the mark by its shape rather than naming the logo is
what keeps a generator from mangling a trademark:

```text
In the lower-right corner of the board, a small raspberry emblem etched into the
silkscreen: a cluster of seven or eight rounded drupelets packed into a rough
heart shape, with two pointed leaves angled up from the top. Drawn flat in the
same uniform line weight as the rest of the illustration, as a mark etched on the
board rather than a sticker, a badge or a photograph. No text beside it.
```

Keep it small and keep it in a corner. It is a maker's mark identifying whose
board this is, not the subject of any of these posts, and it must never take the
amber accent — that belongs to whatever the individual post is about.

## Reference images from the post

The most useful attachments for this style are the post's own diagrams and
photographs of hardware: they tell you the real arrangement of the thing, which
is exactly what an isometric drawing has to get right. Attach the photograph of
the actual board, rig or wiring and ask for its true layout and proportions,
redrawn as line work. Say clearly that colours, textures and backgrounds from
the photograph must be dropped in favour of the palette below.

## Works well for

Build and packaging tooling, pipelines, hardware and Raspberry Pi projects,
language and runtime internals, anything with a real structure worth showing.

## Avoid

Human subjects and anything emotional — the style has no warmth to spend on
them. Also avoid it when the post has no actual mechanism to draw; an isometric
diagram of an abstraction is just noise with nice lines.

## Used by

- `2012-04-03-scala-as-a-functional-oo-hybrid` — one isometric machine built from
  two kinds of part: nested solid blocks on the left for OO, a chain of inline
  units on the right for functional, joined by an amber flanged coupling. An
  inset study shows a sub-assembly equalling a single plain block, which is
  referential transparency drawn literally.
- The `raspberry-pi` series, six posts, all carrying the berry per the Recurring
  motif above: `2015-12-28-pi-console-lead` (jumper wires on two named GPIO
  pins), `2016-01-06-disable-led-for-edimax` (a cutaway dongle, one amber LED),
  `2017-03-01-standard-pi-setup` (an SD card entering the slot beside a
  struck-through monitor), `2017-10-26-upgrade-raspian-jessie-to-stretch` and
  `2019-08-29-upgrade-raspian-stretch-to-buster` (bolted name plates being
  swapped — the second shows three plates rather than two so the pair are
  distinguishable on the index), and
  `2016-03-23-homebrew-temperature-logger` (a probe on a lead).
- `2023-01-01-naming-things-impl` — two interchangeable modules for one socket,
  one with visible compartments labelled "ArrayStack" and one a featureless blank
  labelled "Impl". Note the accent marks the blank module: here the component the
  post is about is the habit it argues against.
