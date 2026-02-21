import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import type { CollectionEntry } from 'astro:content';

export const GET: APIRoute = async ({ url }) => {
  const offset = parseInt(url.searchParams.get('offset') || '0');
  const limit = parseInt(url.searchParams.get('limit') || '12');

  const posts = (await getCollection('blog')) as CollectionEntry<'blog'>[];
  posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

  const paginatedPosts = posts.slice(offset, offset + limit);
  const hasMore = offset + limit < posts.length;

  // Transform posts to a serializable format
  const serializedPosts = paginatedPosts.map(post => ({
    slug: post.slug,
    title: post.data.title,
    subTitle: post.data.subTitle,
    description: post.data.description,
    pubDate: post.data.pubDate.toISOString(),
    categories: post.data.categories,
    heroImage: post.data.heroImage,
  }));

  return new Response(JSON.stringify({
    posts: serializedPosts,
    hasMore,
    nextOffset: offset + limit,
  }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    },
  });
};

