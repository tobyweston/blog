/// <reference types="cypress" />

describe('Video Pages', () => {
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

  const visitVideo = (slug) => {
    cy.visit(`/video/${slug}`);
    cy.waitForPageReady();
  };

  describe('Video index', () => {
    beforeEach(() => {
      cy.visit('/video');
      cy.waitForPageReady();
    });

    it('renders the page header and preview cards', () => {
      cy.get('main h1').should('have.text', 'Videos');
      cy.get('article.video-preview').should('have.length.greaterThan', 0);
      cy.get('article.video-preview').first().within(() => {
        cy.get('h3').should('not.be.empty');
        cy.get('time').should('exist');
        cy.get('a.video-preview-cta[href^="/video/"]').should('exist');
      });
    });
  });

  describe('Video detail pages', () => {
    const videoKeys = ['refactoring', 'lambdas', 'luhn'];

    videoKeys.forEach((videoKey) => {
      describe(`Video: ${videoKey}`, () => {
        let video;

        beforeEach(() => {
          video = testData.videos[videoKey];
          visitVideo(video.slug);
        });

        it('renders title, metadata and content', () => {
          cy.get('main article').should('exist').and('be.visible');
          cy.get('.detail-kicker').should('have.text', 'Video');
          cy.get('h1').should('contain', video.title);
          cy.get('time').should('exist');
          cy.get('.article-description').should('exist').invoke('text').should('not.be.empty');
          cy.get('section.prose').should('exist').and('be.visible');
        });

        it('embeds the expected YouTube frame', () => {
          cy.get('.video-detail-frame iframe')
            .should('have.attr', 'src')
            .and('include', 'youtube-nocookie.com/embed/');
          cy.get('.video-detail-frame iframe').should('have.attr', 'allowfullscreen');
          cy.get('.video-detail-frame iframe').should('have.attr', 'loading', 'lazy');

          if (video.youtubeId) {
            cy.get('.video-detail-frame iframe')
              .should('have.attr', 'src')
              .and('include', video.youtubeId);
          }
        });

        it('matches visual snapshots on mobile and desktop', () => {
          ['mobile', 'desktop'].forEach((viewport) => {
            cy.capturePageAtViewport(video.name, viewport);
          });
        });
      });
    });
  });

  describe('Navigation and metadata', () => {
    it('navigates from video index to detail page', () => {
      cy.visit('/video');
      cy.get('a.video-preview-cta[href^="/video/"]').first().click();
      cy.url().should('match', /\/video\/.+/);
      cy.get('.video-detail-frame iframe').should('exist');
    });

    it('keeps global nav links available on detail pages', () => {
      visitVideo(testData.videos.refactoring.slug);
      cy.get('header nav a[href="/blog"]').should('exist');
      cy.get('header nav a[href="/book"]').should('exist');
      cy.get('header nav a[href="/video"]').should('exist');
      cy.get('header nav a[href="/archive"]').should('exist');
    });

    it('shows SEO and accessibility essentials on detail pages', () => {
      const video = testData.videos.refactoring;
      visitVideo(video.slug);

      cy.title().should('contain', `${video.title} - Videos`);
      cy.get('meta[name="description"]').should('have.attr', 'content').and('not.be.empty');
      cy.get('.video-detail-frame iframe').should('have.attr', 'title', video.title);
    });
  });
});
