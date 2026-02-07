#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const BLOG_DIR = path.join(__dirname, 'astro', 'src', 'content', 'blog');
const UNPUBLISHED_DIR = path.join(__dirname, 'astro', 'src', 'content', 'unpublished');

function fixYAMLQuotes(content) {
  // Replace title: 'text with apostrophe' with title: "text with apostrophe"
  content = content.replace(/title:\s+'([^']*'[^']*)'/g, 'title: "$1"');

  // Handle other fields that might have quotes
  content = content.replace(/description:\s+'([^']*'[^']*)'/g, 'description: "$1"');
  content = content.replace(/keywords:\s+'([^']*'[^']*)'/g, 'keywords: "$1"');

  return content;
}

function processDirectory(dir) {
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.md') || f.endsWith('.mdx'));
  let fixed = 0;

  for (const file of files) {
    const filepath = path.join(dir, file);
    try {
      const content = fs.readFileSync(filepath, 'utf-8');
      const fixed_content = fixYAMLQuotes(content);

      if (content !== fixed_content) {
        fs.writeFileSync(filepath, fixed_content, 'utf-8');
        console.log('✅ Fixed: ' + file);
        fixed++;
      }
    } catch (error) {
      console.error('❌ Error processing ' + file + ': ' + error.message);
    }
  }

  return fixed;
}

console.log('🔧 Fixing YAML quote issues\n');

const blogFixed = processDirectory(BLOG_DIR);
console.log('');
const unpublishedFixed = processDirectory(UNPUBLISHED_DIR);

console.log('\n✅ Total fixed: ' + (blogFixed + unpublishedFixed) + ' files');

