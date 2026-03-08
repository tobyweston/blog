# Post Plan

## Recommended title
Man vs the Model: Quantifying what AI actually added to four weeks of my engineering work

## Alternative titles
- When AI Ships: A Senior Engineer's Mea Culpa and Measurement
- Ghostwriter, Tests and Trade-offs: Comparing AI-assisted Productivity to My Old Self
- How I Let AI Do the Heavy Lifting — And What I Still Had To Do
- Measuring AI Output: A 28‑day case study vs. my earlier peak periods

## Reader
This is for senior engineers and engineering leaders who already use (or are deciding whether to adopt) generative AI in their teams and are interested in empirical evidence that AI is making us faster (or otherwise). You care about measurable delivery, maintainability, not hype. You want practical lessons about when AI actually improves throughput, what it doesn’t, and how to instrument and manage the change. 

## Central insight
AI substantially increased throughput on well-scoped, repeatable engineering work compared to historical peaks. I compared recent work with historical work (4-5 projects) to analyze not just volumen of code but features shipped and value add.  

## Why this matters
People are debating the value of AI, does it make us faster, is it safer. Its relatively early in the adoption curve and there’s a lot of hype and fear. Its helpful to see some empircal data and personal experience report to help people understand what it actually does for us, and how to use it effectively.

## Recommended framework
Reflections and Learnings

## Opening options
- Give a short anecdote and teaser metric: "In Feb–Mar 2026 I shipped a Ghostwriter system plus CI and visual tests. My Feature Point model says it was ~2.8x the average of my historical peaks. Here's what that actually means."

## Outline
1. Introduction: set the scene and state the single comparison question.
2. Method: how I measured productivity (initiative sizing, FeatureValueIndex, commit‑bucket heuristics).
3. Case study — recent AI‑assisted burst: what I built (Ghostwriter pipeline, visual regression, CI), short narrative of workflow and prompts.
4. Historical comparison: chosen windows, why those comparators matter, headline numbers.
5. Interpretation and trade-offs: what the numbers hide and reveal (quality, brittleness, governance, velocity).
6. Overall conclusion: what does the data say about comparing my historical self to my AI‑assisted self.
7. Recommendations, checklist and invitation to discuss.

## Key arguments
- Experience matters: an experienced engineer plus AI ≠ junior engineer plus AI. You get different risk profiles.  
- Measure initiatives, not lines: use an initiative‑sized rubric (novelty, depth, breadth, hardening, user impact) to compare work fairly.  
- Hardening is the multiplier: tests, CI, and reproducible evaluation convert generated code into reliable delivery.  
- Guardrails are cheap insurance: block live API calls in tests, freeze prompts, and automate semantic checks; you won't regret it.  

Example commands / snippets (to include in the post as concrete examples)
- Block real LLM calls during tests:
  export OPENAI_API_KEY=dummy && pytest -q
- A minimal “planner → draft → revise → evaluate” pseudo‑pipeline (shown inline in the post as code-like pseudo):
  planner(prompt) -> draft(prompt, constraints) -> revise(feedback) -> evaluate(metrics)

## Things to avoid
- Claiming AI replaced your expertise — it amplified it.  
- Using raw commit or LOC counts as the sole productivity metric. 
- Presenting the case as vendor marketing or techno-utopianism.  
- Ignoring operational costs: monitoring, dependency updates, model drift.  
- Skipping reproducibility details: prompts, seed data and CI configs must be shareable.
- Claim this is a panacea — it’s a tool with specific strengths and weaknesses, not a magic bullet AND this is just my personal experience
- Don't make this about the measuring framework produced, its about personal experience and data, mention the framework trivially (give an overview of RAG for example to demonstrate the effort / sophistication of the system built, but don't make it the focus of the post)

## Suggested categories
- engineering
- productivity
- leadership
- ai
- reflections

## Suggested topics
- developer productivity metrics (FeatureValueIndex, Feature Points)
- testing & CI for AI‑assisted development
- prompt engineering as a disciplined practice
- RAG/FAISS indexing and operational hardening
- code review, maintainability and governance for generated code