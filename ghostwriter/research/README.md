# Research

Source material used to ground posts.

## Structure

Use two scopes:

- `common/` for reusable research
- `post/<post-slug>/` for post-specific research

Examples:

- `common/dora-metrics.md`
- `common/regulatory-controls.md`
- `post/code-review-as-an-evidence-system/google-notes.md`

Use Markdown or text files.

No frontmatter required.

## Rules

- raw or lightly processed source material is fine
- use `common/` for material likely to be reused
- use `post/<slug>/` for research tied to one article
- `<slug>` should usually match the post idea slug

## CLI

Automatic lookup uses:

- `research/common/`
- `research/post/<topic-slug>/`

You can also pass files explicitly with `--research`.