/// <reference types="cypress" />

describe('Visual Regression - Book & Video Pages', () => {
  beforeEach(() => {
    cy.checkForErrors();
  });

  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  describe('Book page', () => {
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

  describe('Video pages', () => {
    const sampleVideos = [
      { slug: '2019-06-29-refactoring', name: 'video-refactoring' },
      { slug: '2014-05-19-java-lamdas', name: 'video-lambdas' },
    ];

    sampleVideos.forEach(({ slug, name }) => {
      describe(`Video: ${slug}`, () => {
        const url = `/video/${slug}`;

        it('should load without errors', () => {
          cy.visit(url);
          cy.get('body').should('be.visible');
        });

        it('should match visual snapshot on mobile', () => {
          cy.visit(url);
          cy.capturePageAtViewport(name, 'mobile');
        });

        it('should match visual snapshot on desktop', () => {
          cy.visit(url);
          cy.capturePageAtViewport(name, 'desktop');
        });
      });
    });
  });

  describe('Navigation and links', () => {
    it('should navigate from homepage to book', () => {
      cy.visit('/');
      cy.contains('book', { matchCase: false }).first().click();
      cy.url().should('include', '/book');
    });

    it('should navigate from homepage to videos', () => {
      cy.visit('/');
      cy.contains('video', { matchCase: false }).first().click();
      cy.url().should('include', '/video');
    });
  });
});

