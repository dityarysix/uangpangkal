"""Malang Raya — first batch.
- SDIT Insantama Malang, official PPDB 2027/2028: https://insantamamalang.sch.id/ppdb-sdit/
- SMK Telkom Malang, official SPMB 2027/2028: https://smktelkom-mlg.sch.id/spmb
- GetRadius (21 & 23 May 2026), 2026/2027 estimates/ranges for Malang schools.
- SMAN 3 Malang blog, "5 Sekolah Swasta Terbaik di Malang (SD-SMA)" (6 Jun 2024) -> 2024/2025, yearAssumed.
Skipped: Islamic Brilliant School (Kota Batu, outside the area list)."""
from seedlib import L, fee, upsert, add_admission

CHK = "2026-11-22"
KM = "Kota Malang"

INS = {"title": "PPDB SDIT Insantama Malang TA 2027/2028 (situs resmi)", "url": "https://insantamamalang.sch.id/ppdb-sdit/"}
upsert("sdit-insantama-malang", name="SDIT Insantama Malang", city=KM, religion="Islam", website="https://insantamamalang.sch.id",
       level="SD", year="2027/2028", source=INS, checked=CHK,
       registrationFee=450_000, entryFee={"min": 7_500_000}, tuition={"amount": 700_000, "period": "month"},
       otherFees=[fee("Kain seragam", "Uniform fabric", 1_350_000), fee(*("Buku", "Books"), 500_000), fee("Parenting", "Parenting programme", 1_000_000), fee("Kegiatan tahunan", "Annual activities", 2_500_000)],
       notes=L("Uang pangkal = infaq pengembangan. Full day school.", "Entry fee = development infaq. Full-day school."))
add_admission("sdit-insantama-malang", {"level": "SD", "academicYear": "2027/2028",
    "period": L("Pendaftaran 1 November–31 Desember 2026; observasi & wawancara 2 Januari 2027; pengumuman 11 Januari 2027; daftar ulang 12–14 Januari 2027.",
                "Registration 1 November–31 December 2026; observation & interview 2 January 2027; results 11 January 2027; re-registration 12–14 January 2027."),
    "steps": [L("Daftar online di ppdb.insantama.sch.id dan bayar biaya pendaftaran.", "Register online at ppdb.insantama.sch.id and pay the registration fee."),
              L("Unggah berkas administrasi.", "Upload the documents."), L("Ikuti observasi dan wawancara.", "Attend the observation and interview."), L("Daftar ulang bila lulus seleksi.", "Re-register if accepted.")],
    "documents": [L("Scan akta lahir", "Scan of birth certificate"), L("Scan KTP ayah & ibu", "Scans of both parents' ID cards"), L("Scan Kartu Keluarga", "Scan of family card"), L("Pas foto berwarna", "Colour photo")],
    "test": L("Observasi potensi dan karakter calon siswa; wawancara.", "Observation of the child's potential and character; interview."),
    "notes": L("Usia minimal 6 tahun pada Juli tahun ajaran berjalan.", "Minimum age 6 in July of the school year."), "source": INS, "checked": CHK})

ST = {"title": "SPMB SMK Telkom Malang TA 2027/2028 (situs resmi)", "url": "https://smktelkom-mlg.sch.id/spmb"}
upsert("smk-telkom-malang", name="SMK Telkom Malang", city=KM, district="Kedungkandang", address="Jl. Danau Ranau, Sawojajar, Kedungkandang, Kota Malang",
       phone="(0341) 712500", website="https://smktelkom-mlg.sch.id", level="SMK", year="2027/2028", source=ST, checked=CHK,
       registrationFee=350_000, entryFee={"min": 23_525_000, "max": 28_525_000}, tuition={"amount": 650_000, "period": "month"},
       notes=L("DSP per jalur: prioritas rapor Rp23.525.000 (ditutup); jalur potensi akademik Rp24.000.000; jalur tes akademik Rp25.000.000; International Class Program Rp28.525.000. DP Rp12.000.000, sisanya 4 kali angsuran. DSP mencakup DPP, seragam 5 stel + jas almamater, asuransi, MPLS, bahan ajar, ujian, PKL, kunjungan industri, perpisahan, dan SPP Juli. SPP Rp650.000 (reguler) / Rp850.000 (ICP) mulai Agustus 2027.",
               "Development fee by track: report-card priority Rp23,525,000 (closed); academic potential Rp24,000,000; academic test Rp25,000,000; International Class Program Rp28,525,000. Rp12,000,000 down payment, rest in 4 instalments. Covers DPP, 5 uniform sets + blazer, insurance, orientation, materials, exams, internship, industry visits, graduation and July tuition. Tuition Rp650,000 (regular) / Rp850,000 (ICP) from August 2027."))
add_admission("smk-telkom-malang", {"level": "SMK", "academicYear": "2027/2028",
    "period": L("Pendaftaran 10 Agustus–30 Oktober 2026; tes 31 Oktober 2026. Pendaftaran dapat ditutup bila kuota terpenuhi.", "Registration 10 August–30 October 2026; test on 31 October 2026. May close early when full."),
    "test": L("Nilai rapor, psikotes, tes kesamaptaan/fisik, wawancara siswa dan orang tua (jalur tes: CBT & logika).", "Report grades, psychological test, fitness test, student and parent interview (test track: CBT & logic)."),
    "notes": L("Syarat: siswa kelas 9 SMP/MTs atau lulusan 1 tahun sebelumnya; tidak buta warna untuk RPL, TKJ, Animasi/Gim.", "Requirements: grade 9 students or graduates from the previous year; not colour-blind for software, networking and animation/game majors."),
    "source": ST, "checked": CHK})

R1 = {"title": "Biaya Sekolah di Malang 2026: Masuk SD Islam Al Azhar 56 Malang (GetRadius)", "url": "https://getradius.id/news/66045-biaya-sekolah-di-malang-2026-bikin-kaget-masuk-sd-islam-al-azhar-56-malang-bisa-habiskan-puluhan-juta-rupiah", "published": "2026-05-21"}
R2 = {"title": "Biaya Sekolah di Malang 2026: Perbandingan Total SD hingga SMA Favorit (GetRadius)", "url": "https://getradius.id/news/70257-biaya-sekolah-di-malang-2026-perbandingan-total-sd-hingga-sma-favorit-apa-yang-harus-dipersiapkan-orang-tua", "published": "2026-05-23"}
EST = L("Perkiraan/kisaran menurut sumber. Lokasi menurut sumber: Malang.", "Estimate/range according to the source. Location per source: Malang.")
def rng(i, e): return L(EST["id"] + " " + i, EST["en"] + " " + e)
upsert("sd-islam-al-azhar-56-malang", name="SD Islam Al Azhar 56 Malang", city=KM, religion="Islam", level="SD", year="2026/2027", source=R1, checked=CHK,
       entryFee={"min": 18_500_000}, tuition={"amount": 1_700_000, "period": "month"}, notes=EST)
upsert("sekolah-islam-terpadu-al-falah-malang", name="Sekolah Islam Terpadu Al-Falah Malang", city=KM, religion="Islam", level="SD", year="2026/2027", source=R2, checked=CHK,
       entryFee={"min": 10_000_000, "max": 12_000_000}, tuition={"amount": 1_000_000, "period": "month"}, notes=rng("SPP Rp1–1,5 juta.", "Tuition Rp1–1.5M."))
upsert("sekolah-islam-terpadu-al-falah-malang", name="Sekolah Islam Terpadu Al-Falah Malang", city=KM, level="SMP", year="2026/2027", source=R2, checked=CHK,
       entryFee={"min": 15_000_000, "max": 20_000_000}, tuition={"amount": 1_500_000, "period": "month"}, notes=rng("SPP Rp1,5–2 juta.", "Tuition Rp1.5–2M."))
upsert("sekolah-kristen-petra-malang", name="Sekolah Kristen Petra Malang", city=KM, religion="Kristen", level="SD", year="2026/2027", source=R2, checked=CHK,
       entryFee={"min": 12_000_000, "max": 15_000_000}, tuition={"amount": 1_200_000, "period": "month"}, notes=rng("Program bilingual. SPP Rp1,2–1,8 juta.", "Bilingual programme. Tuition Rp1.2–1.8M."))
upsert("sekolah-kristen-petra-malang", name="Sekolah Kristen Petra Malang", city=KM, level="SMA", year="2026/2027", source=R2, checked=CHK,
       entryFee={"min": 18_000_000, "max": 22_000_000}, tuition={"amount": 1_800_000, "period": "month"}, notes=rng("SPP Rp1,8–2,5 juta.", "Tuition Rp1.8–2.5M."))
upsert("sd-muhammadiyah-1-malang", name="SD Muhammadiyah 1 Malang", city=KM, religion="Islam", level="SD", year="2026/2027", source=R2, checked=CHK,
       entryFee={"min": 8_000_000, "max": 10_000_000}, tuition={"amount": 800_000, "period": "month"}, notes=rng("SPP Rp800 ribu–1,2 juta.", "Tuition Rp800k–1.2M."))
upsert("sekolah-islam-sabilillah-malang", name="Sekolah Islam Sabilillah Malang", city=KM, district="Lowokwaru", religion="Islam", address="Jl. Terusan Piranha Atas No.135, Tunjungsekar, Lowokwaru, Kota Malang",
       level="SMA", year="2026/2027", source=R2, checked=CHK, entryFee={"min": 20_000_000, "max": 25_000_000}, tuition={"amount": 2_000_000, "period": "month"},
       notes=rng("Boarding. SPP Rp2–3 juta, belum termasuk kegiatan internasional.", "Boarding. Tuition Rp2–3M, excluding international activities."))

S3 = {"title": "5 Sekolah Swasta Terbaik di Malang Jawa Timur (SD-SMA) (blog SMAN 3 Malang)", "url": "https://sman3malang.sch.id/sekolah-swasta-terbaik-malang-sd-sma/", "published": "2024-06-06"}
O = dict(year="2024/2025", yearAssumed=True, source=S3, checked=CHK)
upsert("sd-unggulan-al-yalu-malang", name="SD Unggulan Al-Ya'lu Malang", city=KM, district="Blimbing", religion="Islam", address="Jl. Teluk Mandar No.055, Arjosari, Blimbing, Kota Malang",
       level="SD", registrationFee=400_000, entryFee={"min": 18_500_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Uang buku tahunan", "Annual books", 2_000_000)], notes=L("Uang pangkal = DPP.", "Entry fee = DPP."), **O)
upsert("smp-laboratorium-um-malang", name="SMP Laboratorium UM Malang", city=KM, district="Lowokwaru", address="Jl. Simpang Bogor No.T-7, Sumbersari, Lowokwaru, Kota Malang",
       level="SMP", otherFees=[fee("Daftar ulang (reguler/inklusi)", "Re-registration (regular/inclusive)", 7_500_000)],
       notes=L("Biaya daftar ulang Rp7.500.000 (reguler/inklusi), Rp8.200.000 (ICP), Rp7.600.000 (tahfidz). Di bawah Yayasan Pendidikan Bhinneka Karya Unit Korpri IKIP Malang.", "Re-registration fee Rp7,500,000 (regular/inclusive), Rp8,200,000 (ICP), Rp7,600,000 (tahfidz). Run by the Bhinneka Karya foundation (IKIP Malang)."), **O)
upsert("brawijaya-smart-school-malang", name="Brawijaya Smart School Malang", city=KM, district="Lowokwaru", address="Jl. Cipayung No.8, Ketawanggede, Lowokwaru, Kota Malang",
       level="SMP", registrationFee=250_000, notes=L("Hanya biaya formulir yang dicantumkan sumber.", "The source lists only the form fee."), **O)
upsert("sma-katolik-cor-jesu-malang", name="SMA Katolik Cor Jesu Malang", city=KM, religion="Katolik", level="SMA", registrationFee=150_000,
       notes=L("Hanya biaya pendaftaran yang dicantumkan sumber. Tersedia asrama.", "The source lists only the registration fee. Boarding available."), **O)
upsert("sekolah-islam-sabilillah-malang", name="Sekolah Islam Sabilillah Malang", city=KM, level="SMA", registrationFee=500_000, entryFee={"min": 10_000_000}, tuition={"amount": 1_500_000, "period": "month"},
       notes=L("Angka 2024 ini jauh lebih rendah daripada perkiraan 2026 dari sumber lain.", "These 2024 figures are much lower than the 2026 estimate from another source."), **O)
print("ok")

# ---- Kota Batu ----
IBS = {"title": "Penerimaan Murid Baru TK Islamic Brilliant School 2027/2028 (situs resmi)", "url": "https://islamicbrilliant.sch.id/"}
upsert("islamic-brilliant-school-batu", name="Islamic Brilliant School (IBS) Batu", city="Kota Batu", religion="Islam", website="https://islamicbrilliant.sch.id",
       level="TK", year="2027/2028", source=IBS, checked=CHK, tuition={"amount": 300_000, "period": "month"},
       notes=L("Besaran uang pangkal tidak dicantumkan. Diskon uang pangkal 30% untuk pendaftaran s.d. Desember 2026 dan 20% s.d. Maret 2027; diskon khusus 10% (keluarga pengurus/staf) dan 7% (jamaah pengajian Nurul Qolby). Inden cukup uang pendaftaran + 20% uang pangkal; uang pangkal bisa diangsur. Katering dan antar-jemput opsional.",
               "The entry fee amount is not published. 30% off the entry fee for registration by December 2026, 20% by March 2027; special 10% (foundation/staff families) and 7% (Nurul Qolby congregation) discounts. Reserve a place with the registration fee + 20% of the entry fee; the entry fee can be paid in instalments. Catering and transport optional."))
print("ok batu")
