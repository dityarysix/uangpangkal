# uangpangkal.com

Private school fees (uang pangkal, SPP) and admission procedures across Indonesia, in Indonesian and English.

- Built with [Astro](https://astro.build) as a static site. The output in `dist/` can be hosted anywhere (Hostinger, Cloudflare Pages, Netlify, Vercel).
- School data lives in `src/content/schools/*.json`, one file per school. The schema is in `src/content.config.ts`, and the build fails if a file doesn't match it.
- A school's area (Jakarta, Tangerang Raya, …) is derived from its `city`; the list lives in `src/lib/areas.ts`.
- School names must be unique. If several campuses share a name (Al-Azhar, BPK Penabur, BINUS…) or the name is common, add the location: "SD Islam Al-Azhar Bekasi".
- Every fee entry must record its `source` (title, URL, publish date), its `academicYear`, and the date it was `checked`. Never estimate fees.

## Commands

```bash
npm install
npm run dev      # local dev server at http://localhost:4321
npm run build    # static site into dist/
```

## Ads and analytics

- AdSense publisher ID and the Google Analytics 4 ID are set in `src/lib/config.ts` (`ADSENSE_CLIENT`, `GA_MEASUREMENT_ID`); the scripts load from `src/layouts/Base.astro`. `public/ads.txt` must stay in place.
- Manual ad units: pass a `slot` to `<AdSlot />`; without one it renders nothing (Auto ads still work).

See `CLAUDE.md` for the full project hand-over (data rules, workflow, scheduled updates).

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

`wrangler.jsonc` is kept so the site can also be deployed to Cloudflare if needed.
