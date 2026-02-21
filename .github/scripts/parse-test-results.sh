#!/bin/bash

# Parse Cypress test results and create GitHub annotations
# This script reads JUnit XML files and outputs GitHub Actions annotations

RESULTS_DIR="astro/cypress/results"

if [ ! -d "$RESULTS_DIR" ]; then
  echo "No test results found"
  exit 0
fi

# Find all XML result files
for xml_file in "$RESULTS_DIR"/*.xml; do
  if [ -f "$xml_file" ]; then
    echo "Processing $xml_file..."

    # Parse failures from JUnit XML and create annotations
    # Extract test case failures
    failures=$(grep -o '<testcase.*</testcase>' "$xml_file" | grep 'failure')

    if [ ! -z "$failures" ]; then
      echo "$failures" | while IFS= read -r line; do
        # Extract test name
        test_name=$(echo "$line" | sed -n 's/.*name="\([^"]*\)".*/\1/p')
        # Extract failure message
        failure_msg=$(echo "$line" | sed -n 's/.*<failure[^>]*>\(.*\)<\/failure>.*/\1/p' | head -c 200)
        # Extract classname (test suite)
        classname=$(echo "$line" | sed -n 's/.*classname="\([^"]*\)".*/\1/p')

        if [ ! -z "$test_name" ]; then
          echo "::error title=Test Failed: $test_name::$classname - $failure_msg"
        fi
      done
    fi
  fi
done

# Count total failures and passes
total_tests=$(find "$RESULTS_DIR" -name "*.xml" -exec grep -c '<testcase' {} + | awk '{s+=$1} END {print s}')
total_failures=$(find "$RESULTS_DIR" -name "*.xml" -exec grep -c '<failure' {} + | awk '{s+=$1} END {print s}')
total_passes=$((total_tests - total_failures))

echo ""
echo "Test Summary:"
echo "✅ Passed: $total_passes"
echo "❌ Failed: $total_failures"
echo "📊 Total: $total_tests"

if [ $total_failures -gt 0 ]; then
  echo "::warning::$total_failures test(s) failed"
  exit 1
fi

exit 0

