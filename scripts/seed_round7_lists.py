"""Round 7 lists.
- CNBC Indonesia, "7 Rekomendasi SD Unggulan Jabodetabek, SPP di Bawah Rp3 Juta" (15 Sep 2026): years as stated per school.
- Lembar Kerja Untuk Anak, "Biaya Masuk SD Swasta Bekasi Bogor" (16 Sep 2026): mentions 2022-2023 figures -> 2022/2023 (assumed).
- Lembar Kerja Untuk Anak, "Biaya Masuk SMP Swasta Terbaik di Surabaya dan Bandung" (9 Oct 2026): Darul Hikam official 2026/2027; others marked "arsip" -> 2023/2024 (assumed).
- PresGo News, "Daftar Biaya SMP Islam di Depok" (14 Apr 2026): -> 2026/2027 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
CNBC = {"title": "7 Rekomendasi SD Unggulan Jabodetabek, SPP di Bawah Rp3 Juta (CNBC Indonesia)", "url": "https://www.cnbcindonesia.com/lifestyle/20260915125442-33-768042/7-rekomendasi-sd-unggulan-jabodetabek-spp-di-bawah-rp3-juta", "published": "2026-09-15"}
LKB = {"title": "Biaya Masuk SD Swasta Bekasi Bogor. Ada Yang Uang Pangkalnya 5 Juta (Lembar Kerja Untuk Anak)", "url": "https://lembarkerjauntukanak.com/biaya-masuk-sd-swasta-bekasi-bogor-ada-yang-uang-pangkalnya-5-juta/", "published": "2026-09-16"}
LKS = {"title": "Biaya Masuk SMP Swasta Terbaik di Surabaya dan Bandung 2026/2027 (Lembar Kerja Untuk Anak)", "url": "https://lembarkerjauntukanak.com/biaya-masuk-smp-swasta-terbaik-di-surabaya-dan-bandung/", "published": "2026-10-09"}
PRG = {"title": "Daftar Biaya SMP Islam di Depok Lengkap dengan Pilihan Sekolah Terbaik (PresGo News)", "url": "https://presgonews.com/pendidikan/sekolah/daftar-biaya-smp-islam-di-depok-lengkap-dengan-pilihan-sekolah-terbaik/", "published": "2026-04-14"}
M = lambda a: {"amount": a, "period": "month"}
def s(slug, name, city, district, address, source, year, level="SD", religion=None, assumed=True, note=("", ""), **f):
    base = {CNBC["url"]: ("Dihimpun CNBC Indonesia dari informasi biaya sekolah.", "Compiled by CNBC Indonesia from school fee information."),
            LKB["url"]: ("Artikel blog; menyebut angka tahun ajaran 2022-2023 dan belum diperbarui. Konfirmasi ke sekolah.", "Blog article; cites 2022-2023 figures and has not been updated. Confirm with the school."),
            LKS["url"]: ("Artikel menandai angka ini sebagai arsip (belum diverifikasi untuk 2026/2027).", "The article marks these as archived figures (not verified for 2026/2027)."),
            PRG["url"]: ("Dari artikel; tahun ajaran tidak disebut.", "From an article; academic year not stated.")}[source["url"]]
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level=level, year=year, source=source, checked=CHK,
           **({"yearAssumed": True} if assumed else {}), notes=L((note[0] + " " + base[0]).strip(), (note[1] + " " + base[1]).strip()), **f)

# CNBC
s("sd-islam-tugasku-jakarta-timur", "SD Islam Tugasku Jakarta Timur", "Jakarta Timur", None, None, CNBC, "2026/2027", religion="Islam", assumed=False,
  note=("Uang pangkal untuk siswa dari TK luar. Total awal Rp49,9 juta termasuk SPP Juli 2026.", "Entry fee for applicants from other kindergartens. Initial total Rp49.9M incl. July 2026 tuition."),
  entryFee={"min": 39_000_000}, tuition=M(2_500_000), otherFees=[fee("Uang kegiatan per tahun", "Activities per year", 6_500_000), fee(*UNIFORM, 1_900_000)])
s("sd-islam-al-azhar-kelapa-gading", "SD Islam Al Azhar Kelapa Gading", "Jakarta Utara", "Kelapa Gading", None, CNBC, "2026/2027", religion="Islam",
  note=("Alazka. Estimasi biaya awal sekitar Rp43,7 juta; seragam Rp1,8–2,3 juta. Tahun ajaran tidak disebut.", "Alazka. Estimated initial cost about Rp43.7M; uniforms Rp1.8–2.3M. Academic year not stated."),
  registrationFee=600_000, entryFee={"min": 39_000_000}, tuition=M(2_300_000), otherFees=[fee("Seragam (min.)", "Uniforms (min.)", 1_800_000)])
s("tara-salvia", "Tara Salvia", "Tangerang Selatan", "Ciputat", None, CNBC, "2027/2028", religion=None, assumed=False,
  note=("Dari panduan penerimaan siswa baru TP 2027/2028. Uang pangkal siswa umum; confirmation deposit Rp5 juta bagian dari uang pangkal.", "From the 2027/2028 admission guide. Entry fee for general applicants; the Rp5M confirmation deposit is part of it."),
  registrationFee=1_000_000, entryFee={"min": 49_000_000}, tuition=M(2_500_000), otherFees=[fee("Uang kegiatan per tahun", "Activities per year", 3_775_000)])
s("sekolah-auliya", "Sekolah Auliya Bintaro", "Tangerang Selatan", None, None, CNBC, "2026/2027", religion="Islam", assumed=False, entryFee={"min": 47_900_000}, tuition=M(2_300_000))
s("al-siddiq-international-school-bekasi", "Al Siddiq International School Bekasi", "Kota Bekasi", None, None, CNBC, "2025/2026", religion="Islam", assumed=False,
  note=("Dari info pendaftaran TA 2025/2026 yang diunggah sekolah (SPP Juli 2025).", "From the school's posted 2025/2026 admission info (July 2025 tuition)."), registrationFee=750_000, tuition=M(1_650_000))
s("al-wildan-islamic-school-depok", "Al Wildan Islamic School Depok", "Depok", None, None, CNBC, "2026/2027", religion="Islam",
  note=("Cabang Depok; angka \"sekitar\", tahun tidak disebut.", "Depok branch; approximate figures, year not stated."), registrationFee=1_000_000, entryFee={"min": 17_500_000}, tuition=M(1_000_000))

# Lembar Kerja: Bogor & Bekasi
Y = "2022/2023"
KBG = "Kabupaten Bogor"
s("sdit-global-insan-madani-bekasi", "SDIT Global Insan Madani Bekasi", "Kota Bekasi", "Jatisampurna", "Jl. Sumur Binong No.29, Jatirangga, Jatisampurna, Kota Bekasi", LKB, Y, religion="Islam",
  note=("SPP sudah termasuk komite.", "Tuition includes committee fee."), registrationFee=250_000, entryFee={"min": 9_765_000}, tuition=M(495_000))
s("knowledge-link-intercultural-school-sentul", "Knowledge Link Intercultural School (KLIS) Sentul", KBG, "Babakan Madang", "Jl. Raya Sirkuit Sentul, Sentul, Babakan Madang, Kabupaten Bogor", LKB, Y,
  note=("Uang pangkal Rp40.000.000, promo diskon 20% menjadi Rp32.000.000.", "Entry fee Rp40,000,000, 20% promo to Rp32,000,000."),
  entryFee={"min": 32_000_000, "max": 40_000_000}, tuition=M(3_500_000), otherFees=[fee("Kegiatan per tahun", "Activities per year", 9_500_000), fee(*UNIFORM, 750_000), fee("Buku per tahun", "Books per year", 2_000_000)])
s("sd-al-imam-islamic-school-cileungsi", "SD Al Imam Islamic School Cileungsi", KBG, "Cileungsi", "Limus Pratama Regency, Jl. Blitar Blok E.12/7B, Limus Nunggal, Cileungsi, Kabupaten Bogor", LKB, Y, religion="Islam",
  note=("Paket masuk gelombang I Rp14.700.000, gelombang II Rp18.000.000, sudah termasuk SPP Juli Rp800.000 dan uang kegiatan.", "Entry package wave I Rp14,700,000, wave II Rp18,000,000, incl. July tuition Rp800,000 and activities."),
  entryFee={"min": 14_700_000, "max": 18_000_000}, tuition=M(800_000))
s("school-of-universe-parung", "School of Universe Parung", KBG, "Parung", "Jl. Raya Parung No.314 KM 43, Pemagar Sari, Parung, Kabupaten Bogor", LKB, Y, religion="Islam",
  note=("Sekolah inklusi. Uang pangkal reguler Rp32.800.000 (termasuk kegiatan tahunan dan SPP Juli Rp1.250.000); ABK dengan pendamping Rp40.250.000 (SPP Rp4.450.000); ABK tanpa pendamping Rp37.000.000 (SPP Rp3.450.000).",
        "Inclusive school. Regular entry Rp32,800,000 (incl. annual activities and July tuition Rp1,250,000); special-needs with aide Rp40,250,000 (tuition Rp4,450,000); without aide Rp37,000,000 (tuition Rp3,450,000)."),
  entryFee={"min": 32_800_000, "max": 40_250_000}, tuition=M(1_250_000))
s("sdit-anugerah-insani-cibinong", "SDIT Anugerah Insani Cibinong", KBG, "Cibinong", "Jl. Raya Pemda, Bojong Depok Baru III, Karadenan, Cibinong, Kabupaten Bogor", LKB, Y, religion="Islam",
  note=("Uang pangkal gelombang I Rp14.180.000, gelombang II Rp15.890.000, termasuk SPP Juli Rp600.000 dan kegiatan Rp1.350.000.", "Entry wave I Rp14,180,000, wave II Rp15,890,000, incl. July tuition Rp600,000 and activities Rp1,350,000."),
  entryFee={"min": 14_180_000, "max": 15_890_000}, tuition=M(600_000))
s("sdit-insantama-bogor", "SDIT Insantama Bogor", "Kota Bogor", "Bogor Barat", "Jl. Hegarmanah IV, Gunung Batu, Bogor Barat, Kota Bogor", LKB, Y, religion="Islam",
  note=("Uang pangkal = infaq pengembangan.", "Entry fee = development donation."), registrationFee=600_000, entryFee={"min": 19_000_000},
  otherFees=[fee("Seragam putra", "Uniforms (boys)", 935_000), fee("Seragam putri", "Uniforms (girls)", 1_045_000)])
s("tugasku-school-cibinong", "Tugasku School Cibinong", KBG, "Cibinong", "Jl. Pangrango 3 No.9, Sukahati, Cibinong, Kabupaten Bogor", LKB, Y, religion="Islam",
  note=("Uang pangkal sudah termasuk SPP Juli.", "Entry fee includes July tuition."), registrationFee=350_000, entryFee={"min": 5_000_000}, tuition=M(700_000))

# Lembar Kerja: SMP Surabaya & Bandung
upsert("smp-unggulan-darul-hikam-bandung", name="SMP Unggulan Darul Hikam Bandung", city="Kota Bandung", district="Coblong", religion="Islam", level="SMP", year="2026/2027", source=LKS, checked=CHK,
       registrationFee=600_000, entryFee={"min": 35_000_000}, tuition=M(2_050_000),
       otherFees=[fee("Biaya kesiswaan", "Student affairs", 3_000_000), fee(*BOOKS, 2_150_000), fee(*UNIFORM, 1_550_000)],
       notes=L("Rincian resmi 2026/2027 menurut artikel. Dana pengembangan Rp35.000.000; SPP Juli termasuk makan siang. Total awal Rp43.750.000. Program lain (Lower Secondary, pesantren) berbeda.",
               "Official 2026/2027 breakdown per the article. Development fee Rp35,000,000; July tuition includes lunch. Initial total Rp43,750,000. Other programmes (Lower Secondary, boarding) differ."))
YA = "2023/2024"
KB = "Kota Bandung"
s("cendekia-muda-elementary-school-bandung", "Cendekia Muda Elementary School", KB, "Arcamanik", None, LKS, YA, level="SMP", religion="Islam",
  note=("SMP Cendekia Muda. Uang pangkal = uang pengembangan.", "SMP Cendekia Muda. Entry = development fee."), registrationFee=1_000_000, entryFee={"min": 19_250_000}, tuition=M(1_800_000),
  otherFees=[fee("Kegiatan tahunan", "Annual activities", 7_000_000), fee(*UNIFORM, 1_300_000)])
s("salman-al-farisi-bandung", "Sekolah Salman Al Farisi Bandung", KB, None, None, LKS, YA, level="SMP", religion="Islam", entryFee={"min": 29_500_000}, tuition=M(1_800_000),
  otherFees=[fee(*UNIFORM, 1_600_000), fee(*ACTIVITY, 4_947_000)])
s("smpk-bpk-penabur-singgasana-bandung", "SMPK BPK Penabur Singgasana Bandung", KB, None, None, LKS, YA, level="SMP", religion="Kristen", registrationFee=200_000, entryFee={"min": 20_500_000}, tuition=M(3_100_000),
  otherFees=[fee("Fasilitas", "Facilities", 190_000)])
s("smp-santa-angela-bandung", "SMP Santa Angela Bandung", KB, None, None, LKS, YA, level="SMP", religion="Katolik", note=("PPDB 2023/2024. Uang pangkal = DPP.", "2023/2024 admission. Entry fee = DPP."),
  registrationFee=200_000, entryFee={"min": 16_500_000}, tuition=M(1_200_000))
SBY = "Surabaya"
s("smp-kristen-logos-surabaya", "SMP Kristen Logos Surabaya", SBY, None, None, LKS, YA, level="SMP", religion="Kristen", note=("Uang pangkal dapat diangsur; buku dan worksheet 3 tahun termasuk.", "Entry fee can be paid in instalments; 3 years of books and worksheets included."),
  entryFee={"min": 32_000_000}, tuition=M(2_100_000))
s("little-sun-school-surabaya", "Little Sun School Surabaya", SBY, None, None, LKS, YA, level="SMP", note=("Uang pangkal = uang pengembangan; belum termasuk komponen lain.", "Entry = development fee; other components extra."),
  registrationFee=1_500_000, entryFee={"min": 40_500_000}, otherFees=[fee("Formulir", "Form", 300_000), fee("Psikotes", "Psychological test", 500_000), fee("Seragam dan perlengkapan", "Uniforms and supplies", 2_500_000)])
s("smp-santa-clara-surabaya", "SMP Santa Clara Surabaya", SBY, None, None, LKS, YA, level="SMP", religion="Katolik", note=("Paket awal (gedung, pengembangan, kegiatan, seragam).", "Initial package (building, development, activities, uniforms)."),
  entryFee={"min": 20_250_000}, tuition=M(1_500_000))
s("smp-jac-surabaya", "SMP Jalinan Adisiswa Cemerlang (JAC) Surabaya", SBY, None, None, LKS, YA, level="SMP", note=("Biaya registrasi Rp25.000.000; kegiatan Rp2,6 juta per semester; seragam Rp750 ribu per set.", "Registration Rp25,000,000; activities Rp2.6M per semester; uniforms Rp750k per set."),
  entryFee={"min": 25_000_000}, tuition=M(2_000_000), otherFees=[fee("Formulir", "Form", 200_000), fee("Biaya tahunan", "Annual fee", 1_000_000)])
s("smp-margie-surabaya", "SMP Margie Surabaya", SBY, None, None, LKS, YA, level="SMP", note=("Paket pendaftaran Rp19.000.000 (pengembangan, buku kelas VII, kegiatan).", "Admission package Rp19,000,000 (development, grade 7 books, activities)."),
  registrationFee=310_000, entryFee={"min": 19_000_000})

# PresGo: SMP Islam Depok
Y = "2026/2027"
s("smpit-darul-abidin-depok", "SMPIT Darul Abidin Depok", "Depok", "Beji", "Jl. Karet Hijau No.23, Beji Timur, Beji, Depok", PRG, Y, level="SMP", religion="Islam",
  note=("Biaya masuk gelombang I Rp29.500.000, gelombang II Rp31.000.000.", "Entry wave I Rp29,500,000, wave II Rp31,000,000."), entryFee={"min": 29_500_000, "max": 31_000_000}, tuition=M(1_320_000))
s("smp-az-zahra-bojongsari", "SMP Az Zahra Bojongsari", "Depok", "Bojongsari", "Jl. Swadaya No.47, Pondok Petir, Bojongsari, Depok", PRG, Y, level="SMP", religion="Islam", registrationFee=300_000, entryFee={"min": 4_800_000}, tuition=M(385_000))
s("smp-prestasi-global-depok", "SMP Prestasi Global Depok", "Depok", "Pancoran Mas", "Jl. Palem I No.1, Perumahan Mampang Indah II, Rangkapan Jaya, Pancoran Mas, Depok", PRG, Y, level="SMP", religion="Islam",
  note=("Total Rp16.500.000. Beasiswa Rp500.000 untuk siswa lanjutan dari Sekolah Prestasi Global.", "Total Rp16,500,000. Rp500,000 scholarship for continuing Prestasi Global students."), registrationFee=300_000, entryFee={"min": 16_500_000}, tuition=M(850_000))
s("smp-tahfidz-ummul-quro-depok", "SMP Tahfidz Quran Ummul Quro Depok", "Depok", "Beji", "Jl. M.H. Sanim, Kukusan, Beji, Depok", PRG, Y, level="SMP", religion="Islam",
  note=("Formulir Rp250.000–Rp350.000; psikotes Rp500.000.", "Form Rp250,000–Rp350,000; psychological test Rp500,000."), registrationFee=250_000, otherFees=[fee("Psikotes", "Psychological test", 500_000)])
s("smp-islam-raden-patah-depok", "SMP Islam Raden Patah Depok", "Depok", "Cilodong", "Jl. Raya Bogor KM 37, Cilodong, Depok", PRG, Y, level="SMP", religion="Islam",
  note=("Biaya masuk gelombang I Rp11 juta, II Rp12 juta, III Rp13 juta.", "Entry wave I Rp11M, II Rp12M, III Rp13M."), registrationFee=400_000, entryFee={"min": 11_000_000, "max": 13_000_000}, tuition=M(700_000))
s("smpit-al-qalam-depok", "SMPIT Al Qalam Depok", "Depok", "Pancoran Mas", "Jl. Pemuda No.41, Depok Lama", PRG, Y, level="SMP", religion="Islam",
  note=("Biaya masuk Rp20.000.000 (putra) / Rp20.400.000 (putri).", "Entry Rp20,000,000 (boys) / Rp20,400,000 (girls)."), entryFee={"min": 20_000_000, "max": 20_400_000}, tuition=M(900_000))
s("smpit-arafah-depok", "SMPIT Arafah Depok", "Depok", "Tapos", "Jl. Pekapuran, Sukamaju Baru, Tapos, Depok", PRG, Y, level="SMP", religion="Islam",
  note=("Uang pangkal = biaya gedung & pembangunan.", "Entry = building fee."), registrationFee=100_000, entryFee={"min": 5_950_000}, tuition=M(420_000),
  otherFees=[fee("Tes", "Test", 150_000), fee("Kegiatan siswa per tahun", "Student activities per year", 1_700_000), fee(*UNIFORM, 850_000)])
