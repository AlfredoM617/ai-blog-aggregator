// @ts-check
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://example.com',
  output: 'server', // ✅ Required for dynamic routing & SSR
  adapter: vercel(), // ✅ Required for deploying to Vercel
  integrations: [mdx(), sitemap()]
});
