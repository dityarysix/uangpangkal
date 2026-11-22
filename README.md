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

## Deployment (GitHub Pages)

`.github/workflows/deploy.yml` builds the site and publishes it to GitHub Pages on every push to `main`. The custom domain is set in `public/CNAME`.

DNS at Hostinger for `uangpangkal.com`:

| Type  | Name  | Value                   |
|-------|-------|-------------------------|
| A     | @     | 185.199.108.153         |
| A     | @     | 185.199.109.153         |
| A     | @     | 185.199.110.153         |
| A     | @     | 185.199.111.153         |
| CNAME | www   | dityarysix.github.io    |

To show ads, set the repository variable `PUBLIC_ADSENSE_CLIENT` (Settings → Secrets and variables → Actions → Variables).

`wrangler.jsonc` is kept so the site can also be deployed to Cloudflare if needed.
