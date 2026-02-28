/// <reference types="cypress" />

describe('Video Pages - Enhanced Tests', () => {
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

  describe('Video Index Page (/video)', () => {
    beforeEach(function() {
      cy.visit(testData.pages.video.url);
    });

    it('should load the video index page', () => {
      cy.get('h1').should('contain', 'Videos');
      cy.get('body').should('be.visible');
    });

    it('should display video preview cards', () => {
      // Check that video cards are rendered
      cy.get('article').should('have.length.greaterThan', 0);
    });

    it('should show video descriptions', () => {
      cy.get('p').should('exist');
    });

    it('should have clickable video links', () => {
      cy.get('a[href*="/video/"]').should('exist');
    });

    it('should display formatted dates', () => {
      // FormattedDate component should render dates
      cy.get('time').should('exist');
    });
  });

  describe('Video Detail Pages', () => {
    const videoKeys = ['refactoring', 'lambdas', 'luhn'];

    videoKeys.forEach((videoKey) => {
      describe(`Video: ${videoKey}`, function() {
        it('should load the video page without errors', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('body').should('be.visible');
        });

        it('should display the correct title', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('h1').should('exist');
          if (video.title) {
            cy.get('h1').should('contain', video.title);
          }
        });

        it('should display "Video" kicker', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('.detail-kicker').should('contain', 'Video');
        });

        it('should display formatted publication date', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('time').should('exist');
        });

        it('should display video description', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('.video-detail-header p').should('exist');
        });

        it('should embed YouTube video iframe', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('.video-detail-frame').should('exist');
          cy.get('.video-detail-frame iframe').should('exist');
        });

        it('should have correct iframe attributes', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('.video-detail-frame iframe')
            .should('have.attr', 'src')
            .and('include', 'youtube-nocookie.com/embed/');

          cy.get('.video-detail-frame iframe')
            .should('have.attr', 'allowfullscreen');

          cy.get('.video-detail-frame iframe')
            .should('have.attr', 'loading', 'lazy');
        });

        it('should embed the correct YouTube video ID if specified', function() {
          const video = testData.videos[videoKey];
          if (video.youtubeId) {
            const url = `/video/${video.slug}`;
            cy.visit(url);
            cy.get('.video-detail-frame iframe')
              .should('have.attr', 'src')
              .and('include', video.youtubeId);
          }
        });

        it('should display video content section', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('.video-detail-content').should('exist');
        });

        it('should have proper responsive video frame', function() {
          const video = testData.videos[videoKey];
          const url = `/video/${video.slug}`;
          cy.visit(url);
          cy.get('.video-detail-frame')
            .should('have.css', 'position', 'relative')
            .should('have.css', 'width')
            .and('not.equal', '0px');
        });

        // Visual regression tests
        it('should match visual snapshots if name specified', function() {
          const video = testData.videos[videoKey];
          if (video.name) {
            const url = `/video/${video.slug}`;
            cy.visit(url);

            // Test both viewports in one visit
            ['mobile', 'desktop'].forEach((viewport) => {
              cy.capturePageAtViewport(video.name, viewport);
            });
          }
        });
      });
    });
  });

  describe('Video Page Navigation', () => {
    it('should navigate from homepage to video index', () => {
      cy.visit('/');
      cy.get('nav a[href="/video"]').click();
      cy.url().should('include', '/video');
      cy.get('h1').should('contain', 'Videos');
    });

    it('should navigate from homepage to videos using text link', () => {
      cy.visit('/');
      cy.contains('video', { matchCase: false }).first().click();
      cy.url().should('include', '/video');
    });

    it('should navigate from video index to video detail', () => {
      cy.visit('/video');
      cy.get('a[href*="/video/"]').first().click();
      cy.url().should('match', /\/video\/.+/);
      cy.get('.video-detail-frame iframe').should('exist');
    });

    it('should have header navigation on video pages', () => {
      cy.visit('/video/2019-06-29-refactoring');
      cy.get('header').should('be.visible');
      cy.get('nav a[href="/blog"]').should('exist');
      cy.get('nav a[href="/book"]').should('exist');
      cy.get('nav a[href="/video"]').should('exist');
      cy.get('nav a[href="/archive"]').should('exist');
    });

    it('should have footer on video pages', () => {
      cy.visit('/video/2019-06-29-refactoring');
      cy.get('footer').should('be.visible');
      cy.get('footer').should('contain', 'Toby Weston');
    });
  });

  describe('Video Page SEO and Meta', () => {
    it('should have proper page title', () => {
      cy.visit('/video/2019-06-29-refactoring');
      cy.title().should('include', 'Videos');
    });

    it('should have meta description', () => {
      cy.visit('/video/2019-06-29-refactoring');
      cy.get('meta[name="description"]').should('exist');
    });

    it('should have proper heading hierarchy', () => {
      cy.visit('/video');
      // Should have at least one h1 for the main content
      cy.get('main h1').should('have.length', 1);
    });
  });

  describe('Video Page Accessibility', () => {
    it('should have alt text for logo', () => {
      cy.visit('/video');
      cy.get('header img').should('have.attr', 'alt');
    });

    it('should have iframe title attribute', () => {
      cy.visit('/video/2019-06-29-refactoring');
      cy.get('.video-detail-frame iframe')
        .should('have.attr', 'title');
    });

    it('should have semantic HTML structure', () => {
      cy.visit('/video/2019-06-29-refactoring');
      cy.get('article').should('exist');
      cy.get('header').should('exist');
      cy.get('main').should('exist');
      cy.get('footer').should('exist');
    });
  });
});



