// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import rehypeMermaid from 'rehype-mermaid';

import sitemap from '@astrojs/sitemap';
import { readFileSync } from 'node:fs';

// Shiki ships no Rego grammar, so load our own TextMate definition.
const rego = JSON.parse(
	readFileSync(new URL('./src/syntax/rego.tmLanguage.json', import.meta.url), 'utf8'),
);

// https://astro.build/config
export default defineConfig({
	site: 'https://baddotrobot.com',
	integrations: [mdx(), sitemap(), tailwind()],
	markdown: {
		syntaxHighlight: {
			type: 'shiki',
			excludeLangs: ['mermaid'],
		},
		shikiConfig: {
			langs: [rego],
		},
		rehypePlugins: [[rehypeMermaid, { strategy: 'inline-svg' }]],
	},
	redirects: {
		'/': '/blog',
	},
});
