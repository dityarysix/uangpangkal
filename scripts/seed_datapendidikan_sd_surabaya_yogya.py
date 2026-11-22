"""Data Pendidikan blog lists.
- "7 Harga Sekolah SD Swasta Terbaik di Surabaya" (dated 1 Oct 2026, but the figures are undated and may be older)
  -> 2026/2027 with yearAssumed and a caution note.
- "[Daftar Lengkap] Harga SD Swasta Terbaik di Yogyakarta" / "7 Harga Sekolah SD Yogyakarta" — the text states the
  figures are for 2021/2022."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

CHK = "2026-11-22"
SBY = {"title": "7 Harga Sekolah SD Swasta Terbaik di Surabaya (Data Pendidikan)", "url": "https://www.datapendidikan.com/blog/harga-sekolah-sd-swasta-terbaik-surabaya/", "published": "2026-10-01"}
CAUTION = L("Situs tidak menyebut tahun ajaran; artikel bertanggal Oktober 2026 tetapi angkanya bisa berasal dari tahun sebelumnya (situs yang sama memakai data 2021/2022 untuk Yogyakarta). ",
            "The site does not state the academic year; the article is dated October 2026 but the figures may be from earlier years (the same site uses 2021/2022 data for Yogyakarta). ")
def cn(i="", e=""): return L(CAUTION["id"] + i, CAUTION["en"] + e)
S = dict(level="SD", year="2026/2027", yearAssumed=True, source=SBY, checked=CHK)
upsert("great-crystal-school-surabaya", name="Great Crystal School Surabaya", city="Surabaya", curriculum=["Internasional"],
       address="Jl. Raya Darmo Permai III, Puncak Permai Square, Surabaya", website="https://www.great.sch.id",
       registrationFee=3_000_000, tuition={"amount": 20_000_000, "period": "year"}, notes=cn("SPP Rp20–90 juta per tahun.", "Tuition Rp20–90 million per year."), **S)
upsert("singapore-national-academy-sidoarjo", name="Singapore National Academy (SNA) Waru", city="Sidoarjo", district="Waru", curriculum=["Internasional"],
       address="Pondok Maspion 4 Blok GH No.1-6, Waru, Sidoarjo", website="https://sna.sch.id",
       registrationFee=4_000_000, tuition={"amount": 56_000_000, "period": "year"}, notes=cn(), **S)
upsert("sampoerna-academy-surabaya", name="Sampoerna Academy Surabaya", city="Surabaya", curriculum=["Internasional"],
       address="Jl. Pakuwon Indah, Surabaya", website="https://www.sampoernaacademy.sch.id",
       registrationFee=6_000_000, tuition={"amount": 90_000_000, "period": "year"}, notes=cn(), **S)
upsert("sd-islam-al-azhar-35-surabaya", name="SD Islam Al Azhar 35 Surabaya", city="Surabaya", district="Mulyorejo", religion="Islam",
       address="Komp. Pakuwon City, Kaisari, Mulyorejo, Surabaya",
       registrationFee=350_000, entryFee={"min": 29_000_000}, tuition={"amount": 1_800_000, "period": "month"},
       otherFees=[fee("Kegiatan per tahun", "Activities per year", 2_800_000), fee(*UNIFORM, 1_390_000), fee(*BOOKS, 1_600_000),
                  fee("Dana syiar", "Syiar fund", 500_000), fee("Uang jamiyah per tahun", "Parents' association per year", 300_000)], notes=cn(), **S)
upsert("sd-kristen-petra-10-surabaya", name="SD Kristen Petra 10 Surabaya", city="Surabaya", religion="Kristen",
       address="Jl. Darmo Harapan PF/2, Tanjungsari, Surabaya",
       registrationFee=400_000, entryFee={"min": 17_000_000}, tuition={"amount": 1_050_000, "period": "month"},
       notes=cn("Uang pangkal untuk siswa dari luar TK Petra.", "Entry fee for students from outside TK Petra."), **S)
upsert("surabaya-intercultural-school", name="Surabaya Intercultural School (SIS)", city="Surabaya", district="Lakarsantri", curriculum=["Internasional"],
       address="Citra Raya, Lakarsantri, Surabaya",
       registrationFee=2_700_000, entryFee={"min": 30_000_000}, tuition={"amount": 211_000_000, "period": "year"},
       notes=cn("Sumber menulis biaya pengembangan Rp30.000.000 \"per tahun\" dan SPP \"Rp211.000.000 per tahun\" (di baris SPP per bulan).",
                "The source lists the development fee as Rp30,000,000 \"per year\" and tuition as \"Rp211,000,000 per year\" (under the monthly tuition line)."), **S)
upsert("sekolah-cikal-surabaya", name="Sekolah Cikal Surabaya", city="Surabaya", district="Sambikerep", curriculum=["IB"],
       address="Jl. Raya Lontar No.103, Lontar, Sambikerep, Surabaya", website="https://www.cikal.co.id",
       entryFee={"min": 58_800_000}, tuition={"amount": 400_000, "period": "month"},
       notes=cn("Sumber menulis biaya pengembangan Rp58.800.000 \"per tahun\" dan SPP Rp400.000 per bulan; angka SPP tampak terlalu rendah untuk sekolah ini, konfirmasi ke sekolah.",
                "The source lists the development fee as Rp58,800,000 \"per year\" and tuition as Rp400,000 per month; the tuition looks too low for this school, so confirm with the school."), **S)

YK = {"title": "Harga SD Swasta Terbaik di Yogyakarta (Data Pendidikan)", "url": "https://www.datapendidikan.com/blog/harga-sd-swasta-terbaik-di-yogyakarta/"}
Y = dict(level="SD", year="2021/2022", source=YK, checked=CHK)
upsert("sdit-luqman-al-hakim-yogyakarta", name="SDIT Luqman Al Hakim Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Islam",
       address="Jl. Timoho II Gg. Delima No.2, Umbulharjo, Yogyakarta", phone="(0274) 542928",
       registrationFee=200_000, entryFee={"min": 25_000_000}, tuition={"amount": 1_400_000, "period": "month"},
       otherFees=[fee("Biaya lainnya", "Other fees", 2_600_000)], notes=L("Total Rp29.200.000.", "Total Rp29,200,000."), **Y)
upsert("sd-muhammadiyah-condongcatur", name="SD Muhammadiyah Condongcatur", city="Sleman", district="Depok", religion="Islam",
       address="Jl. Perumnas Ring Road Utara, Gorongan, Condongcatur, Depok, Sleman",
       registrationFee=250_000, entryFee={"min": 8_000_000}, otherFees=[fee("Seragam, buku dan lainnya (putra)", "Uniforms, books etc. (boys)", 3_600_000), fee("Seragam, buku dan lainnya (putri)", "Uniforms, books etc. (girls)", 4_100_000)],
       notes=L("Uang pangkal = biaya pembangunan. Amal jariyah tiga pilihan: Rp4,5 juta, Rp5 juta, Rp5,5 juta.", "Entry fee = building fee. Voluntary donation in three tiers: Rp4.5, 5 or 5.5 million."), **Y)
upsert("global-islamic-school-jogja", name="Global Islamic School (GIS) Jogja", city="Sleman", district="Depok", religion="Islam",
       address="Jl. Selokan Mataram, Sanggrahan, Maguwoharjo, Depok, Sleman",
       registrationFee=200_000, entryFee={"min": 15_500_000}, tuition={"amount": 1_250_000, "period": "month"},
       otherFees=[fee("Kegiatan dan perlengkapan per tahun", "Activities and supplies per year", 4_375_000), fee(*UNIFORM, 1_200_000), fee("BKOMG per tahun", "Parents' association per year", 200_000)],
       notes=L("Total Rp22.025.000.", "Total Rp22,025,000."), **Y)
upsert("sekolah-bina-anak-sholeh-yogyakarta", name="Sekolah Bina Anak Sholeh (BIAS) Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Islam",
       address="Jl. Mendung Warih, Giwangan, Umbulharjo, Yogyakarta",
       entryFee={"min": 14_000_000, "max": 19_000_000}, tuition={"amount": 1_300_000, "period": "month"},
       notes=L("Biaya masuk sekitar Rp14 juta; sekitar Rp19 juta termasuk seragam dan lainnya (perkiraan).", "Entry about Rp14 million; about Rp19 million including uniforms etc. (approximate)."), **Y)
upsert("sd-al-azhar-31-sinduadi", name="SD Al-Azhar 31 Sinduadi Yogyakarta", city="Sleman", district="Mlati", religion="Islam",
       address="Jl. Padjajaran No.35A / Jl. Pogung Lor, Sinduadi, Mlati, Sleman",
       entryFee={"min": 18_500_000}, tuition={"amount": 680_000, "period": "month"}, notes=L("Angka perkiraan (\"kisaran\").", "Approximate figures."), **Y)
upsert("sd-afkaaruna-sleman", name="SD Afkaaruna Sleman", city="Sleman", district="Pakem", religion="Islam",
       address="Jl. Kaliurang Km 12,5, Pelem, Harjobinangun, Pakem, Sleman",
       entryFee={"min": 17_000_000}, tuition={"amount": 1_000_000, "period": "month"}, notes=L("Angka perkiraan (\"sekitar\").", "Approximate figures."), **Y)
upsert("sd-salman-al-farisi-2-sleman", name="SD Salman Al Farisi 2 Sleman", city="Sleman", district="Ngemplak", religion="Islam",
       address="Jetis, Wedomartani, Ngemplak, Sleman",
       entryFee={"min": 13_000_000}, tuition={"amount": 750_000, "period": "month"}, notes=L("Angka perkiraan (\"sekitar\").", "Approximate figures."), **Y)
print("ok")
