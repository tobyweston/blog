# Nibbles the Cat & Concurrency — hero prompt

- **Post:** `astro/src/content/blog/2010-03-19-nibbles-cat.md`
- **Style:** `concurrency-schematic`, with one cartoon character
- **Series:** the concurrency / tempus-fugit family
- **Written:** 2026-10-03
- **Replaces:** nothing of its own
- **Video:** none

## Why this image

The post is the family's one piece of theatre. Its deadlock is staged as a
kidnapping: a `Kidnapper` thread holds `nibbles` the cat and wants the `cash`, a
`Negotiator` thread holds the cash and wants the cat, and neither will let go
first. The thread dump at the end of the post names the monitor on a class
literally called `Cat`.

So this hero drops the abstract clamps used in the companion detector post and
draws the scene the author wrote, because his metaphor is better than any
mechanism I would invent. Two figures, each gripping what the other wants, pulling
in opposite directions and getting nowhere.

## The cat is the one exception to the house look

Nibbles is drawn in the register of the site's own robot mascot — thick black
outlines, flat white and grey fills, big round expressive eyes, a Victorian
touch, a pale sage-green disc behind — set against the family's sand ground and
charcoal line work. He is the only cartoon element; everything else stays
schematic.

That is deliberate and is not licence to cartoon the rest of the family. The
mascot's register is lent to a character here because the post has one; see the
robot note in `SKILL.md`. Do not ask for the robot logo itself to be drawn, and
do not composite the real logo into this image — it is a different style.

## Prompt

```text
Create a wide 16:9 hero illustration, exactly 1600 x 900 pixels, for a blog post
that explains a deadlock as a kidnapping — one side holding the hostage and
wanting the ransom, the other holding the ransom and wanting the hostage, neither
willing to go first. Output a single flat image, no borders, no frame, no
watermark, no signature.

STYLE
Clean technical schematic in the manner of a timing diagram crossed with an
exploded isometric drawing. Crisp uniform-weight line work in a deep charcoal
ink, restrained flat fills, drawn on a warm pale sand-coloured ground carrying a
faint regular pattern of fine vertical rules, like timing gridlines. Objects in
isometric or three-quarter projection with visible construction lines and small
callout leaders ending in empty circles. Precise and deliberate, not sketchy.
Not photorealistic, not a 3D render, not a glossy marketing render, no glowing
neon or holographic effects.
One single character in this image is drawn differently, as described under
CHARACTER below. Everything else follows the schematic style above.

SUBJECT
Two simple schematic figures drawn in the charcoal line work, facing each other
across the centre of the image, each leaning back and away from the other as
though in a tug of war.

The LEFT figure holds a cat firmly in both arms, clutched to its chest, while its
far hand reaches out towards a small sack held by the other figure.
The RIGHT figure holds a plump sack in both arms, clutched to its chest, while
its far hand reaches out towards the cat.

Neither reaching hand makes contact. There is a clear gap between each
outstretched hand and the thing it is reaching for, and both figures lean back
with their heels dug in. The symmetry must be exact: each holds what the other
wants, and neither is giving it up.

CHARACTER
The cat is drawn in a different register from everything else, as a cartoon:
thick bold black outlines, flat white and light grey fills, a large round head
with two big round expressive eyes, small triangular ears, a neat curled tail,
and a pale sage-green circular disc behind him setting him off from the
background. Slightly exaggerated and appealing, clearly a character rather than
an object, and visibly unimpressed by his situation. He is held, not harmed.
Keep him small enough that the standoff reads first and the cat second.

RECURRING MOTIF
On the LEFT of the image, clear of the main subject, a small hourglass: two
rounded glass bulbs meeting at a narrow waist, held in a slim frame of two end
plates joined by three slender posts. A fine stream of sand falls from the upper
bulb into a small conical heap in the lower one. Drawn flat in the same charcoal
line work as the rest, no colour fill, no text beside it.
Position it so the whole hourglass, base included, sits above the lower third of
the image. It must not touch any edge and must not sit in the bottom fifth.

SUPPORTING DETAIL
Beneath the two figures, a plain horizontal rule, and below it two short
horizontal bars drawn one above the other, each ending in a small blocked square
— two runs, both stopped. Nothing else.

TEXT IN THE IMAGE
No text labels anywhere in this image. No code, braces, semicolons, thread dumps,
stack traces or filenames, no ransom note and no lettering of any kind.

COLOUR
Warm pale sand ground throughout, with its faint vertical timing rules a shade
deeper. Deep charcoal ink for all line work and a mid warm grey for flat fills.
One strong teal accent, and the sage-green disc behind the cat, and no other
colour.
The teal accent belongs to the two outstretched hands and the gap between each
hand and what it reaches for — the point where neither can proceed — and to
nothing else. The hourglass mark stays charcoal.

COMPOSITION FOR A WEB CARD
This image is centre-cropped hard to a wide strip for post cards, about 2.8:1,
and is also used as a social preview. Only the middle 60% of the image height
survives that crop. Keep both figures and the cat inside that central band; the
top 20% and the bottom 20% may be cut away entirely, so put nothing there but
background. Keep everything away from the left and right edges too. The image
must still read at roughly 550 x 190 pixels, so favour large shapes and strong
contrast over fine detail. Balanced composition, not centred symmetrically.
```

## What is most likely to go wrong

- **A hand making contact.** The gaps are the deadlock. If either figure reaches
  what it wants, the image says the opposite of the post.
- **The cat distressed or comical at his own expense.** He is unimpressed, not
  frightened, and not the butt of the joke — the same rule the baker follows in
  `bold-outline-cartoon`.
- **The cat taking over the frame.** The standoff reads first. If he dominates it
  becomes a cat picture.
- **Everything turning cartoon.** One character, schematic everywhere else.
- **A real robot appearing.** The mascot's register is borrowed; the mascot is
  not in this image.
