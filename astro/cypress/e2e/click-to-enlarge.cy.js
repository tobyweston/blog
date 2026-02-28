/// <reference types="cypress" />

describe('ClickToEnlarge Component', () => {
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

  it('opens and closes the dialog via the close button', function() {
    const postUrl = testData.specialPosts.clickToEnlarge.url;
    cy.visit(postUrl);

    cy.get('[data-cte-trigger]').first().as('trigger');
    cy.get('@trigger').invoke('attr', 'data-cte-id').as('cteId');

    cy.get('@cteId').then((cteId) => {
      const selector = `dialog[data-cte-dialog="${cteId}"]`;
      cy.get(selector).as('dialog').should('exist');

      cy.get('@trigger').click();
      cy.get('@dialog').should('have.attr', 'open');

      cy.get('@dialog').find('.cte-close').click();
      cy.get('@dialog').should('not.have.attr', 'open');
    });
  });

  it('closes the dialog when clicking the backdrop', function() {
    const postUrl = testData.specialPosts.clickToEnlarge.url;
    cy.visit(postUrl);

    cy.get('[data-cte-trigger]').first().as('trigger');
    cy.get('@trigger').invoke('attr', 'data-cte-id').as('cteId');

    cy.get('@cteId').then((cteId) => {
      const selector = `dialog[data-cte-dialog="${cteId}"]`;
      cy.get(selector).as('dialog');

      cy.get('@trigger').click();
      cy.get('@dialog').should('have.attr', 'open');

      cy.get('@dialog').click('topLeft');
      cy.get('@dialog').should('not.have.attr', 'open');
    });
  });
});
