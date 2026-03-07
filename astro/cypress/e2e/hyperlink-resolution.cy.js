/// <reference types="cypress" />

describe('Hyperlink resolution', () => {
  const corePages = ['/', '/blog', '/book', '/video', '/archive'];
  const navLinks = ['/blog', '/book', '/video', '/archive'];

  beforeEach(() => {
    cy.checkForErrors();
  });

  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  const assertGlobalNav = () => {
    navLinks.forEach((href) => {
      cy.get(`header nav a[href="${href}"]`).should('exist').and('be.visible');
    });
  };

  const validateSampledInternalLinks = (path, limit = 12) => {
    cy.visit(path);
    cy.waitForPageReady();

    cy.get('a[href^="/"]').then(($links) => {
      const uniqueLinks = [...new Set(
        $links.toArray()
          .map((link) => link.getAttribute('href'))
          .filter((href) => href && !href.startsWith('//'))
          .map((href) => href.split('#')[0].split('?')[0])
          .filter((href) => href && href !== '/')
      )].slice(0, limit);

      uniqueLinks.forEach((href) => {
        cy.request({ url: href, failOnStatusCode: false }).then((response) => {
          expect(response.status, `${path} -> ${href}`).to.be.within(200, 399);
        });
      });
    });
  };

  describe('Header navigation', () => {
    it('shows global navigation links on all core pages', () => {
      corePages.forEach((path) => {
        cy.visit(path);
        cy.waitForPageReady();
        assertGlobalNav();
      });
    });

    it('navigates across sections from the header', () => {
      cy.visit('/blog');
      navLinks.forEach((href) => {
        cy.get(`header nav a[href="${href}"]`).click();
        cy.url().should('include', href);
      });
    });

    it('routes to home/blog when clicking the logo', () => {
      cy.visit('/video');
      cy.get('header .logo-link').click();
      cy.location('pathname').should('eq', '/blog');
    });
  });

  describe('Content links', () => {
    it('navigates from blog index to a blog post', () => {
      cy.visit('/blog');
      cy.get('#posts-grid a[href^="/blog/"]').first().click();
      cy.url().should('match', /\/blog\/.+/);
      cy.get('article').should('exist');
    });

    it('navigates from video index to a video page', () => {
      cy.visit('/video');
      cy.get('a[href^="/video/"]').first().click();
      cy.url().should('match', /\/video\/.+/);
      cy.get('.video-detail-frame iframe').should('exist');
    });

    it('renders at least one book detail link', () => {
      cy.visit('/book');
      cy.get('a[href^="/book/"]').should('have.length.greaterThan', 0);
    });
  });

  describe('Status checks', () => {
    it('returns success for core pages', () => {
      corePages.forEach((path) => {
        cy.request(path).its('status').should('eq', 200);
      });
    });

    it('returns success for representative content pages', () => {
      cy.request('/blog/2022-06-07-lead-time-vs-cycle-time').its('status').should('eq', 200);
      cy.request('/video/2019-06-29-refactoring/').its('status').should('eq', 200);
    });

    it('has no broken sampled internal links on key pages', () => {
      validateSampledInternalLinks('/');
      validateSampledInternalLinks('/blog');
      validateSampledInternalLinks('/video');
    });
  });

  describe('404 handling', () => {
    it('renders a useful 404 page and allows recovery navigation', () => {
      cy.visit('/this-page-does-not-exist', { failOnStatusCode: false });
      cy.get('main').should('contain.text', 'droids');
      cy.get('a[href*="/blog/"]').first().click();
      cy.url().should('match', /\/blog\/.+/);
      cy.get('article').should('exist');
    });
  });

  describe('Basic accessibility of links', () => {
    it('ensures links have href and accessible naming', () => {
      cy.visit('/');
      cy.get('a').each(($link) => {
        cy.wrap($link).should('have.attr', 'href');

        const text = $link.text().trim();
        const ariaLabel = $link.attr('aria-label');
        const hasNamedImage = $link.find('img[alt]').length > 0;
        expect(Boolean(text || ariaLabel || hasNamedImage)).to.equal(true);
      });
    });
  });
});
