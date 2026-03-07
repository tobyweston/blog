# Notes

Rough author thinking.

These are fragments, examples, stories, angles, and working ideas.

## Structure

Use two scopes:

- `common/` for reusable notes
- `posts/<post-slug>/` for notes tied to one article

Examples:

- `common/governance-observations.md`
- `common/dev-friction-notes.md`
- `post/code-review-as-an-evidence-system/outline.md`
- `post/code-review-as-an-evidence-system/anecdotes.md`

Use free-form Markdown or text.

No strict schema required.

## Rules

- messy is fine
- short is fine
- use `common/` for reusable observations
- use `post/<slug>/` for post-specific scratch notes
- `<slug>` should usually match the post idea slug

## CLI

Automatic lookup uses:

- `notes/common/`
- `notes/post/<topic-slug>/`

You can also pass files explicitly with `--notes-file`.