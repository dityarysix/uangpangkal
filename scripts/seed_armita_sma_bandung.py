"""Armita Fibri (blog), "Biaya Masuk SMA Bandung [Update 2026]" (10 May 2026) — https://armitafibri.com/biaya-masuk-sma-bandung/
Years as stated per school (Alfa Centauri 2023/2024; Telkom 2024 -> 2024/2025); others are undated in a 2024-era survey
-> 2024/2025 with yearAssumed. Skipped: UPI Labschool (university lab school), state SMA, schools whose figures are only in images."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

SRC = {"title": "Biaya Masuk SMA Bandung [Update 2026] (blog Armita Fibri)", "url": "https://armitafibri.com/biaya-masuk-sma-bandung/", "published": "2026-05-10"}
CHK = "2026-11-22"
def C(year="2024/2025", assumed=True): return dict(level="SMA", year=year, source=SRC, checked=CHK, **({"yearAssumed": True} if assumed else {}))

upsert("sma-istiqamah-bandung", name="SMA Istiqamah Bandung", city="Kota Bandung", district="Buahbatu", religion="Islam",
       address="Komplek Puragabaya No.14, Jl. Cijaura Girang, Sekejati, Buahbatu, Kota Bandung",
       registrationFee=350_000, entryFee={"min": 7_000_000}, tuition={"amount": 400_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_200_000), fee("Kegiatan kurikulum", "Curriculum activities", 1_000_000), fee("Kegiatan kesiswaan", "Student activities", 500_000), fee("Pengembangan", "Development", 500_000)],
       notes=L("Uang pangkal = dana partisipasi orang tua. Total biaya administrasi Rp10.950.000. Info dari humas sekolah menurut sumber.", "Entry fee = parents' participation fund. Total administration cost Rp10,950,000. The source says the info came from the school's PR office."), **C())
upsert("smait-fithrah-insani-bandung-barat", name="SMAIT Fithrah Insani Bandung Barat", city="Kabupaten Bandung Barat", district="Ngamprah", religion="Islam",
       address="Jl. H. Gofur No.10, Tanimulya, Ngamprah, Kabupaten Bandung Barat",
       registrationFee=450_000, entryFee={"min": 12_000_000}, tuition={"amount": 9_500_000, "period": "semester"},
       notes=L("Uang pangkal = IPP (infaq pembangunan).", "Entry fee = IPP (building infaq)."), **C())
upsert("sma-alfa-centauri-bandung", name="SMA Alfa Centauri Bandung", city="Kota Bandung", district="Bandung Wetan",
       address="Jl. Diponegoro No.48, Citarum, Bandung Wetan, Kota Bandung",
       registrationFee=500_000, entryFee={"min": 28_000_000, "max": 37_500_000}, tuition={"amount": 1_600_000, "period": "month"},
       notes=L("DSP program A Rp39 juta diskon Rp1,5 juta = Rp37,5 juta; program B Rp29 juta diskon Rp1 juta = Rp28 juta.", "Development fee programme A Rp39M less Rp1.5M = Rp37.5M; programme B Rp29M less Rp1M = Rp28M."), **C("2023/2024", False))
upsert("sma-telkom-bandung", name="SMA Telkom Bandung", city="Kabupaten Bandung", district="Dayeuhkolot",
       address="Jl. Radio Palasari Road, Citeureup, Dayeuhkolot, Kabupaten Bandung",
       registrationFee=300_000, tuition={"amount": 480_000, "period": "month"},
       otherFees=[fee("Total biaya masuk tahun 2024", "Total entry cost (2024)", 12_970_000)], **C("2024/2025", False))
upsert("sma-plus-assalaam-bandung", name="SMA Plus Assalaam Bandung", city="Kabupaten Bandung", district="Dayeuhkolot", religion="Islam",
       address="Jl. Terusan Cibaduyut, Cangkuang Kulon, Dayeuhkolot, Kabupaten Bandung",
       registrationFee=350_000, entryFee={"min": 3_250_000},
       otherFees=[fee("Dana kreativitas", "Creativity fund", 2_800_000), fee("Seragam 4 macam", "Uniforms (4 types)", 800_000), fee("Pengembangan kurikulum 1 tahun", "Curriculum development (1 year)", 1_950_000), fee("Kegiatan ujian 1 tahun", "Exams (1 year)", 1_050_000)],
       notes=L("Uang pangkal = biaya pembangunan sekolah (bisa dicicil 10 bulan selama kelas X). Total Rp9.850.000; Rp6.600.000 dibayar di awal (Juli).", "Entry fee = school building fee (can be paid over 10 months in grade 10). Total Rp9,850,000; Rp6,600,000 due upfront (July)."), **C())
upsert("sma-daarut-tauhiid-putra-bandung", name="SMA Daarut Tauhiid Putra Bandung", city="Kabupaten Bandung Barat", district="Parongpong", religion="Islam",
       address="Jl. Cigugur Girang Pangsor, Cigugur Girang, Parongpong, Kabupaten Bandung Barat",
       entryFee={"min": 35_500_000, "max": 40_000_000}, tuition={"amount": 3_700_000, "period": "month"},
       notes=L("Program SMA 4 tahun: biaya pengembangan Rp40 juta; program 3 tahun: Rp35,5 juta. SPP Rp3,7 juta/bulan.", "4-year programme: development fee Rp40M; 3-year programme: Rp35.5M. Tuition Rp3.7M/month."), **C())
upsert("sma-daarut-tauhiid-putri-bandung", name="SMA Daarut Tauhiid Putri Bandung", city="Kota Bandung", district="Sukasari", religion="Islam",
       address="Jl. Gegerkalong Girang Isola, Sukasari, Kota Bandung",
       entryFee={"min": 35_500_000}, tuition={"amount": 3_500_000, "period": "month"}, **C())
upsert("sekolah-kuntum-cemerlang-bandung", name="Sekolah Kuntum Cemerlang Bandung", city="Kota Bandung", district="Cidadap",
       address="Jl. Cipaku Indah XI No.2, Ledeng, Cidadap, Kota Bandung",
       otherFees=[fee("Total biaya masuk (perkiraan)", "Total entry cost (approx.)", 29_350_000)],
       notes=L("Total kira-kira Rp29.350.000, belum termasuk ekskul (Rp150–225 ribu) dan katering (tidak wajib).", "About Rp29,350,000 in total, excluding extracurriculars (Rp150–225k) and catering (optional)."), **C())
upsert("sd-tunas-unggul-bandung", name="Sekolah Tunas Unggul Bandung", city="Kota Bandung", district="Mandalajati",
       entryFee={"min": 25_000_000, "max": 28_000_000},
       notes=L("SMA (Jl. Abah Sastro No.20, Pasir Impun): total biaya masuk sekitar Rp25–28 juta; diskon Rp2 juta untuk alumni dan saudara kandung.", "SMA (Jl. Abah Sastro No.20, Pasir Impun): total entry cost about Rp25–28M; Rp2M off for alumni and siblings."), **C())
upsert("sdit-insan-teladan-cileunyi", name="Sekolah Islam Terpadu Insan Teladan Cileunyi", city="Kabupaten Bandung", district="Cileunyi",
       entryFee={"min": 16_000_000}, tuition={"amount": 2_500_000, "period": "month"},
       notes=L("SMAIT khusus putra (program takhosus/tahfidz). Biaya masuk sekitar Rp16 juta. SPP sudah termasuk makan 3x sehari dan asrama.", "Boys-only SMAIT (tahfidz programme). Entry about Rp16M. Tuition includes 3 meals a day and boarding."), **C())
upsert("sma-edu-global-bandung", name="SMA Edu Global Bandung", city="Kota Bandung", district="Coblong", curriculum=["Internasional"],
       address="Jl. Ir. H. Juanda No.82, Lebakgede, Coblong, Kota Bandung",
       registrationFee=300_000, entryFee={"min": 31_000_000}, tuition={"amount": 2_100_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_600_000), fee("Uang kegiatan tahun pertama", "First-year activity fee", 4_200_000), fee(*BOOKS, 1_102_000)],
       notes=L("Kelas bilingual. Uang pangkal = DSP (bisa dicicil 4x). Kelas nasional plus: pendaftaran Rp750.000 (rincian lain tidak terbaca).", "Bilingual class. Entry fee = DSP (payable in 4 instalments). National-plus class: registration Rp750,000 (other figures not readable)."), **C())
print("ok")
