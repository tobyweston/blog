// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import rehypeMermaid from 'rehype-mermaid';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
	site: 'https://baddotrobot.com',
	integrations: [mdx(), sitemap(), tailwind()],
	markdown: {
		syntaxHighlight: {
			type: 'shiki',
			excludeLangs: ['mermaid'],
		},
		rehypePlugins: [[rehypeMermaid, { strategy: 'inline-svg' }]],
	},
	redirects: {
		'/': '/blog',
	},
});
