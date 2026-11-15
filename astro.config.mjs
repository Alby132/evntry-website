import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// English only for now. Add locales back here when a translated page exists.
export default defineConfig({
  site: 'https://evntry.app',
  build: {
    format: 'file',
  },
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !page.includes('/404'),
    }),
  ],
});
