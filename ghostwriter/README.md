# Ghostwriter

AI-powered blog post generator for my blog. Analyzes existing posts to match writing style and tone.

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Dependencies:
   - `openai` - for AI blog post generation
   - `pyyaml` - for parsing markdown frontmatter

3. **Set your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Deactivate

When done, deactivate the virtual environment:
```bash
deactivate
```


## Usage 

Plan with research and notes:

```bash
python plan_post.py \
  --topic "Code review as an evidence system" \
  --angle "review is not just collaboration, it is assurance" \
  --research research/dora-notes.md,research/control-framework.md \
  --notes-file notes/code-review-ideas.md
```

Draft from the approved plan:

```bash
python generate_post.py \
  --plan output/plans/2026-03-07-code-review-as-an-evidence-system.plan.md
```

Revise deliberately:

```bash
python revise_post.py \
  --input ../astro/src/content/blog/2026-03-07-code-review-as-an-evidence-system.mdx \
  --mode stronger-hook
```


# Example real workflow

## Plan

```shell 
python plan_post.py  --topic "Code review as an evidence system"
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