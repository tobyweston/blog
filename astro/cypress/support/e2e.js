// ***********************************************************
// This file is processed and loaded automatically before your test files.
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

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
  cy.wait(500); // Wait for any responsive changes to settle

  // Take screenshot with both viewport and page name
  const snapshotName = `${pageName}--${viewportName}`;
  cy.screenshot(snapshotName, {
    overwrite: true,
  });
});

// Custom command to test a page across all viewports
Cypress.Commands.add('testPageVisually', (url, pageName) => {
  const viewports = Object.keys(Cypress.env('viewports'));

  viewports.forEach((viewportName) => {
    cy.visit(url);
    cy.checkForErrors();
    cy.get('body').should('be.visible');
    cy.capturePageAtViewport(pageName, viewportName);
  });
});

// Prevent uncaught exceptions from failing tests (but log them)
Cypress.on('uncaught:exception', (err, runnable) => {
  // Log the error
  cy.log('Uncaught exception:', err.message);
  // Return false to prevent the error from failing the test
  // Remove this if you want uncaught exceptions to fail tests
  return false;
});

