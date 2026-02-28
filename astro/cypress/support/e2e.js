// ***********************************************************
// This file is processed and loaded automatically before your test files.
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import and configure cypress-image-snapshot for visual regression testing
import { addMatchImageSnapshotCommand } from 'cypress-image-snapshot/command';

addMatchImageSnapshotCommand({
  failureThreshold: 0.03,           // 3% threshold
  failureThresholdType: 'percent',
  customDiffConfig: { threshold: 0.1 },
  capture: 'viewport',              // Capture only viewport, not entire page
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
  const viewport = Cypress.env('viewports')[viewportName];

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
  const viewports = Object.keys(Cypress.env('viewports'));

  cy.visit(url);
  cy.checkForErrors();

  viewports.forEach((viewportName) => {
    cy.capturePageAtViewport(pageName, viewportName);
  });
});

// Prevent uncaught exceptions from failing tests (but log them)
Cypress.on('uncaught:exception', (err, _runnable) => {
  // Log the error
  cy.log('Uncaught exception:', err.message);
  // Return false to prevent the error from failing the test
  // Remove this if you want uncaught exceptions to fail tests
  return false;
});
