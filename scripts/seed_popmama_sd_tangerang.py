"""Popmama, "18 Daftar SD di Tangerang Raya dan Biaya Masuk 2025/2026" (10 Nov 2025).
Figures copied verbatim from the article. The article covers academic year 2025/2026."""
from seedlib import L, fee, upsert, UNIFORM, ACTIVITY, BOOKS

SRC = {"title": "18 Daftar SD di Tangerang Raya dan Biaya Masuk 2025/2026 (Popmama)",
       "url": "https://www.popmama.com/big-kid/6-9-years-old/daftar-sd-di-tangerang-raya-dan-biaya-masuk-2025-2026-00-8zdst-vg8hpm",
       "published": "2025-11-10"}
C = dict(area="jabodetabek", level="SD", year="2025/2026", source=SRC, checked="2026-11-22")
TS = "Tangerang Selatan"

upsert("sdi-cikal-harapan-bsd", name="SDI Cikal Harapan", city=TS, district="Serpong", religion="Islam",
       address="BSD City, Serpong, Tangerang Selatan",
       registrationFee=350_000, entryFee={"min": 18_000_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Biaya kegiatan belajar mengajar (per tahun)", "Teaching & learning fee (per year)", 4_000_000), fee(*UNIFORM, 1_200_000)], **C)
upsert("sekolah-auliya", name="Sekolah Auliya", city=TS, district="Pondok Aren", religion="Islam",
       address="Jl. Jombang Raya No.1, Parigi, Pondok Aren, Tangerang Selatan", website="https://sekolahauliya.sch.id",
       registrationFee=750_000, entryFee={"min": 47_900_000}, tuition={"amount": 2_300_000, "period": "month"},
       notes=L("Biaya pendaftaran = observasi & wawancara. Biaya masuk bisa dicicil dan ada diskon.", "Registration fee = observation & interview. Entry fee can be paid in instalments; discounts available."), **C)
upsert("sd-islam-al-azhar-17-bintaro", name="SD Islam Al-Azhar 17 Bintaro", city=TS, district="Pondok Aren", religion="Islam",
       address="Jl. Bonjol No.9, Pondok Karya, Pondok Aren, Tangerang Selatan",
       registrationFee=550_000, entryFee={"min": 38_000_000}, tuition={"amount": 2_200_000, "period": "month"}, **C)
upsert("sekolah-tunas-indonesia-bintaro", name="Sekolah Tunas Indonesia", city=TS, district="Pondok Aren", curriculum=["Nasional Plus"],
       address="Jl. Jombang Raya Bintaro Jaya No.18, Parigi, Tangerang Selatan",
       registrationFee=400_000, entryFee={"min": 28_000_000}, tuition={"amount": 2_900_000, "period": "month"},
       notes=L("Seragam & buku ± Rp3.000.000/tahun.", "Uniforms & books ~Rp3,000,000/year."), **C)
upsert("insan-cendekia-madani", name="Insan Cendekia Madani (ICM)", city=TS, district="Serpong", religion="Islam",
       address="Gg. H. Amat, Jl. Maruga Raya, Ciater, Serpong, Tangerang Selatan",
       registrationFee=900_000, entryFee={"min": 39_000_000, "max": 65_000_000}, tuition={"amount": 5_650_000, "period": "month"},
       notes=L("Uang pangkal Rp39.000.000 dengan diskon sampai Desember 2025; harga normal Rp65.000.000. Sekolah berasrama.",
               "Entry fee Rp39,000,000 with discount until December 2025; normal price Rp65,000,000. Boarding school."), **C)
upsert("stella-maris-school-bsd", name="Stella Maris School", city=TS, district="Serpong", religion="Katolik",
       address="Jl. Artha Kencana Kav C1, Kencana Loka, Serpong, Tangerang Selatan",
       entryFee={"min": 27_048_000, "max": 30_000_000}, tuition={"amount": 2_700_000, "period": "month"},
       notes=L("Uang pangkal Rp30.000.000, diskon 2%+8% menjadi Rp27.048.000. SPP naik Rp130.000/tahun. Uang kegiatan, buku, dan seragam diinfokan kemudian.",
               "Entry fee Rp30,000,000, 2%+8% discount to Rp27,048,000. Tuition rises Rp130,000/year. Activity, book and uniform fees announced later."), **C)
upsert("sdit-bait-adzkia-ciputat", name="SDIT Bait Adzkia Islamic School", city=TS, district="Ciputat", religion="Islam",
       address="Jl. Suka Damai VI, Serua Indah, Ciputat, Tangerang Selatan",
       registrationFee=300_000, entryFee={"min": 6_000_000}, tuition={"amount": 600_000, "period": "month"},
       otherFees=[fee("Buku siswa (per tahun)", "Student books (per year)", 1_350_000), fee("Seragam (6 set)", "Uniforms (6 sets)", 1_500_000),
                  fee("Sampul rapor", "Report cover", 100_000), fee("Sarpras (pemeliharaan, lab komputer, server & aplikasi)", "Facilities (maintenance, computer lab, server & app)", 650_000),
                  fee("Uang kegiatan termasuk ekskul (per tahun)", "Activities incl. extracurriculars (per year)", 2_000_000)],
       notes=L("Uang pangkal = infaq gedung. SPP khusus kelas 1.", "Entry fee = building infaq. Tuition for grade 1."), **C)
upsert("sd-islam-at-taqwa-pamulang", name="SD Islam At-Taqwa", city=TS, district="Pamulang", religion="Islam",
       address="Jl. Benda Timur 15, Benda Baru, Pamulang, Tangerang Selatan",
       registrationFee=200_000, entryFee={"min": 2_900_000}, tuition={"amount": 250_000, "period": "month"},
       otherFees=[fee("Seragam (6 stel)", "Uniforms (6 sets)", 1_650_000), fee("Buku paket", "Textbooks", 1_650_000)],
       notes=L("Uang pangkal = dana pembangunan. SPP sudah termasuk ekskul, flat sampai kelas 6.", "Entry fee = building fund. Tuition includes extracurriculars, flat until grade 6."), **C)
upsert("tara-salvia", name="Tara Salvia", city=TS, district="Ciputat",
       address="Jl. Menjangan Raya No.9, Sawah Lama, Ciputat, Tangerang Selatan",
       registrationFee=1_000_000, entryFee={"min": 47_000_000}, tuition={"amount": 2_425_000, "period": "month"},
       otherFees=[fee("Uang kegiatan (per tahun)", "Activity fee (per year)", 3_725_000)], **C)
upsert("bpk-penabur-bintaro", name="BPK Penabur Bintaro Jaya", city=TS, district="Pondok Aren", religion="Kristen",
       address="Jl. Panglima Polim Blok A6 No.1, Sektor 7 Bintaro Jaya, Pondok Jaya, Pondok Aren, Tangerang Selatan",
       registrationFee=350_000, entryFee={"min": 21_200_000}, tuition={"amount": 2_650_000, "period": "month"},
       notes=L("Belum termasuk buku, seragam, uang kegiatan, dan ekskul.", "Excludes books, uniforms, activity fee and extracurriculars."), **C)
upsert("st-johns-catholic-school-bsd", name="St. John's Catholic School BSD", city=TS, district="Serpong", religion="Katolik",
       address="Jl. Kencana Loka Raya Sektor 12 No.8, BSD City, Rawa Buntu, Serpong, Tangerang Selatan",
       registrationFee=500_000, entryFee={"min": 65_000_000}, tuition={"amount": 4_650_000, "period": "month"},
       notes=L("Uang pangkal sudah termasuk seragam dan buku selama satu tahun pertama. Ekstrakurikuler Rp1–3 juta/tahun.",
               "Entry fee includes uniforms and books for the first year. Extracurriculars Rp1–3 million/year."), **C)
upsert("mentari-intercultural-school-bintaro", name="Mentari Intercultural School Bintaro", city=TS, district="Pondok Aren", curriculum=["Cambridge"],
       address="Jl. Perigi Baru No.7A, Parigi Baru, Pondok Aren, Tangerang Selatan",
       registrationFee=800_000, entryFee={"min": 73_500_000}, tuition={"amount": 5_350_000, "period": "month"},
       otherFees=[fee("Buku & materi belajar (Grade 1)", "Books & learning materials (Grade 1)", 4_280_000), fee("Kelas renang Grade 1 (8 sesi)", "Grade 1 swimming (8 sessions)", 1_000_000),
                  fee("Asuransi kecelakaan (per tahun)", "Personal accident insurance (per year)", 200_000)],
       notes=L("Uang pangkal = development fee (Grade 1–6). SPP untuk Grade 1; tiap grade berbeda. Seragam: TBA.",
               "Entry fee = development fee (Grades 1–6). Tuition shown for Grade 1; each grade differs. Uniforms: TBA."), **C)
upsert("global-jaya-school", name="Global Jaya School", city=TS, district="Pondok Aren", curriculum=["IB"],
       address="Jl. Emerald Boulevard, Bintaro Jaya, Pondok Aren, Tangerang Selatan", website="https://www.globaljaya.com",
       entryFee={"min": 27_000_000, "max": 113_000_000}, tuition={"amount": 36_360_000, "period": "quarter"},
       otherFees=[fee("Seragam (3 set)", "Uniforms (3 sets)", 800_000)],
       notes=L("SP development fee Rp27.000.000 per 1 tahun atau Rp113.000.000 untuk 6 tahun. SPP per tahun Rp133.320.000 (termasuk diskon 1 bulan).",
               "Development fee Rp27,000,000 per year or Rp113,000,000 for 6 years. Tuition per year Rp133,320,000 (includes one month's discount)."), **C)
upsert("binus-school-serpong", name="BINUS School Serpong", city=TS, district="Serpong Utara", curriculum=["Cambridge"],
       address="Jl. Lengkong Karya–Jelupang No.58, Jelupang, Serpong Utara, Tangerang Selatan",
       registrationFee=300_000, entryFee={"min": 97_000_000}, tuition={"amount": 19_500_000, "period": "quarter"},
       notes=L("Uang pangkal = enrollment fee (Grade 1–6).", "Entry fee = enrolment fee (Grades 1–6)."), **C)
upsert("sd-harapan-bangsa-modernland", name="SD Harapan Bangsa Modernland", city="Kota Tangerang", district="Tangerang",
       address="Jl. Pulau Putri Raya Kav 10, Modernland, Tangerang, Kota Tangerang",
       registrationFee=400_000, entryFee={"min": 46_942_250}, tuition={"amount": 3_412_500, "period": "month"}, **C)
upsert("jade-school-serpong", name="Jade School", city=TS, district="Serpong Utara",
       address="Jl. Raya Serpong Km. 8, Pakulonan, Serpong Utara, Tangerang Selatan", website="https://www.jade-school.com",
       registrationFee=0, entryFee={"min": 0}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee("Biaya administrasi per semester", "Administration fee per semester", 1_500_000)],
       notes=L("Tanpa uang pendaftaran dan uang pangkal. Estimasi seragam Rp1.000.000; ekskul Rp400.000/ekskul; kegiatan maksimal Rp1.000.000/kegiatan.",
               "No registration or entry fee. Estimated uniforms Rp1,000,000; extracurriculars Rp400,000 each; activities up to Rp1,000,000 each."), **C)
upsert("tunas-bangsa-christian-school-gading-serpong", name="Tunas Bangsa Christian School Gading Serpong", city="Kabupaten Tangerang", district="Kelapa Dua", religion="Kristen",
       address="Jl. Kelapa Gading Selatan Sektor IIA Blok HA 1, Pakulonan Barat, Kelapa Dua, Kabupaten Tangerang",
       registrationFee=250_000, entryFee={"min": 29_000_000}, tuition={"amount": 2_750_000, "period": "month"}, **C)
upsert("sekolah-pelita-harapan-lippo-village", name="Sekolah Pelita Harapan Lippo Village", city="Kabupaten Tangerang", district="Kelapa Dua", curriculum=["Internasional"],
       address="Jl. Boulevard Palem Raya No.2500, Lippo Village, Kelapa Dua, Kabupaten Tangerang",
       registrationFee=3_000_000, entryFee={"min": 56_500_000, "max": 214_200_000}, tuition={"amount": 214_000_000, "period": "year"},
       notes=L("Sumber mencantumkan biaya per tahun akademik: 1 tahun Rp56.500.000; 2 tahun Rp99.500.000; 3 tahun Rp128.000.000; 4 tahun Rp157.000.000; 5 tahun Rp185.000.000; 6 tahun Rp214.200.000. SPP/tahun kelas 1–2 Rp214.000.000; kelas 3–6 Rp223.000.000.",
               "Source lists fees by number of academic years: 1 year Rp56,500,000; 2 years Rp99,500,000; 3 years Rp128,000,000; 4 years Rp157,000,000; 5 years Rp185,000,000; 6 years Rp214,200,000. Tuition per year grades 1–2 Rp214,000,000; grades 3–6 Rp223,000,000."), **C)
print("ok")
