# CLAUDE.md — uangpangkal.com

Read this whole file before doing anything. It is the hand-over from the agent that built the site and
its data with the owner. Follow it exactly; when in doubt, choose the more careful option and ask the owner.

## 1. What this project is

**uangpangkal.com** is a bilingual (Indonesian/English), ad-funded website that compiles **private school
fees** (uang pangkal / entry fee, SPP / tuition, registration and other fees) and **admission procedures**
(SPMB/PPDB steps, documents, tests, dates) for Indonesian private schools (KB/TK up to SMA/SMK).

- Owner: "Adit" (GitHub `dityarysix`). Writes to you in English (sometimes Indonesian). Non-technical:
  give step-by-step guidance with exact menu names when they must act in a web UI (AdSense, Search Console,
  Hostinger, GitHub). Keep answers concise. **The owner wants to save usage** — avoid unnecessary tool calls,
  long outputs and re-reading big files.
- Repo: `dityarysix/uangpangkal` (branch `main`). Every push to `main` deploys to GitHub Pages.
- Domain `uangpangkal.com` is registered at **Hostinger** (DNS: four GitHub Pages A records + `www` CNAME to
  `dityarysix.github.io`; Hostinger's default nameservers stay as they are). HTTPS is enforced in GitHub Pages.
- Status (Nov 2026): **620 schools, 20 areas**, AdSense **approved** (Nov 2026), Google Analytics live,
  Search Console verified with `https://uangpangkal.com/sitemap-index.xml` submitted.

## 2. Stack and repo map

Astro 7 static site, Node 22 (`.node-version`), no client framework.

```
src/content.config.ts      Zod schema for school JSON (build FAILS on any schema error)
src/content/schools/*.json One file per school; file name = slug = URL (/sekolah/<slug>/)
src/lib/areas.ts           AREAS (slug, name id/en, cities). City strings here are the ONLY valid `city` values
src/lib/i18n.ts            UI strings (t), CURRENT_YEAR, paths, rupiah/rupiahShort formatters
src/lib/config.ts          CORRECTION_ENDPOINT (Formspree), CONTACT_EMAIL, ADSENSE_CLIENT, GA_MEASUREMENT_ID
src/lib/schools.ts         allSchools() (throws on duplicate school NAMES), latestFees, minEntryFee, lowestTuition
src/layouts/Base.astro     <head> (SEO, hreflang, AdSense script, GA4 gtag), header nav, footer
src/views/*.astro          Home, AreaView, SchoolView, CorrectionView, PrivacyView, AboutView
src/pages/...              Thin route files: / , /wilayah/[area]/, /sekolah/[slug]/, /tentang/, /koreksi/,
                           /kebijakan-privasi/, and English /en/, /en/area/, /en/school/, /en/about/,
                           /en/correction/, /en/privacy/, plus 404
src/components/            SchoolCard.astro, AdSlot.astro (renders an AdSense unit only when given `slot`)
public/                    CNAME, ads.txt, robots.txt, favicon.svg, _headers
astro.config.mjs           site URL, @astrojs/sitemap, `redirects` for renamed/removed area URLs
scripts/seedlib.py         Helpers used by every seed script (see §4)
scripts/seed_*.py          One script per research batch; re-runnable; the record of where data came from
scripts/research/          html2text.py, feeblocks.py, tables.py, stats.py (see §6)
.github/workflows/deploy.yml  build + deploy to GitHub Pages on push to main
wrangler.jsonc             Kept only in case the owner ever moves to Cloudflare; unused
```

Commands: `npm ci` (first time), `npx astro build` (must pass before every commit). `npm run dev` for local preview.

## 3. Areas (src/lib/areas.ts)

20 areas: jakarta, tangerang-raya, depok-bogor-raya, bekasi-raya, serang-raya, bandung-raya, tasikmalaya-raya,
semarang-raya, surabaya-raya, malang-raya, yogyakarta-raya, solo-raya, medan-raya, pekanbaru-raya,
padang-raya, batam-raya, palembang-raya, bali, samarinda-raya, makassar-raya. Each lists its exact city
strings (e.g. 'Jakarta Selatan', 'Kota Bekasi', 'Kabupaten Bekasi', 'Surakarta (Solo)', 'Balikpapan',
'Kota Denpasar', 'Badung', 'Ogan Ilir', 'Bukittinggi'). Always open the file to copy a city string exactly.

- Owner decisions: area cards never say "dan sekitarnya"; Bandar Lampung Raya was **replaced by Bali**
  (redirect `/wilayah/bandar-lampung-raya` → `/wilayah/bali/` is in astro.config.mjs). Samarinda Raya
  includes Balikpapan, Bontang and Kutai Kartanegara.
- The home page shows only areas that have ≥1 school. Adding/renaming an area: edit areas.ts, add redirects
  for any changed slug, rebuild. Never remove a city that schools still use (build fails).

## 4. Data model and how to add data

### Schema essentials (see src/content.config.ts)
School: `name` (unique across the site), `city` (from areas.ts), optional `district`, `address`, `npsn`,
`levels` (KB, TK, SD, SMP, SMA, SMK), `curriculum` (we use 'Nasional', 'Cambridge', 'IB', 'Internasional'),
`religion` (Umum, Islam, Kristen, Katolik, Buddha, Hindu), `website`, `phone`, `fees[]`, `admission[]`.

Fee entry: `level`, `academicYear` "YYYY/YYYY", optional `yearAssumed`, `registrationFee`,
`entryFee {min, max?}`, `tuition {amount, period: month|quarter|semester|year}`, `otherFees[{label{id,en}, amount}]`,
`notes{id,en}`, `source{title, url, published?}`, `checked` "YYYY-MM-DD". Amounts are integer rupiah.

Admission entry: `level?`, `academicYear`, `period{id,en}?`, `steps[{id,en}]`, `documents[{id,en}]`,
`test{id,en}?`, `notes{id,en}?`, `source`, `checked`.

### Always add data through a seed script using scripts/seedlib.py
- `upsert(slug, *, name, city, level, year, source, checked, district=, address=, website=, phone=, religion=,
  curriculum=, yearAssumed=, registrationFee=, entryFee=, tuition=, otherFees=, notes=)` — creates/merges the
  school file and adds the fee entry. An existing entry with the **same level + academicYear + source URL is
  replaced**; anything else is appended. Older entries are never deleted. School fields passed as `None`
  (district, address, website, phone, religion) are ignored, but **fee fields passed as `None` are written as
  `null` and break the build** — omit fee keys you don't have (e.g. `**({"registrationFee": x} if x else {})`).
- `ensure_school(slug, *, name, city, levels, **fields)` — school record without fees (admission-only schools).
- `add_admission(slug, entry)` — add/replace an admission entry (matched on level + year + source URL).
- Helpers: `L(id, en)`, `fee(label_id, label_en, amount)`, tuples `UNIFORM`, `BOOKS`, `ACTIVITY`.
- Write a NEW script per batch, e.g. `scripts/seed_monthly_2026_12.py`, with a module docstring listing every
  source (title, URL, publish date) and how the academic year was decided. Run it from `scripts/`
  (`cd scripts && python3 seed_x.py`). Never hand-edit JSON for new data; small fixes to an existing
  script + re-run are fine (scripts are idempotent).
- Pattern used in many scripts: a small local helper `s(slug, name, city, district, address, source, year, ...)`
  that appends a standard caution note to every entry from the same source. Copy that style.
- When adding to a school that already exists, reuse its slug and exact current `name` and `city`
  (read the JSON first, or look it up with grep). Check for duplicates before creating any new school:
  `grep -il "<keyword>" src/content/schools/*.json` and `python3 scripts/research/stats.py`.

### Slugs and names
- Slug: lowercase, hyphenated, include the place for anything that could be ambiguous
  (`sd-islam-al-azhar-35-surabaya`, `sdk-penabur-gading-serpong`).
- **Same-name/chain schools must include the location in the name**: "SD Islam Al-Azhar Bekasi",
  "Sekolah Dian Harapan Medan", "SMA Muhammadiyah 4 Depok". `allSchools()` throws on duplicate names.
- Multi-level schools (TK–SMA under one yayasan/campus) are ONE record with several fee entries/levels,
  unless they are clearly separate campuses with different addresses.

## 5. Data rules (the owner's requirements — non-negotiable)

1. **Every figure has a source and an academic year.** Show the year exactly as the source states it.
   If the source does not state it, infer from context/publish date, set `yearAssumed: true`, and say how
   in the notes (e.g. "published Oct 2023 → 2023/2024 (assumed)"). Prefer the newest year; the target is
   the coming year (currently **2027/2028**), otherwise 2026/2027 or older — older data is allowed but
   must be labelled.
2. **Estimates and ranges are fine** (use entryFee min/max, notes for details) but must keep year + source.
   Never invent or "estimate" a number that is not in a source.
3. **Verify location from the page itself** (address, kecamatan, kota/kabupaten). Search-engine summaries
   frequently put schools in the wrong city (e.g. Al-Falaah turned out to be Ciputat, Mutiara Insani is
   Klaten, MIAS's page says "Kab." but Cihideung is Kota Tasikmalaya). If the city cannot be confirmed,
   do not add the school (or ask).
4. **Notes are bilingual** (`id` and `en`), short, factual: what the entry fee consists of, alternative
   tiers (gelombang/early bird, internal/external, putra/putri, boarding/fullday), caveats, typos in the
   source and how you read them (e.g. "artikel menulis Rp12.000.0000 (dibaca Rp12.000.000)").
5. **Mapping conventions**:
   - entryFee = uang pangkal / uang gedung / DSP / DPP / dana pengembangan / infaq pembangunan / sarana /
     capital fee (one-off). If several one-off parts exist, sum them only when the source clearly presents
     them as the entry cost; otherwise put the main one in entryFee and the rest in otherFees.
   - registrationFee = formulir/pendaftaran/tes. A big "biaya pendaftaran" that is obviously the entry
     package (e.g. Rp28 juta) goes to entryFee with a note saying so.
   - tuition = SPP / uang sekolah, with the right period (month/quarter/semester/year). If a source says
     "per tahun" for an amount that is obviously monthly, keep it monthly and note it.
   - A total that is not itemised (e.g. "estimasi biaya Rp7 juta") → otherFees "Estimasi biaya (tidak dirinci)".
   - Levels: MI → SD, MTs → SMP, MA → SMA (keep "MTs"/"MA" in the name). Pesantren with formal schools:
     one record, entries for the levels offered.
   - Fee 0 is only for government free-school programmes (Banten Sekolah Gratis, Pekanbaru partner SMPs);
     the site shows 0 as "Gratis"/"Free". Always add the note that it applies only to students admitted
     through the programme and that regular fees may differ.
6. **Do not copy competitor directories**: biayasekolah.id, bukusekolah.id, skulmu.com (owner agreed they
   may at most be used as a lead list of school names for empty cities; the data must come from the
   school's own or another original source).
7. **Do not bypass blocks**: sites that return 403/captcha to automated access stay unused (Kumparan,
   Tirto, timedoor, UlasBandung, Batamnews, makassarkota.go.id, Kemendikdasmen portal with captcha).
   Do not retry them with tricks.
8. **Skip unreliable sources and suspicious figures**: e.g. wartamakassar.com list (gave fees for public
   schools), harga.web.id (AI-generated filler), mejasekolah.com and smp5saketi.com (generic/spam),
   "SD Islam Al-Falaah Cipayung" Rp88 jt/Rp62,4 jt per year (looks mislabelled, repeated by copy blogs).
   Blogs that recycle old figures under a new year (Lembar Kerja Untuk Anak) were used only with the older
   year the content implies + yearAssumed + a caution note.
9. **Source priority**: (1) school's own SPMB/PPDB/fees page or PDF/brochure image; (2) local news/
   government lists (partner/free schools); (3) parenting/media lists (HaiBunda, Orami, Popmama,
   theAsianparent, Gebrak, CNBC, IDN Times, Akurat, SobatSekolah, Nakita, Data Pendidikan, Lokalfinds for
   Bali international schools). Official data wins; keep older article entries as history.
10. Schools with no published fees can be admission-only records (`ensure_school` + `add_admission`) when
    a credible source gives admission info (e.g. Tasikmalaya SSK partner SMAs, Dian Harapan campuses).
11. `checked` = the date you actually looked at the source. Never bump `checked` without re-verifying.

## 6. Research workflow (what works)

- Use WebSearch (standard; "extended" for niche cities) to find sources, then fetch pages with curl:
  `curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36" -m 30 -o page.html "<url>"`
  (WebFetch-type subagents have failed in this environment; curl works).
- Save downloads in your scratchpad directory, never in the repo. Convert and inspect with the repo helpers:
  - `python3 -I scripts/research/html2text.py page.html > page.txt`
  - `python3 -I scripts/research/feeblocks.py page.txt` (numbered list items that contain Rp figures)
  - `python3 -I scripts/research/tables.py page.html` (fee tables on school sites)
  - `grep -oE '"datePublished":"[^"]{10}' page.html` to get the publish date.
- Fee tables are often images or image-PDFs: download the image / `pdftoppm -r 110 -png file.pdf out`,
  then view it with the Read tool and transcribe carefully.
- Many school SPMB sites are JavaScript apps (no data in HTML) — move on.
- Good discovery queries: `"SPMB 2027/2028" "uang pangkal" <kota>`, `"<kota>" PPDB rincian biaya`,
  `biaya masuk SD swasta <kota> <year>`, theAsianparent `id.theasianparent.com/sd-swasta-di-<kota>`,
  HaiBunda "20 SD negeri dan swasta <kota> akreditasi ... estimasi biaya", Orami
  `orami.co.id/magazine/sd-swasta-<kota>`, school-group pages listing several units (YABICA, Ibadurrahman,
  Al-Ittihad, Ulil Albab, Adzkia, Al Fitrah), government partner/free-school lists (Balikpapan, Banten,
  Pekanbaru, Jabar SSK).
- `python3 scripts/research/stats.py` → counts per area and per year; `--stale 60` → the 60 schools with the
  oldest data (for the monthly refresh).

## 7. Site behaviour you must keep working

- **Area pages** (`src/views/AreaView.astro`): short H1 "Biaya Sekolah Swasta di <Area>" /
  "Private School Fees in <Area>"; the `<title>` keeps "— Uang Pangkal & SPP" for SEO. The intro paragraphs
  are **computed from the data at build time**: number of schools, list of cities with schools, school types
  present (Islam terpadu / Katolik & Kristen / Buddhis / Hindu / internasional → "sangat beragam dan
  berwarna" only with ≥3 types), and for SD, SMP, SMA the lowest–highest entry fee and monthly SPP using the
  latest entry per school, excluding zero (free-programme) amounts, shown only when ≥2 schools have the
  figure; plus "Sebanyak N sekolah sudah memiliki data tahun ajaran <CURRENT_YEAR-1> atau lebih baru".
  **Never hardcode numbers** (no medians — owner asked to remove them); levels without data are skipped.
- **Home hero** (`i18n.ts` heroTitle/heroLead): "Berapa biaya masuk sekolah swasta?" / "Bandingkan uang
  pangkal, SPP, dan prosedur pendaftaran lebih dari 600 sekolah swasta di 20 kota besar di Indonesia."
  Update the number only if the owner asks (or when it passes a round milestone, ask first).
- **CURRENT_YEAR** in i18n.ts = '2027/2028' (the "latest fees" badge and the recent-data sentence use it).
  Move it forward one year when the next SPMB cycle starts (around August–September), after asking the owner.
- Zero fees display as "Gratis"/"Free" (SchoolView and SchoolCard handle registration, entry and tuition).
- Correction form posts JSON to Formspree `https://formspree.io/f/mjywayed` (free plan: 50 submissions/month)
  with a `_gotcha` honeypot; contact email `info@uangpangkal.com` (Hostinger mail). Privacy policy page
  covers hosting, Formspree, Google Analytics and AdSense cookies — update it if you add any tracker/service.
- SEO: sitemap via @astrojs/sitemap, hreflang id/en, JSON-LD on school pages.

## 8. Ads and analytics (do not break)

- **AdSense**: publisher `ca-pub-4160138577851742` (in `src/lib/config.ts`; the script is in Base.astro
  `<head>`). `public/ads.txt` = `google.com, pub-4160138577851742, DIRECT, f08c47fec0942fa0`.
  **Never remove or change these.** Site approved Nov 2026; Auto ads appear to be on (Google inserts
  `ins.adsbygoogle`). Manual units: `<AdSlot slot="<data-ad-slot>" />` exists in Home, AreaView, SchoolView
  but renders nothing until the owner creates a Display ad unit and gives you its `data-ad-slot` number —
  then set it in those three places (consider a constant in config.ts). Never click ads or suggest anyone does.
  (The `PUBLIC_ADSENSE_CLIENT` env line in deploy.yml is obsolete and harmless.)
- **Google Analytics 4**: `G-DMXW2LLD0M` (config.ts, gtag in Base.astro).
- The owner checks AdSense/GA/Search Console via screenshots. They may later connect their own computer
  (Claude desktop app + Claude in Chrome) so an agent can operate their logged-in browser. Never ask for
  their Google password or 2-step codes.

## 9. Commit, push, deploy

```bash
npx astro build                     # must print "Complete!" with no errors
git add -A
git -c user.name="dityarysix" -c user.email="dityarysix@users.noreply.github.com" commit -m "<short summary>"
git push                             # deploys automatically (about 1–2 minutes)
```
- Add the commit attribution lines your environment instructs you to add (if any). Never put a model name
  in commit messages, code or pages.
- Commit after each coherent batch (don't leave work uncommitted; the cloud container is temporary).
- To confirm a deploy: `gh run list --repo dityarysix/uangpangkal --limit 1`, then
  `gh run watch <id> --repo dityarysix/uangpangkal --exit-status`, then curl the live page.

## 10. Scheduled monthly update (already set up — don't duplicate)

Two scheduled tasks start a fresh session that refreshes data (owner chose the "current" size):
- `trig_017Nj6RdJbte8yigGrQMPiPS` — day 29 of every month, 10:17 WIB (Asia/Jakarta).
- `trig_016VC5sRmbonuLGLtJgCEniD` — 28 February, 10:17 WIB (skips itself if a February update already ran).
Each run: refresh ~60 schools with the oldest data (look for newer official fees; add entries, never delete),
add 20–40 new schools (thin areas first), follow every rule in this file, write
`scripts/seed_monthly_YYYY_MM.py`, build, commit, push, and finish with a short summary (refreshed schools,
new schools per area, new total, problems). Push notifications go to the owner's phone.

### Scholarship info (added Nov 2026)
- Home-page panel "Info Beasiswa" (left side rail on wide screens, collapsible block on small screens) + full pages
  `/beasiswa/` and `/en/scholarships/`. Data: `src/lib/beasiswa.ts` (read its header comment first). Panel and
  guide texts for the free-private-school plan: `src/lib/guide.ts` (guide pages `/panduan/sekolah-swasta-gratis-2027/`,
  `/en/guide/free-private-schools-2027/`).
- Rules (owner's): information ONLY from the scholarship provider's own official site/page (or an official
  press release on the provider's domain); never copy figures from media/aggregators (indbeasiswa, dealls etc.);
  focus SMA/SMK and university; every item has a link to the official site; summaries are drafted by a Haiku
  subagent from the extracted official text and verified by you; nothing that is not on the page (no amounts,
  dates, quotas). Sites that block automated access (Bank Indonesia, SatuBeasiswa, Djarum for bots) are not
  bypassed; Djarum is included from a screenshot of its official page supplied by the owner.
- A third scheduled task `trig_01H4Ph86VMpcUNMP8noRZQ3L` ("Update info beasiswa (akhir bulan)") fires on days
  28-31 at 10:41 WIB; it only works on the LAST day of the month (first real run 30 Nov 2026): re-checks every
  item, adds up to 5 new official providers, builds, opens a PR and merges it. Do not duplicate it.

## 11. Backlog / known gaps (Nov 2026)

- Thin areas: Batam 6, Padang 9, Palembang 13, Bali 13, Makassar 13, Semarang 15, Medan 18, Samarinda 18.
  Batam school sites (SGIA, Kallista, BTB) were unreachable; Monte Sienna, Mondial, Yos Sudarso, Yehonala,
  AIS, Ulil Albab are in. Makassar's official list of 55 partner private SMPs (makassarkota.go.id, June 2026)
  is blocked — look for a news copy with names.
- Unused lists with names (no fees, partner programmes): Jabar SSK lists for Garut (71) and
  Ciamis/Banjar/Pangandaran (100) on Tribun Jabar; Kabupaten Serang SMA/SMK and Pandeglang lists of Banten
  Sekolah Gratis (Sindonews/Tribun Banten). Add only if the owner wants more admission-only/free-programme
  records — prefer schools with real fees.
- 18 Tasikmalaya SSK SMAs are admission-only; replace with fees when found.
- Ideas the owner deferred: outreach to schools to send official fees; a home-page/area "guide" content
  section (partly done via the computed area intro); manual AdSense units (waiting for slot id).
- Ad placement: keep layout clean — no vignette/anchor ads recommended to the owner.

## 12. Behaviour with the owner

- Reply in the owner's language (usually English); site content is always bilingual.
- Before outward-facing or irreversible actions (changing DNS advice, deleting data, sharing anything,
  contacting schools), explain and get the owner's OK.
- Report honestly: what was added, from which sources, what was skipped and why, what failed.
- Keep it economical: batch fetches, read only the parts of files you need, don't re-run whole builds
  more than necessary, don't print huge outputs.
