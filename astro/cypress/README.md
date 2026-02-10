# Cypress Visual Regression Testing

Quick-start guide for visual regression testing with Cypress.

## Quick Start

```bash
cd astro

# Build and start preview server
npm run build
npm run preview &

# Run tests (creates baseline screenshots)
npm run test:visual

# Or open interactive UI (recommended first time)
npm run test:visual:open
```

## What Gets Tested

- **Pages**: Homepage, Blog (index + 3 sample posts), Book, Video, Archive, 404
- **Viewports**: Mobile (375×667), Tablet (768×1024), Desktop (1920×1080)
- **Coverage**: ~30 tests, ~90 screenshots per run

## Commands

```bash
npm run test:visual              # Run all tests
npm run test:visual:open         # Interactive Cypress UI
npm run cypress:run              # Direct run
npm run cypress:open             # Direct UI

# Helper scripts
./cypress/test.sh full           # Complete workflow
./cypress/test.sh test           # Just run tests
./cypress/test.sh open           # Open UI
```

## How It Works

1. **First run** → Creates baseline screenshots in `cypress/screenshots/`
2. **Commit baselines** → They become your reference point
3. **Make CSS changes** → Run tests again to create new screenshots
4. **Compare** → Use git or visual tools to see what changed

## File Structure

```
cypress/
├── e2e/                         # Test specs
│   ├── visual-regression.cy.js  # Core pages
│   ├── blog-posts.cy.js         # Blog tests
│   └── book-video.cy.js         # Book & video tests
├── support/
│   ├── e2e.js                   # Custom commands
│   └── commands.d.ts            # TypeScript definitions
├── plugins/
│   └── index.js                 # Plugin config
├── screenshots/                 # Baseline storage (commit to git!)
├── README.md                    # Full documentation
└── test.sh                      # Helper script
```

## Custom Commands

```javascript
cy.checkForErrors()                       // Monitor console errors
cy.capturePageAtViewport(name, viewport)  // Screenshot specific viewport
cy.testPageVisually(url, name)            // Test page across all viewports
```

## Typical Workflow

### Create Baselines (First Time)

```bash
npm run test:visual
git add cypress/screenshots/
git commit -m "Add visual regression baselines"
```

### After CSS Changes
```bash
npm run test:visual         # New screenshots created
git diff cypress/screenshots/  # See what changed
# If good: git add + commit
# If bad: fix CSS and re-run
```

## Troubleshooting

| Issue               | Fix                                   |
|---------------------|---------------------------------------|
| Port 4321 in use    | `killall node`                        |
| Cypress not found   | `npm install`                         |
| Tests timeout       | Check if site builds: `npm run build` |
| Screenshots missing | Run `npm run test:visual` first       |

## Configuration

- **Base URL**: http://localhost:4321
- **Viewports**: Configured in `cypress.config.js`
- **Threshold**: Pixel differences detected at 0.5%
- **Screenshots**: Native Cypress `cy.screenshot()` functionality

## CI/CD

GitHub Actions workflow included in `.github/workflows/visual-tests.yml`
- Runs on every push and PR
- Tests in Chrome and Firefox
- Uploads diff images on failure
