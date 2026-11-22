"""theAsianparent city SD lists (Jakarta x5, Surabaya, Yogyakarta), published Jul 2022 -> 2022/2023 (assumed).
The Jakarta Timur list was republished 11 Oct 2026, but its figures match 2023 lists -> 2023/2024 (assumed).
New schools get a record; schools already listed get this as an extra dated source.
Skipped: "SD Islam Al-Falaah" Cipayung (Rp88M entry / Rp62.4M per year looks mislabelled)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
def src(city, slug, pub):
    return {"title": f"Daftar SD Swasta di {city} dan Biayanya (theAsianparent)", "url": f"https://id.theasianparent.com/sd-swasta-di-{slug}", "published": pub}
S = {k: src(*v) for k, v in {"JS": ("Jakarta Selatan", "jakarta-selatan", "2022-07-06"), "JT": ("Jakarta Timur", "jakarta-timur", "2026-10-11"), "JB": ("Jakarta Barat", "jakarta-barat", "2022-07-07"),
                             "JU": ("Jakarta Utara", "jakarta-utara", "2022-07-07"), "JP": ("Jakarta Pusat", "jakarta-pusat", "2022-07-07"),
                             "SBY": ("Surabaya", "surabaya", "2022-07-07"), "YGY": ("Yogyakarta", "yogyakarta", "2022-07-07")}.items()}
N = ("Dari artikel; tahun ajaran tidak disebut, kemungkinan sudah berubah.", "From an article; academic year not stated, likely outdated.")
M = lambda a: {"amount": a, "period": "month"}
def s(slug, key, name=None, city=None, district=None, address=None, religion=None, note=("", ""), **f):
    year = "2023/2024" if key == "JT" else "2022/2023"
    kw = {k: v for k, v in dict(name=name, city=city).items() if v}
    if not kw:
        import json, pathlib
        d = json.loads((pathlib.Path(__file__).resolve().parent.parent / f"src/content/schools/{slug}.json").read_text())
        kw = dict(name=d["name"], city=d["city"])
    upsert(slug, district=district, address=address, religion=religion, level="SD", year=year, yearAssumed=True, source=S[key], checked=CHK,
           notes=L((note[0] + " " + N[0]).strip(), (note[1] + " " + N[1]).strip()), **kw, **f)

# ---- New schools
s("sd-yasporbi-1-jakarta", "JS", "SD Yasporbi I Jakarta", "Jakarta Selatan", "Pancoran", "Jl. Deposito I No.22, Kompleks Perumahan Bank Indonesia, Pancoran, Jakarta Selatan",
  entryFee={"min": 26_700_000}, tuition=M(1_300_000), otherFees=[fee("Annual fee", "Annual fee", 4_000_000)])
s("sd-santo-markus-2-jakarta", "JT", "SD Santo Markus 2 Jakarta", "Jakarta Timur", "Cipayung", "Jl. Raya Pondok Gede, Lubang Buaya, Cipayung, Jakarta Timur", "Katolik",
  ("SPP Rp750–800 ribu; seragam Rp750–800 ribu; kegiatan tahunan Rp500–600 ribu.", "Tuition Rp750–800k; uniforms Rp750–800k; annual activities Rp500–600k."),
  registrationFee=200_000, entryFee={"min": 8_500_000}, tuition=M(750_000), otherFees=[fee(*BOOKS, 1_000_000)])
s("sd-islam-teladan-suci-jakarta", "JT", "SD Islam Teladan Suci Jakarta", "Jakarta Timur", "Ciracas", "Jl. Suci No.9, Susukan, Ciracas, Jakarta Timur", "Islam", ("", ""),
  registrationFee=250_000, entryFee={"min": 6_000_000}, tuition=M(500_000), otherFees=[fee(*UNIFORM, 600_000), fee("Foto dan rapor", "Photos and report book", 200_000), fee("Fingerprint", "Fingerprint", 350_000)])
s("sdi-an-najah-kembangan", "JB", "SDI An Najah Kembangan", "Jakarta Barat", "Kembangan", "Jl. Raya Pos Pengumben No.21, Srengseng, Kembangan, Jakarta Barat", "Islam",
  ("Artikel menyebut \"biaya pendaftaran Rp8.000.000\"; dicatat sebagai biaya masuk.", "The article says \"registration Rp8,000,000\"; recorded as the entry cost."), entryFee={"min": 8_000_000}, tuition=M(600_000))
s("sd-mulia-kencana-jakarta", "JB", "SD Mulia Kencana Jakarta", "Jakarta Barat", "Cengkareng", "Jl. Kencana Timur No.2, Cengkareng Barat, Cengkareng, Jakarta Barat", None,
  ("Uang pangkal termasuk SPP bulan pertama.", "Entry fee includes the first month's tuition."), entryFee={"min": 4_000_000}, tuition=M(535_000))
s("sd-sang-timur-jakarta", "JB", "SD Sang Timur Jakarta", "Jakarta Barat", "Kebon Jeruk", "Jl. Karmel Raya No.2, Kebon Jeruk, Jakarta Barat", "Katolik",
  ("Uang pangkal termasuk uang gedung dan SPP bulan pertama. SPP Rp900 ribu–Rp1 juta.", "Entry includes building fee and first month's tuition. Tuition Rp900k–Rp1M."),
  registrationFee=200_000, entryFee={"min": 15_000_000}, tuition=M(900_000), otherFees=[fee("Perlengkapan sekolah", "School supplies", 2_000_000)])
s("sd-bias-wirosaban-yogyakarta", "YGY", "SD Bina Anak Sholeh (BIAS) Wirosaban Yogyakarta", "Kota Yogyakarta", "Umbulharjo", "Jl. Wirosaban Barat No.6, Sorosutan, Umbulharjo, Kota Yogyakarta", "Islam",
  ("Dana penunjang pendidikan Rp3,1 juta per semester. Fasilitas putra Rp5.475.000 / putri Rp5.925.000.", "Education support fund Rp3.1M per semester. Facilities (boys) Rp5,475,000 / (girls) Rp5,925,000."),
  registrationFee=300_000, entryFee={"min": 16_000_000}, tuition=M(2_300_000), otherFees=[fee("Tes & wawancara", "Test & interview", 600_000), fee("Fasilitas (putra)", "Facilities (boys)", 5_475_000)])

# ---- Extra sources for listed schools
s("sekolah-pelita-harapan-kemang-village", "JS", note=("Biaya pendaftaran Rp1 juta (Rp500 ribu bila ada saudara). Tuition kelas 1–2 Rp169,2 juta, kelas 3–6 Rp179,9 juta per tahun; capital fee bertingkat Rp68 juta (1 tahun) s.d. Rp204 juta (6 tahun).",
  "Registration Rp1M (Rp500k with a sibling). Tuition grades 1–2 Rp169.2M, grades 3–6 Rp179.9M per year; capital fee from Rp68M (1 year) to Rp204M (6 years)."),
  registrationFee=1_000_000, entryFee={"min": 68_000_000, "max": 204_000_000}, tuition={"amount": 169_200_000, "period": "year"})
s("bakti-mulya-400", "JS", note=("Bilingual: pangkal Rp35,2 juta, SPP Rp2 juta, tahunan Rp5 juta. Cambridge: pangkal Rp40 juta, SPP Rp2,5 juta, tahunan Rp7,5 juta.", "Bilingual: entry Rp35.2M, tuition Rp2M, annual Rp5M. Cambridge: entry Rp40M, tuition Rp2.5M, annual Rp7.5M."),
  registrationFee=500_000, entryFee={"min": 35_200_000, "max": 40_000_000}, tuition=M(2_000_000))
s("highscope-indonesia-tb-simatupang", "JS", registrationFee=2_000_000, entryFee={"min": 70_000_000}, tuition=M(6_600_000))
s("sd-citra-alam-jakarta", "JS", note=("Uang pangkal Rp20–30 juta; SPP Rp1,8–2 juta.", "Entry Rp20–30M; tuition Rp1.8–2M."), registrationFee=700_000, entryFee={"min": 20_000_000, "max": 30_000_000}, tuition=M(1_800_000))
s("sd-gemala-ananda-jakarta", "JS", note=("Biaya pengembangan Rp9 juta per tahun.", "Development fee Rp9M per year."), registrationFee=650_000, tuition=M(2_500_000), otherFees=[fee("Biaya pengembangan per tahun", "Development fee per year", 9_000_000)])
s("sdit-ar-rahmah-jakarta-timur", "JT", entryFee={"min": 11_500_000}, tuition=M(900_000), otherFees=[fee(*UNIFORM, 1_700_000), fee("Buku dan modul", "Books and modules", 1_200_000), fee(*ACTIVITY, 2_800_000)])
s("sdit-nurul-iman-jakarta-timur", "JT", note=("Uang pangkal termasuk SPP bulan pertama, buku, seragam, kegiatan setahun, gedung.", "Entry includes first month's tuition, books, uniforms, 1 year of activities, building."),
  entryFee={"min": 18_890_000}, tuition=M(985_000))
s("jakarta-islamic-school-joglo", "JB", note=("Disebut \"Jakarta International Islamic School Joglo\"; \"biaya pendaftaran Rp26 juta\" dicatat sebagai biaya masuk.", "Listed as \"Jakarta International Islamic School Joglo\"; \"registration Rp26M\" recorded as the entry cost."),
  entryFee={"min": 26_000_000}, tuition=M(2_000_000))
s("highscope-indonesia-kelapa-gading", "JU", registrationFee=400_000, entryFee={"min": 59_000_000}, tuition=M(4_850_000))
s("sd-al-hikmah-surabaya", "SBY", note=("Uang pangkal = infaq.", "Entry = donation (infaq)."), registrationFee=500_000, entryFee={"min": 30_500_000}, tuition=M(1_900_000), otherFees=[fee("Biaya pengembangan pendidikan", "Education development fee", 2_500_000)])
s("sd-khadijah-surabaya", "SBY", note=("Uang pangkal = infaq.", "Entry = donation (infaq)."), registrationFee=400_000, entryFee={"min": 11_000_000}, tuition=M(700_000),
  otherFees=[fee(*ACTIVITY, 1_700_000), fee(*UNIFORM, 1_700_000), fee(*BOOKS, 1_000_000)])
s("sekolah-alam-insan-mulia-surabaya", "SBY", note=("Uang pangkal = uang gedung.", "Entry = building fee."), registrationFee=350_000, entryFee={"min": 20_000_000}, tuition=M(1_800_000),
  otherFees=[fee(*UNIFORM, 675_000), fee("Daftar ulang", "Re-registration", 3_425_000)])
s("sd-islam-al-azhar-35-surabaya", "SBY", registrationFee=350_000, entryFee={"min": 29_000_000}, tuition=M(1_700_000),
  otherFees=[fee("Jam'iyyah", "Parents' association", 300_000), fee(*ACTIVITY, 2_800_000), fee("Uang sekolah", "School fee", 2_000_000), fee("Uang syiar", "Syiar fee", 2_000_000)])
s("surabaya-intercultural-school", "SBY", note=("Biaya aplikasi Rp2.700.000.", "Application fee Rp2,700,000."), registrationFee=20_000_000, entryFee={"min": 30_000_000}, tuition={"amount": 242_597_250, "period": "year"})
s("sekolah-ciputra-surabaya", "SBY", note=("SPP per tahun Rp28–75 juta.", "Annual tuition Rp28–75M."), registrationFee=1_000_000, tuition={"amount": 28_000_000, "period": "year"})
s("sampoerna-academy-surabaya", "SBY", note=("Pendaftaran Rp3–6 juta; SPP per tahun Rp43–90 juta.", "Registration Rp3–6M; annual tuition Rp43–90M."), registrationFee=3_000_000, tuition={"amount": 43_000_000, "period": "year"})
s("sd-al-azhar-31-sinduadi", "YGY", note=("Uang pangkal = biaya iuran.", "Entry = contribution fee."), entryFee={"min": 14_500_000}, tuition=M(780_000), otherFees=[fee("Uang tahunan", "Annual fee", 3_650_000), fee(*UNIFORM, 1_050_000)])
s("sd-muhammadiyah-condongcatur", "YGY", note=("Amal jariyah pilihan Rp4,5/5/5,5 juta; seragam putra Rp3,8 juta / putri Rp4,1 juta.", "Optional endowment Rp4.5/5/5.5M; uniforms boys Rp3.8M / girls Rp4.1M."),
  registrationFee=250_000, entryFee={"min": 8_000_000}, tuition=M(675_000))
s("olifant-school-yogyakarta", "YGY", note=("SD Olifant.", "Olifant primary."), registrationFee=950_000, entryFee={"min": 25_000_000}, tuition=M(2_000_000), otherFees=[fee("Biaya tahunan", "Annual fee", 7_250_000), fee(*UNIFORM, 950_000)])
s("sd-budi-mulia-dua-panjen", "YGY", registrationFee=200_000, entryFee={"min": 25_000_000}, tuition=M(1_500_000), otherFees=[fee("Uang kegiatan per tahun", "Activities per year", 10_000_000)])
s("sd-muhammadiyah-sapen-yogyakarta", "YGY", note=("Uang pangkal = biaya pengembangan sekolah.", "Entry = school development fee."), entryFee={"min": 10_000_000}, tuition=M(625_000), otherFees=[fee("Seragam putri", "Uniforms (girls)", 2_140_000)])
s("jogjakarta-montessori-school", "YGY", note=("Uang tahunan sekitar Rp4,5 juta.", "Annual fee about Rp4.5M."), entryFee={"min": 29_500_000}, tuition=M(1_700_000))
s("sd-islam-al-azhar-55-yogyakarta", "YGY", entryFee={"min": 26_500_000}, tuition=M(1_300_000))
s("sd-salman-al-farisi-2-sleman", "YGY", note=("Uang pangkal sekitar Rp13 juta.", "Entry fee about Rp13M."), entryFee={"min": 13_000_000}, tuition=M(750_000))
