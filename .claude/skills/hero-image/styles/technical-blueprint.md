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

**The Scala mark.** The `scala` posts carry it. Paste verbatim:

```text
In the lower-left corner of the image, clear of the main subject, a Scala mark: a
compact emblem of two parallel curved bands sweeping up to the right and curling
back on themselves, like a flattened spiral staircase seen from the side. Drawn
in a strong crimson red, flat, with no outline, no circle or roundel around it
and no text beside it.
```

This mark is the one place a fifth colour enters the palette. It is always
crimson, because that red is the mark's identity and a navy Scala emblem reads as
a mistake — but it is kept small and parked in a corner, while the amber accent
stays on whatever the post is about and is always the larger warm shape. Two warm
hues at very different sizes and distances do not compete; two at similar sizes
would, so do not let the mark grow.

**The Debian swirl.** The `Deploying to Debian` series carries the swirl, and
unlike the berry it sits centrally and takes the accent. Paste verbatim:

```text
Stamped across the centre of the main object, a Debian swirl mark: a single
tapering spiral stroke, broad where it begins at the upper right and narrowing
smoothly to a fine point as it coils inward and down, like a curl of smoke. One
unbroken stroke, no outline around it, no text beside it, drawn flat as a mark
stencilled onto the surface rather than a sticker or a rendered logo.
```

**The Java cup.** Where a post is about moving Java somewhere, the cup marks the
thing being moved. Paste verbatim, adapting only which object carries it:

```text
On the face of the cylindrical canister, a Java mark: a plain cup seen from the
side with three short curling wisps of steam rising from it, drawn as one simple
flat silhouette in the line colour. No saucer, no handle detail, no text beside
it, and no circle or roundel around it.
```

It stays in the line colour. When it shares an image with the swirl, the cup
marks what goes in and the swirl marks where it lands, so only one of them is
warm.

The two motifs are deliberately opposite, and the contrast is the point:

| | Raspberry | Debian swirl |
|---|---|---|
| Placement | small, lower-right corner | large, centre of the main object |
| Colour | line colour, never the accent | takes the warm accent |
| Role | a maker's mark saying whose board this is | the subject's own identity |

The swirl can hold the accent without breaking the palette rule because in both
of those posts it is stamped on the very thing the post is about — the package,
the repository — so marking the brand and marking the subject are the same act.
Do not copy that licence to a post where the mark sits on something incidental.

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
- The `scala` posts, seven of them, all carrying the crimson mark in the
  lower-left: exception handling (a two-way sorting chute), mixins (sleeves
  sliding onto a shaft, deliberately not a tree), the learning curve (a ramp
  steep then shallow, drawn from the post's own chart), the JMock/Scalamock
  cheat sheet (a conversion plate of matched fittings), implicit parameters and
  implicit functions (the same machine and spare-parts rack in both, a plug
  arriving by itself and then an adapter doing the same), and type classes
  (three unrelated shapes wearing clip-on collars that present an identical
  fitting, with nothing above them).
- The `Deploying to Debian` series, two posts, both carrying the swirl centrally
  and in the accent: `2019-09-02-deploy-java-to-debian` (loose parts descending
  into one crate, the canister marked with the Java cup and the crate stamped
  with the swirl, so the image reads Java going into Debian) and
  `2019-09-03-create-debian-repositories` (a rack of the same crates, sealed and
  feeding out through a pipe). The crates are drawn alike on purpose so the pair
  read as before and after.
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
