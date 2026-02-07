#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const BLOG_DIR = path.join(__dirname, 'astro', 'src', 'content', 'blog');
const UNPUBLISHED_DIR = path.join(__dirname, 'astro', 'src', 'content', 'unpublished');

function fixYAMLFrontmatter(content) {
  // Split on the frontmatter boundary
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return content;

  let fm = match[1];
  const body = match[2];

  // Fix mismatched quotes and ensure proper YAML
  // For each field: key: value, ensure value has matching quotes

  const lines = fm.split('\n');
  const fixedLines = [];

  for (let line of lines) {
    if (!line.trim()) {
      fixedLines.push(line);
      continue;
    }

    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) {
      fixedLines.push(line);
      continue;
    }

    const key = line.substring(0, colonIdx).trim();
    let value = line.substring(colonIdx + 1).trim();

    // Check for mismatched or problematic quotes
    if (value) {
      // If it starts and ends with single quote but doesn't have matching quotes
      if (value.startsWith("'") && !value.endsWith("'")) {
        value = '"' + value.substring(1);
      } else if (value.startsWith('"') && !value.endsWith('"')) {
        value = value + '"';
      }
      // If it starts with double quote but ends with single
      else if (value.startsWith('"') && value.endsWith("'")) {
        value = value.substring(0, value.length - 1) + '"';
      }
      // If it starts with single quote but ends with double
      else if (value.startsWith("'") && value.endsWith('"')) {
        value = '"' + value.substring(1, value.length - 1) + '"';
      }

      // Ensure all quotes are properly paired
      // If value contains special chars but isn't quoted, quote it
      if (value.includes(':') || value.includes('#') || value.includes('-')) {
        if (!value.startsWith('"') && !value.startsWith("'")) {
          value = '"' + value + '"';
        }
      }
    }

    fixedLines.push(`${key}: ${value}`);
  }

  const newFm = fixedLines.join('\n');
  return `---\n${newFm}\n---\n${body}`;
}

function processDirectory(dir) {
  const files = fs.readdirSync(dir).filter(f => (f.endsWith('.md') || f.endsWith('.mdx')) && !f.startsWith('.'));
  let fixed = 0;

  for (const file of files) {
    const filepath = path.join(dir, file);
    try {
      const content = fs.readFileSync(filepath, 'utf-8');
      const fixed_content = fixYAMLFrontmatter(content);

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

console.log('🔧 Comprehensive YAML frontmatter fix\n');

const blogFixed = processDirectory(BLOG_DIR);
console.log('');
const unpublishedFixed = processDirectory(UNPUBLISHED_DIR);

console.log('\n✅ Total fixed: ' + (blogFixed + unpublishedFixed) + ' files');

