"""Malang Raya batch 2 + Kudus (figures verbatim; years as stated or assumed and labelled).
- IDN Times, "Kisaran Biaya Masuk SD Swasta di Malang Tahun Ajaran 2024/25" (31 Oct 2024).
- Malang Raya Media, "Biaya Masuk SD di Kota Malang" (18 Jan 2024) -> 2024/2025, yearAssumed.
- Data Pendidikan, "7 Harga Sekolah SD Swasta Terbaik di Malang" (dated Oct 2026, undated figures) -> 2026/2027 yearAssumed + caution.
- Hai Malang, SMA Islam Sabilillah admission procedure (12 Jul 2024).
- SMK RUS Kudus, official "Biaya Pendidikan 2026-2027" (PDF, 29 Sep 2025)."""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS

CHK = "2026-11-22"
KM = "Kota Malang"
IDN = {"title": "Kisaran Biaya Masuk SD Swasta di Malang Tahun Ajaran 2024/25 (IDN Times)", "url": "https://www.idntimes.com/life/family/reyvan-maulid/biaya-masuk-sd-swasta-di-malang-c1c2", "published": "2024-10-31"}
MRM = {"title": "Biaya Masuk SD di Kota Malang (Malang Raya Media)", "url": "https://malangraya.media/lifestyle/pendidikan/2024/01/biaya-masuk-sd-di-kota-malang/", "published": "2024-01-18"}
DP = {"title": "7 Harga Sekolah SD Swasta Terbaik di Malang (Data Pendidikan)", "url": "https://www.datapendidikan.com/blog/harga-sekolah-sd-terbaik-di-malang/", "published": "2026-10-01"}
I = dict(city=KM, level="SD", year="2024/2025", source=IDN, checked=CHK)
M = dict(city=KM, level="SD", year="2024/2025", yearAssumed=True, source=MRM, checked=CHK)
D = dict(city=KM, level="SD", year="2026/2027", yearAssumed=True, source=DP, checked=CHK)
CAU = L("Sumber tidak menyebut tahun; artikel bertanggal Oktober 2026 tetapi angkanya bisa lebih lama.", "The source gives no year; the article is dated October 2026 but the figures may be older.")

upsert("sd-islam-al-azhar-56-malang", name="SD Islam Al Azhar 56 Malang", registrationFee=500_000, entryFee={"min": 17_500_000}, tuition={"amount": 1_550_000, "period": "month"},
       otherFees=[fee("Uang jamiyyah", "Parents' association", 300_000), fee("Uang kegiatan", "Activity fee", 2_300_000)], **I)
upsert("sd-islam-al-azhar-56-malang", name="SD Islam Al Azhar 56 Malang", entryFee={"min": 14_000_000}, tuition={"amount": 1_350_000, "period": "month"},
       otherFees=[fee("Uang buku tahunan", "Annual books", 2_000_000), fee("Seragam laki-laki", "Uniforms (boys)", 1_397_000), fee("Seragam perempuan", "Uniforms (girls)", 1_529_000),
                  fee("Dana syiar", "Syiar fund", 500_000), fee("Dana jamiyah", "Parents' association", 300_000)], notes=L("Uang pangkal = infaq.", "Entry fee = infaq."), **M)
upsert("my-little-island-school-malang", name="My Little Island School Malang", curriculum=["Cambridge", "IB"],
       registrationFee=200_000, entryFee={"min": 24_000_000}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_700_000), fee("Biaya kegiatan", "Activity fee", 2_500_000)], notes=L("Uang pangkal = DPP.", "Entry fee = DPP."), **I)
upsert("sd-lab-um-malang", name="SD Laboratorium UM Malang", entryFee={"min": 4_000_000}, tuition={"amount": 500_000, "period": "month"},
       otherFees=[fee("Dana kegiatan dan alat pendidikan", "Activities & learning materials", 5_000_000), fee("Seragam dan buku tulis", "Uniforms & exercise books", 950_000)],
       notes=L("Uang pangkal = dana pembangunan.", "Entry fee = building fund."), **I)
upsert("sekolah-islam-sabilillah-malang", name="Sekolah Islam Sabilillah Malang", religion="Islam", district="Lowokwaru",
       entryFee={"min": 19_500_000}, tuition={"amount": 1_445_000, "period": "month"},
       otherFees=[fee("Seragam laki-laki", "Uniforms (boys)", 1_365_000), fee("Seragam perempuan", "Uniforms (girls)", 1_395_000)],
       notes=L("SD (Jl. Terusan Piranha Atas No.114). Uang pangkal = infaq.", "SD (Jl. Terusan Piranha Atas No.114). Entry fee = infaq."), **I)
upsert("sekolah-islam-sabilillah-malang", name="Sekolah Islam Sabilillah Malang", entryFee={"min": 13_000_000}, tuition={"amount": 900_000, "period": "month"},
       notes=L("SD. " + CAU["id"] + " Uang pangkal = uang pembelajaran/gedung.", "SD. " + CAU["en"] + " Entry fee = learning/building fee."), **D)
upsert("sd-insan-amanah-malang", name="SD Insan Amanah Malang", religion="Islam", address="Blok M Griyashanta, Jl. Soekarno–Hatta, Kota Malang", phone="(0341) 410206",
       entryFee={"min": 12_000_000}, tuition={"amount": 600_000, "period": "month"}, otherFees=[fee(*UNIFORM, 1_095_000)], notes=L("Uang pangkal = DPP.", "Entry fee = DPP."), **M)
upsert("sd-anak-saleh-malang", name="SD Anak Saleh Malang", district="Lowokwaru", religion="Islam", address="Jl. Arumba No.31, Tunggulwulung, Lowokwaru, Kota Malang",
       entryFee={"min": 14_900_000}, tuition={"amount": 1_300_000, "period": "month"},
       otherFees=[fee("Seragam laki-laki", "Uniforms (boys)", 2_000_000), fee("Seragam perempuan", "Uniforms (girls)", 2_200_000)], notes=L("Uang pangkal = infaq.", "Entry fee = infaq."), **M)
upsert("pj-global-school-malang", name="PJ Global School Malang", entryFee={"min": 12_000_000}, tuition={"amount": 825_000, "period": "month"},
       otherFees=[fee("Her-registrasi per tahun", "Annual re-registration", 3_000_000), fee(*UNIFORM, 1_200_000)], notes=L("Uang pangkal = DPP.", "Entry fee = DPP."), **M)
upsert("brawijaya-smart-school-malang", name="Brawijaya Smart School Malang", entryFee={"min": 4_000_000, "max": 6_000_000}, tuition={"amount": 400_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_600_000), fee("Buku kelas 1", "Grade 1 books", 750_000), fee("Dana kegiatan per tahun", "Activities per year", 700_000)],
       notes=L("SD. DPP Rp4–6 juta; SPP Rp400–600 ribu.", "SD. Development fee Rp4–6M; tuition Rp400–600k."), **M)
upsert("sdit-insan-permata-malang", name="SDIT Insan Permata Malang", district="Lowokwaru", religion="Islam", address="Jl. Akordion Utara No.3, Tunggulwulung, Lowokwaru, Kota Malang",
       entryFee={"min": 7_750_000, "max": 12_750_000}, tuition={"amount": 450_000, "period": "month"},
       otherFees=[fee("Makan (per bulan)", "Meals (per month)", 185_000), fee("Kegiatan", "Activities", 1_000_000), fee(*UNIFORM, 1_300_000), fee("Peralatan siswa dan buku", "Supplies and books", 950_000)],
       notes=L(CAU["id"] + " DPP dan SPP proporsional (lima kategori): DPP Rp7,75–12,75 juta; SPP Rp450–850 ribu.", CAU["en"] + " Development fee and tuition are proportional (five categories): Rp7.75–12.75M; tuition Rp450–850k."), **D)

HM = {"title": "Biaya Masuk SMA Islam Sabilillah Malang & Cara Pendaftaran (Hai Malang)", "url": "https://haimalang.com/2024/07/12/wajib-disimak-biaya-masuk-sma-islam-sabilillah-malang-lengkap-beserta-cara-pendaftaran/"}
add_admission("sekolah-islam-sabilillah-malang", {"level": "SMA", "academicYear": "2025/2026",
    "steps": [L("Buka sekolahsabilillah.sch.id, buat akun (pilih satuan pendidikan dan jalur), unggah Kartu Keluarga.", "Go to sekolahsabilillah.sch.id, create an account (choose unit and track), upload the family card."),
              L("Transfer biaya pendaftaran Rp450.000 ke virtual account BNI.", "Pay the Rp450,000 registration fee to the BNI virtual account."),
              L("Login dengan NIK calon siswa, isi biodata dan unggah berkas.", "Log in with the child's NIK, fill in the profile and upload documents."),
              L("Ikuti wawancara kesiapan belajar/seleksi sesuai jadwal dengan membawa bukti pendaftaran.", "Attend the readiness interview/selection with the registration receipt.")],
    "documents": [L("Kartu Keluarga", "Family card"), L("Akta kelahiran", "Birth certificate"), L("Surat keterangan aktif belajar", "Proof of current enrolment"),
                  L("Pas foto 3x4 berwarna", "3x4 colour photo"), L("Piagam penghargaan (jika ada)", "Award certificates (if any)"), L("Surat keterangan sehat dari dokter", "Doctor's health certificate")],
    "test": L("Wawancara kesiapan belajar/seleksi.", "Readiness interview/selection."),
    "notes": L("Jalur: prestasi undangan, inden internal/eksternal, reguler internal/eksternal. Berdasarkan artikel Juli 2024; tahun ajaran diasumsikan.", "Tracks: invited achievers, early internal/external, regular internal/external. Based on a July 2024 article; academic year assumed."),
    "source": HM, "checked": CHK})

RUS = {"title": "Rincian Biaya Registrasi PMB TP 2026/2027 — SMK RUS Kudus (dokumen resmi)", "url": "https://smkrus.sch.id/wp-content/uploads/2025/10/BIaya-Pendidikan-2026-2027.pdf", "published": "2025-09-29"}
upsert("smk-rus-kudus", name="SMK RUS Kudus", city="Kabupaten Kudus", website="https://smkrus.sch.id", level="SMK", year="2026/2027", source=RUS, checked=CHK,
       entryFee={"min": 3_000_000, "max": 12_000_000}, tuition={"amount": 500_000, "period": "month"},
       otherFees=[fee("Keperluan peserta didik putra", "Student package (boys)", 1_925_000), fee("Keperluan peserta didik putri", "Student package (girls)", 2_065_000)],
       notes=L("Uang gedung/SPI dan SPP Juli 2026 per program: DKV desain grafika Rp3.000.000 & Rp550.000 (dari Kudus) / Rp6.000.000 & Rp750.000 (luar Kudus); DKV teknik grafika Rp3.000.000 & Rp500.000; Animasi Rp4.000.000 & Rp650.000 (Kudus); PPLG/RPL Rp12.000.000 & Rp1.350.000 (luar Kudus). Uang gedung boleh lebih dari angka tertera. SPP sudah termasuk ujian, kunjungan industri, karya wisata; tidak ada iuran bulanan lain.",
               "Building fee and July 2026 tuition by programme: graphic design Rp3,000,000 & Rp550,000 (from Kudus) / Rp6,000,000 & Rp750,000 (outside Kudus); print technology Rp3,000,000 & Rp500,000; animation Rp4,000,000 & Rp650,000 (Kudus); software/game development Rp12,000,000 & Rp1,350,000 (outside Kudus). The building fee may be paid above the listed amount. Tuition includes exams, industry visits and trips; no other monthly charges."))
print("ok")
