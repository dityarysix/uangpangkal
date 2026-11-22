"""Official school SPMB/PPDB pages (figures verbatim):
- SMP Santa Maria Surabaya 2027/2028: https://ppdb.sanmarosu-jatim.sch.id/profile/SMP-SURABAYA
- SMP Muhammadiyah 6 Surabaya 2026/2027: https://smpmusix.com/index.php/rincian-pembiayaan-ppdb/
- SMP Muhammadiyah 3 Yogyakarta 2027/2028: https://smpmugayogya.sch.id/info-ppdb/
- BP IBS Bogor 2027/2028: https://www.bpibs.sch.id/pendaftaran/biaya-sekolah-bp-ibs
- Al-Falaah Ciputat 2027/2028: https://sekolahal-falaah.sch.id/ppdb-sd-islam-al-falaah/ and /ppdb-smp-islam-al-falaah/"""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS

CHK = "2026-11-22"

# ---- SMP Santa Maria Surabaya ----
SM = {"title": "SPMB SMP Santa Maria Surabaya TA 2027/2028 (situs resmi)", "url": "https://ppdb.sanmarosu-jatim.sch.id/profile/SMP-SURABAYA"}
upsert("sekolah-santa-maria-surabaya", name="Sekolah Santa Maria Surabaya", city="Surabaya", religion="Katolik",
       address="Jl. Raya Darmo No.49, Surabaya", website="https://ppdb.sanmarosu-jatim.sch.id",
       level="SMP", year="2027/2028", source=SM, checked=CHK,
       registrationFee=325_000, entryFee={"min": 14_200_000, "max": 16_200_000}, tuition={"amount": 1_400_000, "period": "month"},
       otherFees=[fee("Uang kegiatan", "Activity fee", 2_890_000)],
       notes=L("Uang pangkal = uang pengembangan dan sarana pendidikan. Jalur khusus (dari SD Santa Maria Surabaya/Sidoarjo): Rp14.200.000, SPP Rp1.400.000. Jalur prestasi: Rp15.200.000, SPP Rp1.500.000. Jalur umum I: Rp16.200.000, SPP Rp1.600.000. Potongan Rp500.000 per keluarga untuk saudara kandung; potongan 5% jika uang pengembangan dibayar lunas; cicilan 50% lalu 5 kali angsuran; potongan 5% jika SPP 1 tahun dilunasi Juli–Agustus 2027.",
               "Entry fee = development & facilities fee. Special track (from SD Santa Maria Surabaya/Sidoarjo): Rp14,200,000, tuition Rp1,400,000. Achievement track: Rp15,200,000, tuition Rp1,500,000. General track I: Rp16,200,000, tuition Rp1,600,000. Rp500,000 sibling discount per family; 5% off if the development fee is paid in full; or 50% upfront then 5 monthly instalments; 5% off if a full year's tuition is paid in July–August 2027."))
add_admission("sekolah-santa-maria-surabaya", {"level": "SMP", "academicYear": "2027/2028",
    "period": L("Tahap 1 (jalur prestasi): pendaftaran 1–10 September 2026; tes literasi dan numerasi 12 September 2026.", "Stage 1 (achievement track): registration 1–10 September 2026; literacy and numeracy test 12 September 2026."),
    "steps": [L("Daftar di ppdb.sanmarosu-jatim.sch.id.", "Register at ppdb.sanmarosu-jatim.sch.id."),
              L("Beli formulir SPMB Rp325.000 via VA BCA.", "Buy the SPMB form (Rp325,000) via BCA virtual account."),
              L("Isi data dan unggah berkas (scan/foto dokumen asli, maks. 1 MB).", "Enter details and upload documents (scans/photos of originals, max 1 MB)."),
              L("Ikuti tes literasi dan numerasi (Bahasa Indonesia dan Matematika kelas 5 SD).", "Take the literacy and numeracy test (grade 5 Indonesian and maths)."),
              L("Diterima jika lolos filter akademis dan filter keuangan (uang pengembangan dan uang kegiatan lunas).", "Accepted once both the academic filter and the financial filter (development and activity fees paid) are passed.")],
    "documents": [L("Surat pernyataan bermaterai Rp10.000", "Signed statement with Rp10,000 duty stamp"), L("Rapor kelas IV dan V semester 1 dan 2", "Grade 4 and 5 report cards, both semesters"),
                  L("Kartu Keluarga", "Family card (Kartu Keluarga)"), L("Akta kelahiran", "Birth certificate"),
                  L("Surat baptis Katolik (bagi yang sudah dibaptis)", "Catholic baptism certificate (if baptised)"), L("Foto berwarna terbaru", "Recent colour photo"),
                  L("Piagam penghargaan (jalur prestasi non-akademis)", "Award certificates (non-academic achievement track)")],
    "test": L("Tes literasi dan numerasi.", "Literacy and numeracy test."), "source": SM, "checked": CHK})

# ---- SMP Muhammadiyah 6 Surabaya ----
MU6 = {"title": "Rincian Pembiayaan SPMB 2026–2027 — SMP Muhammadiyah 6 Surabaya (situs resmi)", "url": "https://smpmusix.com/index.php/rincian-pembiayaan-ppdb/"}
upsert("smp-muhammadiyah-6-surabaya", name="SMP Muhammadiyah 6 Surabaya", city="Surabaya", district="Karang Pilang", religion="Islam",
       address="Jl. Kemlaten Baru No.43, Kebraon, Karang Pilang, Surabaya", website="https://smpmusix.com",
       level="SMP", year="2026/2027", source=MU6, checked=CHK,
       registrationFee=250_000, entryFee={"min": 1_000_000, "max": 4_000_000}, tuition={"amount": 475_000, "period": "month"},
       otherFees=[fee("Tabungan (per bulan)", "Savings (per month)", 25_000), fee("Dana kegiatan siswa (per tahun)", "Student activity fund (per year)", 4_000_000),
                  fee("Buku paket & LKS (1 tahun)", "Textbooks & workbooks (1 year)", 1_150_000)],
       notes=L("Uang pangkal = uang pembangunan: gelombang inden Rp1.000.000, gelombang 1 Rp3.000.000, gelombang 2 Rp4.000.000. Belum termasuk seragam.",
               "Entry fee = building fee: early (inden) wave Rp1,000,000, wave 1 Rp3,000,000, wave 2 Rp4,000,000. Uniforms not included."))

# ---- SMP Muhammadiyah 3 Yogyakarta ----
MU3 = {"title": "Info PPDB — SMP Muhammadiyah 3 Yogyakarta (situs resmi)", "url": "https://smpmugayogya.sch.id/info-ppdb/"}
upsert("smp-muhammadiyah-3-yogyakarta", name="SMP Muhammadiyah 3 Yogyakarta", city="Kota Yogyakarta", district="Wirobrajan", religion="Islam",
       address="Jl. Kapten Pierre Tendean 19, Wirobrajan, Yogyakarta", phone="(0274) 375158", website="https://smpmugayogya.sch.id",
       level="SMP", year="2027/2028", yearAssumed=True, source=MU3, checked=CHK,
       registrationFee=50_000, tuition={"amount": 450_000, "period": "month"},
       otherFees=[fee("Dana operasional pendidikan (kegiatan 1 tahun)", "Education operating fund (1 year of activities)", 4_000_000),
                  fee("Seragam laki-laki (opsional)", "Uniforms, boys (optional)", 1_500_000), fee("Seragam perempuan (opsional)", "Uniforms, girls (optional)", 1_750_000),
                  fee("Buku pelajaran (opsional)", "Textbooks (optional)", 1_250_000)],
       notes=L("Fullday: dana pengembangan dan infaq amal jariyah ditentukan saat wawancara sesuai kemampuan. SPP kelas reguler Rp450.000, kelas peminatan (IT, bilingual, KKO, riset, tahfidz) Rp600.000. Boarding: total masuk Rp18.650.000 (putra) / Rp18.900.000 (putri), termasuk infaq min. Rp4.000.000 dan dana pengembangan min. Rp5.000.000; biaya bulanan Rp1.650.000–Rp1.800.000 (makan, asrama, kegiatan asrama, SPP). Halaman berjudul 2027/2028 tetapi teksnya juga menyebut 2025/2026; jadwal gelombang menunjukkan penerimaan 2027/2028.",
               "Day school: development fund and infaq are set at the interview according to ability. Tuition: regular class Rp450,000, specialist classes (IT, bilingual, sports, research, tahfidz) Rp600,000. Boarding: total on entry Rp18,650,000 (boys) / Rp18,900,000 (girls), including infaq of at least Rp4,000,000 and development fund of at least Rp5,000,000; monthly Rp1,650,000–Rp1,800,000 (meals, boarding, boarding activities, tuition). The page is titled 2027/2028 but its text also mentions 2025/2026; the wave dates point to the 2027/2028 intake."))
add_admission("smp-muhammadiyah-3-yogyakarta", {"level": "SMP", "academicYear": "2027/2028",
    "period": L("Gelombang inden Juli–3 Oktober 2026; gelombang 1: 5 Oktober 2026–6 Februari 2027; gelombang 2: 8 Februari–24 April 2027; gelombang 3: 26 April–Juli 2027.",
                "Early (inden) wave July–3 October 2026; wave 1: 5 October 2026–6 February 2027; wave 2: 8 February–24 April 2027; wave 3: 26 April–July 2027."),
    "steps": [L("Buat akun dan bayar formulir.", "Create an account and pay the form fee."), L("Isi biodata di aplikasi.", "Fill in the profile in the app."),
              L("Wawancara dan tes.", "Interview and test."), L("Pengumuman.", "Announcement."), L("Registrasi/daftar ulang maks. 5 hari setelah pengumuman.", "Re-register within 5 days of the announcement.")],
    "documents": [L("Fotokopi rapor kelas 5 semester 2", "Copy of grade 5 semester 2 report"), L("Fotokopi ijazah (2 lembar, menyusul)", "Copy of primary certificate (2, can follow later)"),
                  L("Nilai ASPD asli (khusus peserta DIY, menyusul)", "Original ASPD score (DIY applicants, can follow later)"), L("Fotokopi akta kelahiran", "Copy of birth certificate"),
                  L("Fotokopi Kartu Keluarga (3 lembar)", "Copies of family card (3)"), L("Pas foto 3x4 (3 lembar)", "3x4 photos (3)"),
                  L("Fotokopi KMS/PIP/PKH jika punya", "Copy of KMS/PIP/PKH card if any")],
    "notes": L("Mengundurkan diri setelah membayar: Rp5.000.000 tidak dikembalikan.", "Withdrawing after payment: Rp5,000,000 is retained."), "source": MU3, "checked": CHK})

# ---- BP IBS Bogor ----
BP = {"title": "Rincian Pembiayaan SMP dan SMA BP IBS 2027/2028 (situs resmi)", "url": "https://www.bpibs.sch.id/pendaftaran/biaya-sekolah-bp-ibs"}
BPS = dict(name="BP IBS Bogor", city="Kota Bogor", district="Tanah Sareal", religion="Islam",
           address="Jl. Cimanggu Permai No.16, Kedung Jaya, Tanah Sareal, Kota Bogor", website="https://www.bpibs.sch.id",
           year="2027/2028", source=BP, checked=CHK)
upsert("bp-ibs-bogor", level="SMP", registrationFee=750_000, entryFee={"min": 55_000_000}, tuition={"amount": 4_900_000, "period": "month"},
       otherFees=[fee("Daftar ulang (tahun kedua dst.)", "Re-registration (second year onward)", 8_500_000)],
       notes=L("Sekolah berasrama. Uang pangkal dibayar setelah lulus tes; mencakup fasilitas asrama, ekskul, kokurikuler, field trip, outing class, seragam, dan buku paket. SPP mencakup operasional, makan 3x sehari, dan laundry. Biaya pendaftaran mencakup tes dan konsumsi untuk 3 orang.",
               "Boarding school. Entry fee is paid after passing the test; covers boarding, extracurriculars, co-curriculars, field trips, outings, uniforms and textbooks. Tuition covers operations, 3 meals a day and laundry. Registration covers the tests and meals for 3 people."), **BPS)
upsert("bp-ibs-bogor", level="SMA", registrationFee=750_000, entryFee={"min": 27_500_000, "max": 55_000_000}, tuition={"amount": 5_500_000, "period": "month"},
       otherFees=[fee("Daftar ulang kelas 10 ke 11", "Re-registration grade 10 to 11", 10_000_000), fee("Daftar ulang kelas 11 ke 12", "Re-registration grade 11 to 12", 12_500_000)],
       notes=L("Uang pangkal Rp27.500.000 dari SMP BP IBS; Rp55.000.000 dari luar. SMA Diniyyah daftar ulang Rp7.500.000. SPP mencakup makan 3x sehari dan laundry.",
               "Entry fee Rp27,500,000 from BP IBS junior high; Rp55,000,000 from outside. SMA Diniyyah re-registration Rp7,500,000. Tuition includes 3 meals a day and laundry."), **BPS)
for lvl, t_id, t_en in [("SMP", "Psikotes; tes mata pelajaran umum (Bahasa Indonesia, Bahasa Inggris, Matematika, IPA, Diniyyah); tes baca Al-Qur'an; wawancara calon santri dan orang tua; tes kesehatan.",
                         "Psychological test; general subjects test (Indonesian, English, maths, science, Islamic studies); Quran reading test; student and parent interviews; health check."),
                        ("SMA", "Psikotes; wawancara santri (Bahasa Arab, baca kitab, hafalan, kepribadian); wawancara orang tua (manhaj); tes literasi Bahasa Indonesia, Bahasa Inggris, dan numerasi.",
                         "Psychological test; student interview (Arabic, text reading, memorisation, personality); parent interview; Indonesian and English literacy and numeracy tests.")]:
    add_admission("bp-ibs-bogor", {"level": lvl, "academicYear": "2027/2028", "test": L(t_id, t_en), "source": BP, "checked": CHK})

# ---- Al-Falaah Ciputat (Tangsel) ----
AFS = dict(name="Sekolah Islam Al-Falaah Ciputat", city="Tangerang Selatan", district="Ciputat", religion="Islam",
           address="Villa Mutiara, Sawah Baru, Ciputat, Tangerang Selatan", website="https://sekolahal-falaah.sch.id", year="2027/2028", checked=CHK)
SD_SRC = {"title": "Prosedur SPMB SD Islam Al-Falaah TA 2027/2028 (situs resmi)", "url": "https://sekolahal-falaah.sch.id/ppdb-sd-islam-al-falaah/"}
SMP_SRC = {"title": "Prosedur SPMB SMP Islam Al-Falaah TA 2027/2028 (situs resmi)", "url": "https://sekolahal-falaah.sch.id/ppdb-smp-islam-al-falaah/"}
PAY = ("Pembayaran lunas atau 2 tahap (60% lalu 40% pada 25 Januari–3 Februari 2027). Mengundurkan diri: dipotong 80% dari total pembayaran. SPP naik Rp50.000 per tahun. Sudah termasuk seragam 6 stel, kegiatan 1 tahun, SPP Juli 2027, buku paket 1 tahun, dan BKOMG.",
       "Pay in full or in 2 stages (60%, then 40% on 25 January–3 February 2027). Withdrawal: 80% of the total is retained. Tuition rises Rp50,000 a year. Includes 6 uniform sets, 1 year of activities, July 2027 tuition, 1 year of textbooks and parents' association fee.")
upsert("sekolah-islam-al-falaah-ciputat", level="SD", source=SD_SRC, registrationFee=450_000, entryFee={"min": 12_907_500, "max": 17_210_000},
       tuition={"amount": 1_065_000, "period": "month"}, otherFees=[fee("Seragam, kegiatan & buku paket 1 tahun, BKOMG", "Uniforms, activities & textbooks for 1 year, parents' association", 6_025_000)],
       notes=L("Uang pangkal normal Rp17.210.000; diskon 25% (dari TK Al-Falaah) Rp12.907.500; 15% (kakak/adik di AF) Rp14.628.500; 10% (kakak/adik alumni AF) Rp15.489.000. Total normal Rp24.300.000. " + PAY[0],
               "Entry fee Rp17,210,000 normally; 25% off (from TK Al-Falaah) Rp12,907,500; 15% off (sibling at AF) Rp14,628,500; 10% off (sibling alumni) Rp15,489,000. Normal total Rp24,300,000. " + PAY[1]), **AFS)
upsert("sekolah-islam-al-falaah-ciputat", level="SMP", source=SMP_SRC, registrationFee=350_000, entryFee={"min": 8_294_000, "max": 12_760_000},
       tuition={"amount": 1_025_000, "period": "month"}, otherFees=[fee("Seragam, kegiatan & buku paket 1 tahun, BKOMG", "Uniforms, activities & textbooks for 1 year, parents' association", 6_645_000)],
       notes=L("Uang pangkal normal Rp12.760.000; diskon 35% (dari SD Al-Falaah) Rp8.294.000; 15% (kakak/adik di AF) Rp10.846.000; 10% (kakak/adik alumni AF) Rp11.484.000. Total normal Rp20.430.000. " + PAY[0],
               "Entry fee Rp12,760,000 normally; 35% off (from SD Al-Falaah) Rp8,294,000; 15% off (sibling at AF) Rp10,846,000; 10% off (sibling alumni) Rp11,484,000. Normal total Rp20,430,000. " + PAY[1]), **AFS)
add_admission("sekolah-islam-al-falaah-ciputat", {"level": "SD", "academicYear": "2027/2028",
    "period": L("Psikotes eksternal 17 Oktober 2026; observasi akademik dan wawancara orang tua 31 Oktober 2026; pengumuman 11 November 2026; pembayaran tahap I 11–20 November 2026.",
                "External psychological test 17 October 2026; academic observation and parent interview 31 October 2026; results 11 November 2026; first payment 11–20 November 2026."),
    "steps": [L("Daftar online di sekolahal-falaah.sch.id dan isi formulir.", "Register online at sekolahal-falaah.sch.id and fill in the form."), L("Bayar formulir Rp450.000.", "Pay the Rp450,000 form fee."),
              L("Panitia menghubungi untuk kelengkapan administrasi.", "The committee contacts you about paperwork."), L("Ikuti psikotes, observasi akademik, dan wawancara orang tua.", "Attend the psychological test, academic observation and parent interview.")],
    "test": L("Psikotes, observasi akademik siswa, wawancara orang tua.", "Psychological test, academic observation, parent interview."),
    "notes": L("Usia 6 tahun pada Juli 2027.", "Age 6 by July 2027."), "source": SD_SRC, "checked": CHK})
add_admission("sekolah-islam-al-falaah-ciputat", {"level": "SMP", "academicYear": "2027/2028",
    "period": L("Seleksi 24 Oktober 2026; pengumuman 4 November 2026; pembayaran tahap I 4–13 November 2026.", "Selection 24 October 2026; results 4 November 2026; first payment 4–13 November 2026."),
    "steps": [L("Daftar online dan isi formulir.", "Register online and fill in the form."), L("Bayar formulir Rp350.000.", "Pay the Rp350,000 form fee."),
              L("Ikuti observasi akademik dan wawancara orang tua.", "Attend the academic observation and parent interview.")],
    "test": L("Observasi akademik siswa dan wawancara orang tua.", "Academic observation and parent interview."), "source": SMP_SRC, "checked": CHK})
print("ok")
