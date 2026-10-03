# Brand assets

Real logos, sourced from their rights holders and used unmodified. These are
composited into hero images rather than drawn by a generator — see the
`FreeAgent, OAuth & HTTP` prompts in `documents/hero-prompts/`.

| File | Source | Licence / terms |
|---|---|---|
| `freeagent.svg`, `freeagent.png` | [FreeAgent brand assets](https://www.freeagent.com/company/branding/), `mark--full-colour` bundle | Trademark of FreeAgent. Guidelines: "Don't modify the FreeAgent logos in any way", "Don't change the colour or dimensions", maintain the original height-to-width ratio, not for physical merchandise. Used here editorially, to illustrate posts about FreeAgent's own API. |
| `robot-mascot.png` | The site's own mascot, extracted from `astro/public/images/heroes/robot-cane-og.png` and given an alpha channel by flood-filling the white background from the corners, so his white body and eyes survive. | The author's own artwork. No external terms. |
| `log4j.png` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Apache_Log4j_Logo.png) | Tagged Apache License 2.0, author the Apache Software Foundation. The ASF treats project logos as trademarks regardless; its policy targets logos used to denote someone else's product or service, where a hero on a post *about* Log4j is editorial use referring to the thing itself. |
| `internet-explorer.png` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Internet_Explorer_logo_for_Windows_7.jpg), CC0; white background flood-filled from the corners to give it alpha | Microsoft trademark. Used editorially on a post about an IE8 rendering bug. Microsoft's guidelines are stricter than Apache's or FreeAgent's; this is nominative use of a discontinued product's mark. |
| `command-key.png` | Rendered from U+2318 in Arial Unicode, set in the blueprint's navy | **Not a trademark.** A standard interface symbol predating Apple's use of it. Chosen deliberately *instead* of the Apple logo — see below. |
| `oauth.svg`, `oauth.png` | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Oauth_logo.svg) | **CC BY-SA 3.0**, by **Chris Messina**. Attribution is required. |

## Obligations

**The OAuth logo needs crediting.** CC BY-SA 3.0 requires attribution wherever it
appears. The three OAuth posts carry it in their heroes, so a credit belongs
either in those posts or in a site-wide image credits page:

> OAuth logo by Chris Messina, CC BY-SA 3.0

ShareAlike is the open question. A logo placed in a reserved corner of an
otherwise independent illustration is best read as a collection rather than an
adaptation, which would not propagate the licence to the whole hero — but that is
a judgement, not a certainty. If that is not a risk worth carrying, the
alternative is to drop the OAuth mark and keep only FreeAgent's.

**The mascot is composited, never generated.** The same rule as the two logos,
for the same reason: a model's approximation of a mascot that appears elsewhere
on the site is a worse mascot. Where a post needs a character rather than the
mascot itself — the cat in `2010-03-19-nibbles-cat` — its *register* is described
in words instead, and the real artwork is not used. See the robot note in
`SKILL.md` for how often it should appear at all.

**The Apple logo is not used here, and that is deliberate.** The Mac Tips post was
originally to carry it. Apple permits referring to products by name in text but
does not permit third parties to use the Apple logo in their own materials, and
publishes no asset for editorial use — the only mark considered for this site
where the rights holder's position is a plain no rather than yes-with-conditions.
The command glyph carries the same meaning to the same readers and carries none
of the question.

**Neither logo may be redrawn, recoloured or stretched.** That is why the prompts
reserve empty space and explicitly forbid drawing an emblem: a generated
approximation of either mark would breach FreeAgent's terms and misrepresent
Messina's.
