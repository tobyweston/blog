#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const OCTOPRESS_DIR = path.join(__dirname, 'source', '_posts');
const BLOG_DIR = path.join(__dirname, 'astro', 'src', 'content', 'blog');
const UNPUBLISHED_DIR = path.join(__dirname, 'astro', 'src', 'content', 'unpublished');

/**
 * Parse YAML frontmatter from Octopress format
 */
function parseOctopressFrontmatter(content) {
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

    // Remove quotes if present
    if ((value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    frontmatter[key] = value;
  }

  return { frontmatter, body };
}

/**
 * Extract date from filename or frontmatter
 */
function extractDate(filename, frontmatter) {
  const match = filename.match(/^(\d{4}-\d{2}-\d{2})/);
  if (match) {
    return match[1];
  }

  if (frontmatter.date) {
    const dateMatch = frontmatter.date.match(/^(\d{4}-\d{2}-\d{2})/);
    if (dateMatch) return dateMatch[1];
  }

  return '';
}

/**
 * Build normalized Astro frontmatter
 */
function buildAstroFrontmatter(fm, filename) {
  const lines = [];

  if (fm.title) lines.push(`title: ${fm.title.startsWith("'") ? fm.title : `'${fm.title}'`}`);

  const pubDate = extractDate(filename, fm);
  if (pubDate) lines.push(`pubDate: '${pubDate}'`);

  if (fm.categories) {
    const cats = fm.categories.trim();
    // Convert comma-separated to space-separated if needed
    const normalized = cats.split(',').map(c => c.trim()).join(' ');
    lines.push(`categories: '${normalized}'`);
  }

  if (fm.keywords) lines.push(`keywords: "${fm.keywords}"`);
  if (fm.description) lines.push(`description: "${fm.description}"`);

  if (fm.published === 'false') lines.push(`published: false`);

  return `---\n${lines.join('\n')}\n---`;
}

/**
 * Process a single Octopress file
 */
function processOctopressFile(filename) {
  const filepath = path.join(OCTOPRESS_DIR, filename);

  try {
    const content = fs.readFileSync(filepath, 'utf-8');
    const { frontmatter, body } = parseOctopressFrontmatter(content);

    // Build new frontmatter
    const newFrontmatter = buildAstroFrontmatter(frontmatter, filename);
    const newContent = `${newFrontmatter}\n${body}`;

    // Determine destination
    const isUnpublished = frontmatter.published === 'false';
    const targetDir = isUnpublished ? UNPUBLISHED_DIR : BLOG_DIR;
    const targetFilename = filename.replace(/\.markdown$/, '.md');
    const targetPath = path.join(targetDir, targetFilename);

    // Write to target
    fs.writeFileSync(targetPath, newContent, 'utf-8');

    console.log(`✅ ${filename} → ${targetDir}/${targetFilename}${isUnpublished ? ' (unpublished)' : ''}`);

    return { success: true, filename, targetDir, isUnpublished };
  } catch (error) {
    console.error(`❌ ${filename}: ${error.message}`);
    return { success: false, filename, error: error.message };
  }
}

/**
 * Main migration function
 */
function migrateOctopress() {
  console.log('📝 Starting Phase 2: Migrate Remaining Octopress Posts\n');

  if (!fs.existsSync(OCTOPRESS_DIR)) {
    console.error('❌ Octopress directory not found');
    process.exit(1);
  }

  const files = fs.readdirSync(OCTOPRESS_DIR)
    .filter(f => f.endsWith('.markdown') || f.endsWith('.md'));

  if (files.length === 0) {
    console.log('✨ No Octopress posts to migrate');
    return;
  }

  console.log(`Found ${files.length} Octopress posts to migrate:\n`);

  const results = files.map(processOctopressFile);

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
migrateOctopress();

