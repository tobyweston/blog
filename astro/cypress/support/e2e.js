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
addMatchImageSnapshotCommand({
  failureThreshold: 0.03,           // 3% threshold
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

// Custom command to check for console errors
Cypress.Commands.add('checkForErrors', () => {
  cy.window().then((win) => {
    // Track console errors
    cy.spy(win.console, 'error').as('consoleError');
  });
});

// Custom command to take full page screenshot at different viewports
Cypress.Commands.add('capturePageAtViewport', (pageName, viewportName) => {
  const viewport = viewports[viewportName];
  if (!viewport) {
    throw new Error(`Missing Cypress env viewport definition for "${viewportName}"`);
  }

  cy.viewport(viewport.width, viewport.height);

  // Wait for responsive layout to settle and content to be visible
  cy.get('body').should('be.visible');
  cy.get('img').should('be.visible');
  cy.window().then((win) => {
    if (win.document.fonts) {
      return win.document.fonts.ready;
    }
  });

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
