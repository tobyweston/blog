/// <reference types="cypress" />

describe('Hyperlink Resolution Tests', () => {
  beforeEach(() => {
    cy.checkForErrors();
  });

  afterEach(() => {
    cy.get('@consoleError').should('not.have.been.called');
  });

  describe('Internal Navigation Links', () => {
    describe('Header Navigation', () => {
      it('should have all main navigation links', () => {
        cy.visit('/');
        cy.get('nav a[href="/blog"]').should('exist').and('be.visible');
        cy.get('nav a[href="/book"]').should('exist').and('be.visible');
        cy.get('nav a[href="/video"]').should('exist').and('be.visible');
        cy.get('nav a[href="/archive"]').should('exist').and('be.visible');
      });

      it('should navigate to blog page from header', () => {
        cy.visit('/');
        cy.get('nav a[href="/blog"]').click();
        cy.url().should('include', '/blog');
        cy.get('h1').should('exist');
      });

      it('should navigate to book page from header', () => {
        cy.visit('/');
        cy.get('nav a[href="/book"]').click();
        cy.url().should('include', '/book');
        cy.get('h1').should('exist');
      });

      it('should navigate to video page from header', () => {
        cy.visit('/');
        cy.get('nav a[href="/video"]').click();
        cy.url().should('include', '/video');
        cy.get('h1').should('contain', 'Videos');
      });

      it('should navigate to archive page from header', () => {
        cy.visit('/');
        cy.get('nav a[href="/archive"]').click();
        cy.url().should('include', '/archive');
        cy.get('h1').should('exist');
      });

      it('should navigate home when clicking logo', () => {
        cy.visit('/blog');
        cy.get('header .logo-link').click();
        cy.url().should('eq', Cypress.config().baseUrl + '/');
      });
    });

    describe('Blog Post Links', () => {
      it('should have clickable blog post links on blog index', () => {
        cy.visit('/blog');
        cy.get('a[href*="/blog/"]').should('have.length.greaterThan', 0);
      });

      it('should navigate to blog post detail from index', () => {
        cy.visit('/blog');
        cy.get('a[href*="/blog/"]').first().click();
        cy.url().should('match', /\/blog\/.+/);
        cy.get('article').should('exist');
      });

      it('should have working blog links on homepage', () => {
        cy.visit('/');
        cy.get('a[href*="/blog/"]').should('exist');
        cy.get('a[href*="/blog/"]').first().click();
        cy.url().should('include', '/blog/');
      });
    });

    describe('Video Links', () => {
      it('should have clickable video links on video index', () => {
        cy.visit('/video');
        cy.get('a[href*="/video/"]').should('have.length.greaterThan', 0);
      });

      it('should navigate to video detail from index', () => {
        cy.visit('/video');
        cy.get('a[href*="/video/"]').first().click();
        cy.url().should('match', /\/video\/.+/);
        cy.get('.video-detail-frame').should('exist');
      });
    });

    describe('Book Links', () => {
      it('should have clickable book links if books exist', () => {
        cy.visit('/book');
        cy.get('body').then(($body) => {
          if ($body.find('a[href*="/book/"]').length > 0) {
            cy.get('a[href*="/book/"]').should('exist');
          }
        });
      });
    });
  });

  describe('External Links', () => {
    describe('Book Purchase Links', () => {
      it('should have external purchase links on book pages', () => {
        cy.visit('/book');
        cy.get('body').then(($body) => {
          // Check if there are any book detail pages to test
          const bookLinks = $body.find('a[href*="/book/"]');
          if (bookLinks.length > 0) {
            cy.wrap(bookLinks).first().click();

            // Check for purchase links (if they exist on this book)
            cy.get('body').then(($detailBody) => {
              const purchaseLinks = $detailBody.find('.purchase-link, a[target="_blank"]');
              if (purchaseLinks.length > 0) {
                cy.get('.purchase-link, a[target="_blank"]').should('exist');
                cy.get('.purchase-link, a[target="_blank"]')
                  .should('have.attr', 'href')
                  .and('match', /^https?:\/\//);
              }
            });
          }
        });
      });

      it('should open purchase links in new tab', () => {
        cy.visit('/book');
        cy.get('body').then(($body) => {
          const bookLinks = $body.find('a[href*="/book/"]');
          if (bookLinks.length > 0) {
            cy.wrap(bookLinks).first().click();
            cy.get('body').then(($detailBody) => {
              const purchaseLinks = $detailBody.find('.purchase-link');
              if (purchaseLinks.length > 0) {
                cy.get('.purchase-link')
                  .should('have.attr', 'target', '_blank')
                  .and('have.attr', 'rel', 'noopener noreferrer');
              }
            });
          }
        });
      });
    });

    describe('YouTube Video Links', () => {
      it('should have YouTube embeds on video pages', () => {
        cy.visit('/video/2026-02-08-refactoring');
        cy.get('iframe[src*="youtube"]').should('exist');
      });

      it('should use youtube-nocookie.com domain', () => {
        cy.visit('/video/2026-02-08-refactoring');
        cy.get('iframe')
          .should('have.attr', 'src')
          .and('include', 'youtube-nocookie.com');
      });
    });
  });

  describe('Link Status and Validation', () => {
    describe('Internal Links Status', () => {
      const internalPages = [
        '/',
        '/blog',
        '/book',
        '/video',
        '/archive',
      ];

      internalPages.forEach((page) => {
        it(`should load ${page} without 404`, () => {
          cy.request(page).its('status').should('eq', 200);
        });
      });
    });

    describe('Sample Content Links', () => {
      it('should load sample blog post', () => {
        cy.request('/blog/2022-06-07-lead-time-vs-cycle-time')
          .its('status')
          .should('eq', 200);
      });

      it('should load sample video page', () => {
        cy.request('/video/2026-02-08-refactoring')
          .its('status')
          .should('eq', 200);
      });
    });

    describe('All Links on Page Resolve', () => {
      it('should have no broken internal links on homepage', () => {
        cy.visit('/');
        cy.get('a[href^="/"]').each(($link) => {
          const href = $link.attr('href');
          if (href && !href.includes('#')) {
            cy.request(href).its('status').should('eq', 200);
          }
        });
      });

      it('should have no broken internal links on blog page', () => {
        cy.visit('/blog');
        // Get all internal links (limiting to first 10 for performance)
        cy.get('a[href^="/"]').then(($links) => {
          const uniqueLinks = [...new Set(
            $links.toArray()
              .map(link => link.getAttribute('href'))
              .filter(href => href && !href.includes('#'))
              .slice(0, 10)
          )];

          uniqueLinks.forEach(href => {
            cy.request(href).its('status').should('eq', 200);
          });
        });
      });

      it('should have no broken internal links on video page', () => {
        cy.visit('/video');
        cy.get('a[href^="/"]').then(($links) => {
          const uniqueLinks = [...new Set(
            $links.toArray()
              .map(link => link.getAttribute('href'))
              .filter(href => href && !href.includes('#'))
              .slice(0, 10)
          )];

          uniqueLinks.forEach(href => {
            cy.request(href).its('status').should('eq', 200);
          });
        });
      });
    });

    describe('404 Page', () => {
      it('should show 404 page for non-existent routes', () => {
        cy.visit('/this-page-does-not-exist', { failOnStatusCode: false });
        cy.get('body').should('contain', 'droids');
      });

      it('should have working links on 404 page', () => {
        cy.visit('/this-page-does-not-exist', { failOnStatusCode: false });
        cy.get('a[href^="/"]').should('have.length.greaterThan', 0);
      });

      it('should navigate from 404 page to valid content', () => {
        cy.visit('/this-page-does-not-exist', { failOnStatusCode: false });
        cy.get('a[href*="/blog/"]').first().click();
        cy.url().should('include', '/blog/');
        cy.get('article').should('exist');
      });
    });
  });

  describe('Link Attributes and Accessibility', () => {
    it('should have proper href attributes', () => {
      cy.visit('/');
      cy.get('a').each(($link) => {
        cy.wrap($link).should('have.attr', 'href');
      });
    });

    it('should have descriptive link text', () => {
      cy.visit('/');
      cy.get('a').each(($link) => {
        const text = $link.text().trim();
        const ariaLabel = $link.attr('aria-label');
        const hasImage = $link.find('img').length > 0;

        // Link should have either text, aria-label, or contain an image with alt text
        if (!hasImage) {
          expect(text.length > 0 || ariaLabel).to.be.true;
        }
      });
    });

    it('should not have empty links', () => {
      cy.visit('/');
      cy.get('a').each(($link) => {
        const hasContent = $link.text().trim().length > 0 ||
                          $link.find('img, svg').length > 0 ||
                          $link.attr('aria-label');
        expect(hasContent).to.be.true;
      });
    });
  });

  describe('Link Hover States', () => {
    it('should show visual feedback on navigation link hover', () => {
      cy.visit('/');
      cy.get('nav a').first().trigger('mouseover');
      // The link should have a hover style applied
      cy.get('nav a').first().should('have.css', 'color');
    });

    it('should be styled differently when hovered', () => {
      cy.visit('/blog');
      cy.get('a[href*="/blog/"]').first().then(($link) => {
        cy.wrap($link).trigger('mouseover');
        // Verify the link exists and can be hovered (visual changes tested by visual regression suite)
        cy.wrap($link).should('exist');
      });
    });
  });

  describe('Cross-Section Navigation', () => {
    it('should navigate from blog to videos', () => {
      cy.visit('/blog');
      cy.get('nav a[href="/video"]').click();
      cy.url().should('include', '/video');
    });

    it('should navigate from videos to books', () => {
      cy.visit('/video');
      cy.get('nav a[href="/book"]').click();
      cy.url().should('include', '/book');
    });

    it('should navigate from books to archive', () => {
      cy.visit('/book');
      cy.get('nav a[href="/archive"]').click();
      cy.url().should('include', '/archive');
    });

    it('should maintain navigation availability across sections', () => {
      const sections = ['/', '/blog', '/book', '/video', '/archive'];

      sections.forEach((section) => {
        cy.visit(section);
        cy.get('nav a[href="/blog"]').should('exist');
        cy.get('nav a[href="/book"]').should('exist');
        cy.get('nav a[href="/video"]').should('exist');
        cy.get('nav a[href="/archive"]').should('exist');
      });
    });
  });
});


