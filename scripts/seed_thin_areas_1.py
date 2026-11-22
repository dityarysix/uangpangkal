"""Thin areas, round 1.
- Data Pendidikan, "7 Harga Sekolah SD Swasta Terbaik di Cilegon" (3 Jul 2026): no year -> 2026/2027 (assumed).
- theAsianparent SD lists: Makassar (7 Jul 2022), Samarinda (8 Jul 2022) -> 2022/2023 (assumed);
  Padang (republished 12 Oct 2026, figures older than Adzkia's official 2026/27 schedule) -> 2022/2023 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
M = lambda a: {"amount": a, "period": "month"}
DP = {"title": "7 Harga Sekolah SD Swasta Terbaik di Cilegon (Data Pendidikan)", "url": "https://www.datapendidikan.com/blog/sekolah-sd-terbaik-di-cilegon/", "published": "2026-07-03"}
def tap(city, slug, pub):
    return {"title": f"Daftar SD Swasta di {city} dan Biayanya (theAsianparent)", "url": f"https://id.theasianparent.com/sd-swasta-di-{slug}", "published": pub}
MKS, SMD, PDG = tap("Makassar", "makassar", "2022-07-07"), tap("Samarinda", "samarinda", "2022-07-08"), tap("Padang", "padang", "2026-10-12")
def s(slug, name, city, district, address, source, year, religion="Islam", note=("", ""), **f):
    base = ("Dari artikel; tahun ajaran tidak disebut. Konfirmasi ke sekolah.", "From an article; academic year not stated. Confirm with the school.")
    if source is PDG:
        base = ("Artikel diterbitkan ulang Okt 2026, tetapi angkanya tampak lebih lama; tahun ajaran tidak disebut.", "Article republished Oct 2026, but the figures look older; academic year not stated.")
    import json, pathlib
    p = pathlib.Path(__file__).resolve().parent.parent / f"src/content/schools/{slug}.json"
    if p.exists():
        d = json.loads(p.read_text()); name, city = d["name"], d["city"]
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year=year, yearAssumed=True, source=source, checked=CHK,
           notes=L((note[0] + " " + base[0]).strip(), (note[1] + " " + base[1]).strip()), **f)

# Cilegon
CG, Y = "Cilegon", "2026/2027"
s("sdit-al-khairiyah-cilegon", "SDIT Al Khairiyah Cilegon", CG, "Citangkil", "Jl. KH. Enggus Arja No.1, Citangkil, Kota Cilegon", DP, Y, note=("Pendaftaran termasuk tes psikotes; SPP ditanyakan ke sekolah.", "Registration includes a psychological test; ask the school for tuition."), registrationFee=350_000)
s("sd-islam-al-azhar-40-cilegon", "SD Islam Al Azhar 40 Cilegon", CG, "Purwakarta", "Jl. KH Yasin Beji No.51, Kotabumi, Purwakarta, Kota Cilegon", DP, Y, note=("Al Azhar 40 YPKS. Hanya biaya pendaftaran yang disebut.", "Al Azhar 40 YPKS. Only the registration fee is given."), registrationFee=350_000)
s("sdit-raudhatul-jannah-cilegon", "SDIT Raudhatul Jannah Cilegon", CG, "Cibeber", "Jl. Pondok Cilegon Indah No.70, Cibeber, Kota Cilegon", DP, Y,
  note=("Uang pangkal = infaq pengembangan pendidikan; artikel menulis \"Rp3.900.00\" (dibaca Rp3.900.000).", "Entry = development donation; the article writes \"Rp3.900.00\" (read as Rp3,900,000)."),
  registrationFee=200_000, entryFee={"min": 3_900_000}, tuition=M(700_000), otherFees=[fee("Kegiatan edukatif", "Educational activities", 700_000)])
s("sdit-tahfidz-daarul-muminin-cilegon", "SDIT Tahfidz Daarul Mu'minin Cilegon", CG, "Jombang", "Jl. Mawar, Lingkungan Barokah, Jombang Wetan, Kota Cilegon", DP, Y, note=("Hanya SPP yang disebut.", "Only tuition is given."), tuition=M(425_000))
s("sd-peradaban-cilegon", "SD Peradaban Cilegon", CG, "Cibeber", "Jl. KH Abdul Latif No.08, Karangasem, Cibeber, Kota Cilegon", DP, Y, note=("Hanya SPP yang disebut.", "Only tuition is given."), tuition=M(500_000))

# Makassar
KM, Y = "Kota Makassar", "2022/2023"
s("sd-islam-al-azhar-makassar", "SD Islam Al Azhar Makassar", KM, "Rappocini", "Jl. Aroeppala / Jl. Hertasning Baru, Gunung Sari, Rappocini, Kota Makassar", MKS, Y,
  registrationFee=300_000, entryFee={"min": 15_000_000}, tuition=M(1_180_000), otherFees=[fee("Jam'iyyah", "Parents' association", 150_000), fee(*UNIFORM, 1_260_000)])
s("sit-al-biruni-mandiri-makassar", "SIT Al-Biruni Mandiri Makassar", KM, "Panakkukang", "Jl. Karantina No.4, Sinrijala, Panakkukang, Kota Makassar", MKS, Y,
  note=("Kelas reguler: kegiatan Rp7 juta/tahun, SPP Rp2,2 juta. ICP Class: kegiatan Rp8,5 juta, SPP Rp2,5 juta.", "Regular class: activities Rp7M/year, tuition Rp2.2M. ICP Class: activities Rp8.5M, tuition Rp2.5M."),
  entryFee={"min": 40_000_000}, tuition=M(2_200_000), otherFees=[fee("Kegiatan tahunan (reguler)", "Annual activities (regular)", 7_000_000), fee(*UNIFORM, 2_500_000)])
s("sekolah-islam-athirah-makassar", "Sekolah Islam Athirah Makassar", KM, None, "Athirah I: Jl. Kajaolalido No.22; Athirah II: Jl. Raya Baruga No.26, Makassar", MKS, Y,
  note=("Artikel hanya menyebut biaya masuk dan bulanan sekitar Rp23 juta.", "The article only gives entry and monthly fees of about Rp23M."), otherFees=[fee("Biaya masuk & bulanan (estimasi)", "Entry & monthly (estimate)", 23_000_000)])
s("sdit-wahdah-islamiyah-makassar", "SDIT Wahdah Islamiyah Makassar", KM, "Manggala", "Jl. Raya Baruga No.12B, Antang, Manggala, Kota Makassar", MKS, Y, entryFee={"min": 6_000_000}, tuition=M(500_000))
s("sdit-al-fatih-makassar", None, None, None, None, MKS, Y, note=("Potongan uang pangkal Rp1 juta untuk lanjutan TK B.", "Rp1M entry discount for TK B continuers."),
  registrationFee=350_000, entryFee={"min": 17_000_000}, tuition=M(1_200_000),
  otherFees=[fee("Observasi", "Observation", 350_000), fee("Seragam putra", "Uniforms (boys)", 1_275_000), fee("Seragam putri", "Uniforms (girls)", 1_375_000), fee("Buku paket", "Textbooks", 1_250_000), fee("Dana kegiatan per tahun", "Activities per year", 1_000_000), fee("Komite per tahun", "Committee per year", 250_000)])
s("al-akhyar-islamic-school-makassar", None, None, None, None, MKS, Y, note=("Uang pangkal Rp3 juta + infaq sarpras Rp10 juta. Potongan Rp1 juta (dari TK Al Akhyar), Rp500 ribu (saudara kandung).", "Entry Rp3M + facilities donation Rp10M. Rp1M off (from TK Al Akhyar), Rp500k off (sibling)."),
  entryFee={"min": 13_000_000}, tuition=M(750_000), otherFees=[fee("Infaq kegiatan per tahun", "Activities donation per year", 1_000_000)])
s("sekolah-islam-ar-raafi-makassar", None, None, None, None, MKS, Y, note=("Biaya masuk sekitar Rp2 juta.", "Entry about Rp2M."), entryFee={"min": 2_000_000}, tuition=M(400_000))

# Samarinda
KS = "Kota Samarinda"
s("sd-islam-bunga-bangsa-samarinda", "SD Islam Bunga Bangsa Samarinda", KS, None, None, SMD, Y, entryFee={"min": 17_500_000}, tuition=M(1_000_000))
s("sd-al-firdaus-islamic-school-samarinda", "SD Al Firdaus Islamic School Samarinda", KS, None, None, SMD, Y, note=("Hanya biaya pendaftaran yang disebut.", "Only the registration fee is given."), registrationFee=250_000)
s("sd-islam-tahfidz-quran-al-quds-samarinda", "SD Islam Tahfidz Quran Al Quds Samarinda", KS, "Samarinda Ulu", "Gedung Al Ishlah lt. 2, Jl. Air Hitam (samping flyover), Samarinda Ulu", SMD, Y,
  note=("Uang pangkal = infaq. Seragam Rp850–975 ribu; katering Rp10.000/hari.", "Entry = donation. Uniforms Rp850–975k; catering Rp10,000/day."),
  registrationFee=300_000, entryFee={"min": 13_000_000}, tuition=M(575_000), otherFees=[fee("Seragam (min.)", "Uniforms (min.)", 850_000), fee(*BOOKS, 537_000)])
s("sdia-unggulan-al-fatah-samarinda", "SDIA Unggulan Al Fatah Samarinda", KS, "Sambutan", "Jl. Sukses No.37, Sambutan, Kota Samarinda", SMD, Y,
  note=("Uang pangkal = jariyah gedung. Seragam Rp1,1–1,3 juta.", "Entry = building donation. Uniforms Rp1.1–1.3M."), entryFee={"min": 1_000_000}, tuition=M(100_000),
  otherFees=[fee("Seragam (min.)", "Uniforms (min.)", 1_100_000), fee(*ACTIVITY, 500_000)])

# Padang
KP = "Kota Padang"
s("sekolah-islam-adzkia-padang", None, None, None, None, PDG, Y, note=("SDIT Adzkia Kuranji. Pendaftaran Rp125.000 (internal) / Rp250.000 (eksternal). Uang bulanan minimal Rp1 juta. Qardh al-hasan Rp2 juta.", "SDIT Adzkia Kuranji. Registration Rp125,000 (internal) / Rp250,000 (external). Minimum monthly Rp1M. Qardh al-hasan Rp2M."),
  registrationFee=250_000, entryFee={"min": 7_500_000}, tuition=M(1_000_000), otherFees=[fee("Uang PBM 1 tahun", "Learning fee (1 year)", 1_500_000), fee("Perlengkapan sekolah", "School supplies", 700_000), fee("Komite", "Committee", 300_000)])
s("sdit-arafah-andalas-padang", "SDIT Arafah Andalas Padang", KP, "Padang Timur", "Jl. Kampung Terendam, Andalas, Padang Timur, Kota Padang", PDG, Y,
  note=("Artikel menyebut \"biaya pendaftaran Rp7.800.000\"; dicatat sebagai biaya masuk.", "The article says \"registration Rp7,800,000\"; recorded as the entry cost."), entryFee={"min": 7_800_000}, tuition=M(575_000))
s("sd-islam-kreatif-makkah-padang", "SD Islam Kreatif Makkah Padang", KP, "Padang Timur", "Jl. Jati 1 No.14E, Sawahan, Padang Timur, Kota Padang", PDG, Y, entryFee={"min": 8_500_000}, tuition=M(500_000), otherFees=[fee("Uang menu per bulan", "Meals per month", 350_000)])
s("sdit-dar-el-iman-padang", "SDIT Dar el-Iman Padang", KP, "Nanggalo", "Komplek Islamic Centre Dar el-Iman, Jl. Gunung Juaro, Surau Gadang, Nanggalo, Kota Padang", PDG, Y, entryFee={"min": 7_000_000})
s("sekolah-alam-ar-royyan-padang", "Sekolah Alam Ar-Royyan Padang", KP, "Lubuk Begalung", "Jl. Bhakti ABRI No.40B, Pagambiran Ampalu Nan XX, Lubuk Begalung, Kota Padang", PDG, Y,
  note=("Uang pangkal = sarana. Bisa dibayar 3 tahap; potongan sarana Rp2 juta untuk lanjutan TKIT Ar-Royyan. Modul tema Rp250 ribu dan ATK Rp225 ribu per semester.", "Entry = facilities fee. Payable in 3 stages; Rp2M off for TKIT Ar-Royyan continuers. Theme modules Rp250k and stationery Rp225k per semester."),
  registrationFee=225_000, entryFee={"min": 6_000_000}, tuition=M(350_000),
  otherFees=[fee("Seragam putra (4 stel)", "Uniforms boys (4 sets)", 1_000_000), fee("Seragam putri (4 stel)", "Uniforms girls (4 sets)", 1_200_000), fee("Uang kegiatan per tahun", "Activities per year", 1_200_000), fee("Modul Qur'an", "Qur'an module", 100_000)])
s("sdit-permata-padang", "SDIT Permata Padang", KP, "Padang Timur", "Jl. Andalas Baru No.25B, Simpang Haru, Padang Timur, Kota Padang", PDG, Y, entryFee={"min": 6_500_000}, tuition=M(350_000))
s("sd-islam-al-azhar-32-padang", "SD Islam Al-Azhar 32 Padang", KP, None, "Jl. Khatib Sulaiman No.86, Kota Padang", PDG, Y,
  note=("Uang pangkal = uang mahar. SPP reguler Rp900.000; bilingual/tahfiz Rp980.000.", "Entry = \"mahar\" fee. Tuition regular Rp900,000; bilingual/tahfiz Rp980,000."),
  registrationFee=250_000, entryFee={"min": 10_000_000}, tuition=M(900_000), otherFees=[fee("Jam'iyyah/komite per tahun", "Association/committee per year", 200_000)])
