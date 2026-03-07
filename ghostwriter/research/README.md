# Research

Source material used to ground posts.

These are **external references or detailed material** the post should draw from.

Examples:

- conference notes
- research papers
- internal documents
- regulator guidance
- long technical explanations

## Structure

Simple Markdown or text files.

Example:

```
dora-metrics.md
code-review-study.txt
basel-controls-notes.md
```

No frontmatter required.

## Usage

Research can be:

- automatically discovered in this folder
- explicitly referenced when planning a post

Example:

```shell
python plan_post.py \
    --topic "Code review as evidence" \
    --research research/dora-metrics.md
```

## Rules

- Prefer raw source material
- Avoid summarising too heavily
- Posts should extract insights from this material