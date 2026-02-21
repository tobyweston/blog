import { defineConfig } from 'cypress';

export default defineConfig({
  e2e: {
    baseUrl: 'http://localhost:4321',
    viewportWidth: 1920,
    viewportHeight: 1080,
    video: false,
    screenshotOnRunFailure: true,
    setupNodeEvents: () => {
      // Plugins are handled in support/e2e.js
    },
  },

  reporter: 'junit',
  reporterOptions: {
    mochaFile: 'cypress/results/test-results-[hash].xml',
    toConsole: true,
    outputs: true,
    testCaseSwitchClassnameAndName: false,
    suiteTitleSeparatedBy: ' > ',
    useFullSuiteTitle: true,
  },

  env: {
    // Viewport configurations for different device sizes
    viewports: {
      mobile: { width: 375, height: 667 },
      tablet: { width: 768, height: 1024 },
      desktop: { width: 1920, height: 1080 },
    },
  },
});

