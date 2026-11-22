"""Jakarta lists, round 2.
- Orami "Rekomendasi SDIT di Jakarta" (30 Apr 2025): no year -> 2025/2026 (assumed).
- Gebrak.id, "Segini Kisaran Biaya Masuk SD-SD Swasta Islam di Jakarta Selatan" (2 Dec 2025): form periods Sep 2025–Jun 2026 -> 2026/2027 (assumed).
- HaiBunda, "Biaya Masuk SD Swasta di Jakarta Timur" (1 Nov 2021): -> 2022/2023 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
ORS = {"title": "Rekomendasi SDIT di Jakarta (Orami)", "url": "https://www.orami.co.id/magazine/rekomendasi-sdit-di-jakarta", "published": "2025-04-30"}
GEB = {"title": "Orang Tua Sebaiknya Tahu, Segini Kisaran Biaya Masuk SD-SD Swasta Islam di Jakarta Selatan (Gebrak.id)", "url": "https://www.gebrak.id/2025/12/orang-tua-sebaiknya-tahu-segini-kisaran-biaya-masuk-sd-sd-swasta-islam-di-jakarta-selatan.html", "published": "2025-12-02"}
HBT = {"title": "Biaya Masuk SD Swasta di Jakarta Timur, Catat Bun (HaiBunda)", "url": "https://www.haibunda.com/parenting/20211101170245-61-249940/biaya-masuk-sd-swasta-di-jakarta-timur-catat-bun", "published": "2021-11-01"}
def s(slug, name, city, district, address, source, year, note=None, religion="Islam", **f):
    base = {ORS["url"]: ("Perkiraan dari artikel; tahun ajaran tidak disebut.", "Approximate figures from an article; academic year not stated."),
            GEB["url"]: ("Dari artikel (berbagai sumber); tahun ajaran diasumsikan dari periode formulir Sep 2025–Jun 2026.", "From an article (various sources); year assumed from the Sep 2025–Jun 2026 form periods."),
            HBT["url"]: ("Dari artikel 2021; kemungkinan sudah berubah.", "From a 2021 article; likely outdated.")}[source["url"]]
    nid, nen = note or ("", "")
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year=year, yearAssumed=True, source=source, checked=CHK,
           notes=L((nid + " " + base[0]).strip(), (nen + " " + base[1]).strip()), **f)
M = lambda a: {"amount": a, "period": "month"}
JS, JT, JP, JB, JU = "Jakarta Selatan", "Jakarta Timur", "Jakarta Pusat", "Jakarta Barat", "Jakarta Utara"

# Orami SDIT (2025)
s("sdit-ibnu-sina-jakarta", "SDIT Ibnu Sina Jakarta", JT, "Duren Sawit", "Jl. Madrasah II No.10, Duren Sawit, Jakarta Timur", ORS, "2025/2026",
  ("Pendaftaran termasuk observasi. Pindahan kelas 2–3 Rp21.850.000, kelas 4–6 Rp19.850.000, SPP pindahan Rp900.000.", "Registration includes observation. Transfers grades 2–3 Rp21,850,000, grades 4–6 Rp19,850,000, transfer tuition Rp900,000."),
  registrationFee=500_000, entryFee={"min": 21_850_000}, tuition=M(1_000_000), otherFees=[fee("POMG per tahun", "Parents' association per year", 120_000)])
s("sdit-darul-athfal-jakarta", "SDIT Darul Athfal Jakarta", JB, "Kebon Jeruk", "Jl. Anggrek Cakra No.24, Kebon Jeruk, Jakarta Barat", ORS, "2025/2026", ("Kisaran biaya masuk.", "Approximate entry cost."), entryFee={"min": 25_700_000})
s("sdit-almaka-jakarta", "SDIT Almaka Jakarta", JB, "Kalideres", "Jl. Peta Selatan No.2, Kalideres, Jakarta Barat", ORS, "2025/2026", ("Hanya biaya formulir yang disebut.", "Only the form fee is given."), registrationFee=350_000)
s("sdit-al-huda-kelapa-gading", "SDIT Al-Huda Kelapa Gading", JU, "Kelapa Gading", "Jl. Musik Raya No.2 Blok Z, Pegangsaan Dua, Kelapa Gading, Jakarta Utara", ORS, "2025/2026",
  ("Uang pangkal = dana sumbangan pendidikan.", "Entry fee = education contribution."), registrationFee=300_000, entryFee={"min": 13_000_000}, tuition=M(1_200_000),
  otherFees=[fee("Seragam putra", "Uniforms (boys)", 2_200_000), fee("Seragam putri", "Uniforms (girls)", 2_500_000), fee("Buku dan modul", "Books and modules", 1_500_000), fee("UKM dan operasional per tahun", "Activities & operations per year", 3_200_000)])
s("sdit-al-mubarak-jakarta", "SDIT Al Mubarak Jakarta", JP, "Cempaka Putih", "Jl. Pramuka Sari III No.24, Rawasari, Jakarta Pusat", ORS, "2025/2026", None, registrationFee=300_000, entryFee={"min": 12_000_000}, tuition=M(650_000))
s("sdit-kaffah-islamic-school-senen", "SDIT Kaffah Islamic School", JP, "Senen", "Jl. Pramuka 16 No.549A, Paseban, Senen, Jakarta Pusat", ORS, "2025/2026", ("Formulir termasuk psikotes.", "Form fee includes psychological test."),
  registrationFee=300_000, entryFee={"min": 8_000_000}, tuition=M(400_000))

# Gebrak (Dec 2025)
Y = "2026/2027"
s("darsyafii-islamic-school-jakarta", "Darsyafii Islamic School", JS, "Pasar Minggu", "Jl. Buncit Raya, Pasar Minggu, Jakarta Selatan", GEB, Y, None,
  registrationFee=1_200_000, entryFee={"min": 50_000_000}, tuition=M(4_200_000), otherFees=[fee("Annual fee", "Annual fee", 6_000_000)])
s("sd-al-ikhlas-cipete", "SD Al-Ikhlas Cipete", JS, "Cilandak", "Jl. Cipete II, Cipete Selatan, Cilandak, Jakarta Selatan", GEB, Y,
  ("Uang pangkal Rp35.000.000 (dari TK Islam Al-Ikhlas) / Rp38.000.000 (TK luar).", "Entry fee Rp35,000,000 (from TK Islam Al-Ikhlas) / Rp38,000,000 (external)."),
  registrationFee=450_000, entryFee={"min": 35_000_000, "max": 38_000_000}, tuition=M(2_400_000))
s("sd-islam-al-azhar-4-kebayoran-lama", "SD Islam Al Azhar 4 Kebayoran Lama", JS, "Kebayoran Lama", "Jl. Ciputat Raya No.5A, Kebayoran Lama, Jakarta Selatan", GEB, Y,
  ("Formulir Rp400.000 (Sep–Des 2025), Rp450.000 (Jan–Mar 2026), Rp500.000 (Apr–Jun 2026).", "Form Rp400,000 (Sep–Dec 2025), Rp450,000 (Jan–Mar 2026), Rp500,000 (Apr–Jun 2026)."),
  registrationFee=400_000, entryFee={"min": 25_500_000}, tuition=M(1_500_000), otherFees=[fee("Iuran jam'iyyah per tahun", "Parents' association per year", 400_000), fee("Iuran Tilawati per tahun", "Tilawati Qur'an programme per year", 900_000)])
s("green-montessori-school-jakarta", "Green Montessori School", JS, "Pancoran", "Jl. Duren Tiga Raya No.133, Duren Tiga, Pancoran, Jakarta Selatan", GEB, Y,
  ("Uang pangkal = educational development contribution. Termly fee kelas 1–3 Rp16.500.000, kelas 4–6 Rp19.800.000; yearly fee Rp7.000.000 / Rp8.400.000.", "Entry = educational development contribution. Termly fee grades 1–3 Rp16,500,000, grades 4–6 Rp19,800,000; yearly fee Rp7,000,000 / Rp8,400,000."),
  religion=None, entryFee={"min": 72_500_000}, tuition={"amount": 16_500_000, "period": "quarter"}, otherFees=[fee("Booking fee", "Booking fee", 26_000_000), fee("Yearly fee (kelas 1–3)", "Yearly fee (grades 1–3)", 7_000_000)])
s("dwi-matra-islamic-elementary-school", "Dwi Matra Islamic Elementary School", JS, "Cilandak", "Jl. M.P.R. II Dalam No.30A, Cilandak Barat, Jakarta Selatan", GEB, Y,
  ("Uang pangkal Rp32.000.000 (dari TK Dwi Matra) / Rp36.000.000 (TK luar).", "Entry fee Rp32,000,000 (from TK Dwi Matra) / Rp36,000,000 (external)."),
  entryFee={"min": 32_000_000, "max": 36_000_000}, tuition=M(2_000_000), otherFees=[fee("Booking fee", "Booking fee", 2_500_000)])
s("madina-islamic-school-tebet", "Madina Islamic School Tebet", JS, "Tebet", "Jl. Tebet Dalam IV, Tebet, Jakarta Selatan", GEB, Y,
  ("Uang tahunan Rp8.741.125 (putra) / Rp9.041.125 (putri).", "Annual fee Rp8,741,125 (boys) / Rp9,041,125 (girls)."),
  registrationFee=1_000_000, entryFee={"min": 45_500_000}, tuition=M(3_800_000), otherFees=[fee("Uang tahunan (putra)", "Annual fee (boys)", 8_741_125)])
s("sd-islam-al-azhar-2-pasar-minggu", "SD Islam Al Azhar 2 Pasar Minggu", JS, "Pasar Minggu", None, GEB, Y, ("Kelas reguler.", "Regular class."),
  registrationFee=550_000, entryFee={"min": 35_500_000}, tuition=M(1_775_000))

# HaiBunda Jakarta Timur (2021)
Y21 = "2022/2023"
s("jakarta-islamic-school-cipinang", "Jakarta Islamic School (JIS) Cipinang Melayu", JT, "Makasar", "Jl. Manunggal I No.17, Komplek Kodam, Cipinang Melayu, Makasar, Jakarta Timur", HBT, Y21,
  ("Uang pangkal sudah termasuk uang kegiatan dan buku.", "Entry fee includes activities and books."), entryFee={"min": 27_500_000}, tuition=M(2_600_000), otherFees=[fee("Daftar ulang per tahun", "Annual re-registration", 3_500_000)])
s("kids-republic-jakarta", "Kids Republic", JT, "Jatinegara", "Jl. Cipinang Bali I No.5A, Cipinang Muara, Jatinegara, Jakarta Timur", HBT, Y21, ("Kegiatan tahunan sudah termasuk buku.", "Annual activities include books."),
  religion=None, registrationFee=650_000, entryFee={"min": 28_000_000}, tuition=M(2_250_000), otherFees=[fee(*UNIFORM, 1_500_000), fee("Kegiatan tahunan", "Annual activities", 4_000_000)])
