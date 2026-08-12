import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    tag: z.string(),
    lang: z.string().default('en'),
    ogTitle: z.string().optional(),
  }),
});

export const collections = { blog };
