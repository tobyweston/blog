#!/bin/bash

# Setup Verification Script for Cypress Visual Regression Testing
# This script verifies that all components are properly installed and configured

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_DIR"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Cypress Visual Regression - Setup Check${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check 1: Node modules
echo -n "Checking node_modules... "
if [ -d "node_modules" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗${NC}"
    echo "Run: npm install"
    exit 1
fi

# Check 2: Cypress installed
echo -n "Checking Cypress installation... "
if [ -d "node_modules/cypress" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗${NC}"
    echo "Run: npm install --save-dev cypress"
    exit 1
fi

# Check 3: cypress-image-snapshot installed
echo -n "Checking cypress-image-snapshot... "
if [ -d "node_modules/cypress-image-snapshot" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗${NC}"
    echo "Run: npm install --save-dev cypress-image-snapshot"
    exit 1
fi

# Check 4: Configuration files
echo -n "Checking cypress.config.js... "
if [ -f "cypress.config.js" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗${NC}"
    exit 1
fi

# Check 5: Test files
echo -n "Checking test files... "
TEST_COUNT=$(find cypress/e2e -name "*.cy.js" 2>/dev/null | wc -l)
if [ "$TEST_COUNT" -ge 3 ]; then
    echo -e "${GREEN}✓ ($TEST_COUNT tests)${NC}"
else
    echo -e "${RED}✗${NC}"
    exit 1
fi

# Check 6: Support files
echo -n "Checking support files... "
if [ -f "cypress/support/e2e.js" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗${NC}"
    exit 1
fi

# Check 7: Directory structure
echo -n "Checking directory structure... "
if [ -d "cypress/screenshots" ] && [ -d "cypress/e2e" ] && [ -d "cypress/support" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗${NC}"
    exit 1
fi

# Check 8: Build output
echo -n "Checking if site is built... "
if [ -d "dist" ]; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${YELLOW}⚠${NC} (Run: npm run build)"
fi

# Check 9: Server check (non-blocking)
echo -n "Checking if preview server is running... "
if curl -s http://localhost:4321 > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${YELLOW}⚠${NC} (Run: npm run preview)"
fi

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Setup verification complete!${NC}"
echo ""
echo "Next steps:"
echo "  1. Build the site:     ${BLUE}npm run build${NC}"
echo "  2. Start preview:      ${BLUE}npm run preview${NC} (in separate terminal)"
echo "  3. Create baselines:   ${BLUE}npm run test:visual:baseline${NC}"
echo "  4. Run tests:          ${BLUE}npm run test:visual${NC}"
echo ""
echo "Documentation:"
echo "  - Quick start:         ${BLUE}../CYPRESS_QUICKSTART.md${NC}"
echo "  - Full docs:           ${BLUE}cypress/README.md${NC}"
echo "  - Implementation:      ${BLUE}../IMPLEMENTATION_SUMMARY.md${NC}"
echo ""

