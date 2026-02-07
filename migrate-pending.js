#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const PENDING_DIR = path.join(__dirname, 'astro', 'src', 'content', 'pending');
const BLOG_DIR = path.join(__dirname, 'astro', 'src', 'content', 'blog');
const UNPUBLISHED_DIR = path.join(__dirname, 'astro', 'src', 'content', 'unpublished');

/**
 * Parse YAML frontmatter from a markdown file
 */
function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) {
    throw new Error('Invalid frontmatter format');
  }

  const frontmatterStr = match[1];
  const body = match[2];

  const frontmatter = {};
  const lines = frontmatterStr.split('\n');

  for (const line of lines) {
    if (!line.trim()) continue;

    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) continue;

    const key = line.substring(0, colonIndex).trim();
    let value = line.substring(colonIndex + 1).trim();

    // Remove quotes
    if ((value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    frontmatter[key] = value;
  }

  return { frontmatter, body };
}

/**
 * Normalize date format to YYYY-MM-DD
 */
function normalizePubDate(dateStr) {
  if (!dateStr) return '';

  // Already in YYYY-MM-DD format
  if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
    return `'${dateStr}'`;
  }

  // With time: 2008-12-29 14:05:00 +00:00 or similar
  const match = dateStr.match(/^(\d{4}-\d{2}-\d{2})/);
  if (match) {
    return `'${match[1]}'`;
  }

  return `'${dateStr}'`;
}

/**
 * Build normalized frontmatter
 */
function buildFrontmatter(fm) {
  const lines = [];

  // Only include essential fields in standard order
  if (fm.title) lines.push(`title: ${fm.title.startsWith("'") ? fm.title : `'${fm.title}'`}`);
  if (fm.pubDate) lines.push(`pubDate: ${normalizePubDate(fm.pubDate)}`);
  if (fm.categories) lines.push(`categories: '${fm.categories}'`);
  if (fm.keywords) lines.push(`keywords: "${fm.keywords}"`);
  if (fm.description) lines.push(`description: "${fm.description}"`);
  if (fm.published === 'false') lines.push(`published: false`);

  return `---\n${lines.join('\n')}\n---`;
}

/**
 * Process a single pending file
 */
function processPendingFile(filename) {
  const filepath = path.join(PENDING_DIR, filename);

  try {
    const content = fs.readFileSync(filepath, 'utf-8');
    const { frontmatter, body } = parseFrontmatter(content);

    // Normalize frontmatter
    const normalizedFrontmatter = buildFrontmatter(frontmatter);
    const normalizedContent = `${normalizedFrontmatter}\n${body}`;

    // Convert .markdown to .md
    const targetFilename = filename.replace(/\.markdown$/, '.md');

    // Determine destination
    const isUnpublished = frontmatter.published === 'false';
    const targetDir = isUnpublished ? UNPUBLISHED_DIR : BLOG_DIR;
    const targetPath = path.join(targetDir, targetFilename);

    // Write to target
    fs.writeFileSync(targetPath, normalizedContent, 'utf-8');

    // Delete from pending
    fs.unlinkSync(filepath);

    console.log(`✅ ${filename} → ${path.relative(__dirname, targetPath)}${isUnpublished ? ' (unpublished)' : ''}`);

    return { success: true, filename, targetDir, isUnpublished };
  } catch (error) {
    console.error(`❌ ${filename}: ${error.message}`);
    return { success: false, filename, error: error.message };
  }
}

/**
 * Main migration function
 */
function migratePending() {
  console.log('📝 Starting Phase 1: Reconcile Pending Posts\n');

  if (!fs.existsSync(PENDING_DIR)) {
    console.error('❌ Pending directory not found');
    process.exit(1);
  }

  const files = fs.readdirSync(PENDING_DIR)
    .filter(f => f.endsWith('.markdown') || f.endsWith('.md'));

  if (files.length === 0) {
    console.log('✨ No pending posts to migrate');
    return;
  }

  console.log(`Found ${files.length} pending posts to process:\n`);

  const results = files.map(processPendingFile);

  const successful = results.filter(r => r.success).length;
  const failed = results.filter(r => !r.success).length;

  console.log(`\n📊 Summary:`);
  console.log(`✅ Migrated: ${successful}/${files.length}`);
  if (failed > 0) {
    console.log(`❌ Failed: ${failed}/${files.length}`);
  }

  const unpublished = results.filter(r => r.isUnpublished).length;
  if (unpublished > 0) {
    console.log(`🔒 Unpublished: ${unpublished}`);
  }
}

// Run migration
migratePending();

