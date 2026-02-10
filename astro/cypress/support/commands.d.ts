/// <reference types="cypress" />

// Add TypeScript definitions for custom commands
declare global {
  namespace Cypress {
    interface Chainable<Subject = any> {
      /**
       * Custom command to check for console errors
       * @example cy.checkForErrors()
       */
      checkForErrors(): Chainable<void>;

      /**
       * Custom command to capture page at specific viewport
       * @example cy.capturePageAtViewport('homepage', 'mobile')
       */
      capturePageAtViewport(pageName: string, viewportName: string): Chainable<void>;

      /**
       * Custom command to test a page visually across all viewports
       * @example cy.testPageVisually('/', 'homepage')
       */
      testPageVisually(url: string, pageName: string): Chainable<void>;
    }
  }
}

