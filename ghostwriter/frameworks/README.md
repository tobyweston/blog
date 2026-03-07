# Frameworks

Reusable thinking models used when planning posts.

These represent **mental tools I use when reasoning about problems**. They are not tied to a specific post.

## Structure

Each framework is one Markdown file with YAML frontmatter.

Example:

```
---
name: Trust Lifecycle
slug: trust-lifecycle
topics:
- trust
- governance
- compliance
  summary: >
  Short explanation of the model.
  key_claims:
- claim
- claim
  argument_patterns:
- typical argument structure
  example_phrasing:
- phrases Toby might use
  guardrails:
- misuse to avoid
---

Optional extended explanation below the frontmatter.

```

## Rules

- One framework per file
- Stable concepts only (not post-specific ideas)
- Used by the planner to shape arguments