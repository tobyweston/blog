Sensible structure for the blog (recommended)

Goal
- Provide a clean, predictable project structure so you can iterate on visual design (themes) independently from content.

Top-level layout
- astro/                -> main Astro project
  - public/             -> static assets served as-is (images, favicon, fonts)
  - src/
    - components/       -> small reusable UI components (Header, Footer, Icon, etc.)
    - layouts/          -> page layouts (Main.astro, BlogPost.astro, Book.astro)
    - pages/            -> Astro pages (index.astro, rss.xml.js etc.)
    - content/          -> content collections (content/blog/, content/unpublished/)
    - themes/           -> place theme implementations here (fresh-tailwind, fresh-css)
      - fresh-tailwind/  -> Tailwind-based theme (input.css, README.md)
    - styles/           -> optional global CSS / legacy styles
  - astro.config.mjs     -> Astro config
  - package.json

Guidelines
- Keep the theme isolated under `src/themes/<theme-name>`.
  - The theme should contain a single entry CSS (e.g. `input.css`) and any theme-specific components if needed.
  - `BaseHead.astro` should import the theme's entry CSS; when you want to switch themes, swap the import.
- Public assets (images/fonts) should be in `astro/public/`.
- Content files live under `astro/src/content/blog/` and use frontmatter for metadata.
- Keep `components/` small and focused — they are theme-agnostic where possible.

What I added/changed in this session
- Added a Tailwind-based starter under `astro/src/themes/fresh-tailwind/input.css`.
- Created `postcss.config.cjs` and `tailwind.config.cjs` in `astro/`.
- Added devDependencies to `astro/package.json` (`tailwindcss`, `postcss`, `autoprefixer`).
- Updated `BaseHead.astro` to import `input.css` so you can switch themes by changing that import.
- Stripped site styles to a minimal starting point to let you design afresh.

Recommended next steps
- If you want Tailwind development to work locally, run `npm install` in `astro/` and then `npm run dev`.
- Add a theme README under each theme explaining design tokens, utility classes to use, and how to switch themes.
- Decide on canonical image location (we recommend `astro/public/images/`) and keep originals in `public/` for archival.
- If you prefer non-Tailwind themes, create `src/themes/fresh-css/` and import its CSS instead of the Tailwind input.

Quick commands
```bash
# from repo root
cd astro
npm install
npm run dev   # or npm run build
```

If you want, I can now:
- Fully scaffold a production-ready Tailwind theme with a design system and a few components.
- Or create a tiny CSS-only starter theme (no build deps) if you prefer not to add Tailwind.

