# Cypress Test Suite

## Run Tests

```bash
cd astro

# Build and preview (required first)
npm run build && npm run preview &

# Run all tests
npm run test:visual

# Interactive mode
npm run test:visual:open
```

## Test Coverage

**Visual Regression** (3 viewports: mobile 375×667, tablet 768×1024, desktop 1920×1080):
- `visual-regression.cy.js` - Homepage, archive, 404
- `blog-posts.cy.js` - Blog index + sample posts
- `book-pages.cy.js` - Book pages

**Functional**:
- `video-pages.cy.js` - Video embeds
- `hyperlink-resolution.cy.js` - Link validation
- `click-to-enlarge.cy.js` - Image interactions

## Screenshots & Baselines

**First time setup (create baselines):**
```bash
npm run test:visual:baseline
git add cypress/results/screenshots/
git commit -m "Add visual regression baselines"
```

**After changes (comparison tests):**
```bash
npm run test:visual                    # Creates new screenshots, compares to baseline
git diff cypress/results/screenshots/  # Review visual changes
```

Baselines are stored in `cypress/results/screenshots/` and committed to git. Tests fail if new screenshots differ from baselines.

## Config

- Base URL: `http://localhost:4321`
- Viewports: Defined in `cypress.config.js` env.viewports
- Results: `cypress/results/` (screenshots + JUnit XML)
- Port conflict: `killall node`
