"""Round 4, Jabodetabek.
- SMPIT BISA Depok, official SPMB page (TA 2027/2028).
- Nurhikmah Bekasi, official SPMB 2027/2028 page (registration fees only).
- Lembar Kerja Untuk Anak, "Biaya SD Jakarta Selatan dan Timur Tahun Ajaran Baru 2026" (28 Sep 2026).
  The article says "tahun ajaran baru 2026" but several figures mention COVID-19 adjustments,
  so they are likely older; marked yearAssumed with a caution note.
- Data Pendidikan, "7 Harga Sekolah SD Swasta Terbaik di Jakarta Selatan" (2 Oct 2026, no year stated)."""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"

# --- SMPIT BISA Depok (official)
BISA = {"title": "SPMB SMPIT BISA Depok TA 2027/2028 (situs resmi)", "url": "https://smpit.bisa.sch.id/spmb/"}
upsert("smpit-bisa-depok", name="SMPIT BISA Depok", city="Depok", district="Pancoran Mas",
       address="Jl. Cagar Alam Selatan No.17, Pancoran Mas, Kota Depok", website="https://smpit.bisa.sch.id/", religion="Islam",
       level="SMP", year="2027/2028", source=BISA, checked=CHK,
       registrationFee=500_000, entryFee={"min": 7_500_000, "max": 9_500_000}, tuition={"amount": 850_000, "period": "month"},
       notes=L("Uang pangkal 3 pilihan: I Rp9.500.000, II Rp8.500.000, III Rp7.500.000 (termasuk seragam, modul, kegiatan). Kuota 20 putra dan 10 putri.",
               "Three entry-fee options: I Rp9,500,000, II Rp8,500,000, III Rp7,500,000 (incl. uniforms, modules, activities). Quota 20 boys and 10 girls."))
add_admission("smpit-bisa-depok", {"level": "SMP", "academicYear": "2027/2028",
    "period": L("Gelombang 2: 1 Des 2026–31 Jan 2027; gelombang 3: 1 Feb–30 Apr 2027", "Wave 2: 1 Dec 2026–31 Jan 2027; wave 3: 1 Feb–30 Apr 2027"),
    "steps": [L("Bayar uang pendaftaran Rp500.000 (transfer BSI a.n. SDIT BISA Depok)", "Pay the Rp500,000 registration fee (BSI transfer to SDIT BISA Depok)"),
              L("Isi formulir pendaftaran online", "Fill in the online registration form"),
              L("Buat janji jadwal tes dan observasi dengan sekolah", "Book a test and observation slot with the school"),
              L("Ikuti tes dan observasi dengan membawa Formulir Data dan Informasi Tambahan (FDIT)", "Attend the test and observation, bringing the completed additional data form (FDIT)"),
              L("Jika lulus: lunasi uang masuk, lengkapi berkas, tanda tangani Surat Patuh Aturan Pendidikan", "If accepted: pay the entry fee in full, submit documents, sign the school rules agreement")],
    "documents": [L("Fotokopi rapor kelas 4, 5 dan 6", "Copy of grade 4, 5 and 6 report cards"), L("Fotokopi ijazah dilegalisir (3 lembar)", "Legalised diploma copies (3)"),
                  L("Surat keterangan baik dari sekolah asal", "Good-conduct letter from previous school"), L("Fotokopi akta kelahiran, KK, KTP ayah dan ibu (masing-masing 3 lembar)", "Copies of birth certificate, family card, both parents' ID cards (3 each)"),
                  L("Pas foto 3×4 dan 4×6 latar biru (masing-masing 4 lembar)", "Blue-background photos 3×4 and 4×6 (4 each)"), L("Surat keterangan sehat dari puskesmas", "Health certificate from a community health centre"),
                  L("Sertifikat prestasi (jika ada)", "Achievement certificates (if any)")],
    "notes": L("Alur pendaftaran one day service.", "One-day-service registration flow."), "source": BISA, "checked": CHK})

# --- Nurhikmah Bekasi (official, registration fees only)
NH = {"title": "Informasi SPMB 2027/2028 Sekolah Nurhikmah (situs resmi)", "url": "https://nurhikmah.sch.id/informasi-ppdb-2025-2026/"}
NHC = dict(name="Sekolah Islam Nurhikmah Bekasi", city="Kota Bekasi", district="Pondok Melati", website="https://nurhikmah.sch.id/", religion="Islam",
           year="2027/2028", source=NH, checked=CHK)
nh_note = L("Halaman resmi hanya mencantumkan biaya pendaftaran; uang pangkal dan SPP tidak dipublikasikan.", "The official page lists registration fees only; entry fee and tuition are not published.")
upsert("sekolah-islam-nurhikmah-bekasi", level="TK", registrationFee=500_000, notes=nh_note, **NHC)
upsert("sekolah-islam-nurhikmah-bekasi", level="SD", registrationFee=600_000,
       notes=L("Pendaftaran Rp600.000 (siswa luar); Rp200.000 untuk lulusan TK Nurhikmah. " + nh_note["id"], "Registration Rp600,000 (external); Rp200,000 for TK Nurhikmah graduates. " + nh_note["en"]), **NHC)
upsert("sekolah-islam-nurhikmah-bekasi", level="SMP", registrationFee=600_000,
       notes=L("Pendaftaran Rp600.000 (siswa luar); Rp250.000 untuk lulusan SD Nurhikmah. " + nh_note["id"], "Registration Rp600,000 (external); Rp250,000 for SD Nurhikmah graduates. " + nh_note["en"]), **NHC)
upsert("sekolah-islam-nurhikmah-bekasi", level="SMA", registrationFee=600_000,
       notes=L("Pendaftaran Rp600.000 (siswa luar); Rp250.000 untuk lulusan SMP Nurhikmah. " + nh_note["id"], "Registration Rp600,000 (external); Rp250,000 for SMP Nurhikmah graduates. " + nh_note["en"]), **NHC)

# --- Lembar Kerja Untuk Anak (Jakarta Selatan & Timur SD)
LK = {"title": "Biaya SD Jakarta Selatan dan Timur Tahun Ajaran Baru 2026 (Lembar Kerja Untuk Anak)", "url": "https://lembarkerjauntukanak.com/biaya-sd-jakarta-selatan-dan-timur/", "published": "2026-09-28"}
C = dict(level="SD", year="2026/2027", yearAssumed=True, source=LK, checked=CHK)
CAUT = ("Artikel menyebut tahun ajaran 2026, tetapi sebagian angka menyebut penyesuaian COVID-19 sehingga kemungkinan data lama. Konfirmasi ke sekolah.",
        "The article says academic year 2026, but some figures mention COVID-19 adjustments, so they may be older. Confirm with the school.")
def n(i="", e=""):
    return L((i + " " + CAUT[0]).strip(), (e + " " + CAUT[1]).strip())
JS, JT = "Jakarta Selatan", "Jakarta Timur"

upsert("sekolah-kembang-jakarta", name="Sekolah Kembang", city=JS, district="Mampang Prapatan", address="Jl. Kemang II No.1, Bangka, Mampang Prapatan, Jakarta Selatan",
       registrationFee=10_000_000, entryFee={"min": 50_000_000}, tuition={"amount": 45_000_000, "period": "year"},
       otherFees=[fee(*ACTIVITY, 3_250_000)], notes=n(), **C)
upsert("sd-kupu-kupu-jakarta", name="SD Kupu-Kupu", city=JS, district="Mampang Prapatan", address="Jl. Bangka VII Dalam No.14, Pela Mampang, Mampang Prapatan, Jakarta Selatan",
       registrationFee=200_000, entryFee={"min": 46_500_000, "max": 48_500_000}, tuition={"amount": 2_300_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 695_000)], notes=n("Biaya formulir Rp200.000.", "Form fee Rp200,000."), **C)
upsert("sekolah-cikal-cilandak", name="Sekolah Cikal Cilandak", city=JS, district="Cilandak", address="Jl. TB Simatupang Kav. 18, Cilandak Barat, Jakarta Selatan",
       entryFee={"min": 93_900_000, "max": 104_300_000}, tuition={"amount": 6_000_000, "period": "month"},
       notes=n("Uang pangkal Rp104,3 juta (non-sibling) / Rp93,9 juta (sibling). Tuition Rp6 juta/bulan, Rp17,4 juta/3 bulan, atau Rp65,8 juta/tahun.",
               "Entry fee Rp104.3M (non-sibling) / Rp93.9M (sibling). Tuition Rp6M/month, Rp17.4M/3 months, or Rp65.8M/year."), **C)
upsert("sd-bina-gita-gemilang-jakarta", name="SD Bina Gita Gemilang", city=JS, district="Tebet", address="Jl. Prof. Dr. Soepomo No.11, Tebet Barat, Jakarta Selatan",
       registrationFee=750_000, entryFee={"min": 33_000_000, "max": 34_000_000}, tuition={"amount": 3_100_000, "period": "month"},
       notes=n("Uang pangkal Rp34 juta; Rp33 juta untuk alumni TK Kinderfield. SPP Rp9,3 juta per term atau Rp3,1 juta per bulan.",
               "Entry fee Rp34M; Rp33M for TK Kinderfield alumni. Tuition Rp9.3M per term or Rp3.1M per month."), **C)
upsert("sd-kreativitas-anak-indonesia-jakarta", name="SD Kreativitas Anak Indonesia", city=JS, district="Jagakarsa", address="Jl. Kedondong No.18, Jagakarsa, Jakarta Selatan",
       entryFee={"min": 28_300_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Uang tahunan", "Annual fee", 4_150_000)], notes=n(), **C)
upsert("sd-gemala-ananda-jakarta", name="SD Gemala Ananda", city=JS, district="Cilandak", address="Jl. Lebak Bulus III No.93G, Lebak Bulus, Cilandak, Jakarta Selatan",
       entryFee={"min": 0}, tuition={"amount": 2_480_000, "period": "month"},
       otherFees=[fee("Uang tahunan", "Annual fee", 9_000_000)], notes=n("Tidak ada uang pangkal.", "No entry fee."), **C)
upsert("green-montessori-school-jakarta", name="Green Montessori School", city=JS, district="Pancoran", address="Jl. Duren Tiga Raya No.133, Duren Tiga, Pancoran, Jakarta Selatan",
       entryFee={"min": 75_000_000}, tuition={"amount": 11_800_000, "period": "quarter"},
       otherFees=[fee("Uang tahunan kelas 1–3", "Annual fee grades 1–3", 4_500_000), fee("Uang tahunan kelas 4–6", "Annual fee grades 4–6", 5_000_000)],
       notes=n("Termly fee Rp11,8 juta (kelas 1–3) / Rp13,9 juta (kelas 4–6).", "Termly fee Rp11.8M (grades 1–3) / Rp13.9M (grades 4–6)."), **C)
upsert("sekolah-alam-indonesia-cipedak", name="Sekolah Alam Indonesia Cipedak", city=JS, district="Jagakarsa", address="Jl. Pembangunan No.51, Cipedak, Jagakarsa, Jakarta Selatan",
       registrationFee=600_000, entryFee={"min": 18_000_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee("Biaya sit in", "Sit-in fee", 600_000), fee("Uang tahunan", "Annual fee", 4_500_000)], notes=n(), **C)

upsert("kids-republic-jakarta", name="Kids Republic", city=JT, district="Jatinegara", address="Jl. Cipinang Bali I No.5A, Cipinang Muara, Jatinegara, Jakarta Timur",
       registrationFee=500_000, entryFee={"min": 30_000_000}, tuition={"amount": 2_500_000, "period": "month"},
       otherFees=[fee("Annual fee kelas 1–3", "Annual fee grades 1–3", 5_000_000), fee("Annual fee kelas 4–6", "Annual fee grades 4–6", 6_875_000), fee(*UNIFORM, 1_500_000)],
       notes=n("Tuition Rp2,5 juta (kelas 1–3) / Rp3 juta (kelas 4–6).", "Tuition Rp2.5M (grades 1–3) / Rp3M (grades 4–6)."), **C)
upsert("sd-nizamia-andalusia-jakarta", name="SD Nizamia Andalusia", city=JT, district="Cipayung", address="Jl. Raya Mabes Hankam No.15-16, Bambu Apus, Cipayung, Jakarta Timur", religion="Islam",
       registrationFee=750_000, entryFee={"min": 39_800_000}, tuition={"amount": 2_800_000, "period": "month"},
       otherFees=[fee("Material fee", "Material fee", 4_900_000)], notes=n("Enrollment fee Rp39,8 juta. SPP naik sekitar 8% di tahun kedua.", "Enrollment fee Rp39.8M. Tuition rises about 8% in the second year."), **C)
upsert("sd-kinderfield-jakarta-timur", name="SD Kinderfield Jakarta Timur", city=JT, district="Duren Sawit", address="Jl. Rawa Domba No.88, Duren Sawit, Jakarta Timur",
       registrationFee=2_500_000, entryFee={"min": 42_000_000}, tuition={"amount": 4_200_000, "period": "month"},
       otherFees=[fee("Tes masuk", "Entrance test", 500_000), fee("Uang tahunan", "Annual fee", 10_000_000), fee("Buku & aktivitas (tahunan)", "Books & activities (annual)", 4_500_000)],
       notes=n("Tuition Rp4,2 juta di kelas 1, turun hingga Rp3,1 juta di kelas 6.", "Tuition Rp4.2M in grade 1, falling to Rp3.1M in grade 6."), **C)
upsert("embun-pagi-islamic-school-jakarta", name="Embun Pagi Islamic School", city=JT, district="Duren Sawit", address="Jl. Raya Kalimalang No.8, Pondok Kelapa, Duren Sawit, Jakarta Timur", religion="Islam",
       registrationFee=650_000, entryFee={"min": 34_000_000, "max": 38_000_000}, tuition={"amount": 2_700_000, "period": "month"},
       otherFees=[fee("Buku (min.)", "Books (min.)", 1_500_000), fee("Buku (maks.)", "Books (max.)", 2_000_000)],
       notes=n("Uang pangkal: early bird Rp34 juta, gelombang 1 Rp35 juta, gelombang 2 Rp36 juta, gelombang 3 (normal) Rp38 juta.",
               "Entry fee: early bird Rp34M, wave 1 Rp35M, wave 2 Rp36M, wave 3 (normal) Rp38M."), **C)
upsert("sdit-ar-rahmah-jakarta-timur", name="SDIT Ar-Rahmah Jakarta Timur", city=JT, district="Duren Sawit", address="Jl. Duren Sawit Barat II Blok F No.2, Klender, Duren Sawit, Jakarta Timur", religion="Islam",
       entryFee={"min": 12_000_000}, tuition={"amount": 950_000, "period": "month"},
       otherFees=[fee("Seragam putra", "Uniforms (boys)", 1_700_000), fee("Seragam putri", "Uniforms (girls)", 2_000_000), fee("Buku/modul", "Books/modules", 1_300_000), fee("Uang kegiatan per tahun", "Activities per year", 2_800_000)],
       notes=n("Dana sumbangan pendidikan Rp12 juta.", "Education contribution Rp12M."), **C)
upsert("sdit-nurul-iman-jakarta-timur", name="SDIT Nurul Iman Jakarta Timur", city=JT, district="Duren Sawit", address="Jl. Kesehatan No.7, Pondok Bambu, Duren Sawit, Jakarta Timur", religion="Islam",
       registrationFee=200_000, entryFee={"min": 18_500_000}, tuition={"amount": 970_000, "period": "month"},
       notes=n("Biaya masuk Rp18,5 juta sudah termasuk diskon 20% penyesuaian COVID-19.", "Entry fee Rp18.5M already includes a 20% COVID-19 discount."), **C)
upsert("global-islamic-school-condet", name="Global Islamic School Condet", city=JT, district="Kramat Jati", address="Jl. Raya Condet No.5, Balekambang, Kramat Jati, Jakarta Timur", religion="Islam",
       registrationFee=550_000, entryFee={"min": 30_500_000}, tuition={"amount": 1_850_000, "period": "month"},
       otherFees=[fee("Kegiatan, perlengkapan tahunan, BKOMG + SPP bulan pertama", "Activities, annual supplies, BKOMG + first month's tuition", 9_700_000)], notes=n(), **C)

# --- Data Pendidikan (Jakarta Selatan SD)
DP = {"title": "7 Harga Sekolah SD Swasta Terbaik di Jakarta Selatan (Data Pendidikan)", "url": "https://www.datapendidikan.com/blog/harga-sekolah-sd-terbaik-di-jakarta-selatan/", "published": "2026-10-02"}
D = dict(level="SD", year="2026/2027", yearAssumed=True, source=DP, checked=CHK)
DN = ("Artikel tidak menyebut tahun ajaran.", "The article does not state the academic year.")
upsert("sd-muhammadiyah-5-jakarta", name="SD Muhammadiyah 5 Jakarta", city=JS, district="Kebayoran Baru", address="Jl. Limau III No.3, Kebayoran Baru, Jakarta Selatan", religion="Islam",
       entryFee={"min": 12_000_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee("Program kegiatan 1 tahun", "Activities (1 year)", 3_500_000), fee(*UNIFORM, 1_400_000), fee(*BOOKS, 1_300_000)],
       notes=L("Uang pangkal = biaya gedung Rp5.000.000 + BPP Rp7.000.000. Total sekitar Rp19.000.000. " + DN[0], "Entry fee = building Rp5,000,000 + development Rp7,000,000. Total about Rp19,000,000. " + DN[1]), **D)
upsert("raffles-christian-school-pondok-pinang", name="Raffles Christian School Pondok Pinang", city=JS, district="Kebayoran Lama", address="Jl. Gedung Hijau Raya I No.1, Pondok Pinang, Kebayoran Lama, Jakarta Selatan", religion="Kristen",
       entryFee={"min": 32_000_000}, tuition={"amount": 58_000_000, "period": "semester"},
       otherFees=[fee("Biaya tes", "Test fee", 500_000)], notes=L("Biaya pengembangan Rp32 juta. " + DN[0], "Development fee Rp32M. " + DN[1]), **D)
upsert("sekolah-lentera-indonesia-jakarta", name="Sekolah Lentera Indonesia", city=JS, district="Kebayoran Lama", address="Jl. Sultan Iskandar Muda No.98, Kebayoran Lama Utara, Jakarta Selatan",
       registrationFee=200_000, tuition={"amount": 92_000_000, "period": "year"},
       otherFees=[fee("Ujian masuk", "Entrance exam", 1_000_000), fee("Deposit (dapat dikembalikan)", "Refundable deposit", 2_000_000)], notes=L(DN[0], DN[1]), **D)
upsert("sd-al-ikhlas-cipete", name="SD Al-Ikhlas Cipete", city=JS, district="Cilandak", address="Jl. Cipete III No.10, Cipete Selatan, Jakarta Selatan", religion="Islam",
       registrationFee=300_000, entryFee={"min": 27_500_000, "max": 28_500_000},
       notes=L("Uang pangkal Rp28.500.000 (siswa luar) / Rp27.500.000 (dari TK Al-Ikhlas). " + DN[0], "Entry fee Rp28,500,000 (external) / Rp27,500,000 (from TK Al-Ikhlas). " + DN[1]), **D)
