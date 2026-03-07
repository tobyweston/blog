# Frameworks

Reusable thinking models used when planning posts.

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

Optional explanation may follow below the frontmatter.
```

## Rules

- one framework per file
- reusable across multiple posts
- stable concepts only