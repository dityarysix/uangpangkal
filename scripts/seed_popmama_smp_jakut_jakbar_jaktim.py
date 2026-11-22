"""Popmama, "Intip Biaya SMP di Jakarta Utara, Barat, dan Timur TA 2026/2027!" (22 Dec 2025).
Figures copied verbatim from the article."""
from seedlib import L, fee, upsert, BOOKS

SRC = {"title": "Intip Biaya SMP di Jakarta Utara, Barat, dan Timur TA 2026/2027 (Popmama)",
       "url": "https://www.popmama.com/big-kid/10-12-years-old/intip-biaya-smp-di-jakarta-utara-barat-dan-timur-ta-2026-2027-00-sdwkg-0j19nt",
       "published": "2025-12-22"}
C = dict(area="jabodetabek", level="SMP", year="2026/2027", source=SRC, checked="2026-11-22")

upsert("smp-wijaya-kusuma-penjaringan", name="SMP Wijaya Kusuma", city="Jakarta Utara", district="Penjaringan",
       address="Jl. Bandengan 80, Penjaringan, Jakarta Utara",
       entryFee={"min": 6_140_000, "max": 8_170_000}, tuition={"amount": 850_000, "period": "month"},
       notes=L("Biaya masuk laki-laki Rp6.140.000–Rp7.940.000; perempuan Rp6.370.000–Rp8.170.000. SPP = iuran akademik.",
               "Entry fee for boys Rp6,140,000–Rp7,940,000; girls Rp6,370,000–Rp8,170,000. Tuition = academic contribution."), **C)
upsert("smpit-ash-shiddiq-jakarta", name="SMPIT Ash-Shiddiq Jakarta", city="Jakarta Utara", district="Koja", religion="Islam",
       address="Jl. Bendungan Melayu Utara, Koja, Jakarta Utara",
       entryFee={"min": 19_830_000, "max": 19_980_000}, tuition={"amount": 1_050_000, "period": "month"},
       notes=L("Biaya masuk ikhwan (putra) Rp19.830.000, akhwat (putri) Rp19.980.000, sudah termasuk SPP Juli 2026.",
               "Entry fee for boys Rp19,830,000, girls Rp19,980,000, including July 2026 tuition."), **C)
upsert("westin-school", name="Westin School", city="Jakarta Utara", district="Penjaringan",
       registrationFee=150_000, entryFee={"min": 12_500_000}, tuition={"amount": 1_700_000, "period": "month"}, **C)
upsert("highscope-indonesia-kelapa-gading", name="Sekolah HighScope Indonesia Kelapa Gading", city="Jakarta Utara",
       address="Jl. Pegangsaan Dua No.22, Jakarta Utara",
       registrationFee=300_000, entryFee={"min": 62_000_000}, tuition={"amount": 5_900_000, "period": "month"},
       otherFees=[fee("Observasi & tes kelas", "Observation & placement test", 500_000)],
       notes=L("Biaya masuk untuk grade 7–9.", "Entry fee for grades 7–9."), **C)
upsert("sekolah-citra-kasih-jakarta-kalideres", name="Sekolah Citra Kasih Jakarta", city="Jakarta Barat", district="Kalideres",
       registrationFee=350_000, entryFee={"min": 24_500_000}, tuition={"amount": 1_650_000, "period": "month"}, **C)
upsert("bpk-penabur-smpk-7-kedoya", name="SMPK 7 BPK Penabur", city="Jakarta Barat", district="Kebon Jeruk", religion="Kristen",
       address="Komplek Sunrise Garden, Kedoya Utara, Jakarta Barat",
       registrationFee=400_000, entryFee={"min": 36_000_000}, tuition={"amount": 3_460_000, "period": "month"},
       notes=L("Kelas nasional Rp3.460.000/bulan; kelas bilingual Rp4.280.000/bulan.", "National class Rp3,460,000/month; bilingual class Rp4,280,000/month."), **C)
upsert("smp-islam-al-azhar-10-kembangan", name="SMP Islam Al Azhar 10 Kembangan", city="Jakarta Barat", district="Kembangan", religion="Islam",
       address="Jl. H. Saaba, Meruya Selatan, Kembangan, Jakarta Barat",
       registrationFee=550_000, entryFee={"min": 31_721_000, "max": 33_721_000}, tuition={"amount": 2_025_000, "period": "month"},
       otherFees=[fee("Buku paket kelas VII", "Grade 7 textbooks", 1_800_000), fee("Seragam + ASBD", "Uniforms + ASBD", 1_754_000)],
       notes=L("Uang pangkal Rp31.721.000 untuk lulusan SDI Al Azhar; Rp33.721.000 untuk siswa dari luar.",
               "Entry fee Rp31,721,000 for SDI Al Azhar graduates; Rp33,721,000 for external students."), **C)
upsert("labschool-rawamangun", name="Labschool Rawamangun", city="Jakarta Timur", district="Pulo Gadung",
       address="Jl. Pemuda No.248, Rawamangun, Jakarta Timur",
       registrationFee=500_000, entryFee={"min": 33_000_000, "max": 35_000_000},
       notes=L("Uang pangkal jalur prestasi Rp33.000.000; jalur tes Rp35.000.000. Biaya pendaftaran termasuk seleksi.",
               "Entry fee via achievement track Rp33,000,000; via test track Rp35,000,000. Registration fee includes selection."), **C)
upsert("smp-islam-pb-soedirman-cijantung", name="SMP Islam PB Soedirman Cijantung", city="Jakarta Timur", district="Pasar Rebo", religion="Islam",
       address="Jl. Raya Bogor Km. 24, Cijantung, Jakarta Timur",
       registrationFee=450_000, entryFee={"min": 14_000_000, "max": 18_500_000}, tuition={"amount": 1_260_000, "period": "month"},
       notes=L("Kelas reguler: biaya masuk Rp14.000.000, SPP Rp1.260.000/bulan. Kelas FLC (bilingual): Rp18.500.000 dan Rp1.610.000/bulan.",
               "Regular class: entry Rp14,000,000, tuition Rp1,260,000/month. FLC (bilingual) class: Rp18,500,000 and Rp1,610,000/month."), **C)
upsert("sekolah-cikal-amri-setu", name="Sekolah Cikal Amri Setu", city="Jakarta Timur", district="Cipayung",
       address="Jl. Raya Setu No.3, Jakarta Timur",
       entryFee={"min": 23_067_000, "max": 59_500_000},
       notes=L("Biaya masuk Year 7 Rp59.500.000; Year 8 Rp46.134.000; Year 9 Rp23.067.000; pendidikan inklusi (3 tahun) Rp55.000.000.",
               "Entry fee Year 7 Rp59,500,000; Year 8 Rp46,134,000; Year 9 Rp23,067,000; inclusive education (3 years) Rp55,000,000."), **C)
print("ok")
