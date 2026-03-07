# Comparing AI to Me (5 years ago)

I'm interested in terms of features or real value-add, how a recent burst of AI assisted coding compared to me from several years ago when I was coding alot in OSS.

The five-year-go-me was passionate about code craft and quality. I would labour deisgn decisions and build complex systems that would be low maintenance and high quality. I would write tests first, relentlessly focus on refactoring and good object-oriented (or functional-esq design).

Recent me is much more "vibe" coding. I've focused a lot on organisational leadership, running a large team and setting the same standards at the org level that I was practicing passionatly in five-year-ago-me. I just don't have time to code as much any more but am trying to create a culture of high quality, experienced coders.

As a seasons developer, I feel I can guide AI to produce the features I want whilst still maintaining architectural and design control. I can insist on standards, tests and it feels like I can take much bigger swings. Of course I want to see if I can quantify that feeling.

## Hypothesis

Can I measure the recent activity in terms of actual features or value to a period of my career where I was mode prolific.


## Recent AI driven burst

Over the last 4 weeks (Feb 7 to Mar 7, 2026), your work clusters into a few clear themes based on code changes:

1. Ghostwriter became a full writing system (major burst on Mar 7)
You built a multi-stage pipeline: style profiling, planning, drafting, revising, and evaluation.
It evolved from simple corpus-based prompting into semantic RAG with chunking + FAISS index + embedding search (not just keyword matching).
You added an operator CLI for end-to-end flow with interactive revision/evaluation steps and dry-run support.
You hardened it with real test coverage and CI, including explicit blocking of real OpenAI calls in tests.
Key code areas: ghostwriter/ghostwriter.py, ghostwriter/retrieve.py, ghostwriter/build_index.py, .github/workflows/ghostwriter-tests.yml

2. You built and then stabilized visual regression testing in Astro
Added Cypress visual/e2e test suite, baseline/snapshot workflow, and CI execution across browsers.
Then spent multiple passes fixing brittle selectors, stale snapshots, browser variance tolerance, and CI node/browser setup.
Net effect: moved from “tests exist” to “tests are reliable enough to run as a gate.”
Key files: .github/workflows/visual-tests.yml, astro/cypress.config.js

3. You reshaped site navigation and listing UX
Root now redirects to /blog; old dated URL patterns are redirected to canonical slugs.
Blog index got two-column cards + infinite scroll + staged card reveal behavior.
Archive became cross-content (blog + video) with title/subtitle filtering and hiding empty year groups.
Key files: astro/astro.config.mjs, astro/src/pages/blog/index.astro, astro/src/pages/archive/index.astro, astro/src/pages/blog/[year]/[month]/[day]/[...slug].astro

4. You improved publishing/SEO/distribution plumbing
Added JSON-LD/robots/llms.txt and keyword/frontmatter propagation work.
Added Giscus discussions and Google Analytics integration.
Upgraded Astro/dependencies (including the Astro 4→5 security-driven upgrade), aligned Node versions, and tuned deploy workflow.
Key files: astro/src/layouts/BlogPost.astro, astro/src/components/ui/Giscus.astro, .github/workflows/deploy-pages.yml

5. Content production and migration clean-up continued alongside platform work
Added/updated posts, videos, book pages, hero imagery, and older markdown/MDX migration fixes.
There’s a clear pattern of “publish content while modernizing architecture/testability.”
Quick read on momentum:

225 commits in 4 weeks.
Heavy Astro phase (site/platform/testing) through Feb and early Mar.
Then a concentrated Ghostwriter product sprint on Mar 7 (26 commits touching ghostwriter/ in this period).

Thats pretty feature rich development in 4 weeks of part time snatch-coding.


## Comparison prompts

> compare this activity to some of my other most populate github projects. I'm interested if this recent activity produce more code and value than my most busy periods working on other open source tools. I'm trying to quantify how much faster AI is making me

I’ll quantify this with actual Git metrics: first for this repo, then for your other local repos (or GitHub via API if needed), and normalize by time windows to estimate relative output velocity and likely value density. I’m starting by discovering candidate repos and extracting comparable commit/churn stats.

I only have this repo locally, so I’ll pull your public GitHub repo stats and commit history from GitHub to compare against your busiest open-source projects by stars/activity.

I’m switching to direct GitHub API calls from the terminal for cleaner metrics (stars, forks, commit frequency, churn). If sandbox blocks network, I’ll request one-time escalation automatically.

I found your top public repos by stars; next I’m calculating each repo’s peak 4-week burst (commits and churn) from GitHub contributor stats so we can compare this current sprint apples-to-apples.

The GitHub stats endpoint is asynchronous and returning 202, so I’m switching to a more reliable method: clone your top repos and compute peak 28-day windows directly from raw Git history (commits + lines added/deleted).

The author filter didn’t match your historical commit identity consistently, so I’m now detecting your actual commit signatures per repo and recomputing the windows accurately.

I’ve got the peak-window metrics now; I’m doing one final pass to add “value proxies” (test/CI/docs/system breadth) so the speed comparison isn’t just raw line churn.

I’m adding one more high-star repo (Refactoring-Chapter-1) so the comparison covers your star-ranked top set more completely, then I’ll give you a speed multiplier estimate.

sat for 40m