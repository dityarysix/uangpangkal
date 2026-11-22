"""SMA (and a few other) fee lists, approximate figures labelled with year and source.
- News TNG, "11 SMA Swasta Terbaik di Tangerang Selatan, dari yang Termurah hingga Premium" (21 Mar 2025) -> 2025/2026, yearAssumed.
- Hartaku, "Biaya Pendidikan Anak SMA di Jakarta dan Sekitarnya" (9 Jan 2026), estimates -> 2026/2027, yearAssumed. Only schools whose campus is clear.
- Orami, "8 Sekolah Internasional di Jogja, Lengkap dengan Biayanya" (18 Jun 2025) -> 2025/2026, yearAssumed; only entries whose level is clear."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

CHK = "2026-11-22"
NT = {"title": "11 SMA Swasta Terbaik di Tangerang Selatan, dari yang Termurah hingga Premium (News TNG)", "url": "https://newstangerang.com/11-sma-swasta-terbaik-di-tangerang-selatan-dari-yang-termurah-hingga-premium/", "published": "2025-03-21"}
T = dict(level="SMA", year="2025/2026", yearAssumed=True, source=NT, checked=CHK)
TS = "Tangerang Selatan"
EST = L("Perkiraan menurut sumber.", "Estimate according to the source.")
upsert("sma-muhammadiyah-25-pamulang", name="SMA Muhammadiyah 25 Pamulang", city=TS, district="Pamulang", religion="Islam",
       tuition={"amount": 900_000, "period": "month"}, notes=L("Program tahfidz tersedia. Uang pangkal tidak dicantumkan.", "Tahfidz programme available. Entry fee not listed."), **T)
upsert("sma-ekayana-ehipassiko-school", name="SMA Ekayana Ehipassiko School", city=TS, religion="Buddha",
       entryFee={"min": 20_000_000}, tuition={"amount": 1_980_000, "period": "month"}, notes=L("Promo uang pangkal \"Rp20 jutaan\" (perkiraan).", "Promotional entry fee \"around Rp20 million\" (approximate)."), **T)
upsert("sma-islam-sinar-cendekia", name="SMA Islam Sinar Cendekia", city=TS, religion="Islam",
       tuition={"amount": 2_098_000, "period": "month"}, notes=L("SPP sudah termasuk kegiatan dan perlengkapan sekolah.", "Tuition includes activities and school supplies."), **T)
upsert("sma-plus-pembangunan-jaya-bintaro", name="SMA Plus Pembangunan Jaya Bintaro", city=TS, district="Pondok Aren",
       entryFee={"min": 34_000_000}, tuition={"amount": 2_585_000, "period": "month"}, notes=L("Uang pangkal mencakup seragam, kegiatan, dan ekstrakurikuler.", "Entry fee covers uniforms, activities and extracurriculars."), **T)
upsert("syafana-islamic-school", name="Syafana Islamic School", city=TS, religion="Islam",
       tuition={"amount": 3_050_000, "period": "month"}, otherFees=[fee("Biaya tahunan (perkiraan)", "Annual fee (approx.)", 5_000_000)], notes=EST, **T)
upsert("sekolah-pahoa", name="Sekolah Pahoa", city="Kabupaten Tangerang", district="Kelapa Dua",
       entryFee={"min": 36_000_000}, tuition={"amount": 3_410_000, "period": "month"}, notes=L("Kelas adaptif bahasa Mandarin. Uang pangkal sekitar Rp36 juta.", "Adaptive Mandarin classes. Entry fee about Rp36M."), **T)
upsert("sma-kharisma-bangsa", name="SMA Kharisma Bangsa", city=TS, curriculum=["Cambridge"],
       tuition={"amount": 5_250_000, "period": "month"}, notes=L("SPP sudah termasuk biaya ujian Cambridge.", "Tuition includes Cambridge exam fees."), **T)
upsert("sekolah-cikal-serpong", name="Sekolah Cikal Serpong", city=TS, district="Serpong",
       entryFee={"min": 40_000_000}, tuition={"amount": 6_100_000, "period": "month"}, notes=L("SPP mulai Rp6,1 juta tergantung program; uang pangkal sekitar Rp40 juta.", "Tuition from Rp6.1M depending on programme; entry about Rp40M."), **T)
upsert("binus-school-serpong", name="BINUS School Serpong", city=TS, registrationFee=300_000, entryFee={"min": 96_000_000},
       tuition={"amount": 6_700_000, "period": "month"}, notes=L("Uang pangkal = enrollment fee.", "Entry fee = enrolment fee."), **T)
upsert("sampoerna-academy-bsd", name="Sampoerna Academy BSD", city=TS, tuition={"amount": 8_650_000, "period": "month"},
       notes=L("Sekitar Rp8,65 juta per bulan; ada opsi pembayaran triwulanan.", "About Rp8.65M per month; quarterly payment option."), **T)
upsert("global-jaya-school", name="Global Jaya School", city=TS, tuition={"amount": 12_077_083, "period": "month"},
       notes=L("Sekitar Rp12.077.083 per bulan (setara biaya tahunan dibagi 12).", "About Rp12,077,083 per month (annual fee divided by 12)."), **T)

HK = {"title": "Biaya Pendidikan Anak SMA di Jakarta dan Sekitarnya (Hartaku)", "url": "https://hartaku.co.id/edukasi/artikel/biaya-pendidikan-anak-sma-di-jakarta-dan-sekitarny-DwPdkna5XO", "published": "2026-01-09"}
H = dict(level="SMA", year="2026/2027", yearAssumed=True, source=HK, checked=CHK)
upsert("sma-islam-al-azhar-3-kebayoran-baru", name="SMA Islam Al Azhar 3 Kebayoran Baru", city="Jakarta Selatan", district="Kebayoran Baru", religion="Islam",
       registrationFee=550_000, entryFee={"min": 60_000_000}, tuition={"amount": 6_600_000, "period": "month"}, notes=EST, **H)
upsert("labschool-rawamangun", name="Labschool Rawamangun", city="Jakarta Timur", registrationFee=300_000, entryFee={"min": 16_000_000},
       tuition={"amount": 850_000, "period": "month"}, notes=L(EST["id"] + " Angka SMA ini jauh di bawah angka SMP dari sumber lain; konfirmasi ke sekolah.", EST["en"] + " These SMA figures are far below the SMP figures from another source; confirm with the school."), **H)
upsert("jakarta-intercultural-school", name="Jakarta Intercultural School (JIS)", city="Jakarta Selatan", curriculum=["IB"],
       registrationFee=5_000_000, entryFee={"min": 495_000_000, "max": 500_000_000}, tuition={"amount": 212_000_000, "period": "semester"},
       otherFees=[fee("Technology fee", "Technology fee", 6_300_000), fee("EAL program fee", "EAL programme fee", 67_600_000)],
       notes=L(EST["id"] + " Uang pangkal = capital fee.", EST["en"] + " Entry fee = capital fee."), **H)
upsert("sekolah-cikal-lebak-bulus", name="Sekolah Cikal Lebak Bulus", city="Jakarta Selatan", district="Cilandak",
       entryFee={"min": 104_300_000}, tuition={"amount": 6_000_000, "period": "month"},
       otherFees=[fee("Joining fee", "Joining fee", 12_000_000), fee("Development fee (min.)", "Development fee (min.)", 25_000_000),
                  fee("Seragam (min.)", "Uniforms (min.)", 2_000_000), fee("Buku & materi per tahun (min.)", "Books & materials per year (min.)", 3_000_000)],
       notes=L(EST["id"] + " Development fee Rp25–50 juta; seragam Rp2–4 juta; buku Rp3–6 juta per tahun.", EST["en"] + " Development fee Rp25–50M; uniforms Rp2–4M; books Rp3–6M per year."), **H)

OR = {"title": "8 Sekolah Internasional di Jogja, Lengkap dengan Biayanya (Orami)", "url": "https://www.orami.co.id/magazine/sekolah-internasional-di-jogja", "published": "2025-06-18"}
O = dict(year="2025/2026", yearAssumed=True, source=OR, checked=CHK)
upsert("sma-internasional-budi-mulia-dua-yogyakarta", name="SMA Internasional Budi Mulia Dua Yogyakarta", city="Sleman", district="Ngemplak", curriculum=["Internasional"],
       address="Jl. Raya Tajem, Kenayan, Wedomartani, Ngemplak, Sleman", level="SMA",
       registrationFee=500_000, entryFee={"min": 25_000_000}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee("Aktivitas tahunan (perkiraan)", "Annual activities (approx.)", 10_000_000)], notes=L(EST["id"] + " Total biaya awal sekitar Rp36,5 juta.", EST["en"] + " Total initial cost about Rp36.5M."), **O)
upsert("jogjakarta-montessori-school", name="Jogjakarta Montessori School", city="Sleman", district="Ngaglik", curriculum=["Montessori"],
       address="Jl. Lempongsari No.136B, Jongkang, Sariharjo, Ngaglik, Sleman", level="SD",
       entryFee={"min": 29_500_000}, tuition={"amount": 1_700_000, "period": "month"},
       notes=L("Uang pangkal = biaya komplementer. Total tahun pertama diperkirakan sekitar Rp54.900.000.", "Entry fee = complementary fee. First-year total estimated at about Rp54,900,000."), **O)
upsert("fawwaz-global-islamic-school-yogyakarta", name="Fawwaz Global Islamic School Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Islam",
       address="Jl. Ipda Tut Harsono No.45, Muja Muju, Umbulharjo, Yogyakarta", level="TK",
       registrationFee=500_000, entryFee={"min": 14_500_000, "max": 17_500_000}, tuition={"amount": 1_800_000, "period": "month"},
       otherFees=[fee("Biaya tahunan", "Annual fee", 5_000_000), fee("Kegiatan & ekskul per tahun (perkiraan)", "Activities & extracurriculars per year (approx.)", 3_000_000),
                  fee("Seragam & bahan ajar per tahun (perkiraan)", "Uniforms & materials per year (approx.)", 2_000_000)],
       notes=L("Pra-TK/TK. Biaya pengembangan dan SPP (Rp1,8–2,3 juta) tergantung gelombang. Sumber menyebut tahun ajaran 2025–2026.", "Pre-K/K. Development fee and tuition (Rp1.8–2.3M) depend on the wave. The source states academic year 2025–2026."),
       **{**O, "yearAssumed": False})
print("ok")
