"""HaiBunda school lists (Jabodetabek). None state an academic year, so the year is
assumed from the publication date (Oct 2023 -> 2023/2024, Oct 2024 -> 2024/2025) unless
the article names one. Schools with no fee figure at all are skipped."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
def src(title, url, pub):
    return {"title": title + " (HaiBunda)", "url": url, "published": pub}
MUH = src("19 Rekomendasi SD Muhammadiyah di Jakarta Lengkap dengan Alamat dan Estimasi Biayanya", "https://www.haibunda.com/parenting/20241010182157-61-350742/19-rekomendasi-sd-muhammadiyah-di-jakarta-lengkap-dengan-alamat-dan-estimasi-biayanya", "2024-10-10")
KRI = src("15 SD Kristen Akreditasi A di Jakarta Beserta Biaya & Alamat Lengkapnya", "https://www.haibunda.com/parenting/20231005212714-61-317837/15-sd-kristen-akreditasi-a-di-jakarta-beserta-biaya-alamat-lengkapnya", "2023-10-05")
KAT = src("15 SD Katolik Akreditasi A di Jakarta Beserta Biaya dan Alamat Lengkapnya", "https://www.haibunda.com/parenting/20231009113427-61-318808/15-sd-katolik-akreditasi-a-di-jakarta-beserta-biaya-dan-alamat-lengkapnya", "2023-10-09")
BUD = src("15 SD Buddhis Akreditasi A di Jakarta Beserta Informasi Biaya & Alamat Lengkap", "https://www.haibunda.com/parenting/20231009163309-61-318317/15-sd-buddhis-akreditasi-a-di-jakarta-beserta-informasi-biaya-alamat-lengkap", "2023-10-09")
JGK = src("10 SD Swasta Jagakarsa Akreditasi Terbaik Beserta Alamat & Estimasi Biaya", "https://www.haibunda.com/parenting/20241018123131-61-350996/10-sd-swasta-jagakarsa-akreditasi-terbaik-beserta-alamat-estimasi-biaya", "2024-10-18")
DPK = src("20 SD Negeri dan Swasta Depok Akreditasi Terbaik Beserta Alamat & Estimasi Biaya", "https://www.haibunda.com/parenting/20241017112425-61-350999/20-sd-negeri-dan-swasta-depok-akreditasi-terbaik-beserta-alamat-estimasi-biaya", "2024-10-17")
NOTE = ("Estimasi biaya dari artikel; tahun ajaran tidak disebut. Konfirmasi ke sekolah.", "Estimated fees from an article; academic year not stated. Confirm with the school.")
def s(slug, name, city, district, address, source, year, religion=None, note=None, **fees):
    nid, nen = (note or ("", ""))
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year=year, yearAssumed=True,
           source=source, checked=CHK, notes=L((nid + " " + NOTE[0]).strip(), (nen + " " + NOTE[1]).strip()), **fees)
REG = lambda n: {"registrationFee": n}
Y24, Y23 = "2024/2025", "2023/2024"
JS, JT, JP, JB, JU = "Jakarta Selatan", "Jakarta Timur", "Jakarta Pusat", "Jakarta Barat", "Jakarta Utara"

# Muhammadiyah (Oct 2024)
s("sd-muhammadiyah-1-jakarta", "SD Muhammadiyah 1 Jakarta", JP, "Kemayoran", "Jl. Garuda No.33, Gunung Sahari Selatan, Kemayoran, Jakarta Pusat", MUH, Y24, "Islam", ("Biaya formulir pendaftaran.", "Registration form fee."), **REG(350_000))
s("sd-muhammadiyah-2-jakarta", "SD Muhammadiyah 2 Jakarta", JP, "Senen", "Jl. Kramat Raya No.49, Senen, Jakarta Pusat", MUH, Y24, "Islam", ("Pendaftaran Rp200.000 (dari luar) / Rp150.000 (dari dalam).", "Registration Rp200,000 (external) / Rp150,000 (internal)."), **REG(200_000))
s("sds-muhammadiyah-8-jakarta", "SDS Muhammadiyah 8 Jakarta", JT, "Duren Sawit", "Jl. Bunga Rampai X, Malaka Jaya, Duren Sawit, Jakarta Timur", MUH, Y24, "Islam", None,
  registrationFee=150_000, otherFees=[fee("Tes pemetaan dan kematangan", "Placement & readiness test", 400_000)])
s("sd-muhammadiyah-24-jakarta", "SD Muhammadiyah 24 Jakarta", JT, "Pulo Gadung", "Jl. Balai Pustaka No.2, Rawamangun, Pulo Gadung, Jakarta Timur", MUH, Y24, "Islam", None, **REG(300_000))
s("sds-muhammadiyah-23-jakarta", "SDS Muhammadiyah 23 Jakarta", JT, "Matraman", "Jl. Rambutan No.4, Utan Kayu Utara, Matraman, Jakarta Timur", MUH, Y24, "Islam", None,
  registrationFee=150_000, entryFee={"min": 5_000_000}, tuition={"amount": 400_000, "period": "month"},
  otherFees=[fee("Kegiatan 1 tahun", "Activities (1 year)", 800_000), fee("Infaq", "Donation", 250_000), fee("Seragam putra", "Uniforms (boys)", 770_000), fee("Seragam putri", "Uniforms (girls)", 950_000), fee(*BOOKS, 450_000)])
s("sd-muhammadiyah-5-jakarta", "SD Muhammadiyah 5 Jakarta", JS, "Kebayoran Baru", "Jl. Limau I-II-III Blok B, Kramat Pela, Kebayoran Baru, Jakarta Selatan", MUH, Y24, "Islam",
  ("Uang pangkal = uang pengembangan pendidikan.", "Entry fee = education development fee."),
  registrationFee=400_000, entryFee={"min": 18_682_500}, tuition={"amount": 1_000_000, "period": "month"}, otherFees=[fee(*UNIFORM, 1_817_500), fee(*BOOKS, 1_500_000)])
s("sd-al-bayyinah-muhammadiyah-jakarta", "SD Al Bayyinah Muhammadiyah", JS, "Jagakarsa", "Jl. RM. Kahfi II No.78, Cipedak, Jagakarsa, Jakarta Selatan", MUH, Y24, "Islam",
  ("Biaya PPDB gelombang 1 Rp12.200.000, gelombang 2 Rp14.000.000.", "Admission package wave 1 Rp12,200,000, wave 2 Rp14,000,000."), registrationFee=300_000, entryFee={"min": 12_200_000, "max": 14_000_000})
upsert("sdi-muhammadiyah-28-jakarta", name="SDI Muhammadiyah 28 Jakarta", city=JS, district="Kebayoran Lama", address="Jl. Panjang No.8, Cipulir, Kebayoran Lama, Jakarta Selatan", religion="Islam",
       level="SD", year="2025/2026", source=MUH, checked=CHK, registrationFee=100_000, entryFee={"min": 12_000_000},
       notes=L("Biaya PPDB 2025/2026 Rp12.000.000 (paket masuk). Estimasi dari artikel.", "2025/2026 admission package Rp12,000,000. Estimate from an article."))
s("sds-muhammadiyah-6-jakarta", "SDS Muhammadiyah 6 Jakarta", JS, "Tebet", "Jl. Tebet Timur Raya No.565, Tebet Timur, Jakarta Selatan", MUH, Y24, "Islam", ("Biaya formulir pendaftaran.", "Registration form fee."), **REG(500_000))

# Kristen (Oct 2023)
s("sd-bukit-sion-jakarta", "SD Swasta Bukit Sion", JB, "Kembangan", "Jl. Meruya Ilir Raya No.114, Srengseng, Kembangan, Jakarta Barat", KRI, Y23, "Kristen", None, **REG(500_000))
s("sd-kalam-kudus-3-jakarta", "SD Kalam Kudus III Jakarta", JB, "Cengkareng", "Komplek Perumahan Kosambi Baru Blok D4/1, Cengkareng, Jakarta Barat", KRI, Y23, "Kristen",
  ("Artikel hanya menyebut \"estimasi biaya Rp7.000.000\" tanpa rincian.", "The article only gives an \"estimated cost of Rp7,000,000\" without a breakdown."), otherFees=[fee("Estimasi biaya (tidak dirinci)", "Estimated cost (not itemised)", 7_000_000)])
s("sd-kristen-ora-et-labora-jakarta", "SD Kristen Ora Et Labora", JS, "Kebayoran Baru", "Jl. Panglima Polim I No.32a, Melawai, Kebayoran Baru, Jakarta Selatan", KRI, Y23, "Kristen",
  ("Artikel hanya menyebut \"estimasi biaya Rp25.500.000\" tanpa rincian.", "The article only gives an \"estimated cost of Rp25,500,000\" without a breakdown."), otherFees=[fee("Estimasi biaya (tidak dirinci)", "Estimated cost (not itemised)", 25_500_000)])
s("sdk-4-bpk-penabur-jakarta", "SDK 4 BPK Penabur Jakarta", JT, "Duren Sawit", "Jl. Tarum Barat Blok KK, Pondok Bambu, Duren Sawit, Jakarta Timur", KRI, Y23, "Kristen",
  ("Uang pangkal = uang gedung.", "Entry fee = building fee."), registrationFee=350_000, entryFee={"min": 21_900_000}, tuition={"amount": 2_850_000, "period": "month"})

# Katolik (Oct 2023)
for slug, name, city, dist, addr, reg in [
    ("sds-santo-yoseph-jakarta", "SDS Santo Yoseph Jakarta", JP, "Sawah Besar", "Jl. Dwiwarna Raya No.1-3, Kartini, Sawah Besar, Jakarta Pusat", 150_000),
    ("sds-santo-vincentius-jakarta", "SDS Santo Vincentius Jakarta", JT, "Jatinegara", "Jl. Otto Iskandardinata No.76, Bidara Cina, Jatinegara, Jakarta Timur", 200_000),
    ("sd-santo-paulus-jakarta", "SD Santo Paulus Jakarta", JU, "Tanjung Priok", "Jl. Danau Agung 13 No.4, Sunter Agung, Tanjung Priok, Jakarta Utara", 50_000),
    ("sd-bunda-hati-kudus-jakarta", "SD Bunda Hati Kudus Jakarta", JB, "Grogol Petamburan", "Jl. Rahayu No.22, Jelambar, Grogol Petamburan, Jakarta Barat", 150_000),
    ("sd-tarakanita-3-jakarta", "SD Tarakanita 3 Jakarta", JS, "Kebayoran Lama", "Jl. Juraganan Raya No.1, Grogol Utara, Kebayoran Lama, Jakarta Selatan", 150_000),
    ("sd-don-bosco-1-jakarta", "SD Don Bosco I Jakarta", JT, "Pulo Gadung", "Jl. Pulomas Barat No.5, Kayu Putih, Pulo Gadung, Jakarta Timur", 100_000),
]:
    s(slug, name, city, dist, addr, KAT, Y23, "Katolik", ("Hanya biaya pendaftaran yang disebut.", "Only the registration fee is given."), **REG(reg))
s("sekolah-mahabodhi-vidya-jakarta", "Sekolah Mahabodhi Vidya Jakarta", JB, "Kalideres", "Jl. Palem Anggur Kav. 8, Pegadungan, Kalideres, Jakarta Barat", BUD, Y23, "Buddha", ("Hanya biaya pendaftaran yang disebut.", "Only the registration fee is given."), **REG(200_000))

# Jagakarsa (Oct 2024)
s("sds-cita-buana-jakarta", "SDS Cita Buana", JS, "Jagakarsa", "Jl. Paso No.84, Jagakarsa, Jakarta Selatan", JGK, Y24, None,
  ("Uang pendaftaran Rp500.000–Rp750.000. Kurikulum Merdeka + IPC.", "Registration Rp500,000–Rp750,000. Kurikulum Merdeka + IPC."), **REG(500_000))
s("sdi-al-azhar-syuhada-jagakarsa", "SDI Al Azhar Syuhada Jagakarsa", JS, "Jagakarsa", "Jl. Jagakarsa Raya No.38, Jakarta Selatan", JGK, Y24, "Islam",
  ("Uang pangkal Rp9.800.000 + uang pembangunan Rp10.000.000 (dari luar) / Rp7.000.000 (dari TK Al Azhar Syuhada).", "Entry fee Rp9,800,000 + building fee Rp10,000,000 (external) / Rp7,000,000 (from TK Al Azhar Syuhada)."),
  registrationFee=200_000, entryFee={"min": 16_800_000, "max": 19_800_000})
s("sds-smart-school-jagakarsa", "SDS Smart School Jagakarsa", JS, "Jagakarsa", "Jl. Kecapi No.49, Jagakarsa, Jakarta Selatan", JGK, Y24, None,
  ("Artikel hanya menyebut \"biaya sekolah Rp36.570.250\" tanpa rincian.", "The article only gives \"school fees Rp36,570,250\" without a breakdown."), otherFees=[fee("Biaya sekolah (tidak dirinci)", "School fees (not itemised)", 36_570_250)])
s("sd-citra-alam-jakarta", "SD Citra Alam", JS, "Jagakarsa", "Jl. Damai No.54, Ciganjur, Jagakarsa, Jakarta Selatan", JGK, Y24, "Islam",
  ("Uang pangkal = investasi pendidikan. Artikel menulis SPP \"Rp1.850.00\" (dibaca Rp1.850.000).", "Entry fee = education investment. The article writes tuition as \"Rp1.850.00\" (read as Rp1,850,000)."),
  registrationFee=700_000, entryFee={"min": 30_000_000}, tuition={"amount": 1_850_000, "period": "month"}, otherFees=[fee("Kegiatan sekolah", "School activities", 4_000_000), fee(*UNIFORM, 550_000)])
s("sdit-al-biruni-jakarta", "SDIT Al Biruni Jakarta", JS, "Jagakarsa", "Gg. Kancil I No.43, Lenteng Agung, Jagakarsa, Jakarta Selatan", JGK, Y24, "Islam", ("Hanya biaya formulir yang disebut.", "Only the form fee is given."), **REG(300_000))

# Depok (Oct 2024)
s("sdit-al-haraki-depok", "SDIT Al-Haraki Depok", "Depok", "Pancoran Mas", "Jl. Belimbing III No.1-2, Pancoran Mas, Depok", DPK, Y24, "Islam",
  ("Pendaftaran Rp600.000 (non-Haraki Preschool) / Rp400.000 (dari Haraki Preschool).", "Registration Rp600,000 (external) / Rp400,000 (from Haraki Preschool)."), **REG(600_000))
s("al-fauzien-islamic-school-depok", "Al Fauzien Islamic School Depok", "Depok", "Pancoran Mas", "Blok V Pesona Depok Estate, Jl. Margonda Raya No.12, Pancoran Mas, Depok", DPK, Y24, "Islam", None,
  registrationFee=500_000, entryFee={"min": 27_100_000}, tuition={"amount": 1_385_000, "period": "month"},
  otherFees=[fee("Jamiyyah", "Parents' association", 100_000), fee(*ACTIVITY, 1_335_000), fee("Perlengkapan", "Supplies", 993_000), fee(*UNIFORM, 1_800_000), fee("Kesehatan", "Health", 95_000)])
s("sd-dian-didaktika-cinere", "SD Dian Didaktika Cinere", "Depok", "Cinere", "Jl. Rajawali Blok F No.10 & 16, Cinere, Depok", DPK, Y24, "Islam", None,
  registrationFee=500_000, entryFee={"min": 30_750_000}, tuition={"amount": 2_450_000, "period": "month"},
  otherFees=[fee(*UNIFORM, 1_600_000), fee(*BOOKS, 1_300_000), fee("Kegiatan tahunan", "Annual activities", 3_500_000), fee("Iuran bulanan", "Monthly levy", 20_000)])
s("sds-cakra-buana-depok", "SDS Cakra Buana Depok", "Depok", "Pancoran Mas", "Jl. Raya Sawangan No.91, Pancoran Mas, Depok", DPK, Y24, None,
  ("Uang pangkal normal Rp35.000.000; early bird Rp26.000.000.", "Entry fee Rp35,000,000 normal; Rp26,000,000 early bird."), entryFee={"min": 26_000_000, "max": 35_000_000}, tuition={"amount": 2_750_000, "period": "month"})
