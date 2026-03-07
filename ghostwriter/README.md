# Ghostwriter

Blog post generator for my blog. Analyzes existing posts to match writing style, tone and argument structure.

The system uses **semantic retrieval over my blog corpus, frameworks, research and notes** to plan and draft posts before deliberate revision.

## Setup

1. **Create and activate virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

Dependencies:

* `openai` – embeddings and AI writing
* `pyyaml` – markdown frontmatter parsing
* `faiss-cpu` – semantic vector retrieval

3. **Set your OpenAI API key:**

```bash
export OPENAI_API_KEY='your-api-key-here'
```

4. **Build the semantic index (required once):**

```bash
python build_index.py
```

This indexes:

* blog corpus
* frameworks
* research
* notes

The index is stored in:

```
cache/
```

## Deactivate

When done, deactivate the virtual environment:

```bash
deactivate
```


# Quick Start

Ghostwriter works best when used through the CLI orchestrator.

## 1. Build the semantic index (first time only)

```bash
python build_index.py
````

Re-run this whenever you add or modify:

* blog posts
* frameworks
* research
* notes



## 2. Generate a new post

```bash
python ghostwriter.py new "Code review as an evidence system"
```

The CLI will guide you through:

1. plan generation
2. plan review
3. draft generation
4. optional revision
5. optional evaluation



## 3. Typical pipeline

```mermaid
flowchart LR
    A[Topic] --> B[Semantic Retrieval]
    B --> C[Plan]
    C --> D[Draft]
    D --> E[Revise]
    E --> F[Evaluate]
```

Ghostwriter deliberately **plans before writing**.

The plan determines:

* the central idea
* the structure
* any relevant frameworks
* supporting examples



## 4. Rebuild the index when content changes

```bash
python ghostwriter.py reindex
```

This updates the semantic retrieval index used for planning and drafting.




# Usage

The system follows this pipeline:

```
retrieve → plan → draft → revise → evaluate
```

You can run the steps individually or via the CLI orchestrator.



## Recommended CLI workflow

Create a new post:

```bash
python ghostwriter.py new "Code review as an evidence system"
```

This will:

1. generate a plan
2. pause for review
3. generate the draft
4. optionally revise
5. optionally evaluate

Rebuild the semantic index when content changes:

```bash
python ghostwriter.py reindex
```



# Direct tool usage

These scripts can also be run individually.

## Plan

Plan with research and notes:

```bash
python plan_post.py \
  --topic "Code review as an evidence system" \
  --angle "review is not just collaboration, it is assurance" \
  --research research/common/dora-notes.md,research/common/control-framework.md \
  --notes-file notes/common/code-review-ideas.md
```



## Draft

Draft from the approved plan:

```bash
python generate_post.py \
  --plan output/plans/2026-03-07-code-review-as-an-evidence-system.plan.md
```



## Revise deliberately

```bash
python revise_post.py \
  --input ../astro/src/content/blog/2026-03-07-code-review-as-an-evidence-system.mdx \
  --mode stronger-hook
```

Revision modes include:

```
tighten
stronger-hook
more-like-me
less-tutorial
more-opinionated
add-framework
sharpen-argument
```



# Example real workflow

## Plan

```shell
python plan_post.py --topic "Code review as an evidence system"
```

## Draft

```shell
python generate_post.py --plan output/plans/2026-03-07-code-review-as-an-evidence-system.plan.md
```

## Tighten

```shell
python revise_post.py \
  --input ../astro/src/content/blog/2026-03-07-code-review-as-an-evidence-system.mdx \
  --mode tighten
```

## Evaluate

```shell
python evaluate_post.py \
  --input ../astro/src/content/blog/2026-03-07-code-review-as-an-evidence-system.mdx
```

