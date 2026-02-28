/// <reference types="cypress" />

describe('Book Pages - Visual Regression & Navigation', () => {
  beforeEach(() => {
    cy.checkForErrors();
  });

  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  describe('Book Detail Page', () => {
    const bookUrl = '/book/scala-for-dava-devs';

    it('should load book page without errors', () => {
      cy.visit(bookUrl);
      cy.get('body').should('be.visible');
    });

    it('should match visual snapshot on mobile', () => {
      cy.visit(bookUrl);
      cy.capturePageAtViewport('book-detail', 'mobile');
    });

    it('should match visual snapshot on tablet', () => {
      cy.visit(bookUrl);
      cy.capturePageAtViewport('book-detail', 'tablet');
    });

    it('should match visual snapshot on desktop', () => {
      cy.visit(bookUrl);
      cy.capturePageAtViewport('book-detail', 'desktop');
    });
  });

  describe('Book Navigation', () => {
    it('should navigate from homepage to book', () => {
      cy.visit('/');
      cy.contains('book', { matchCase: false }).first().click();
      cy.url().should('include', '/book');
    });

    it('should have header navigation on book pages', () => {
      cy.visit('/book/scala-for-dava-devs');
      cy.get('header').should('be.visible');
      cy.get('nav a[href="/blog"]').should('exist');
      cy.get('nav a[href="/book"]').should('exist');
      cy.get('nav a[href="/video"]').should('exist');
      cy.get('nav a[href="/archive"]').should('exist');
    });

    it('should have footer on book pages', () => {
      cy.visit('/book/scala-for-dava-devs');
      cy.get('footer').should('be.visible');
      cy.get('footer').should('contain', 'Toby Weston');
    });
  });
});

