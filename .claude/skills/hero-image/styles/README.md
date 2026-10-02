# House styles

One file per style. A hero uses exactly one of them — mixing is how a site ends
up looking like a stock library.

Each file has the same shape so they're interchangeable in the prompt skeleton:

| Section | Purpose |
|---|---|
| `Style block` | Pasted **verbatim** into the prompt's `STYLE` section. The shared part. Don't edit it per post. |
| `Palette` | Pasted **verbatim** into the prompt's `COLOUR` section. |
| `Recurring characters` | Optional. Characters or motifs that carry across a series. |
| `Works well for` | When to reach for it. |
| `Avoid` | Subjects that come out badly in this style. |
| `Used by` | Posts already using it, so you can look at the result. |

## Adding a style

Copy the shape of an existing file. A style earns its place when two or more
posts need a look the current three can't carry — not because a single post
fancies something different. Add it to the category mapping table in `SKILL.md`
at the same time, otherwise it will never be chosen automatically.

When a style's first image is generated, record the post under `Used by` and keep
the prompt in `documents/hero-prompts/`. That pairing — prompt plus result — is
what makes the next one consistent.
