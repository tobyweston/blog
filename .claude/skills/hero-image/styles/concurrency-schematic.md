# Concurrency schematic

For the concurrency, threading and tempus-fugit posts. Mechanically it is a close
relative of `technical-blueprint` — same crisp isometric line work — but it reads
as a separate family on the index, because the ground, the accent and the corner
mark are all different.

The point of the separation: these posts are a long-running thread through the
blog, written over several years around one library, and they should look like a
set you can pick out at a glance.

## Style block

```text
Clean technical schematic in the manner of a timing diagram crossed with an
exploded isometric drawing. Crisp uniform-weight line work in a deep charcoal
ink, restrained flat fills, drawn on a warm pale sand-coloured ground carrying a
faint regular pattern of fine vertical rules, like timing gridlines. Objects in
isometric or three-quarter projection with visible construction lines and small
callout leaders ending in empty circles. Precise and deliberate, not sketchy.
Not photorealistic, not a 3D render, not a cartoon, not a glossy marketing
render, no glowing neon or holographic effects.
```

## Palette

```text
Warm pale sand ground throughout, with its faint vertical timing rules a shade
deeper. Deep charcoal ink for all line work and a mid warm grey for flat fills.
One strong teal accent, reserved for the single component the post is about —
teal against sand is what separates this family from the blue-and-amber
blueprint at thumbnail size. No other colour.
```

## Recurring motif: the hourglass

Every post in this family carries it, in place of any language logo. It is the
temporal idiom the series is named for — *tempus fugit*, time flies — and an
hourglass is the one shape for time that still reads as itself at 192px, where a
clock face is just a grey circle. Paste
verbatim:

```text
On the LEFT of the image, clear of the main subject, a small hourglass: two
rounded glass bulbs meeting at a narrow waist, held in a slim frame of two end
plates joined by three slender posts. A fine stream of sand falls from the upper
bulb into a small conical heap in the lower one. Drawn flat in the same charcoal
line work as the rest, no colour fill, no text beside it.
Position it so the whole hourglass, base included, sits above the lower third of
the image. It must not touch any edge and must not sit in the bottom fifth.
```

It stays in the line colour and never takes the teal — the accent belongs to
whatever the individual post is about.

## Interleaving

Where a post is about two things running through one another, draw it as a
two-strand braid: two lines crossing over and under each other repeatedly along
a run. It is the clearest shorthand for interleaving that survives being shrunk,
and it recurs naturally across the family without being forced.

## Works well for

Threads, locks, executors, deadlocks, test runners that do something concurrent,
and the tempus-fugit releases themselves.

## Avoid

Posts where concurrency is incidental. A post about SWT's UI thread is really
about a user interface and belongs in `technical-blueprint` with the rest of the
SWT group — the test is whether the concurrency is the subject or the setting.

## Reference images from the post

As `technical-blueprint`: take a diagram's real arrangement and drop its colours.
Thread dumps and stack traces are text and must not be drawn.

## Used by

- The concurrency and tempus-fugit family, eleven posts written between 2008 and
  2011 — see `documents/hero-prompts/` for each.
