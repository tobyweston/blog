/// <reference types="cypress" />

describe('Visual Regression - Blog Posts', () => {
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

  // Test a representative sample of blog posts from fixture
  const postKeys = ['recent', 'midEra', 'older'];

  postKeys.forEach((postKey) => {
    describe(`Blog post: ${postKey}`, function() {
      it('should load without errors', function() {
        const post = testData.blogPosts[postKey];
        const url = `/blog/${post.slug}`;
        cy.visit(url);
        cy.get('body').should('be.visible');

        // Stronger assertions for blog post structure
        cy.get('article').should('exist').and('be.visible');
        cy.get('article h1')
          .should('exist')
          .and('not.be.empty')
          .and('have.length', 1);
        cy.get('article time[datetime]')
          .should('exist')
          .and('have.attr', 'datetime')
          .and('match', /^\d{4}-\d{2}-\d{2}/);
        cy.get('article .post-content, article .prose')
          .should('exist')
          .and('not.be.empty');
      });

      it('should match visual snapshots across all viewports', function() {
        const post = testData.blogPosts[postKey];
        const url = `/blog/${post.slug}`;
        cy.visit(url);

        // Test all viewports in one visit
        ['mobile', 'tablet', 'desktop'].forEach((viewport) => {
          cy.capturePageAtViewport(post.name, viewport);
        });
      });
    });
  });

  describe('Blog navigation', () => {
    it('should navigate between blog posts', () => {
      cy.visit('/blog');
      cy.get('a').contains('Lead Time').first().click();
      cy.url().should('include', '/blog/');

      // Verify we're on a valid blog post page
      cy.get('article').should('exist').and('be.visible');
      cy.get('h1').should('exist').and('not.be.empty');
    });

    it('should have working navigation elements', () => {
      cy.visit('/blog/2022-06-07-lead-time-vs-cycle-time');

      // Verify header exists and has navigation
      cy.get('header').should('be.visible');
      cy.get('header nav').should('exist');
      cy.get('header nav a').should('have.length.greaterThan', 0);

      // Verify footer exists and has content
      cy.get('footer').should('be.visible');
      cy.get('footer').invoke('text').should('not.be.empty');
    });
  });
});

