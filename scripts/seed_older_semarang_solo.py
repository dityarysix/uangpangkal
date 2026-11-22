"""Older / approximate data, included per the site's policy (always labelled with year and source).
- theAsianparent, "Cek Biaya Masuk SD Swasta yang Ada di Semarang Tahun 2022" (7 Jul 2022). Years per figures stated.
- Orami, "7 SD di Solo, Swasta dan Negeri, Lengkap dengan Biaya!" (30 Jun 2025) — broad ranges; state schools skipped."""
from seedlib import L, fee, upsert, UNIFORM

CHK = "2026-11-22"
TAP = {"title": "Cek Biaya Masuk SD Swasta yang Ada di Semarang Tahun 2022 (theAsianparent)", "url": "https://id.theasianparent.com/cek-biaya-masuk-sd-swasta-yang-ada-di-semarang-tahun-2022", "published": "2022-07-07"}
upsert("sd-hj-isriati-baiturrahman-1-semarang", name="SD Hj. Isriati Baiturrahman 1 Semarang", city="Kota Semarang", district="Semarang Tengah", religion="Islam",
       address="Jl. Pandanaran No.126, Pekunden, Semarang Tengah, Kota Semarang", phone="(024) 8411168",
       level="SD", year="2020/2021", source=TAP, checked=CHK,
       entryFee={"min": 9_000_000}, tuition={"amount": 850_000, "period": "month"},
       otherFees=[fee("Administrasi, tes psikologi, asuransi 6 tahun, operasional", "Administration, psych test, 6-year insurance, operations", 2_745_000),
                  fee(*UNIFORM, 1_339_000), fee("Paket buku 1 tahun", "Books (1 year)", 2_946_000), fee("Iuran komite", "Committee fee", 50_000)],
       notes=L("Uang pangkal = sumbangan pendidikan. SPP = syahriyah Juli 2020. Total Rp16.930.000.", "Entry fee = education contribution. Tuition = July 2020 syahriyah. Total Rp16,930,000."))
upsert("sd-islam-tunas-harapan-semarang", name="SD Islam Tunas Harapan Semarang", city="Kota Semarang", district="Tembalang", religion="Islam",
       address="Jl. Tulus Harapan No.1, Sendangmulyo, Tembalang, Kota Semarang",
       level="SD", year="2018/2019", source=TAP, checked=CHK,
       entryFee={"min": 5_000_000}, tuition={"amount": 300_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 650_000), fee("Kegiatan ekstra", "Extracurriculars", 250_000), fee("Kesiswaan", "Student affairs", 200_000)],
       notes=L("Uang pangkal = SPI. SPP Juli 2018. Total Rp6.400.000.", "Entry fee = SPI. Tuition as of July 2018. Total Rp6,400,000."))
A = dict(level="SD", year="2022/2023", yearAssumed=True, source=TAP, checked=CHK)
APPROX = L("Angka perkiraan (\"sekitar\") tanpa tahun; artikel terbit Juli 2022.", "Approximate figures without a year; article published July 2022.")
upsert("sd-islam-al-azhar-25-semarang", name="SD Islam Al Azhar 25 Semarang", city="Kota Semarang", religion="Islam",
       entryFee={"min": 19_000_000}, tuition={"amount": 900_000, "period": "month"}, notes=APPROX, **A)
upsert("sd-semesta-bilingual-school-semarang", name="SD Semesta Bilingual School Semarang", city="Kota Semarang", district="Banyumanik",
       address="Jl. Setiabudi No.116, Srondol Kulon, Banyumanik, Kota Semarang",
       entryFee={"min": 25_000_000}, tuition={"amount": 2_000_000, "period": "month"}, notes=APPROX, **A)
upsert("sd-al-azhar-14-semarang", name="SD Al Azhar 14 Semarang", city="Kota Semarang", district="Tembalang", religion="Islam",
       address="Jl. Klenteng Sari, Tembalang, Kota Semarang",
       entryFee={"min": 19_000_000}, tuition={"amount": 900_000, "period": "month"}, notes=APPROX, **A)
upsert("sd-islam-bilingual-annisa-semarang", name="SD Islam Bilingual Annisa Semarang", city="Kota Semarang", district="Semarang Tengah", religion="Islam",
       address="Jl. Abimanyu Raya No.17-19, Pindrikan Lor, Semarang Tengah, Kota Semarang", phone="(024) 3511057",
       entryFee={"min": 4_900_000}, notes=L("Biaya pendaftaran/masuk berkisar Rp4,9 juta (perkiraan).", "Registration/entry about Rp4.9 million (approximate)."), **A)

OR = {"title": "7 SD di Solo, Swasta dan Negeri, Lengkap dengan Biaya! (Orami)", "url": "https://www.orami.co.id/magazine/sd-di-solo", "published": "2025-06-30"}
O = dict(city="Surakarta (Solo)", level="SD", year="2025/2026", yearAssumed=True, source=OR, checked=CHK)
RANGE = L("Kisaran biaya menurut sumber (perkiraan).", "Fee ranges according to the source (approximate).")
upsert("sdit-insan-mulia-surakarta", name="SDIT Insan Mulia Surakarta", district="Laweyan", religion="Islam", address="Jl. Duku VII, Jajar, Laweyan, Surakarta",
       registrationFee=300_000, tuition={"amount": 600_000, "period": "month"},
       otherFees=[fee("Kegiatan per tahun (min.)", "Activities per year (min.)", 1_000_000), fee("Seragam (min.)", "Uniforms (min.)", 750_000)],
       notes=L(RANGE["id"] + " SPP Rp600–700 ribu; kegiatan Rp1–1,2 juta/tahun; seragam Rp750–900 ribu. Uang pangkal tidak dicantumkan.",
               RANGE["en"] + " Tuition Rp600–700k; activities Rp1–1.2 million/year; uniforms Rp750–900k. Entry fee not listed."), **O)
upsert("sd-kristen-manahan-surakarta", name="SD Kristen Manahan Surakarta", district="Banjarsari", religion="Kristen", address="Jl. MT Haryono No.12, Manahan, Banjarsari, Surakarta",
       registrationFee=300_000, entryFee={"min": 8_000_000, "max": 15_000_000}, tuition={"amount": 700_000, "period": "month"},
       notes=L(RANGE["id"] + " Pendaftaran Rp300 ribu–1,5 juta; uang pangkal (gedung/seragam/buku) Rp8–15 juta; SPP Rp700 ribu–1 juta; kegiatan Rp1–2 juta/tahun.",
               RANGE["en"] + " Registration Rp300k–1.5M; entry (building/uniform/books) Rp8–15M; tuition Rp700k–1M; activities Rp1–2M/year."), **O)
upsert("sd-kanisius-serengan-surakarta", name="SD Kanisius Serengan Surakarta", district="Serengan", religion="Katolik", address="Jl. Veteran 229, Serengan, Surakarta",
       registrationFee=300_000, entryFee={"min": 5_000_000, "max": 15_000_000}, tuition={"amount": 500_000, "period": "month"},
       notes=L(RANGE["id"] + " Pendaftaran Rp300 ribu–1,5 juta; uang pangkal Rp5–15 juta; SPP Rp500 ribu–1 juta; kegiatan Rp1–2 juta/tahun.",
               RANGE["en"] + " Registration Rp300k–1.5M; entry Rp5–15M; tuition Rp500k–1M; activities Rp1–2M/year."), **O)
upsert("sd-islam-diponegoro-surakarta", name="SD Islam Diponegoro Surakarta", district="Pasar Kliwon", religion="Islam", address="Jl. Kaliwidas No.2, Pasar Kliwon, Surakarta",
       registrationFee=150_000, entryFee={"min": 10_000_000, "max": 15_000_000}, tuition={"amount": 800_000, "period": "month"},
       notes=L(RANGE["id"] + " SPP Rp800 ribu–1 juta.", RANGE["en"] + " Tuition Rp800k–1M."), **O)
print("ok")
