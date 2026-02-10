/// <reference types="cypress" />

describe('Visual Regression - Core Pages', () => {
  // Track console errors
  beforeEach(() => {
    cy.checkForErrors();
  });

  // After each test, check if console.error was called
  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  const pages = [
    { url: '/', name: 'homepage' },
    { url: '/blog', name: 'blog-index' },
    { url: '/book', name: 'book-index' },
    { url: '/video', name: 'video-index' },
    { url: '/archive', name: 'archive' },
  ];

  pages.forEach(({ url, name }) => {
    describe(`${name} page`, () => {
      it('should load without errors', () => {
        cy.visit(url);
        cy.get('body').should('be.visible');
      });

      it('should match visual snapshot on mobile', () => {
        cy.visit(url);
        cy.capturePageAtViewport(name, 'mobile');
      });

      it('should match visual snapshot on tablet', () => {
        cy.visit(url);
        cy.capturePageAtViewport(name, 'tablet');
      });

      it('should match visual snapshot on desktop', () => {
        cy.visit(url);
        cy.capturePageAtViewport(name, 'desktop');
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

