"""SMA round 2 (+ other levels from the same official sources).
- SAIM Surabaya, official external tuition brochure 2026/2027 (PDF): uang pangkal per level, 25% early discount.
- Technosa School (Tangsel), official "Info dan Biaya SD/SMP/SMA Umum" page.
- SMA Kristen Terang Bangsa Semarang, official SMA page (current promo, year not stated -> 2027/2028 assumed).
- Nakita, "Daftar Lengkap Biaya Sekolah SMA di Solo Tahun Ajaran 2023-2024".
- Orami, "7 Sekolah Internasional di Surabaya" (only the Sampoerna SMA entry-fee upper bound is used)."""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS

CHK = "2026-11-22"
SAIM = {"title": "SAIM Surabaya — External Tuition Fee Academic Year 2026-2027 (brosur resmi)", "url": "https://cdnc.heyzine.com/files/uploaded/29a5615317bab526d1b95eea41b5d548aa85573d.pdf"}
SS = dict(name="Sekolah Alam Insan Mulia (SAIM) Surabaya", city="Surabaya", year="2026/2027", source=SAIM, checked=CHK,
          address="SAIM East 1: Jl. Medokan Semampir Indah 99-101; SAIM East 2: Jl. Keputih Tegal No.54, Surabaya", phone="0811-3200-0111", website="https://www.saim.sch.id")
PAY = ("Harga normal Rp{n}; diskon 25% menjadi Rp{d} untuk pendaftaran awal. Bayar awal 30% maks. 10 hari setelah diterima, sisanya 5 termin; lunas paling lambat 30 Juni 2026. Termasuk seragam. Daftar ulang dan SPP diinformasikan kemudian.",
       "Normal price Rp{n}; 25% early-registration discount to Rp{d}. 30% within 10 days of acceptance, then 5 instalments; fully paid by 30 June 2026. Includes uniforms. Re-registration and tuition announced later.")
def saim(level, reg, normal, disc):
    nf, df = f"{normal:,}".replace(",", "."), f"{disc:,}".replace(",", ".")
    upsert("sekolah-alam-insan-mulia-surabaya", level=level, registrationFee=reg, entryFee={"min": disc, "max": normal},
           notes=L(PAY[0].format(n=nf, d=df), PAY[1].format(n=f"{normal:,}", d=f"{disc:,}")), **SS)
saim("KB", 350_000, 11_500_000, 8_625_000)
saim("TK", 350_000, 14_000_000, 10_500_000)
saim("SD", 500_000, 26_000_000, 19_500_000)
saim("SMP", 600_000, 21_500_000, 16_125_000)
saim("SMA", 600_000, 23_500_000, 17_625_000)
add_admission("sekolah-alam-insan-mulia-surabaya", {"academicYear": "2026/2027",
    "steps": [L("Isi formulir di admission.saim.schoolmate.id.", "Fill in the form at admission.saim.schoolmate.id."),
              L("Cek email untuk tautan login.", "Check your email for the login link."),
              L("Bayar biaya pendaftaran, isi data siswa dan orang tua, unggah dokumen, pilih jadwal observasi.", "Pay the registration fee, fill in student and parent details, upload documents, choose an observation slot."),
              L("Pengumuman penerimaan, lalu bayar uang pangkal; setelah lunas orang tua mendapat akun LMS SAIM.", "Results are announced, then pay the entry fee; once paid, parents receive an LMS account.")],
    "documents": [L("Kartu Keluarga", "Family card (Kartu Keluarga)"), L("Akta kelahiran", "Birth certificate"), L("Foto", "Photo"), L("Ijazah (SMP dan SMA)", "Previous certificate (SMP and SMA)")],
    "test": L("Observasi.", "Observation."),
    "notes": L("Usia minimal per Juli 2026: PG A 2 tahun, PG B 3 tahun, TK A 4 tahun, SD 6 tahun. Biaya pendaftaran SMP/SMA termasuk tes kesehatan.", "Minimum age by July 2026: PG A 2, PG B 3, TK A 4, SD 6. SMP/SMA registration includes a health check."),
    "source": SAIM, "checked": CHK})

TC = {"title": "Info dan Biaya SD/SMP/SMA Umum — Technosa School (situs resmi)", "url": "https://www.technosa.sch.id/daftar/info-dan-biaya-sd-smp-sma-umum/"}
TCS = dict(name="Technosa School", city="Tangerang Selatan", district="Serpong Utara", address="Jl. Raya Pd. Jagung No.67, Pondok Jagung Timur, Serpong Utara, Tangerang Selatan",
           website="https://www.technosa.sch.id", year="2026/2027", yearAssumed=True, source=TC, checked=CHK)
TN = L("Uang pangkal bisa dicicil sesuai periode yang disepakati. Biaya yang sudah dibayar tidak dapat dikembalikan. Uang buku menyesuaikan harga buku.", "The entry fee can be paid in agreed instalments. Payments are non-refundable. Book costs depend on book prices.")
upsert("technosa-school", level="SD", registrationFee=250_000, entryFee={"min": 10_000_000}, tuition={"amount": 750_000, "period": "month"},
       otherFees=[fee("Uang kegiatan per tahun", "Activities per year", 1_700_000), fee(*UNIFORM, 800_000)], notes=TN, **TCS)
upsert("technosa-school", level="SMP", registrationFee=250_000, entryFee={"min": 10_000_000}, tuition={"amount": 900_000, "period": "month"},
       otherFees=[fee("Uang kegiatan per tahun", "Activities per year", 2_000_000), fee("Seragam + jas laboratorium", "Uniforms + lab coat", 850_000)], notes=TN, **TCS)
upsert("technosa-school", level="SMA", registrationFee=250_000, entryFee={"min": 10_000_000}, tuition={"amount": 950_000, "period": "month"},
       otherFees=[fee("Uang kegiatan per tahun", "Activities per year", 2_000_000), fee("Seragam + jas laboratorium", "Uniforms + lab coat", 900_000)], notes=TN, **TCS)

TB = {"title": "SMA Kristen Terang Bangsa — Biaya & Alur Pendaftaran (situs resmi)", "url": "https://terbang.sch.id/akademik/SMA"}
upsert("terang-bangsa-christian-school-semarang", name="Terang Bangsa Christian School Semarang", city="Kota Semarang", district="Semarang Barat", religion="Kristen", curriculum=["Cambridge"],
       address="Jl. Arteri Utara, Komplek Grand Marina A3, Tawangsari, Semarang Barat, Kota Semarang", website="https://terbang.sch.id",
       level="SMA", year="2027/2028", yearAssumed=True, source=TB, checked=CHK,
       registrationFee=25_000, entryFee={"min": 6_000_000, "max": 10_000_000}, tuition={"amount": 900_000, "period": "month"},
       otherFees=[fee("Uang pengembangan pendidikan", "Education development fee", 1_750_000), fee(*UNIFORM, 1_100_000)],
       notes=L("Uang pangkal normal Rp10.000.000; promo gelombang 2 diskon 40% menjadi Rp6.000.000. Halaman tidak menyebut tahun ajaran.", "Normal entry fee Rp10,000,000; wave 2 promotion 40% off to Rp6,000,000. The page does not state the academic year."))
add_admission("terang-bangsa-christian-school-semarang", {"level": "SMA", "academicYear": "2027/2028",
    "steps": [L("Beli formulir di Admission gedung A lt. 1 (Rp25.000), atau isi formulir online lalu admin menghubungi sesuai antrean.", "Buy the form at Admissions, building A floor 1 (Rp25,000), or fill in the online form and wait for the admin to contact you."),
              L("Tanya jawab informasi sekolah di Admission.", "Q&A about the school at Admissions."),
              L("Serahkan formulir, bukti transfer, dan kelengkapan pendaftaran ke TU jenjang.", "Hand the form, transfer receipt and documents to the level's administration office."),
              L("Pengukuran seragam, lalu siswa siap mengikuti pembelajaran.", "Uniform fitting, then the student is ready to start.")],
    "source": TB, "checked": CHK})

NK = {"title": "Daftar Lengkap Biaya Sekolah SMA di Solo Tahun Ajaran 2023-2024 (Nakita)", "url": "https://nakita.grid.id/read/023714272/daftar-lengkap-biaya-sekolah-sma-di-solo-tahun-ajaran-2023-2024-beserta-fasilitas-yang-dimiliki?page=all"}
N = dict(level="SMA", year="2023/2024", source=NK, checked=CHK)
upsert("sma-abbs-surakarta", name="SMA ABBS Surakarta", city="Surakarta (Solo)", district="Banjarsari", religion="Islam",
       address="Jl. Tarumanegara III, Banyuanyar, Banjarsari, Surakarta",
       entryFee={"min": 9_150_000, "max": 13_650_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee("Fasilitas boarding", "Boarding facilities", 8_850_000)], notes=L("Biaya masuk jalur khusus Rp9.150.000; jalur reguler Rp13.650.000.", "Entry fee special track Rp9,150,000; regular track Rp13,650,000."), **N)
upsert("insan-cendekia-boarding-school-sukoharjo", name="Insan Cendekia Boarding School Sukoharjo", city="Sukoharjo", district="Baki",
       entryFee={"min": 13_600_000}, tuition={"amount": 2_600_000, "period": "month"},
       otherFees=[fee("Buku dan kegiatan", "Books and activities", 3_600_000), fee(*UNIFORM, 1_100_000)], notes=L("Uang pangkal = DSP.", "Entry fee = DSP."), **N)
upsert("sma-batik-1-surakarta", name="SMA Batik 1 Surakarta", city="Surakarta (Solo)", district="Laweyan", address="Jl. Slamet Riyadi No.445, Pajang, Laweyan, Surakarta",
       registrationFee=250_000, entryFee={"min": 7_500_000, "max": 14_500_000}, tuition={"amount": 500_000, "period": "month"},
       notes=L("Kelas reguler: pendaftaran Rp250.000, SPP Rp500.000, DPP Rp7.500.000 (di bagian lain tertulis Rp8.000.000). Kelas internasional: Rp300.000, SPP Rp1.750.000, DPP Rp13.500.000 (atau Rp14.500.000). Angka DPP di sumber tidak konsisten.",
               "Regular class: registration Rp250,000, tuition Rp500,000, development fee Rp7,500,000 (elsewhere Rp8,000,000). International class: Rp300,000, tuition Rp1,750,000, development fee Rp13,500,000 (or Rp14,500,000). The source is inconsistent on the development fee."), **N)
upsert("smait-insan-mulia-surakarta", name="SMAIT Insan Mulia Surakarta", city="Surakarta (Solo)", district="Laweyan", religion="Islam",
       address="Jl. Manggis IV, Jajar, Laweyan, Surakarta", phone="(0271) 7471984",
       registrationFee=300_000, entryFee={"min": 9_000_000}, tuition={"amount": 600_000, "period": "month"},
       otherFees=[fee("Kegiatan", "Activities", 1_200_000), fee("Seragam putra", "Uniforms (boys)", 1_550_000), fee("Seragam putri", "Uniforms (girls)", 1_700_000)],
       notes=L("Jalur reguler. Uang pangkal = pengembangan. Tersedia juga program boarding.", "Regular track. Entry fee = development fee. A boarding programme is also available."), **N)

OR = {"title": "7 Sekolah Internasional di Surabaya, Ada Kisaran Biaya! (Orami)", "url": "https://www.orami.co.id/magazine/sekolah-internasional-di-surabaya"}
upsert("sampoerna-academy-surabaya", name="Sampoerna Academy Surabaya", city="Surabaya", level="SMA", year="2025/2026", yearAssumed=True, source=OR, checked=CHK,
       entryFee={"min": 150_000_000}, notes=L("Sumber: uang pangkal dari Rp26 juta (prasekolah) hingga Rp150 juta untuk program SMA (perkiraan).", "Source: entry fee from Rp26M (preschool) up to Rp150M for the SMA programme (estimate)."))
print("ok")
