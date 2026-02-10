/// <reference types="cypress" />

describe('Visual Regression - Blog Posts', () => {
  beforeEach(() => {
    cy.checkForErrors();
  });

  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  // Test a representative sample of blog posts
  const samplePosts = [
    { slug: '2022-06-07-lead-time-vs-cycle-time', name: 'recent-blog-post' },
    { slug: '2015-09-25-pair-tests-dont-work', name: 'mid-era-blog-post' },
    { slug: '2010-07-11-growing-team-skills', name: 'older-blog-post-with-mdx' },
  ];

  samplePosts.forEach(({ slug, name }) => {
    describe(`Blog post: ${slug}`, () => {
      const url = `/blog/${slug}`;

      it('should load without errors', () => {
        cy.visit(url);
        cy.get('body').should('be.visible');
        cy.get('article').should('exist');
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

  describe('Blog navigation', () => {
    it('should navigate between blog posts', () => {
      cy.visit('/blog');
      cy.get('a').contains('Lead Time').first().click();
      cy.url().should('include', '/blog/');
      cy.get('article').should('exist');
    });

    it('should have working navigation elements', () => {
      cy.visit('/blog/2022-06-07-lead-time-vs-cycle-time');
      cy.get('header').should('be.visible');
      cy.get('footer').should('be.visible');
    });
  });
});

