"""Orami SD swasta lists per Jakarta city (Oct 2023). No academic year stated -> 2023/2024 (assumed).
Most figures are given as "sekitar" (approximately)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
def src(city, url, pub):
    return {"title": f"Rekomendasi SD Swasta di {city} dan Biayanya (Orami)", "url": url, "published": pub}
JT_S = src("Jakarta Timur", "https://www.orami.co.id/magazine/sd-swasta-jakarta-timur", "2023-10-03")
JP_S = src("Jakarta Pusat", "https://www.orami.co.id/magazine/sd-swasta-jakarta-pusat", "2023-10-06")
JU_S = src("Jakarta Utara", "https://www.orami.co.id/magazine/sd-swasta-jakarta-utara", "2023-10-05")
JS_S = src("Jakarta Selatan", "https://www.orami.co.id/magazine/sd-swasta-jakarta-selatan", "2023-10-02")
N = ("Perkiraan biaya dari artikel; tahun ajaran tidak disebut.", "Approximate fees from an article; academic year not stated.")
def s(slug, name, city, district, address, source, religion=None, note=None, **f):
    nid, nen = note or ("", "")
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year="2023/2024", yearAssumed=True,
           source=source, checked=CHK, notes=L((nid + " " + N[0]).strip(), (nen + " " + N[1]).strip()), **f)
M = lambda a: {"amount": a, "period": "month"}
JS, JT, JP, JU = "Jakarta Selatan", "Jakarta Timur", "Jakarta Pusat", "Jakarta Utara"

# Jakarta Timur
s("sd-tarakanita-5-jakarta", "SD Tarakanita 5 Jakarta", JT, "Pulo Gadung", "Jl. Pemuda No.6, Rawamangun, Pulo Gadung, Jakarta Timur", JT_S, "Katolik", None,
  entryFee={"min": 16_000_000}, tuition=M(1_200_000), otherFees=[fee(*UNIFORM, 700_000), fee(*BOOKS, 700_000)])
s("sd-emiisc-jakarta", "SD EMIISc Jakarta", JT, "Kramat Jati", "Jl. Raya Condet No.27, Batu Ampar, Kramat Jati, Jakarta Timur", JT_S, "Islam", ("Pendaftaran termasuk tes masuk.", "Registration includes the entrance test."),
  registrationFee=500_000, entryFee={"min": 20_000_000}, tuition=M(1_100_000))
s("embun-pagi-islamic-school-jakarta", "Embun Pagi Islamic School", JT, "Duren Sawit", "Jl. Raya Kalimalang No.8, Pondok Kelapa, Duren Sawit, Jakarta Timur", JT_S, "Islam",
  ("Uang pangkal = uang fasilitas sekolah. Artikel menulis SPP Rp2,7 juta \"per tahun\"; kemungkinan per bulan.", "Entry fee = school facilities fee. The article says tuition Rp2.7M \"per year\"; probably per month."),
  registrationFee=650_000, entryFee={"min": 29_000_000}, tuition=M(2_700_000),
  otherFees=[fee("Uang pendidikan per tahun", "Education fee per year", 3_800_000), fee("Kegiatan tahunan", "Annual activities", 2_000_000), fee("Komite per tahun", "Committee per year", 350_000)])
s("sd-islam-al-azhar-13-rawamangun", "SD Islam Al Azhar 13 Rawamangun", JT, "Pulo Gadung", "Jl. Sunan Giri No.1, Rawamangun, Pulo Gadung, Jakarta Timur", JT_S, "Islam",
  ("Uang pangkal sudah mencakup daftar ulang hingga kelas 6 dan seragam. Komite Rp300–400 ribu/tahun.", "Entry fee covers re-registration up to grade 6 and uniforms. Committee Rp300–400k/year."),
  entryFee={"min": 35_700_000}, tuition=M(1_600_000), otherFees=[fee(*BOOKS, 1_900_000)])
s("sd-bojana-tirta-islamic-school-jakarta", "SD Bojana Tirta Islamic School", JT, "Pulo Gadung", "Jl. Bojana Tirta Raya No.3A, Pisangan Timur, Jakarta Timur", JT_S, "Islam",
  ("Artikel menyebut \"biaya pendaftaran Rp28 juta\"; dicatat sebagai biaya masuk.", "The article says \"registration fee Rp28M\"; recorded as the entry fee."), entryFee={"min": 28_000_000}, tuition=M(1_750_000))
s("global-islamic-school-condet", "Global Islamic School Condet", JT, "Kramat Jati", "Jl. Raya Condet No.5, Balekambang, Kramat Jati, Jakarta Timur", JT_S, "Islam",
  ("Artikel menulis SPP Rp1,85 juta \"per tahun\"; kemungkinan per bulan.", "The article says tuition Rp1.85M \"per year\"; probably per month."),
  registrationFee=550_000, entryFee={"min": 30_500_000}, tuition=M(1_850_000),
  otherFees=[fee("Kegiatan tahunan", "Annual activities", 2_780_000), fee("Perlengkapan tahunan", "Annual supplies", 4_350_000), fee("POMG per tahun", "Parents' association per year", 250_000)])
s("sd-islam-al-azhar-20-cibubur", "SD Islam Al Azhar 20 Cibubur", JT, "Ciracas", "Jl. Abdulrahman No.9, Cibubur, Ciracas, Jakarta Timur", JT_S, "Islam", ("Buku Rp1,85–2 juta per tahun.", "Books Rp1.85–2M per year."),
  registrationFee=350_000, entryFee={"min": 25_000_000}, tuition=M(1_250_000), otherFees=[fee(*BOOKS, 1_850_000), fee("Seragam tahun pertama", "First-year uniforms", 1_500_000)])

# Jakarta Pusat
s("sd-budi-mulia-jakarta", "SD Budi Mulia Jakarta", JP, "Kemayoran", "Jl. Gunung Sahari No.91, Gunung Sahari Selatan, Kemayoran, Jakarta Pusat", JP_S, "Katolik", ("Uang pangkal = uang gedung.", "Entry fee = building fee."),
  registrationFee=60_000, entryFee={"min": 5_800_000}, tuition=M(590_000), otherFees=[fee("Perlengkapan sekolah", "School supplies", 1_500_000)])
s("tunas-bangsa-christian-school-gunung-sahari", "Tunas Bangsa Christian School Gunung Sahari", JP, "Sawah Besar", "Jl. Gunung Sahari 12 No.11, Gunung Sahari Utara, Sawah Besar, Jakarta Pusat", JP_S, "Kristen", None,
  entryFee={"min": 11_700_000}, tuition=M(1_125_000), otherFees=[fee("Kegiatan dan sarana per tahun", "Activities & facilities per year", 1_750_000), fee("Perlengkapan sekolah", "School supplies", 1_700_000)])
s("sd-santa-maria-juanda-jakarta", "SD Santa Maria Juanda Jakarta", JP, "Gambir", "Jl. Ir. H. Juanda No.29, Kebon Kelapa, Gambir, Jakarta Pusat", JP_S, "Katolik", ("Uang kegiatan Rp1,2–3 juta.", "Activity fee Rp1.2–3M."),
  registrationFee=1_500_000, entryFee={"min": 24_500_000}, tuition=M(1_500_000), otherFees=[fee("Kegiatan (min.)", "Activities (min.)", 1_200_000), fee("Perlengkapan sekolah", "School supplies", 2_000_000)])
s("mahatma-gandhi-school-jakarta", "Mahatma Gandhi School Jakarta", JP, "Kemayoran", "Komplek Kemayoran Blok B-16 No.2, Jl. Tabing, Gunung Sahari Utara, Jakarta Pusat", JP_S, None, None,
  registrationFee=350_000, entryFee={"min": 10_500_000}, tuition=M(1_950_000), otherFees=[fee("Annual fee", "Annual fee", 1_700_000), fee("Perlengkapan sekolah", "School supplies", 1_400_000)])
s("perguruan-cikini", "Perguruan Cikini", JP, "Menteng", "Jl. Cikini Raya No.74-76, Cikini, Menteng, Jakarta Pusat", JP_S, None, None, entryFee={"min": 20_000_000}, tuition=M(850_000))
s("sd-melania-3-jakarta", "SD Melania III Jakarta", JP, "Cempaka Putih", "Jl. Percetakan Negara No.31, Cempaka Putih Barat, Jakarta Pusat", JP_S, "Katolik", None,
  registrationFee=150_000, entryFee={"min": 4_000_000}, tuition=M(500_000))
s("sd-muhammadiyah-1-jakarta", "SD Muhammadiyah 1 Jakarta", JP, "Kemayoran", "Jl. Garuda No.33, Gunung Sahari Selatan, Kemayoran, Jakarta Pusat", JP_S, "Islam",
  ("Uang pangkal Rp8.380.000 (gelombang 1) / Rp8.600.000 (gelombang 2).", "Entry fee Rp8,380,000 (wave 1) / Rp8,600,000 (wave 2)."), registrationFee=300_000, entryFee={"min": 8_380_000, "max": 8_600_000}, tuition=M(500_000))

# Jakarta Utara
s("jac-school-kelapa-gading", "JAC School Kelapa Gading", JU, "Kelapa Gading", "Jl. Pegangsaan Dua No.75, Pegangsaan Dua, Kelapa Gading, Jakarta Utara", JU_S, None, None,
  entryFee={"min": 24_000_000}, tuition=M(2_200_000), otherFees=[fee(*ACTIVITY, 2_000_000)])
s("sd-kristen-ipeka-pluit", "SD Kristen IPEKA Pluit", JU, "Penjaringan", "Jl. Pluit Timur Raya No.1, Pluit, Penjaringan, Jakarta Utara", JU_S, "Kristen", None,
  registrationFee=300_000, entryFee={"min": 24_000_000}, tuition=M(2_400_000))
s("sd-islam-al-azhar-kelapa-gading", "SD Islam Al Azhar Kelapa Gading", JU, "Kelapa Gading", "Jl. Boulevard Timur No.1, Kelapa Gading Timur, Jakarta Utara", JU_S, "Islam", None,
  entryFee={"min": 18_000_000}, tuition=M(1_100_000), otherFees=[fee(*ACTIVITY, 2_350_000), fee(*BOOKS, 250_000)])
s("sdk-6-bpk-penabur-kelapa-gading", "SDK 6 BPK Penabur Kelapa Gading", JU, "Kelapa Gading", "Jl. Raya Kelapa Hybrida Blok QA3, Kelapa Gading Barat, Jakarta Utara", JU_S, "Kristen", None,
  registrationFee=350_000, entryFee={"min": 28_100_000}, tuition=M(2_850_000), otherFees=[fee(*ACTIVITY, 1_000_000)])
s("sd-gandhi-ancol", "SD Gandhi Ancol", JU, "Pademangan", "Jl. Pangandaran I No.4, Ancol, Pademangan, Jakarta Utara", JU_S, None,
  ("Nasional plus: pangkal Rp16 juta, SPP Rp1,8 juta. Internasional: pangkal Rp23 juta, SPP Rp2,25 juta.", "National plus: entry Rp16M, tuition Rp1.8M. International: entry Rp23M, tuition Rp2.25M."),
  registrationFee=100_000, entryFee={"min": 16_000_000, "max": 23_000_000}, tuition=M(1_800_000), otherFees=[fee("Peralatan per tahun", "Equipment per year", 1_500_000)])
s("mahatma-gading-intercultural-school", "Mahatma Gading Intercultural School", JU, "Kelapa Gading", "Komplek Villa Gading Indah, Jl. Boulevard Blok Q, Kelapa Gading Barat, Jakarta Utara", JU_S, None, None,
  registrationFee=350_000, entryFee={"min": 36_000_000}, tuition=M(3_350_000))
s("sd-jubilee-jakarta", "SD Jubilee Jakarta", JU, None, None, JU_S, "Kristen", None,
  entryFee={"min": 35_000_000}, tuition=M(2_500_000), otherFees=[fee(*BOOKS, 2_500_000), fee(*UNIFORM, 800_000)])

# Jakarta Selatan
s("sd-al-ikhlas-cipete", "SD Al-Ikhlas Cipete", JS, "Cilandak", "Jl. Cipete III No.10, Cipete Selatan, Jakarta Selatan", JS_S, "Islam",
  ("Uang pangkal Rp33 juta (dari TK luar) / Rp30 juta (dari TK Al-Ikhlas).", "Entry fee Rp33M (external) / Rp30M (from TK Al-Ikhlas)."), registrationFee=300_000, entryFee={"min": 30_000_000, "max": 33_000_000}, tuition=M(2_000_000))
s("sd-kupu-kupu-jakarta", "SD Kupu-Kupu", JS, "Mampang Prapatan", "Jl. Bangka VII Dalam No.14, Pela Mampang, Mampang Prapatan, Jakarta Selatan", JS_S, None,
  ("Uang pangkal Rp49,7 juta (tanpa relasi) / Rp49,2 juta (ada relasi).", "Entry fee Rp49.7M (no relation) / Rp49.2M (with relation)."), registrationFee=200_000, entryFee={"min": 49_200_000, "max": 49_700_000}, tuition=M(2_450_000))
s("sekolah-pelita-harapan-kemang-village", "Sekolah Pelita Harapan Kemang Village", JS, "Mampang Prapatan", "Jl. Kemang Raya No.36, Bangka, Mampang Prapatan, Jakarta Selatan", JS_S, "Kristen",
  ("Artikel hanya menyebut biaya tahunan \"kurang lebih Rp80 jutaan\".", "The article only gives annual fees of \"roughly Rp80 million\"."), tuition={"amount": 80_000_000, "period": "year"})
s("highscope-indonesia-tb-simatupang", "HighScope Indonesia TB Simatupang", JS, "Cilandak", "Jl. TB Simatupang No.8, Cilandak Barat, Jakarta Selatan", JS_S, None,
  ("Kisaran biaya SD sekitar Rp70 jutaan; SPP Rp6,6 juta/bulan.", "Primary fees around Rp70M; tuition Rp6.6M/month."), tuition=M(6_600_000), otherFees=[fee("Kisaran biaya (tidak dirinci)", "Fee range (not itemised)", 70_000_000)])
