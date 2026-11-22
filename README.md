# uangpangkal.com

Private school fees (uang pangkal, SPP) and admission procedures across Indonesia, in Indonesian and English.

- Built with [Astro](https://astro.build) as a static site. The output in `dist/` can be hosted anywhere (Hostinger, Cloudflare Pages, Netlify, Vercel).
- School data lives in `src/content/schools/*.json`, one file per school. The schema is in `src/content.config.ts`, and the build fails if a file doesn't match it.
- Every fee entry must record its `source` (title, URL, publish date), its `academicYear`, and the date it was `checked`. Never estimate fees.

## Commands

```bash
npm install
npm run dev      # local dev server at http://localhost:4321
npm run build    # static site into dist/
```

## Ads

Set `PUBLIC_ADSENSE_CLIENT=ca-pub-XXXXXXXX` at build time and pass a `slot` to `<AdSlot />` to show AdSense units. Until then, placeholders are shown.

## URLs

| Page   | Indonesian           | English              |
|--------|----------------------|----------------------|
| Home   | `/`                  | `/en/`               |
| Area   | `/wilayah/<area>/`   | `/en/area/<area>/`   |
| School | `/sekolah/<slug>/`   | `/en/school/<slug>/` |
| About  | `/tentang/`          | `/en/about/`         |

## Deployment (Cloudflare Pages)

Cloudflare Pages is connected to this repository, so every push to `main` rebuilds the site and publishes it.

- Build command: `npm run build`
- Build output directory: `dist`
- Node version: set by `.node-version` (22)
- Optional environment variable: `PUBLIC_ADSENSE_CLIENT`
