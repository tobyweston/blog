import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE_TITLE, SITE_DESCRIPTION } from '../consts';

export async function GET(context) {
	const posts = await getCollection('blog');
	// Filter entries to ensure each item has at least a title or description
	const items = posts
		.filter(post => {
			const title = post.data?.title;
			const desc = post.data?.description;
			return (title && String(title).trim().length > 0) || (desc && String(desc).trim().length > 0);
		})
		.map(post => ({
			title: post.data.title || undefined,
			description: post.data.description || undefined,
			pubDate: post.data.pubDate,
			link: `/blog/${post.slug}/`,
		}));

	return rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site: context.site,
		items,
	});
}
