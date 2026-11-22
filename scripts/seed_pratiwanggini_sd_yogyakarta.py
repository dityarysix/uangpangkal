"""Pratiwanggini (parent blog), "Biaya Pendidikan 18 SD Islam Favorit di Yogyakarta" (23 Jun 2024).
Written for the next intake; SD Budi Mulia Dua Panjen is explicitly 2025/2026, others -> 2025/2026 yearAssumed.
Figures verbatim; "uang pangkal dll + annual fee" amounts are stored as the entry fee with that wording in the notes."""
from seedlib import L, fee, upsert

SRC = {"title": "Biaya Pendidikan 18 SD Islam Favorit di Yogyakarta (blog Pratiwanggini)", "url": "https://pratiwanggini.net/2024/06/biaya-pendidikan-sd-islam/", "published": "2024-06-23"}
CHK = "2026-11-22"
C = dict(level="SD", year="2025/2026", yearAssumed=True, source=SRC, checked=CHK, religion="Islam")
PA = L("Uang pangkal di sini = uang pangkal dll + annual fee (sesuai sumber).", "Entry fee here = entry fee etc. + annual fee (as given by the source).")

upsert("sd-al-azhar-31-sinduadi", name="SD Al-Azhar 31 Sinduadi Yogyakarta", city="Sleman", district="Mlati", phone="(0274) 885765",
       registrationFee=400_000, entryFee={"min": 22_075_000, "max": 23_380_000}, tuition={"amount": 895_000, "period": "month"},
       otherFees=[fee("Herregistrasi kenaikan kelas (min.)", "Annual re-registration (min.)", 4_880_000)],
       notes=L("Sumber memuat dua rincian (sekolah juga membuka kelas tahfidz): Rp22.075.000, SPP Rp895.000, herregistrasi Rp4.880.000; dan Rp23.380.000, SPP Rp1.200.000, herregistrasi Rp4.980.000. " + PA["id"] + " SPP belum termasuk ekskul dan antar jemput.",
               "The source gives two breakdowns (the school also runs a tahfidz class): Rp22,075,000, tuition Rp895,000, re-registration Rp4,880,000; and Rp23,380,000, tuition Rp1,200,000, re-registration Rp4,980,000. " + PA["en"] + " Tuition excludes extracurriculars and transport."), **C)
upsert("sd-islam-al-azhar-55-yogyakarta", name="SD Islam Al Azhar 55 Yogyakarta", city="Sleman", district="Mlati", phone="WA +62 813-5510-1155",
       address="Jl. Padjajaran, Sinduadi, Mlati, Sleman",
       registrationFee=450_000, entryFee={"min": 34_220_000}, tuition={"amount": 1_740_000, "period": "month"},
       otherFees=[fee("Herregistrasi kenaikan kelas", "Annual re-registration", 7_180_000)], notes=L("Uang pangkal dll. SPP belum termasuk antar jemput dan ekskul.", "Entry fee etc. Tuition excludes transport and extracurriculars."), **C)
upsert("sd-budi-mulia-dua-panjen", name="SD Budi Mulia Dua Panjen", city="Sleman", district="Ngemplak", phone="(0274) 485551 / WA +62 812-1575-909",
       address="Dusun Kergan, Kenayan, Wedomartani, Ngemplak, Sleman",
       registrationFee=285_000, entryFee={"min": 26_500_000}, tuition={"amount": 1_675_000, "period": "month"},
       otherFees=[fee("Learning activities per tahun", "Learning activities per year", 11_500_000)],
       notes=L("Uang pangkal = joining fee. SPP siswa reguler Rp1.675.000; siswa inklusi Rp3.175.000. Sumber menyebut ini biaya tahun 2025/2026.", "Entry fee = joining fee. Tuition: regular Rp1,675,000; inclusive programme Rp3,175,000. The source states these are 2025/2026 fees."),
       **{**C, "yearAssumed": False})
upsert("sd-bias-yogyakarta-ii", name="SD BIAS Yogyakarta II", city="Sleman", district="Ngaglik", phone="(0274) 4538094 / WA +62 821-3872-4737",
       address="Jl. Kaliurang Km 10,9, Ngaglik, Sleman", website="https://sekolahbias.sch.id/sd",
       entryFee={"min": 27_925_000}, tuition={"amount": 2_300_000, "period": "month"},
       otherFees=[fee("Biaya semesteran", "Semester fee", 3_100_000)], notes=L("Uang pangkal awal. Termasuk ekskul, family day, PKL, dll.", "Initial entry fee. Includes extracurriculars, family day, field study, etc."), **C)
upsert("sd-bias-yogyakarta-iii", name="SD BIAS Yogyakarta III", city="Sleman", district="Ngaglik", phone="(0274) 2832284 / WA +62 821-3872-4737",
       address="Jl. Palagan Tentara Pelajar Km 7,9, Sariharjo, Ngaglik, Sleman", website="https://sekolahbias.sch.id/sd",
       entryFee={"min": 30_525_000}, tuition={"amount": 2_400_000, "period": "month"},
       notes=L("Uang pangkal dll + kegiatan per semester (family day, PKL, ekskul).", "Entry fee etc. + per-semester activities (family day, field study, extracurriculars)."), **C)
upsert("sd-afkaaruna-sleman", name="Afkaaruna Islamic School Sleman", city="Sleman", district="Pakem", phone="WA +62 813-9377-7227",
       entryFee={"min": 21_050_000}, tuition={"amount": 1_100_000, "period": "month"},
       notes=L("Jenjang dasar berbentuk Madrasah Ibtidaiyah (setara SD). " + PA["id"] + " SPP termasuk katering dan snack.", "Primary level is a Madrasah Ibtidaiyah (equivalent to SD). " + PA["en"] + " Tuition includes catering and snacks."), **C)
upsert("sd-budi-mulia-dua-pandeansari", name="SD Budi Mulia Dua Pandeansari", city="Sleman", district="Depok", phone="(0274) 889939 / WA +62 822-2522-5512",
       address="Komp. Pandean Sari Blok IV, Condongcatur, Depok, Sleman",
       entryFee={"min": 28_150_000}, tuition={"amount": 1_375_000, "period": "month"}, notes=PA, **C)
upsert("sdit-luqman-al-hakim-sleman", name="SDIT Luqman Al Hakim Sleman", city="Sleman", district="Ngaglik", phone="(0274) 866744 / WA +62 857-4725-5761",
       address="Jl. Palagan Tentara Pelajar No.52, Sedan, Sariharjo, Ngaglik, Sleman",
       registrationFee=350_000, entryFee={"min": 25_000_000}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee("Antar jemput (per bulan)", "Transport (per month)", 900_000), fee("SIMPATI subsidi yatim & dhuafa (per bulan)", "SIMPATI orphan subsidy (per month)", 100_000),
                  fee("Komite per tahun", "Committee per year", 125_000), fee("Iuran JSIT, Pramuka, dll. per tahun", "JSIT, scouts etc. per year", 150_000),
                  fee("Seragam putra", "Uniforms (boys)", 1_650_000), fee("Seragam putri", "Uniforms (girls)", 1_800_000)],
       notes=L("Uang pangkal = IPP (Infaq Pengembangan Pendidikan). SPP termasuk makan dan snack.", "Entry fee = IPP (education development infaq). Tuition includes meals and snacks."), **C)
upsert("sd-teladan-yogyakarta", name="SD Teladan Yogyakarta", city="Sleman", district="Gamping", phone="(0274) 2923001 / WA +62 856-0217-2302",
       address="Jl. Kabupaten No.99 Km 0,5, Nogotirto, Gamping, Sleman",
       registrationFee=300_000, entryFee={"min": 17_000_000}, tuition={"amount": 1_600_000, "period": "month"},
       otherFees=[fee("Daftar ulang", "Re-registration", 6_500_000)], notes=L("SPP termasuk katering dan snack.", "Tuition includes catering and snacks."), **C)
upsert("global-islamic-school-jogja", name="Global Islamic School (GIS) Jogja", city="Sleman", district="Depok", phone="(0274) 2809609 / WA +62 811-2632-208",
       registrationFee=500_000, entryFee={"min": 27_350_000}, tuition={"amount": 1_425_000, "period": "month"},
       otherFees=[fee("Herregistrasi kenaikan kelas", "Annual re-registration", 6_045_000)], notes=L("Uang pangkal awal. SPP belum termasuk katering, antar jemput, ekskul.", "Initial entry fee. Tuition excludes catering, transport and extracurriculars."), **C)
upsert("sd-muhammadiyah-condongcatur", name="SD Muhammadiyah Condongcatur", city="Sleman", district="Depok", phone="(0274) 486619 / WA +62 851-0082-6777",
       entryFee={"min": 16_510_000}, tuition={"amount": 845_000, "period": "month"},
       notes=L(PA["id"] + " SPP termasuk katering dan snack. Ekskul Rp150–350 ribu.", PA["en"] + " Tuition includes catering and snacks. Extracurriculars Rp150–350k."), **C)
upsert("gistrav-islamia-school-jogja", name="GISTRAV Islamia School Jogja", city="Sleman", district="Ngaglik", phone="WA +62 811-2505-053",
       address="GISTRAV Edu Land, Jl. Gito Gati, Rejodani 2, Sariharjo, Ngaglik, Sleman",
       registrationFee=200_000, entryFee={"min": 16_669_000}, tuition={"amount": 1_400_000, "period": "month"},
       otherFees=[fee("Herregistrasi", "Re-registration", 2_780_000)], notes=PA, **C)
upsert("sd-salman-al-farisi-2-sleman", name="SD Salman Al Farisi 2 Sleman", city="Sleman", district="Ngemplak",
       entryFee={"min": 13_940_000}, tuition={"amount": 825_000, "period": "month"},
       notes=L(PA["id"] + " Iuran bulanan termasuk katering dan snack. Ekskul Rp150–350 ribu.", PA["en"] + " Monthly fee includes catering and snacks. Extracurriculars Rp150–350k."), **C)
upsert("sdit-salsabila-2-klaseman", name="SDIT Salsabila 2 Klaseman", city="Sleman", district="Ngaglik",
       address="Jl. Pamularsih, Klaseman, Sinduharjo, Ngaglik, Sleman",
       entryFee={"min": 9_230_000}, tuition={"amount": 500_000, "period": "month"}, notes=PA, **C)
upsert("sdii-al-abidin-yogyakarta", name="SDII Al Abidin Yogyakarta", city="Sleman", district="Ngemplak", address="Jetis, Wedomartani, Ngemplak, Sleman",
       entryFee={"min": 10_000_000, "max": 13_000_000}, tuition={"amount": 600_000, "period": "month"}, notes=PA, **C)
upsert("sdit-taruna-al-quran-yogyakarta", name="SDIT Taruna Al Qur'an Yogyakarta", city="Sleman", district="Ngaglik",
       address="Jl. Lempongsari Gg. Bawal, Jongkang, Sariharjo, Ngaglik, Sleman", website="https://taruna-alquran.com/sd-islam-terpadu-taruna-al-quran",
       entryFee={"min": 13_825_000}, tuition={"amount": 650_000, "period": "month"}, notes=PA, **C)
upsert("sd-islam-al-azhar-cairo-yogyakarta", name="SD Islam Al Azhar Cairo Yogyakarta", city="Sleman", district="Ngaglik",
       address="Jl. Bimo No.1, Ngangkruk, Sardonoharjo, Ngaglik, Sleman",
       entryFee={"min": 25_700_000}, tuition={"amount": 1_130_000, "period": "month"},
       otherFees=[fee("Katering dan snack (per bulan)", "Catering and snacks (per month)", 440_000)], **C)
upsert("sdit-alam-nurul-islam-yogyakarta", name="SDIT Alam Nurul Islam Yogyakarta", city="Sleman", district="Gamping",
       address="Jl. Ringroad Barat, Cambahan, Nogotirto, Gamping, Sleman",
       registrationFee=200_000, entryFee={"min": 16_000_000}, tuition={"amount": 930_000, "period": "month"},
       otherFees=[fee("Wakaf", "Endowment (wakaf)", 1_000_000), fee("Seragam putra", "Uniforms (boys)", 1_290_000), fee("Seragam putri", "Uniforms (girls)", 1_700_000),
                  fee("Herregistrasi kenaikan kelas", "Annual re-registration", 3_000_000)],
       notes=L("Biaya masuk bisa berbeda tergantung gelombang dan asal TK. SPP termasuk konsumsi.", "Entry fee varies by wave and kindergarten of origin. Tuition includes meals."), **C)
print("ok")
