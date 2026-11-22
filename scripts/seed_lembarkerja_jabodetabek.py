"""Lembar Kerja Untuk Anak blog posts (Sep 2026). The posts say "tahun ajaran 2026" but most
figures are recycled from 2020–2023; each entry uses the oldest year the text implies and is
marked as assumed, with a caution note."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
def src(title, slug, pub):
    return {"title": title + " (Lembar Kerja Untuk Anak)", "url": f"https://lembarkerjauntukanak.com/{slug}/", "published": pub}
JP_ = src("Biaya Masuk SD di Jakarta Pusat Terbaru", "biaya-masuk-sd-di-jakarta-pusat-terbaru", "2026-09-07")
JBU = src("Biaya Masuk SD Jakarta Barat dan Utara", "biaya-masuk-sd-jakarta-barat-dan-utara", "2026-09-07")
TNG = src("Biaya Masuk Sekolah Dasar di Tangerang & Tangerang Selatan", "biaya-masuk-sekolah-dasar-di-tangerang-tangerang-selatan", "2026-09-08")
JKT = src("Biaya Sekolah Dasar di Jakarta", "biaya-sekolah-dasar-di-jakarta", "2026-09-08")
C = ("Artikel blog menyebut tahun ajaran 2026, tetapi angkanya tampak lama (2020–2023). Konfirmasi ke sekolah.", "The blog post says academic year 2026, but the figures look old (2020–2023). Confirm with the school.")
M = lambda a: {"amount": a, "period": "month"}
def s(slug, name, city, district, address, source, year, religion=None, note=("", ""), assumed=True, **f):
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year=year, source=source, checked=CHK,
           **({"yearAssumed": True} if assumed else {}), notes=L((note[0] + " " + C[0]).strip(), (note[1] + " " + C[1]).strip()), **f)
JS, JT, JP, JB, JU = "Jakarta Selatan", "Jakarta Timur", "Jakarta Pusat", "Jakarta Barat", "Jakarta Utara"

# Jakarta Pusat (waves Oct 2022–Jul 2023 -> 2023/2024)
s("sekolah-bunda-mulia-petojo", "Sekolah Bunda Mulia Petojo", JP, None, None, JP_, "2023/2024", "Katolik",
  ("Uang pangkal Rp6.000.000 (reguler) / Rp13.000.000 (bilingual), termasuk seragam dan buku tahun pertama. SPP Rp950.000 (reguler) / Rp1.950.000 (bilingual).", "Entry Rp6,000,000 (regular) / Rp13,000,000 (bilingual), incl. first-year uniforms and books. Tuition Rp950,000 (regular) / Rp1,950,000 (bilingual)."),
  registrationFee=250_000, entryFee={"min": 6_000_000, "max": 13_000_000}, tuition=M(950_000))
s("sd-paskalis-1-jakarta", "SD Paskalis 1 Jakarta", JP, None, None, JP_, "2023/2024", "Katolik",
  ("Uang pangkal gelombang I (Okt–Des 2022) Rp2.200.000, II Rp2.500.000, III Rp2.700.000, IV (Jul 2023) Rp3.000.000. SPP belum termasuk ekskul.", "Entry wave I (Oct–Dec 2022) Rp2,200,000, II Rp2,500,000, III Rp2,700,000, IV (Jul 2023) Rp3,000,000. Tuition excludes extracurriculars."),
  assumed=False, registrationFee=85_000, entryFee={"min": 2_200_000, "max": 3_000_000}, tuition=M(280_000))
s("sds-taman-siswa-jakarta", "SDS Taman Siswa Jakarta", JP, None, None, JP_, "2023/2024", None, ("SPP termasuk kaos olahraga dan seragam batik.", "Tuition includes a sports shirt and batik uniform."), tuition=M(300_000))

# Jakarta Barat & Utara (discounts "until Oct 2020" -> 2021/2022; some explicitly 2020/2021)
Y = "2021/2022"
s("st-johns-catholic-school-meruya", "St. John's Catholic School Meruya", JB, "Kembangan", "Taman Villa Meruya, Jakarta Barat", JBU, Y, "Katolik", registrationFee=250_000, entryFee={"min": 21_000_000}, tuition=M(2_550_000))
s("jakarta-islamic-school-joglo", "Jakarta Islamic School (JISc) Joglo", JB, "Kembangan", "Jl. Rudal V No.16, Joglo, Jakarta Barat", JBU, Y, "Islam",
  ("Uang pangkal termasuk 6 seragam dan SPP 1 bulan. Kenaikan SPP 10–20% per tingkat.", "Entry fee includes 6 uniforms and 1 month's tuition. Tuition rises 10–20% per grade."),
  registrationFee=500_000, entryFee={"min": 26_550_000}, tuition=M(2_050_000),
  otherFees=[fee("Daftar ulang per tahun (±)", "Annual re-registration (approx.)", 3_000_000), fee("Buku per tahun", "Books per year", 1_500_000), fee("Native speaker per tahun", "Native speaker per year", 1_100_000)])
s("sd-sumbangsih-grogol", "SD Sumbangsih Grogol", JB, "Grogol Petamburan", None, JBU, "2020/2021", None,
  ("Total biaya masuk gelombang I Rp11.450.000, gelombang II Rp13.200.000 (paket buku, seragam, dokumen, kegiatan 1 tahun, SPP 1 bulan).", "Total entry wave I Rp11,450,000, wave II Rp13,200,000 (books, uniforms, documents, 1 year of activities, 1 month's tuition)."),
  assumed=False, entryFee={"min": 11_450_000, "max": 13_200_000})
s("sd-plus-hang-tuah-1-jakarta", "SD Plus Hang Tuah 1 Jakarta", JU, None, None, JBU, "2020/2021", None,
  ("Total biaya masuk Rp7.250.000 termasuk SPP 1 bulan Rp400.000, buku, seragam, dana pendidikan.", "Total entry Rp7,250,000 incl. 1 month's tuition Rp400,000, books, uniforms, education fund."),
  assumed=False, entryFee={"min": 7_250_000}, tuition=M(400_000))
s("bina-tunas-bangsa-school-jakarta", "Bina Tunas Bangsa School", JU, None, None, JBU, Y, None, ("Belum termasuk buku dan kegiatan.", "Excludes books and activities."),
  registrationFee=4_000_000, entryFee={"min": 61_000_000}, tuition=M(4_950_000))
s("sekolah-pelangi-kasih-jakarta", "Sekolah Pelangi Kasih", JU, None, "Taman Grisenda, Jakarta Utara", JBU, Y, "Kristen", ("Biaya tes Rp200.000; uang pendaftaran Rp6.000.000.", "Test Rp200,000; registration Rp6,000,000."),
  registrationFee=6_000_000, entryFee={"min": 15_000_000}, tuition={"amount": 12_000_000, "period": "quarter"})

# Tangerang & Tangsel (no year -> 2023/2024 assumed)
Y = "2023/2024"
s("sekolah-pahoa", "Sekolah Pahoa", "Kabupaten Tangerang", "Kelapa Dua", "Jl. Ki Hajar Dewantara No.6, Summarecon Serpong, Pakulonan Barat, Kelapa Dua, Kabupaten Tangerang", TNG, Y, None,
  ("Biaya masuk dan lain-lain Rp28.800.000.", "Entry and other fees Rp28,800,000."), entryFee={"min": 28_800_000}, tuition=M(2_700_000))
s("sd-poris-indah-tangerang", "SD Poris Indah Tangerang", "Kota Tangerang", "Cipondoh", "Yayasan Bina Pratama, Jl. Blok Ambon, Cipondoh Indah, Cipondoh, Kota Tangerang", TNG, Y, None, entryFee={"min": 10_135_000}, tuition=M(640_000))
s("sdit-cordova-1-tangerang", "SDIT Cordova 1 Tangerang", "Kota Tangerang", "Periuk", "Cluster Alamanda Blok E6 No.1, Periuk, Kota Tangerang", TNG, Y, "Islam", entryFee={"min": 13_400_000}, tuition=M(640_000))
s("sekolah-islamic-village-tangerang", "Sekolah Islamic Village Tangerang", "Kabupaten Tangerang", "Kelapa Dua", "Komp. Pendidikan Islamic Village, Jl. Islamic Raya, Kelapa Dua, Kabupaten Tangerang", TNG, Y, "Islam", entryFee={"min": 29_000_000}, tuition=M(1_750_000))
s("sdit-citra-matahari-pamulang", "SDIT Citra Matahari Pamulang", "Tangerang Selatan", "Pamulang", "Jl. H. Nurleman No.30, Benda Baru, Pamulang, Tangerang Selatan", TNG, Y, "Islam", entryFee={"min": 12_200_000}, tuition=M(650_000))
s("sekolah-budi-luhur-pondok-aren", "Sekolah Budi Luhur Pondok Aren", "Tangerang Selatan", "Pondok Aren", "Jl. Jombang Raya No.77, Pondok Aren, Tangerang Selatan", TNG, Y, None, entryFee={"min": 23_500_000}, tuition=M(1_000_000))
s("perguruan-islam-al-syukro-universal", "Perguruan Islam Al Syukro Universal", "Tangerang Selatan", "Ciputat", "Jl. Otista Raya H. Ma'ung, Ciputat, Tangerang Selatan", TNG, Y, "Islam",
  ("SPP belum termasuk katering (Rp17.500/hari).", "Tuition excludes catering (Rp17,500/day)."), entryFee={"min": 23_315_000}, tuition=M(800_000))

# Jakarta (no year -> 2023/2024 assumed)
s("sd-islam-al-azhar-1-kebayoran-baru", "SD Islam Al Azhar 1 Kebayoran Baru", JS, "Kebayoran Baru", "Komplek Masjid Agung Al-Azhar, Jl. Sisingamangaraja, Gunung, Kebayoran Baru, Jakarta Selatan", JKT, Y, "Islam",
  ("Disebut \"SD Al-Azhar Pusat\". Uang pangkal Rp38.825.000 (alumni TK Al-Azhar) / Rp43.000.000 (non-alumni).", "Called \"SD Al-Azhar Pusat\". Entry Rp38,825,000 (TK Al-Azhar alumni) / Rp43,000,000 (others)."),
  registrationFee=350_000, entryFee={"min": 38_825_000, "max": 43_000_000}, tuition=M(2_200_000))
s("sd-pangudi-luhur-jakarta", "SD Pangudi Luhur Jakarta", JS, "Cilandak", "Jl. H. Nawi Raya No.21, Gandaria Selatan, Cilandak, Jakarta Selatan", JKT, Y, "Katolik",
  entryFee={"min": 13_000_000}, tuition=M(900_000), otherFees=[fee("Biaya pengembangan", "Development fee", 4_000_000), fee("UKK per bulan", "UKK per month", 200_000)])
s("sd-harapan-prestasi-jakarta", "SD Harapan Prestasi Jakarta", JT, "Kramat Jati", "Jl. Dewi Sartika No.293A, Cawang, Kramat Jati, Jakarta Timur", JKT, Y, None,
  entryFee={"min": 28_000_000}, tuition=M(1_800_000), otherFees=[fee("Pengembangan per tahun", "Development per year", 4_500_000)])
s("sd-keenkids-jakarta", "SD KeenKids Jakarta", JS, "Kebayoran Lama", "Jl. Ciputat Raya No.1, Kebayoran Lama Utara, Jakarta Selatan", JKT, Y, None,
  ("Tuition fee Rp7 juta per 6 bulan, ditambah SPP Rp2,8 juta per bulan (menurut artikel).", "Tuition Rp7M per 6 months, plus Rp2.8M monthly (per the article)."), tuition=M(2_800_000), otherFees=[fee("Tuition fee per semester", "Tuition fee per semester", 7_000_000)])
