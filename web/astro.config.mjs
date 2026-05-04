// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// GitHub Pages deployment for tastydrinks/cicero-by-claude.
// The site lives at https://tastydrinks.github.io/cicero-by-claude/.
// Both `site` and `base` matter: `site` feeds canonical URLs and the
// sitemap; `base` prefixes every asset and page route so things resolve
// under the project subpath.
export default defineConfig({
  site: 'https://tastydrinks.github.io',
  base: '/cicero-by-claude/',
  trailingSlash: 'always',
  output: 'static',
  integrations: [mdx(), sitemap()],
  build: {
    format: 'directory',
  },
});
