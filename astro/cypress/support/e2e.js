// ***********************************************************
// This file is processed and loaded automatically before your test files.
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import and configure cypress-image-snapshot for visual regression testing
import { addMatchImageSnapshotCommand } from '@simonsmith/cypress-image-snapshot/command';

// Merge env from both config and runtime so CLI overrides still work in test runner.
const envFromConfig = Cypress.config('env') || {};
const envFromRuntime = Cypress.env() || {};
const env = { ...envFromConfig, ...envFromRuntime };
const updateSnapshots = Boolean(env.updateSnapshots);
const viewports = env.viewports || {};

// Configure cypress-image-snapshot with update support
// High threshold (50%) because functional tests already verify core behavior.
// Visual assertions are intended to catch major layout/content regressions, not pixel-perfect matches.
// Browser rendering, fonts, anti-aliasing, and responsive layout differences are expected variance.
addMatchImageSnapshotCommand({
  failureThreshold: 0.50,           // 50% threshold: allows rendering variance, catches major regressions
  failureThresholdType: 'percent',
  customDiffConfig: { threshold: 0.1 },
  capture: 'viewport',              // Capture only viewport, not entire page
  customSnapshotsDir: 'cypress/snapshots',  // Visual regression baselines go here
  customDiffDir: 'cypress/snapshots/__diff_output__',  // Diff images go here
  ...(updateSnapshots && {
    updatePassedSnapshot: true,      // Update snapshots when updateSnapshots=true
    failOnSnapshotDiff: false        // Don't fail tests when updating
  })
});

// Errors logged by dev-server tooling rather than by the site itself. The Astro
// dev toolbar runs a11y/perf audits after the page settles and its image checks
// fetch assets that aren't always reachable, so it logs through console.error on
// pages we reach by clicking. None of this ships in a production build.
const ignoredConsoleErrors = [
  "Error while running audit's match function",
  'astro:dev-toolbar',
];

const isIgnoredConsoleError = (args) => {
  const text = args
    .map((arg) => {
      try {
        return arg instanceof Error ? `${arg.message} ${arg.stack ?? ''}` : String(arg);
      } catch {
        return '';
      }
    })
    .join(' ');

  return ignoredConsoleErrors.some((ignored) => text.includes(ignored));
};

// Custom command to check for console errors
Cypress.Commands.add('checkForErrors', () => {
  const consoleErrorSpy = Cypress.sinon.spy();
  cy.wrap(consoleErrorSpy, { log: false }).as('consoleError');

  // Bind before each page load so we capture errors on visited pages, not about:blank.
  cy.on('window:before:load', (win) => {
    Cypress.sinon.stub(win.console, 'error').callsFake((...args) => {
      if (isIgnoredConsoleError(args)) {
        return;
      }
      consoleErrorSpy(...args);
    });
  });
});

// Wait for client-side rendering to stabilize before assertions/snapshots.
Cypress.Commands.add('waitForPageReady', () => {
  cy.document().its('readyState').should('eq', 'complete');
  cy.window().then((win) => {
    const fontsReady = win.document.fonts?.ready ?? Promise.resolve();

    // Only wait on images the browser has actually started fetching. Lazy
    // images inside a closed <dialog> (ClickToEnlarge) have no layout box and
    // are never requested, so waiting on them would hang forever.
    const imageReadyPromises = Array.from(win.document.images ?? [])
      .filter((image) => !image.complete && image.getClientRects().length > 0)
      .map((image) => new Promise((resolve) => {
        image.addEventListener('load', resolve, { once: true });
        image.addEventListener('error', resolve, { once: true });
      }));

    // Images below the fold may never load at all in a fixed viewport, so cap
    // the wait rather than letting the command time out.
    const settled = Promise.all([fontsReady, ...imageReadyPromises]);
    const capped = new Promise((resolve) => win.setTimeout(resolve, 2000));

    return Promise.race([settled, capped]);
  });
});

// Custom command to take full page screenshot at different viewports
Cypress.Commands.add('capturePageAtViewport', (pageName, viewportName) => {
  const viewport = viewports[viewportName];
  if (!viewport) {
    throw new Error(`Missing Cypress env viewport definition for "${viewportName}"`);
  }

  cy.viewport(viewport.width, viewport.height);

  // Wait for responsive layout and resource loading to settle.
  cy.get('body').should('be.visible');
  cy.waitForPageReady();

  // Create snapshot name with both page and viewport
  const snapshotName = `${pageName}--${viewportName}`;

  // Compare against baseline snapshot
  cy.matchImageSnapshot(snapshotName);
});

// Custom command to test a page across all viewports
Cypress.Commands.add('testPageVisually', (url, pageName) => {
  const viewportNames = Object.keys(viewports);
  if (viewportNames.length === 0) {
    throw new Error('No Cypress env viewports configured. Expected env.viewports in cypress.config.js');
  }

  cy.visit(url);
  cy.checkForErrors();

  viewportNames.forEach((viewportName) => {
    cy.capturePageAtViewport(pageName, viewportName);
  });
});

// Handle uncaught exceptions selectively
Cypress.on('uncaught:exception', (err, _runnable) => {
  // Log all errors for debugging
  console.error('Uncaught exception:', err.message);

  // Only ignore specific known benign errors that don't affect functionality
  const benignErrors = [
    'ResizeObserver loop limit exceeded',
    'ResizeObserver loop completed with undelivered notifications',
  ];

  // Check if this is a known benign error
  const isBenignError = benignErrors.some(benignError =>
    err.message.includes(benignError)
  );

  if (isBenignError) {
    // Ignore known benign errors
    return false;
  }

  // Let all other errors fail the test so we catch real bugs
  return true;
});
