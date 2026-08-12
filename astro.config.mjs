import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://evntry.app',
  build: {
    format: 'file',
  },
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'de', 'it', 'pl', 'hr', 'sl'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
  integrations: [
    mdx(),
    sitemap({
      i18n: {
        defaultLocale: 'en',
        locales: {
          en: 'en-GB',
          de: 'de-DE',
          it: 'it-IT',
          pl: 'pl-PL',
          hr: 'hr-HR',
          sl: 'sl-SI',
        },
      },
    }),
  ],
});
