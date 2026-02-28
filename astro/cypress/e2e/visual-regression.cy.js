/// <reference types="cypress" />

describe('Visual Regression - Core Pages', () => {
  let testData;

  before(() => {
    cy.fixture('test-data').then((data) => {
      testData = data;
    });
  });

  // Track console errors
  beforeEach(() => {
    cy.checkForErrors();
  });

  // After each test, check if console.error was called
  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  // Use fixture data for pages
  const pageKeys = ['homepage', 'blog', 'book', 'video', 'archive'];

  pageKeys.forEach((pageKey) => {
    describe(`${pageKey} page`, () => {
      it('should load without errors', function() {
        const page = testData.pages[pageKey];
        cy.visit(page.url);

        // Stronger assertions
        cy.get('body').should('be.visible');
        cy.get('h1').should('exist').and('not.be.empty');
        cy.get('main').should('exist').and('be.visible');
        cy.get('header').should('exist').and('be.visible');
        cy.get('footer').should('exist').and('be.visible');
      });

      it('should match visual snapshots across all viewports', function() {
        const page = testData.pages[pageKey];
        cy.visit(page.url);

        // Test all viewports in one visit
        ['mobile', 'tablet', 'desktop'].forEach((viewport) => {
          cy.capturePageAtViewport(page.name, viewport);
        });
      });
    });
  });

  describe('404 page', () => {
    it('should render 404 page', () => {
      cy.visit('/non-existent-page', { failOnStatusCode: false });
      cy.get('body').should('be.visible');
    });

    it('should match visual snapshot on mobile', () => {
      cy.visit('/non-existent-page', { failOnStatusCode: false });
      cy.capturePageAtViewport('404-page', 'mobile');
    });

    it('should match visual snapshot on desktop', () => {
      cy.visit('/non-existent-page', { failOnStatusCode: false });
      cy.capturePageAtViewport('404-page', 'desktop');
    });
  });
});

