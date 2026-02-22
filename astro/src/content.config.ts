import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subTitle: z.string().optional(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    categories: z.string(),
    keywords: z.string().optional(),
  }),
});

const book = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    coverImage: z.string().optional(),
    keywords: z.string().optional(),
    purchaseLinks: z
      .array(
        z.object({
          name: z.string(),
          url: z.string(),
        })
      )
      .optional(),
  }),
});

const video = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subTitle: z.string().optional(),
    description: z.string(),
    pubDate: z.coerce.date(),
    youtubeId: z.string(),
    keywords: z.string().optional(),
  }),
});

export const collections = { blog, book, video };

