/// <reference types="cypress" />

describe('Book Pages - Visual Regression & Navigation', () => {
  let testData;

  before(() => {
    cy.fixture('test-data').then((data) => {
      testData = data;
    });
  });

  beforeEach(() => {
    cy.checkForErrors();
  });

  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  describe('Book Detail Page', () => {
    it('should load book page without errors', function() {
      const book = testData.books.scalaForJavaDevs;
      const bookUrl = `/book/${book.slug}`;
      cy.visit(bookUrl);

      // Stronger assertions for book page structure
      cy.get('body').should('be.visible');
      cy.get('h1').should('exist').and('not.be.empty');
      cy.get('main').should('exist').and('be.visible');
    });

    it('should match visual snapshots across all viewports', function() {
      const book = testData.books.scalaForJavaDevs;
      const bookUrl = `/book/${book.slug}`;
      cy.visit(bookUrl);

      // Test all viewports in one visit
      ['mobile', 'tablet', 'desktop'].forEach((viewport) => {
        cy.capturePageAtViewport(book.name, viewport);
      });
    });
  });

  describe('Book Navigation', () => {
    it('should navigate from homepage to book', () => {
      cy.visit('/');
      cy.contains('book', { matchCase: false }).first().click();
      cy.url().should('include', '/book');
    });

    it('should have header navigation on book pages', function() {
      const book = testData.books.scalaForJavaDevs;
      const bookUrl = `/book/${book.slug}`;
      cy.visit(bookUrl);
      cy.get('header').should('be.visible');
      cy.get('nav a[href="/blog"]').should('exist');
      cy.get('nav a[href="/book"]').should('exist');
      cy.get('nav a[href="/video"]').should('exist');
      cy.get('nav a[href="/archive"]').should('exist');
    });

    it('should have footer on book pages', function() {
      const book = testData.books.scalaForJavaDevs;
      const bookUrl = `/book/${book.slug}`;
      cy.visit(bookUrl);
      cy.get('footer').should('be.visible');
      cy.get('footer').should('contain', 'Toby Weston');
    });
  });
});

