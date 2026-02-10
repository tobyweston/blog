#!/bin/bash

# Cypress Visual Testing Helper Script
# This script helps manage the visual regression testing workflow

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_DIR"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

function print_usage() {
    echo "Cypress Visual Testing Helper"
    echo ""
    echo "Usage: ./cypress/test.sh [command]"
    echo ""
    echo "Commands:"
    echo "  baseline      Create new baseline screenshots"
    echo "  test          Run visual regression tests"
    echo "  open          Open Cypress interactive mode"
    echo "  clean         Remove all screenshots and snapshots"
    echo "  server        Start the preview server (in background)"
    echo "  full          Build, start server, and run tests"
    echo ""
}

function check_server() {
    if curl -s http://localhost:4321 > /dev/null; then
        echo -e "${GREEN}✓ Server is running${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠ Server is not running at http://localhost:4321${NC}"
        echo "Start it with: npm run preview"
        return 1
    fi
}

function create_baseline() {
    echo -e "${GREEN}Creating baseline screenshots...${NC}"
    check_server || exit 1
    npm run test:visual:baseline
    echo -e "${GREEN}✓ Baselines created${NC}"
    echo "Review changes with: git status cypress/snapshots/"
}

function run_tests() {
    echo -e "${GREEN}Running visual regression tests...${NC}"
    check_server || exit 1
    npm run test:visual
    echo -e "${GREEN}✓ Tests completed${NC}"
}

function open_cypress() {
    echo -e "${GREEN}Opening Cypress interactive mode...${NC}"
    check_server || echo -e "${YELLOW}Remember to start the server first!${NC}"
    npm run test:visual:open
}

function clean_screenshots() {
    echo -e "${YELLOW}Cleaning screenshots and snapshots...${NC}"
    rm -rf cypress/screenshots/*
    rm -rf cypress/snapshots/**/__diff_output__/
    echo -e "${GREEN}✓ Cleaned${NC}"
}

function start_server() {
    echo -e "${GREEN}Starting preview server in background...${NC}"
    npm run preview &
    SERVER_PID=$!
    echo "Server PID: $SERVER_PID"
    echo "Waiting for server to start..."
    sleep 5
    if check_server; then
        echo -e "${GREEN}✓ Server started successfully${NC}"
    else
        echo -e "${RED}✗ Server failed to start${NC}"
        exit 1
    fi
}

function run_full() {
    echo -e "${GREEN}Running full test workflow...${NC}"
    echo "1. Building site..."
    npm run build

    echo "2. Starting preview server..."
    npm run preview &
    SERVER_PID=$!

    echo "Waiting for server..."
    sleep 5

    if check_server; then
        echo "3. Running tests..."
        npm run test:visual

        # Kill server
        kill $SERVER_PID 2>/dev/null || true

        echo -e "${GREEN}✓ Full workflow completed${NC}"
    else
        kill $SERVER_PID 2>/dev/null || true
        echo -e "${RED}✗ Server failed to start${NC}"
        exit 1
    fi
}

# Main command handling
case "${1:-}" in
    baseline)
        create_baseline
        ;;
    test)
        run_tests
        ;;
    open)
        open_cypress
        ;;
    clean)
        clean_screenshots
        ;;
    server)
        start_server
        ;;
    full)
        run_full
        ;;
    help|--help|-h)
        print_usage
        ;;
    *)
        if [ -n "${1:-}" ]; then
            echo -e "${RED}Unknown command: $1${NC}"
            echo ""
        fi
        print_usage
        exit 1
        ;;
esac

