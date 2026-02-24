import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    urlSlug: z.string(),
    translationKey: z.string(),
    lang: z.enum(['ko', 'en']),
    date: z.date(),
    lastModified: z.date().optional(),
    excerpt: z.string(),
    tags: z.array(z.string()),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog: blogCollection };
