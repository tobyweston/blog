# Ghostwriter CLI

This CLI orchestrates the full blog-writing pipeline:

plan → review → draft → revise → evaluate

It is intentionally **guided and verbose** so you don't have to remember the workflow.



# Core Command

Create a new post:

```
python ghostwriter.py new "Your blog topic"
```

Example:

```
python ghostwriter.py new "Why compliance fails developers"
```

Pipeline:

1. Create plan
2. Pause for human review
3. Generate draft
4. Optional revision pass
5. Optional evaluation



# Typical Workflow

```
python ghostwriter.py new "Code review as an evidence system"
```

You will be prompted to:

1. Review the generated plan
2. Confirm drafting
3. Optionally revise
4. Optionally evaluate

This keeps **human judgement in the loop**.



# Providing More Direction

Add an **angle** or thesis:

```
python ghostwriter.py new
"Code review as an evidence system"
--angle "code review is actually an assurance mechanism"
```

Add quick notes for the planner:

```
--notes "Frame around trust and evidence"
```


# Using Research Documents

Provide specific research files:

```
python ghostwriter.py new "Trust in software delivery" --research research/common/dora-metrics.md
```

Multiple files:

```
--research file1.md,file2.md,file3.md
```



# Using Notes

Provide structured notes:

```
--notes-file notes/post/trust-in-software-delivery/outline.md
```

Multiple:

```
--notes-file file1.md,file2.md
```



# Automatic Mode

Run without interactive prompts:

```
python ghostwriter.py new "Topic" --auto
```



# Automatic Revision

Run a revision pass automatically:

```
python ghostwriter.py new "Topic" --auto --auto-revision --revision-mode tighten
```

Revision modes:

```
tighten
stronger-hook
more-like-me
less-tutorial
more-opinionated
add-framework
```

See [REVISIONS.md](REVISIONS.md) readme for details on each mode.


# Rebuilding the Semantic Index

Run this when content changes.

```
python ghostwriter.py reindex
```

This rebuilds the vector index from:

```
blog corpus
frameworks
research
notes
```



# Folder Structure

The CLI expects this structure.

```
ghostwriter/
frameworks/
research/
common/
post/<slug>/

notes/
common/
post/<slug>/

output/
plans/
drafts/

cache/

```



# Research & Notes Scoping

Automatic retrieval searches:

```
research/common
research/post/<topic-slug>

notes/common
notes/post/<topic-slug>

```

You can override with `--research` or `--notes-file`.



# Recommended Alias

Add a shell alias:

```
alias gw="python /path/to/blog/ghostwriter/ghostwriter.py"
```

Then run:

```
gw new "Topic"
gw reindex
```



# When to Rebuild the Index

Run:

```
gw reindex
```

after adding or editing:

- blog posts
- frameworks
- research documents
- notes



# Mental Model

Elite Writer works like this:

```
content sources
↓
semantic retrieval
↓
plan generation
↓
draft writing
↓
revision
↓
evaluation
```

Think of it as a **personal writing engine**, not just a prompt.



# Best Practice

Always review the **plan** before drafting.

The plan determines:

- argument
- structure
- framework
- examples

If the plan is weak, the draft will be weak.



# Philosophy

The system is designed to:

- keep humans in control
- use retrieval instead of hallucination
- enforce clear argument structure
- maintain your writing voice


