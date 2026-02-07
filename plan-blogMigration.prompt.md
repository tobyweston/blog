# Plan: Migrate Octopress Blog Posts to Astro (Updated)

## Executive Summary

**Migration Status: 56/56 posts accounted for, 47 posts published to Astro**

- ✅ **Published to Astro Blog** (47 posts): Already migrated and live in `astro/src/content/blog/`
- ⏳ **Pending Migration** (20 posts): In `astro/src/content/pending/` awaiting review and migration
- 🔒 **Drafts/Unpublished** (9 posts): In `astro/src/content/unpublished/` (non-live, but available)
- 📚 **Remaining in Octopress** (8 posts): In `source/_posts/` (old Octopress source, not yet migrated)

**Total posts accounted for: 47 + 20 + 9 + 8 = 84 posts** (includes some duplicates across categories)

---

## Current State Breakdown

### ✅ Already Migrated to Astro Blog (47 posts)
These posts are **live in `astro/src/content/blog/`** and ready to publish:

**Years Covered:** 2008, 2012–2022
- 2008: 1 post (2008-12-17)
- 2012: 17 posts (through 2012-10-06)
- 2013–2022: 29 posts (remaining years)

**File Formats:**
- Markdown (`.md`): ~42 posts
- MDX (`.mdx`): ~5 posts

**Sample Posts:** Transaction management, OAuth, scalars, Java 8, functional programming, Scala, Raspberry Pi, build monitors, etc.

---

### ⏳ Pending Migration (20 posts)
**Location:** `astro/src/content/pending/`

These posts are **in Astro frontmatter format but awaiting review** before moving to the live blog folder. They need reconciliation with original Octopress source:

**Years Covered:** 2008–2012
- 2008: 2 posts (2008-12-29, 2008-12-30)
- 2009: 6 posts
- 2010: 4 posts
- 2011: 2 posts
- 2012: 6 posts (through 2012-05-05)

**File Extensions:** `.markdown` and `.md` (mixed)

**Posts to Review (20 pending posts, chronologically):**
1. 2008-12-29-swt-support-for-window-licker
2. 2008-12-30-be-explicit-about-ui-thread-in-swt
3. 2009-01-06-be-more-expressive-with-builders
4. 2009-01-22-deprecated-annotation
5. 2009-02-16-more-on-micro-dsls
6. 2009-03-15-swtbot-vs-window-licker
7. 2009-07-29-isnotinstanceofsmell
8. 2009-08-01-java-source-for-mac-osx
9. 2009-08-01-abstracting-reentrantreadwritelock
10. 2009-10-31-performance-monitoring-part-1
11. 2009-11-11-thawte-claim-im-not-to-be-trusted
12. 2010-01-04-type-safe-annotation
13. 2010-07-07-generate-concordion-overviews
14. 2010-07-09-changing-test-gears
15. 2010-07-11-growing-team-skills
16. 2010-07-13-lambdas-vs-closures
17. 2011-08-29-reflecting-on-interviewing-mistakes
18. 2011-10-29-java-source-on-mac
19. 2012-03-28-exception-handling-as-a-system-wide-concern
20. 2012-05-05-stop-ignoring-at-rules

---

### 🔒 Unpublished/Draft Posts (9 posts)
**Location:** `astro/src/content/unpublished/`

These posts are **migrated but marked as drafts** (with `published: false` in Astro). They are **not live on the public site** but available for review/completion:

1. 2012-09-08-dry
2. 2012-08-09-object-oriented-naming
3. 2012-07-17-object-oriented-example
4. 2012-11-18-specialisation
5. 2013-01-22-junit-enclosed-tests
6. 2013-07-16-tail-recursion-optimisation
7. 2014-10-21-universal-qualifier
8. 2015-08-05-scala-implicit-classes
9. 2018-02-04-scala-haskell-to-cheatsheet

**Note:** These should remain as drafts (not published) but still be available in the Astro site. Determine if Astro supports draft posts without publishing them.

---

### 📚 Remaining in Octopress Source (8 posts)
**Location:** `source/_posts/` (original Octopress source)

These posts **have NOT been migrated yet** and exist only in Octopress format:

1. 2012-06-15-yatspec-tutorial-introduction (unpublished)
2. 2012-07-28-structuring-a-rest-layer-part-i
3. 2012-07-29-structuring-a-rest-layer-part-ii
4. 2012-08-01-structuring-a-rest-layer-part-iii
5. 2012-09-03-two-oo-rules (unpublished)
6. 2014-01-20-install-jdk-8-on-mac-osx
7. 2016-07-07-homebrew-gopro
8. 2017-11-01-upgrade-raspian-jessie-to-stretch (unpublished)

**Action Required:** Migrate these 8 posts to `astro/src/content/blog/` (or `/unpublished/` if marked as unpublished).

---

## Migration Workflow

### Phase 1: Reconcile Pending Posts (20 posts)
**Goal:** Validate and move pending posts from staging to live blog.

**Steps:**
1. **Review each post in `astro/src/content/pending/`** for content quality and frontmatter correctness
2. **Cross-reference with original Octopress source** in `source/_posts/` (if available)
3. **Verify frontmatter format** matches Astro schema (pubDate, categories, title, etc.)
4. **Fix any issues** in frontmatter or content
5. **Move posts to `astro/src/content/blog/`** once approved
6. **Delete from `pending/`** folder

**Effort:** ~2-3 hours (10 min per post × 20)

---

### Phase 2: Migrate Remaining Octopress Posts (8 posts)
**Goal:** Convert the final 8 unmigrated posts from Octopress to Astro format.

**Steps:**
1. **Transform frontmatter** for each post:
   - Remove Octopress fields: `layout`, `comments`, `sidebar`
   - Convert `date` → `pubDate` (format: `'YYYY-MM-DD'`)
   - Keep/validate: `title`, `categories`, `keywords`, `description`
   - Handle `published: false` → move to `unpublished/` folder

2. **Content cleanup:** Ensure markdown/MDX content is clean and renders correctly

3. **Move to appropriate folder:**
   - Published posts → `astro/src/content/blog/`
   - Unpublished posts → `astro/src/content/unpublished/`

4. **Validate in Astro:** Test build to confirm no errors

**Effort:** ~1-2 hours (15 min per post × 8)

---

### Phase 3: Finalize Unpublished Posts (9 posts)
**Goal:** Ensure unpublished posts are properly configured as non-live drafts in Astro.

**Steps:**
1. **Check Astro draft/unpublished configuration** in `astro/src/content/config.ts`
2. **Verify all 9 unpublished posts** have correct `published: false` or `draft: true` flag
3. **Confirm they don't appear in RSS feeds** or public site listings
4. **Update frontmatter** if Astro uses different draft syntax

**Effort:** ~1 hour

---

### Phase 4: Validate & Test (All 56 posts)
**Goal:** Ensure all migrated posts build and render correctly in Astro.

**Steps:**
1. **Run Astro build:** `npm run build` from `astro/` folder
2. **Check for errors** in frontmatter validation, missing fields, etc.
3. **Preview locally:** `npm run preview` and spot-check 10+ posts
4. **Verify RSS feed:** Confirm only published posts appear
5. **Check categories/tags:** Ensure categories are properly indexed
6. **Validate images/assets:** Ensure image references work

**Effort:** ~1-2 hours

---

### Phase 5: Archive Octopress Source (Optional)
**Goal:** Clean up or archive old Octopress files.

**Steps:**
1. Create a git tag/branch `octopress-archive` before cleanup
2. Decide: Keep `source/` folder, archive it, or delete it
3. Document the migration for future reference

**Effort:** ~15 min

---

## Key Decisions & Configuration

### Decision 1: Unpublished/Draft Post Strategy
**Current State:** 9 unpublished posts in `astro/src/content/unpublished/` with `published: false` flag.

**Options:**
- **A:** Keep in separate `/unpublished/` folder and configure Astro to exclude them from RSS/public listing
- **B:** Keep in `/blog/` folder with `draft: true` flag in frontmatter
- **C:** Use Astro's native draft feature (if supported in version 4.16+)

**Recommendation:** Check Astro docs for native draft support; if not supported, use Option A (separate folder).

**Implementation Note:** According to Astro's Content Collections docs, use `getCollection()` to retrieve posts and filter by draft status if needed.

---

### Decision 2: Pending Posts Review Process
**Current State:** 20 posts in `astro/src/content/pending/` awaiting approval.

**Questions:**
- Should each pending post be manually reviewed before moving to live blog?
- Should they be validated against original Octopress source?
- Any quality gates or content standards before publishing?

**Recommendation:** Quick spot-check frontmatter + content integrity, then bulk-move to live if all pass. Use a checklist:
- [ ] Frontmatter valid YAML
- [ ] Title, pubDate, categories present
- [ ] Content renders without errors
- [ ] No broken image references
- [ ] Matches Octopress source (if available)

---

### Decision 3: Octopress Source Retention
**Current State:** 8 posts still only in `source/_posts/` (Octopress format).

**Options:**
- **A:** Keep Octopress folder as archive/reference
- **B:** Migrate 8 posts, then delete `source/` folder
- **C:** Migrate 8 posts, then archive `source/` to separate backup branch

**Recommendation:** Migrate the 8 posts first, then keep `source/` as a git backup (no need to delete).

---

## Frontmatter Format Comparison

### Octopress Format (Old)
```yaml
---
layout: post
title: "Post Title"
date: 2012-06-15 19:17
comments: true
categories: java, testing
sidebar: false
published: false
keywords: "keyword1, keyword2"
description: "Brief description"
---
```

### Astro Format (New - Published)
```yaml
---
title: 'Post Title'
pubDate: '2012-06-15'
categories: 'java testing'
keywords: "keyword1, keyword2"
description: "Brief description"
---
```

### Astro Format (Draft/Unpublished)
```yaml
---
title: Post Title
pubDate: 2008-12-29 14:05:00 +00:00
categories: java
keywords: "..."
description: "..."
published: false
---
```

---

## Post Count Summary

| Status | Count | Location | Action |
|--------|-------|----------|--------|
| Published (Live) | 47 | `astro/src/content/blog/` | ✅ Done |
| Pending Review | 20 | `astro/src/content/pending/` | ⏳ Review & move |
| Unpublished/Draft | 9 | `astro/src/content/unpublished/` | 🔄 Finalize config |
| Remaining (Octopress) | 8 | `source/_posts/` | 🚀 Migrate |
| **Total** | **84** | | |

---

## Timeline & Effort (Revised)

| Phase | Task | Effort | Time |
|-------|------|--------|------|
| 1 | Reconcile 20 pending posts | Medium | 2-3 hours |
| 2 | Migrate 8 remaining Octopress posts | Medium | 1-2 hours |
| 3 | Finalize 9 unpublished posts | Low | 1 hour |
| 4 | Validate & test all 56 posts | Medium | 1-2 hours |
| 5 | Archive/cleanup (optional) | Low | 15 min |
| **Total** | | | **5-8 hours** |

---

## Success Criteria

✅ All 20 pending posts reviewed, validated, and moved to `blog/`  
✅ All 8 remaining Octopress posts migrated to Astro format  
✅ All 9 unpublished posts properly configured as drafts (non-live)  
✅ Total 56 posts in Astro with correct frontmatter  
✅ Astro build succeeds without errors (`npm run build`)  
✅ RSS feed contains only published posts (not drafts)  
✅ Local preview shows all 47 published posts (`npm run preview`)  
✅ Categories, keywords, descriptions preserved  
✅ No markdown/MDX content loss  
✅ All image references validated

---

## Next Actions (Priority Order)

1. **Resolve Decision 1:** Finalize unpublished/draft post strategy in Astro
2. **Resolve Decision 2:** Define review checklist for pending posts
3. **Resolve Decision 3:** Decide on Octopress source retention strategy
4. **Start Phase 1:** Review and move 20 pending posts (batch process)
5. **Start Phase 2:** Migrate 8 remaining Octopress posts (create migration script or manual)
6. **Run Phase 3:** Configure Astro to handle drafts correctly
7. **Run Phase 4:** Full validation and testing across all 56 posts
8. **Execute Phase 5:** Archive or cleanup (based on Decision 3)
9. **Deploy:** Verify live site with all posts

---

## Notes & Considerations

- **Astro Version:** Currently using Astro 4.16.13 with MDX 3.1.9 support
- **Content Collections:** Astro uses `getCollection('blog')` to retrieve posts from `src/content/blog/`
- **Draft Filtering:** May need to implement custom filtering in templates to exclude unpublished posts from RSS/sitemap
- **File Extensions:** Mixed `.markdown` and `.md` extensions in pending folder; standardize to `.md` or `.mdx`
- **Categories:** Currently stored as space-separated strings; consider if array format would be better for indexing
- **Backup Strategy:** Ensure git history preserves all post versions before bulk operations

