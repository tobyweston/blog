#!/bin/bash
# Example: Running your first visual regression test

# This script demonstrates the complete workflow from scratch

echo "=== Cypress Visual Regression Testing - Example Workflow ==="
echo ""

# Step 1: Ensure dependencies are installed
echo "Step 1: Checking dependencies..."
cd /Users/toby/code/github/blog/astro
if [ ! -d "node_modules/cypress" ]; then
    echo "Installing dependencies..."
    npm install
fi
echo "✓ Dependencies ready"
echo ""

# Step 2: Build the site
echo "Step 2: Building the site..."
npm run build
echo "✓ Site built"
echo ""

# Step 3: Start the preview server (in background)
echo "Step 3: Starting preview server..."
npm run preview > /tmp/astro-preview.log 2>&1 &
PREVIEW_PID=$!
echo "Preview server started (PID: $PREVIEW_PID)"
echo "Waiting for server to be ready..."
sleep 5

# Check if server is responding
if curl -s http://localhost:4321 > /dev/null 2>&1; then
    echo "✓ Server is ready at http://localhost:4321"
else
    echo "⚠ Server may still be starting up..."
fi
echo ""

# Step 4: Create baseline screenshots
echo "Step 4: Creating baseline screenshots..."
echo "This will take 2-3 minutes..."
npm run test:visual:baseline
echo "✓ Baselines created"
echo ""

# Step 5: Show what was created
echo "Step 5: Reviewing created files..."
echo ""
echo "Baseline screenshots:"
find cypress/snapshots -name "*.png" -type f | head -10
echo ""

# Step 6: Stop the server
echo "Step 6: Cleaning up..."
kill $PREVIEW_PID 2>/dev/null || true
echo "✓ Preview server stopped"
echo ""

# Final instructions
echo "=== Setup Complete! ==="
echo ""
echo "Your baselines are ready. Next steps:"
echo ""
echo "1. Review the screenshots:"
echo "   open cypress/snapshots/"
echo ""
echo "2. Commit the baselines to git:"
echo "   git add cypress/snapshots/"
echo "   git commit -m 'Add visual regression baselines'"
echo ""
echo "3. To run visual tests (after making changes):"
echo "   npm run preview &"
echo "   npm run test:visual"
echo ""
echo "4. To update baselines (after intentional changes):"
echo "   npm run test:visual:baseline"
echo ""

