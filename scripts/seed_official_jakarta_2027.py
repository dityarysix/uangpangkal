"""Official 2027/2028 (or latest) admission pages of Jakarta-area schools, figures verbatim."""
from seedlib import L, fee, upsert, add_admission, ensure_school

CHK = "2026-11-22"

# ---- Annajah, Pesanggrahan (TK/SD/SMP/SMA) ----
AN = {"title": "PPDB Annajah Islamic Jakarta School TP 2027/2028 (situs resmi)", "url": "https://ppdb.annajah-jkt.sch.id/"}
ANS = dict(name="Sekolah Islam Annajah Jakarta", city="Jakarta Selatan", district="Pesanggrahan", religion="Islam",
           address="Jl. Ciledug Raya No.10, Pesanggrahan, Jakarta Selatan", phone="TK (021) 7377677 · SD (021) 73886134 · SMP (021) 7374045 · SMA (021) 7359616",
           website="https://ppdb.annajah-jkt.sch.id", year="2027/2028", source=AN, checked=CHK)
NR = L("Uang pangkal tidak dapat dikembalikan bila mengundurkan diri.", "The entry fee is non-refundable if you withdraw.")
upsert("sekolah-islam-annajah-jakarta", level="TK", registrationFee=200_000, entryFee={"min": 16_860_000}, tuition={"amount": 1_150_000, "period": "month"},
       notes=L("Play group/TK. Uang pangkal termasuk SPP Juli 2027, seragam 5 stel, buku & alat tulis 1 tahun, kegiatan 1 tahun (rekreasi, kunjungan edukasi, manasik haji & tes IQ untuk TK B), rapor, foto.",
               "Playgroup/kindergarten. Entry fee includes July 2027 tuition, 5 uniform sets, a year of books & stationery, a year of activities (trip, educational visits, mock hajj & IQ test for TK B), report book, photo."), **ANS)
upsert("sekolah-islam-annajah-jakarta", level="SD", registrationFee=200_000, entryFee={"min": 17_850_000, "max": 23_800_000}, tuition={"amount": 1_500_000, "period": "month"},
       notes=L("Uang pangkal Rp23.800.000 (dari TK luar Annajah) / Rp17.850.000 (TK Annajah gelombang 1); termasuk SPP Juli 2027, gedung & seragam, buku 1 tahun, kesiswaan, ujian, rapor.",
               "Entry fee Rp23,800,000 (from outside kindergartens) / Rp17,850,000 (Annajah kindergarten, wave 1); includes July 2027 tuition, building & uniforms, a year of books, student affairs, exams, report book."), **ANS)
upsert("sekolah-islam-annajah-jakarta", level="SMP", registrationFee=200_000, entryFee={"min": 14_010_000, "max": 18_680_000}, tuition={"amount": 1_300_000, "period": "month"},
       notes=L("Uang pangkal Rp18.680.000 (dari SD/MI luar) / Rp14.010.000 (SDI Annajah); termasuk seragam 5 stel, SPP Juli 2027, ekskul non-mitra, buku 1 tahun, ulangan umum, LDKS/city tour, jaket almamater. " + NR["id"],
               "Entry fee Rp18,680,000 (from other primary schools) / Rp14,010,000 (SDI Annajah); includes 5 uniform sets, July 2027 tuition, extracurriculars, a year of books, exams, leadership camp/city tour, school jacket. " + NR["en"]), **ANS)
upsert("sekolah-islam-annajah-jakarta", level="SMA", registrationFee=200_000, entryFee={"min": 14_239_000, "max": 18_985_000}, tuition={"amount": 1_300_000, "period": "month"},
       notes=L("Uang pangkal Rp18.985.000 (dari SMP/MTs luar) / Rp14.239.000 (MTs/SMP Annajah); termasuk seragam 6 stel, SPP Juli 2027, ekskul 1 tahun, buku kelas X, ujian, lab bahasa, program riset, LDKS. SPP Rp1.300.000 tidak naik selama 3 tahun, termasuk lab komputer & bahasa. Bayar minimal 50% setelah lulus seleksi, sisanya tahap II. " + NR["id"],
               "Entry fee Rp18,985,000 (from other junior highs) / Rp14,239,000 (Annajah); includes 6 uniform sets, July 2027 tuition, a year of extracurriculars, grade 10 books, exams, language lab, research programme, leadership camp. Tuition Rp1,300,000 is fixed for 3 years and includes computer & language labs. Pay at least 50% after acceptance, the rest in stage II. " + NR["en"]), **ANS)
for lvl, period, docs, test, extra in [
    ("TK", ("Pendaftaran mulai 1 Oktober 2026.", "Registration from 1 October 2026."),
     [L("2 fotokopi akta kelahiran", "2 copies of birth certificate"), L("2 fotokopi Kartu Keluarga", "2 copies of family card"), L("2 foto calon siswa (ukuran 3R)", "2 photos of the child (3R size)")],
     ("Observasi.", "Observation."), ("Usia per Juli 2026: Play group 3–4 tahun; TK A 4–5 tahun; TK B 5–6 tahun.", "Age by July 2026: playgroup 3–4; TK A 4–5; TK B 5–6.")),
    ("SD", ("Pendaftaran mulai 19 Oktober 2026.", "Registration from 19 October 2026."),
     [L("2 fotokopi akta kelahiran", "2 copies of birth certificate"), L("2 fotokopi Kartu Keluarga", "2 copies of family card"), L("Pas foto 4x6 latar merah", "4x6 photo, red background")],
     ("Observasi: pengenalan huruf, angka, dan psikomotorik.", "Observation: letters, numbers and motor skills."), ("Usia minimal 6 tahun pada bulan Juli (sumber menulis Juli 2025).", "Minimum age 6 in July (the source says July 2025).")),
    ("SMP", ("Pendaftaran mulai 19 Oktober 2026.", "Registration from 19 October 2026."),
     [L("Fotokopi akta kelahiran", "Copy of birth certificate"), L("Fotokopi Kartu Keluarga", "Copy of family card"), L("Fotokopi NISN", "Copy of NISN"), L("Surat pernyataan siswa dan orang tua bermaterai", "Signed student & parent statement with duty stamp")],
     ("Observasi atau tes.", "Observation or test."), None),
    ("SMA", ("Pendaftaran mulai 19 Oktober 2026.", "Registration from 19 October 2026."),
     [L("2 fotokopi akta kelahiran", "2 copies of birth certificate"), L("2 fotokopi Kartu Keluarga", "2 copies of family card"), L("2 fotokopi NISN", "2 copies of NISN"), L("2 fotokopi ijazah SMP/MTs", "2 copies of junior high certificate")],
     ("Observasi atau tes.", "Observation or test."), None)]:
    add_admission("sekolah-islam-annajah-jakarta", {"level": lvl, "academicYear": "2027/2028", "period": L(*period),
        "steps": [L("Bayar formulir Rp200.000.", "Pay the Rp200,000 form fee."), L("Ikuti observasi/tes.", "Attend the observation/test."), L("Bila diterima, bayar uang pangkal.", "If accepted, pay the entry fee.")],
        "documents": docs, "test": L(*test), **({"notes": L(*extra)} if extra else {}), "source": AN, "checked": CHK})

# ---- SMA EMIISc Jakarta (2026/2027) ----
EM = {"title": "SPMB SMA EMIISc Jakarta TA 2026/2027 (situs resmi)", "url": "https://emiisc.sch.id/sma-emiisc-jakarta/"}
upsert("sma-emiisc-jakarta", name="SMA EMIISc Jakarta", city="Jakarta Timur", district="Kramat Jati", religion="Islam",
       address="Jl. Raya Condet No.27, Batu Ampar, Kramat Jati, Jakarta Timur", website="https://emiisc.sch.id",
       level="SMA", year="2026/2027", source=EM, checked=CHK,
       registrationFee=600_000, entryFee={"min": 30_000_000}, tuition={"amount": 1_705_000, "period": "month"},
       otherFees=[fee("Uang tahunan (kelas 10)", "Annual fee (grade 10)", 4_990_000)],
       notes=L("Biaya pendaftaran termasuk tes masuk. Uang pangkal minimal 50% dibayar setelah lulus tes, lalu dilunasi. Uang tahunan kelas 11 & 12 berbeda.", "Registration includes the entrance test. Pay at least 50% of the entry fee after passing the test, then the rest. Annual fee differs for grades 11 & 12."))
add_admission("sma-emiisc-jakarta", {"level": "SMA", "academicYear": "2026/2027",
    "steps": [L("Daftar dan bayar biaya pendaftaran & tes.", "Register and pay the registration & test fee."), L("Ikuti tes masuk dan tanda tangan MOU.", "Take the entrance test and sign the MOU."),
              L("Bayar uang pangkal minimal 50%.", "Pay at least 50% of the entry fee."), L("Lunasi sisa uang pangkal.", "Pay the remaining entry fee."), L("Mulai kegiatan belajar.", "Start classes.")],
    "test": L("Tes masuk.", "Entrance test."), "source": EM, "checked": CHK})

# ---- SDIT Al-Uswah Jakarta (2027/2028) ----
AU = {"title": "Info PMB SDIT Al-Uswah TP 2027/2028 (situs resmi)", "url": "https://web.sditaluswahjakarta.sch.id/info-ppdb/"}
upsert("sdit-al-uswah-jakarta", name="SDIT Al-Uswah Jakarta", city="Jakarta Selatan", district="Jagakarsa", religion="Islam",
       address="Jl. Pratama No.21, Srengseng Sawah, Jagakarsa, Jakarta Selatan", website="https://web.sditaluswahjakarta.sch.id",
       level="SD", year="2027/2028", source=AU, checked=CHK,
       entryFee={"min": 12_000_000}, tuition={"amount": 1_100_000, "period": "month"},
       otherFees=[fee("Seragam 6 macam", "Uniforms (6 types)", 1_200_000), fee("Buku tulis & paket 1 tahun", "Exercise & textbooks (1 year)", 1_600_000), fee("Uang kegiatan 1 tahun", "Activities (1 year)", 2_100_000)],
       notes=L("Uang pangkal = dana pengembangan sarana prasarana. SPP termasuk katering dan ekstrakurikuler. Total masuk Rp18.000.000; potongan Rp500.000 untuk 50 pendaftar pertama. Per November 2026 kuota pendaftaran online dan offline sudah terpenuhi.",
               "Entry fee = facilities development fund. Tuition includes catering and extracurriculars. Total on entry Rp18,000,000; Rp500,000 off for the first 50 applicants. As of November 2026 both online and offline quotas are full."))

# ---- Admission info only (no fees published) ----
GZ = {"title": "Pengumuman Penerimaan Peserta Didik Baru 2027/2028 — SMA Kolese Gonzaga (situs resmi)", "url": "https://www.gonzaga.sch.id/en/pengumuman-penerimaan-peserta-didik-baru-2027-2028/"}
ensure_school("sma-kolese-gonzaga", name="SMA Kolese Gonzaga", city="Jakarta Selatan", district="Pasar Minggu", levels=["SMA"], religion="Katolik",
              address="Jl. Pejaten Barat 10A, Jakarta Selatan", phone="(021) 7804986 / WA +62 819-2701-1222", website="https://www.gonzaga.sch.id")
add_admission("sma-kolese-gonzaga", {"level": "SMA", "academicYear": "2027/2028",
    "period": L("Seleksi 2027/2028 sudah selesai; pengumuman 30 Oktober 2026 dan daftar ulang (pertemuan wajib orang tua) 31 Oktober 2026.", "Selection for 2027/2028 is finished; results on 30 October 2026 and re-registration (mandatory parents' meeting) on 31 October 2026."),
    "steps": [L("Pendaftaran online dan tes akademik di sekolah.", "Online registration and an academic test at the school."), L("Pengumuman hasil seleksi.", "Results announced."),
              L("Orang tua calon murid yang diterima wajib hadir sendiri (tidak boleh diwakilkan) untuk daftar ulang; yang tidak hadir dianggap mengundurkan diri.", "Parents of accepted students must attend in person for re-registration; absence counts as withdrawal.")],
    "test": L("Tes akademik.", "Academic test."), "notes": L("Biaya tidak dicantumkan di situs.", "Fees are not published on the site."), "source": GZ, "checked": CHK})

AZ = {"title": "Penerimaan Siswa Baru Perguruan Islam Al-Izhar Pondok Labu (situs resmi)", "url": "https://psb.alizhar.sch.id/"}
ensure_school("al-izhar-pondok-labu", name="Perguruan Islam Al-Izhar Pondok Labu", city="Jakarta Selatan", district="Cilandak", levels=["KB", "TK", "SD", "SMP", "SMA"], religion="Islam",
              address="Jl. RS Fatmawati Kav.49, Pondok Labu, Cilandak, Jakarta Selatan", website="https://psb.alizhar.sch.id")
add_admission("al-izhar-pondok-labu", {"academicYear": "2027/2028",
    "period": L("Pendaftaran 3–17 November 2026 (pukul 14.30 WIB): KB, TK, SD untuk internal; SMP dan SMA untuk internal (reguler), eksternal (early bird, ditutup bila kuota penuh), dan beasiswa.",
                "Registration 3–17 November 2026 (14:30 WIB): KB, TK and SD for internal applicants; SMP and SMA for internal (regular), external (early bird, closes when full) and scholarship tracks."),
    "steps": [L("Daftar online di psb.alizhar.sch.id.", "Register online at psb.alizhar.sch.id."), L("Transfer biaya pendaftaran ke rekening sekolah dan unggah bukti di akun PSB.", "Transfer the registration fee to the school account and upload proof in your PSB account."),
              L("Ikuti seleksi dan wawancara orang tua sesuai jadwal.", "Attend the selection and parent interview on schedule."), L("Pengumuman lewat email orang tua, lalu lunasi biaya pendidikan.", "Results by email to parents, then pay the education fees.")],
    "test": L("Seleksi PSB dan wawancara orang tua.", "Admission selection and parent interview."), "notes": L("Besaran biaya tidak dicantumkan di halaman.", "Fee amounts are not shown on the page."), "source": AZ, "checked": CHK})

SU = {"title": "Pendaftaran SMP Santa Ursula Jakarta — SPMB 2027/2028 (situs resmi)", "url": "https://smp.santaursulajakarta.sch.id/pendaftaran/"}
ensure_school("santa-ursula-jakarta", name="Sekolah Santa Ursula Jakarta", city="Jakarta Pusat", district="Sawah Besar", levels=["SMP"], religion="Katolik",
              address="Jl. Pos No.2, Pasar Baru, Jakarta Pusat", website="https://spmb.santaursulajakarta.sch.id")
add_admission("santa-ursula-jakarta", {"level": "SMP", "academicYear": "2027/2028",
    "period": L("Pendaftaran online dibuka mulai 1 Agustus 2026.", "Online registration opened on 1 August 2026."),
    "notes": L("Biaya tidak dicantumkan; kontak tatausaha@smp.santaursulajakarta.sch.id.", "Fees are not published; contact tatausaha@smp.santaursulajakarta.sch.id."), "source": SU, "checked": CHK})

BL = {"title": "Informasi Pendaftaran Siswa Baru 2027–2028 — SD Budi Luhur Pondok Aren (situs resmi)", "url": "https://sdpa.sekolahbudiluhur.sch.id/pengumuman/informasi-pendaftaran-siswa-baru-2027-2028/"}
ensure_school("sekolah-budi-luhur-pondok-aren", name="Sekolah Budi Luhur Pondok Aren", city="Tangerang Selatan", district="Pondok Aren", levels=["SD"],
              address="Jl. Jombang Raya No.77, Pondok Kacang Timur, Pondok Aren, Tangerang Selatan", phone="Sekretariat 0856-9752-4293", website="https://sdpa.sekolahbudiluhur.sch.id")
add_admission("sekolah-budi-luhur-pondok-aren", {"level": "SD", "academicYear": "2027/2028",
    "period": L("Pendaftaran online dengan nomor antrean; promo early bird diskon 25% pada 14 September–3 Oktober 2026.", "Online registration with queue numbers; 25% early-bird discount from 14 September to 3 October 2026."),
    "steps": [L("Daftar online dan dapatkan nomor antrean.", "Register online and get a queue number."), L("Hadir ke sekolah untuk pembayaran administrasi sesuai jadwal.", "Come to the school to pay the administration fee on the scheduled day."),
              L("Calon siswa dari TK non-Budi Luhur mengikuti observasi bersama guru SD.", "Children from other kindergartens attend an observation with SD teachers."), L("Bila diterima, lunasi biaya administrasi pendidikan lewat transfer.", "If accepted, pay the education fees in full by transfer.")],
    "test": L("Observasi (untuk siswa dari luar TK Budi Luhur).", "Observation (for children from outside TK Budi Luhur)."),
    "notes": L("Besaran biaya tidak dicantumkan; hubungi sekretariat.", "Fee amounts are not published; contact the secretariat."), "source": BL, "checked": CHK})
print("ok")
