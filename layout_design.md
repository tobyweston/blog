# Blog Structure Summary & Page Wireframes

**Last Updated:** February 8, 2026  
**Project Name:** pale-parallax (bad.robot)  
**Framework:** Astro 4.x with TypeScript  
**Site:** https://baddotrobot.com

---

## Overview

This is an **Astro-based static blog**. The blog features:

- **Landing Page**: Hero component with 5 most recent posts
- **Blog**: Article grid with pagination
- **Books**: Book reviews
- **Archive**: Historical post archive with search
- **Videos**: Reserved for future video content

---

## Page Wireframes & Layouts

### 1. LANDING PAGE (/)

List top 5 most recent posts with a hero section and site introduction.

```
┌─────────────────────────────────────────────────────────────-┐
│                      HEADER COMPONENT                        │
│  ┌──────────────┐                        ┌────────────────┐  │
│  │ Robot Logo   │ bad.robot              │ Blog  Books    │  │
│  │ + Title      │ good robots do...      │      Archive   │  │
│  └──────────────┘                        └────────────────┘  │
├──────────────────────────────────────────────────────────-───┤
│                                                              │
│                    HERO COMPONENT                            │
│                ┌─────────────────────────┐                   │
│                │   (hero-kicker)         │                   │
│                │  "Thoughts & experiments"                   │
│                │                         │                   │
│                │  Welcome                │                   │
│                │  (hero-title)           │                   │
│                │                         │                   │
│                │  Notes on programming,  │                   │
│                │  systems and developer  │                   │
│                │  craft                  │                   │
│                │  (hero-subtitle)        │                   │
│                │                         │                   │
│                │   [See Posts] ← CTA     │                   │
│                └─────────────────────────┘                   │
│                                                              │
├─────────────────────────────────────────────────────────-────┤
│                                                              │
│   Recent Posts                                               │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PostCard #1                                            │  │
│  │ ┌────────────────────────────────────────────────────┐ │  │
│  │ │ Title                                              │ │  │
│  │ │ Date                                               │ │  │
│  │ │ Description...                                     │ │  │
│  │ └────────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PostCard #2                                            │  │
│  │ ┌────────────────────────────────────────────────────┐ │  │
│  │ │ Title                                              │ │  │
│  │ │ Date                                               │ │  │
│  │ │ Description...                                     │ │  │
│  │ └────────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                      FOOTER COMPONENT                        │
│           © 2008-2026 Toby Weston. All rights reserved.      │
├──────────────────────────────────────────────────────────────┤
```


### 2. BLOG PAGE (/blog)

```
┌─────────────────────────────────────────────────────────────-┐
│                      HEADER COMPONENT                        │
│  ┌──────────────┐                        ┌────────────────┐  │
│  │ Robot Logo   │ bad.robot              │ Blog  Books    │  │
│  │ + Title      │ good robots do...      │      Archive   │  │
│  └──────────────┘                        └────────────────┘  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Blog                                                        │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PostCard #1                                            │  │
│  │ ┌────────────────────────────────────────────────────┐ │  │
│  │ │ Title                                              │ │  │
│  │ │ Date                                               │ │  │
│  │ │ Description...                                     │ │  │
│  │ └────────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ PostCard #2                                            │  │
│  │ ┌────────────────────────────────────────────────────┐ │  │
│  │ │ Title                                              │ │  │
│  │ │ Date                                               │ │  │
│  │ │ Description...                                     │ │  │
│  │ └────────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│                    ┌──────────────────┐                      │
│                    │ [Older posts] ←  │  (pagination link)   │
│                    └──────────────────┘                      │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                      FOOTER COMPONENT                        │
│           © 2008-2026 Toby Weston. All rights reserved.      │
├──────────────────────────────────────────────────────────────┤
```


### 3. BOOKS PAGE (/book)

```
┌─────────────────────────────────────────────────────────────┐
│                      HEADER COMPONENT                       │
│  ┌──────────────┐                        ┌────────────────┐ │
│  │ Robot Logo   │ bad.robot              │ Blog  Books    │ │
│  │ + Title      │ good robots do...      │      Archive   │ │
│  └──────────────┘                        └────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Books                                                      │
│  (heading text-3xl font-bold)                               │
│                                                             │
│  ┌─────────────────────────┐  ┌─────────────────────────┐   │
│  │ Book Item               │  │ Book Item               │   │
│  │ ┌───────────────────┐   │  │ ┌───────────────────┐   │   │
│  │ │ [Book Title]      │   │  │ │ [Book Title]      │   │   │
│  │ │ [Book image right │   │  │ │ [Book image right │   │   │
│  │ │  aligned]         │   │  │ │  aligned]         │   │   │
│  │ │ Book description  │   │  │ │ Book description  │   │   │
│  │ └───────────────────┘   │  │ └───────────────────┘   │   │
│  └─────────────────────────┘  └─────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────┐  ┌─────────────────────────┐   │
│  │ Book Item               │  │ Book Item               │   │
│  │ ┌───────────────────┐   │  │ ┌───────────────────┐   │   │
│  │ │ [Book Title]      │   │  │ │ [Book Title]      │   │   │
│  │ │ [Book image right │   │  │ │ [Book image right │   │   │
│  │ │  aligned]         │   │  │ │  aligned]         │   │   │
│  │ │ Book description  │   │  │ │ Book description  │   │   │
│  │ └───────────────────┘   │  │ └───────────────────┘   │   │
│  └─────────────────────────┘  └─────────────────────────┘   │
│                                                             │
│  [More books if available...]                               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                      FOOTER COMPONENT                       │
│           © 2008-2026 Toby Weston. All rights reserved.     │
├─────────────────────────────────────────────────────────────┤
```


### 4. ARCHIVE PAGE (/archive)

```
┌─────────────────────────────────────────────────────────────┐
│                      HEADER COMPONENT                       │
│  ┌──────────────┐                        ┌────────────────┐ │
│  │ Robot Logo   │ bad.robot              │ Blog  Books    │ │
│  │ + Title      │ good robots do...      │      Archive   │ │
│  └──────────────┘                        └────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Archive                                                    │
│                                                             │
│  ┌─────────────────────────────────────────────────┐        │
│  │ [Search posts by title...                    ]  │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  2022                                                       │
│  (year heading text-xl font-semibold)                       │
│  • Post Title A                                             │
│    Feb 22, 2022 (text-sm text-slate-500)                    │
│  • Post Title B                                             │
│    Jun 7, 2022  (text-sm text-slate-500)                    │
│                                                             │
│  2019                                                       │
│  (year heading text-xl font-semibold)                       │
│  • Post Title C                                             │
│    Aug 9, 2019  (text-sm text-slate-500)                    │
│  • Post Title D                                             │
│    Sep 2, 2019  (text-sm text-slate-500)                    │
│  • Post Title E                                             │
│    Sep 3, 2019  (text-sm text-slate-500)                    │
│                                                             │
│  2018                                                       │
│  (year heading text-xl font-semibold)                       │
│  • Post Title F                                             │
│    May 19, 2018 (text-sm text-slate-500)                    │
│                                                             │
│  ... [Earlier years continue grouped by year] ...           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                      FOOTER COMPONENT                       │
│           © 2008-2026 Toby Weston. All rights reserved.     │
├─────────────────────────────────────────────────────────────┤
```


### 5. BLOG POST DETAIL PAGE (/blog/[slug])

```
┌─────────────────────────────────────────────────────────────┐
│                      HEADER COMPONENT                       │
│  ┌──────────────┐                        ┌────────────────┐ │
│  │ Robot Logo   │ bad.robot              │ Blog  Books    │ │
│  │ + Title      │ good robots do...      │      Archive   │ │
│  └──────────────┘                        └────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                      BlogPost Layout                        │
│                                                             │
│  Post Title                                                 │
│                                                             │
│  Mar 29, 2012 (FormattedDate component)                     │
│  Categories: Java, Testing, Development                     │
│                                                             │
│  ┌─────────────────────────────────────────────────┐        │
│  │                                                 │        │
│  │  [Hero image (if heroImage field set)]          │        │
│  │  Optimized via Astro Image component            │        │
│  │                                                 │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  ───────────────────────────────────────────────────────    │
│                                                             │
│  This is the body content of the blog post in Markdown      │
│  or MDX format. It can contain:                             │
│                                                             │
│  • Paragraphs                                               │
│  • Code blocks                                              │
│  • Lists                                                    │
│  • Links                                                    │
│  • Images (via ImgTag component)                            │
│  • Embedded content (via astro-embed)                       │
│                                                             │
│  The post content flows naturally with proper spacing.      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                      FOOTER COMPONENT                       │
│           © 2008-2026 Toby Weston. All rights reserved.     │
├─────────────────────────────────────────────────────────────┤
```


### 6. BOOK DETAIL PAGE (/book/[slug])

```
┌─────────────────────────────────────────────────────────────┐
│                      HEADER COMPONENT                       │
│  ┌──────────────┐                        ┌────────────────┐ │
│  │ Robot Logo   │ bad.robot              │ Blog  Books    │ │
│  │ + Title      │ good robots do...      │      Archive   │ │
│  └──────────────┘                        └────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                      Book Layout                            │
│                                                             │
│  Book Title (text-4xl font-bold)                            │
│                                                             │
│  Mar 29, 2012 (FormattedDate component)                     │
│                                                             │
│  ┌─────────────────────────────────────────────────┐        │
│  │                                                 │        │
│  │  [Book Cover Image (if coverImage field set)]   │        │
│  │  Optimized via Astro Image component            │        │
│  │                                                 │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  ───────────────────────────────────────────────────────    │
│                                                             │
│  This is the book description in Markdown or MDX.           │
│  It can contain:                                            │
│                                                             │
│  • Review paragraphs                                        │
│  • Code examples (if relevant)                              │
│  • Lists and quotes                                         │
│  • Links                                                    │
│  • Embedded content                                         │
│                                                             │
│  The review flows naturally with proper spacing.            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                      FOOTER COMPONENT                       │
│           © 2008-2026 Toby Weston. All rights reserved.     │
├─────────────────────────────────────────────────────────────┤
```




