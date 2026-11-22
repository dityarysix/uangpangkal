// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://uangpangkal.com',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
  // Old area URLs from the first launch.
  redirects: {
    '/wilayah/jabodetabek': '/wilayah/jakarta/',
    '/en/area/jabodetabek': '/en/area/jakarta/',
    '/wilayah/bandung': '/wilayah/bandung-raya/',
    '/en/area/bandung': '/en/area/bandung-raya/',
    '/wilayah/semarang': '/wilayah/semarang-raya/',
    '/en/area/semarang': '/en/area/semarang-raya/',
    '/wilayah/surabaya': '/wilayah/surabaya-raya/',
    '/en/area/surabaya': '/en/area/surabaya-raya/',
    '/wilayah/yogyakarta': '/wilayah/yogyakarta-raya/',
    '/en/area/yogyakarta': '/en/area/yogyakarta-raya/',
    '/wilayah/bandar-lampung-raya': '/wilayah/bali/',
    '/en/area/bandar-lampung-raya': '/en/area/bali/',
  },
});
