"""Popmama, "10 Biaya Sekolah SD Swasta di Depok untuk Tahun Ajaran 2026/2027" (10 Feb 2026).
Figures copied verbatim from the article."""
from seedlib import L, fee, upsert, UNIFORM, ACTIVITY, BOOKS

SRC = {"title": "10 Biaya Sekolah SD Swasta di Depok untuk Tahun Ajaran 2026/2027 (Popmama)",
       "url": "https://www.popmama.com/big-kid/6-9-years-old/biaya-sekolah-sd-swasta-di-depok-tahun-ajaran-2026-2027-00-bbqjr-302fg6",
       "published": "2026-02-10"}
C = dict(area="jabodetabek", city="Depok", level="SD", year="2026/2027", source=SRC, checked="2026-11-22")

upsert("ar-rahman-islamic-school-cinere", name="Ar-Rahman Islamic School Cinere", district="Cinere", religion="Islam",
       address="Jl. Bukit Cinere Raya No.15C, Gandul, Cinere, Depok", website="https://arrahman-islamic.sch.id",
       registrationFee=450_000, entryFee={"min": 23_500_000}, tuition={"amount": 1_750_000, "period": "month"},
       otherFees=[fee(*ACTIVITY, 3_450_000), fee("Peralatan", "Supplies", 2_457_000), fee(*UNIFORM, 1_356_000)],
       notes=L("Uang pangkal = uang gedung. SPP Juli 2026.", "Entry fee = building fee. Tuition as of July 2026."), **C)
upsert("lazuardi-al-falah-depok", name="Lazuardi Al-Falah Depok", religion="Islam",
       address="Kompleks LIA, Jl. Margonda Raya No.200, Depok", website="https://depok.lazuardialfalah.sch.id",
       registrationFee=725_000, tuition={"amount": 2_100_000, "period": "month"},
       otherFees=[fee(*BOOKS, 1_100_000)],
       notes=L("Biaya semester: gelombang 2 Rp5.500.000, gelombang 3 Rp5.800.000, gelombang 4 Rp6.100.000. Seragam Rp1.400.000–Rp1.600.000. Belum termasuk pendampingan ABK, ekstrakurikuler, jemputan, katering, dan pentas akhir tahun. Sekolah inklusi.",
               "Semester fee: wave 2 Rp5,500,000, wave 3 Rp5,800,000, wave 4 Rp6,100,000. Uniforms Rp1,400,000–Rp1,600,000. Excludes special-needs support, extracurriculars, transport, catering and end-of-year show. Inclusive school."), **C)
upsert("sd-alam-kampung-sawah-depok", name="SD Alam Kampung Sawah", district="Cilodong", curriculum=["Sekolah Alam"],
       address="Jl. SMPN 6 Kalibaru, Kav BNI D6 No.7, Kalibaru, Cilodong, Depok", website="https://sekolahalamkampungsawah.id",
       registrationFee=350_000, entryFee={"min": 14_900_000}, tuition={"amount": 9_600_000, "period": "year"},
       otherFees=[fee("Uang kegiatan tahunan", "Annual activity fee", 3_600_000), fee("T-shirt dan buku Sahabat Quran", "T-shirt and Sahabat Quran book", 500_000)],
       notes=L("Uang pangkal = infaq pendidikan (sekali saat masuk). SPP bisa dibayar Rp800.000/bulan. Biaya pendaftaran termasuk sit-in.",
               "Entry fee = education infaq (one-off). Tuition can be paid at Rp800,000/month. Registration includes a sit-in."), **C)
upsert("sd-dian-didaktika-cinere", name="SD Dian Didaktika", district="Cinere",
       address="Jl. Rajawali Blok F No.10 & 16, Cinere, Depok", website="https://diandidaktika.sch.id",
       registrationFee=550_000, entryFee={"min": 28_000_000, "max": 32_000_000}, tuition={"amount": 2_750_000, "period": "month"},
       otherFees=[fee("Buku paket", "Textbooks", 2_750_000), fee(*UNIFORM, 1_700_000), fee("POMG", "Parent–teacher association", 20_000), fee(*ACTIVITY, 4_000_000)],
       notes=L("Dari TK Dian Didaktika: pendaftaran Rp550.000, uang pangkal Rp28.000.000. Dari luar: Rp600.000 dan Rp32.000.000.",
               "From TK Dian Didaktika: registration Rp550,000, entry Rp28,000,000. External: Rp600,000 and Rp32,000,000."), **C)
upsert("sdit-cahaya-quran-depok", name="SDIT Cahaya Quran Depok", district="Cilodong", religion="Islam",
       address="Jl. Merah Delima No.11, Sukamaju, Cilodong, Depok", website="https://cahayaquran.sch.id",
       entryFee={"min": 18_250_000}, tuition={"amount": 750_000, "period": "month"},
       notes=L("Biaya masuk gelombang sudah termasuk uang pangkal, seragam 6 setel, uang kegiatan dan buku 1 tahun. SPP kelas 1–3 Rp750.000; kelas 4–6 Rp850.000.",
               "Entry fee includes uang pangkal, 6 uniform sets, and one year of activities and books. Tuition grades 1–3 Rp750,000; grades 4–6 Rp850,000."), **C)
upsert("sdit-darul-abidin-depok", name="SDIT Darul Abidin", district="Beji", religion="Islam",
       address="Jl. Karet Hijau No.52, Beji Timur, Beji, Depok",
       registrationFee=475_000, entryFee={"min": 25_200_000, "max": 28_700_000}, tuition={"amount": 2_080_000, "period": "month"},
       otherFees=[fee("Biaya masuk tahap II", "Entry fee stage II", 2_500_000)],
       notes=L("Formulir Rp475.000–Rp525.000. Uang pangkal = biaya masuk tahap I. Tahap III: Rp300.000/bulan selama 36 bulan.",
               "Form Rp475,000–Rp525,000. Entry fee = stage I. Stage III: Rp300,000/month for 36 months."), **C)
upsert("sdit-nurul-fikri-depok", name="SDIT Nurul Fikri", district="Cimanggis", religion="Islam",
       address="Jl. Tugu Raya No.61, Tugu, Cimanggis, Depok", website="https://sdit.nurulfikri.sch.id",
       registrationFee=500_000, entryFee={"min": 22_500_000},
       otherFees=[fee("Dana pendidikan", "Education fund", 14_000_000), fee("Seragam putra", "Uniforms (boys)", 1_900_000),
                  fee("Seragam putri", "Uniforms (girls)", 2_500_000), fee("Dana tahunan (tahun berikutnya)", "Annual fee (following years)", 3_750_000)],
       notes=L("Pendaftaran Rp500.000–Rp650.000. Uang pangkal = dana pengembangan. SPP tidak dicantumkan sumber.",
               "Registration Rp500,000–Rp650,000. Entry fee = development fund. Tuition not stated by the source."), **C)
upsert("semut-semut-natural-school", name="Semut-Semut The Natural School", district="Cimanggis", curriculum=["Sekolah Alam"],
       address="Jl. Industri Kapal Dalam No.25A, Kelapa Dua, Cimanggis, Depok", website="https://semut-semut.sch.id",
       registrationFee=600_000, entryFee={"min": 29_500_000}, tuition={"amount": 1_875_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 875_000)],
       notes=L("Uang pangkal = uang pendaftaran dan DPPOS. Belum termasuk katering, jemputan, ekstrakurikuler. DPPOS biasanya naik di kelas 3 dan 5.",
               "Entry fee = enrolment & DPPOS fee. Excludes catering, transport, extracurriculars. DPPOS usually increases in grades 3 and 5."), **C)
upsert("sekolah-karakter-cimanggis", name="Sekolah Karakter Cimanggis", district="Cimanggis",
       address="Jl. Raya Jakarta–Bogor Km. 31 No.46, Cimanggis, Depok", website="https://sekolahkarakter.sch.id",
       registrationFee=600_000, entryFee={"min": 25_000_000}, tuition={"amount": 1_600_000, "period": "month"},
       otherFees=[fee("Uang kegiatan tahunan", "Annual activity fee", 6_500_000), fee("Seragam dan literatur", "Uniforms & books", 800_000)],
       notes=L("Biaya pendaftaran termasuk TKS dan orientasi.", "Registration includes readiness test and orientation."), **C)
upsert("sekolah-pribadi-depok", name="Sekolah Pribadi Depok (Pribadi Bilingual School)", curriculum=["Cambridge"],
       address="Jl. Margonda Raya No.229, Depok", website="https://pribadidepok.sch.id",
       registrationFee=1_500_000, entryFee={"min": 53_000_000}, tuition={"amount": 69_850_000, "period": "year"},
       otherFees=[fee("Perlengkapan (tahun pertama)", "Supplies package (first year)", 13_350_000), fee("Perlengkapan (tahun selanjutnya)", "Supplies package (following years)", 8_850_000)],
       notes=L("Perlengkapan termasuk seragam, Cambridge Checkpoint Test, buku, platform pendidikan, outing class, kegiatan, dan kompetisi.",
               "Supplies package includes uniforms, Cambridge Checkpoint Test, books, learning platform, outings, activities and competitions."), **C)
print("ok")
