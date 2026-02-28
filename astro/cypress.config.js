import { defineConfig } from 'cypress';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const { addMatchImageSnapshotPlugin } = require('@simonsmith/cypress-image-snapshot/plugin');

export default defineConfig({
  projectId: 'mnnwjg',
  e2e: {
    baseUrl: 'http://localhost:4321',
    viewportWidth: 1920,
    viewportHeight: 1080,
    video: false,
    screenshotOnRunFailure: true,
    screenshotsFolder: 'cypress/results/screenshots',  // Test failure screenshots go here
    setupNodeEvents(on, config) {
      addMatchImageSnapshotPlugin(on, config);
      return config;
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

