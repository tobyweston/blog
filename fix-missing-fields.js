#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const BLOG_DIR = path.join(__dirname, 'astro', 'src', 'content', 'blog');
const UNPUBLISHED_DIR = path.join(__dirname, 'astro', 'src', 'content', 'unpublished');

function addMissingFields(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return content;

  let fm = match[1];
  const body = match[2];

  const fields = {};
  const lines = fm.split('\n');

  for (let line of lines) {
    if (!line.trim()) continue;
    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) continue;

    const key = line.substring(0, colonIdx).trim();
    let value = line.substring(colonIdx + 1).trim();
    fields[key] = value;
  }

  // Fix mismatched quotes in existing fields
  for (const key in fields) {
    let value = fields[key];
    // Fix closing quotes
    if (value.startsWith('"') && value.endsWith("'")) {
      value = value.substring(0, value.length - 1) + '"';
    } else if (value.startsWith("'") && value.endsWith('"')) {
      value = '"' + value.substring(1, value.length - 1) + '"';
    }
    fields[key] = value;
  }

  // Add missing required fields
  if (!fields.description) {
    fields.description = '""';
  }
  if (!fields.keywords) {
    fields.keywords = '""';
  }

  // Build new frontmatter in order
  const newLines = [];
  const order = ['title', 'pubDate', 'categories', 'keywords', 'description', 'published'];

  for (const key of order) {
    if (key in fields && fields[key]) {
      newLines.push(`${key}: ${fields[key]}`);
    }
  }

  // Add any other fields not in our list
  for (const key in fields) {
    if (!order.includes(key) && fields[key]) {
      newLines.push(`${key}: ${fields[key]}`);
    }
  }

  const newFm = newLines.join('\n');
  return `---\n${newFm}\n---\n${body}`;
}

function processDirectory(dir) {
  const files = fs.readdirSync(dir).filter(f => (f.endsWith('.md') || f.endsWith('.mdx')) && !f.startsWith('.'));
  let fixed = 0;

  for (const file of files) {
    const filepath = path.join(dir, file);
    try {
      const content = fs.readFileSync(filepath, 'utf-8');
      const fixed_content = addMissingFields(content);

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

console.log('🔧 Adding missing required fields\n');

const blogFixed = processDirectory(BLOG_DIR);
console.log('');
const unpublishedFixed = processDirectory(UNPUBLISHED_DIR);

console.log('\n✅ Total fixed: ' + (blogFixed + unpublishedFixed) + ' files');

