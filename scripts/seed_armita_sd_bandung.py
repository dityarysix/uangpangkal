"""Armita Fibri (blog), "Biaya Masuk SD di Bandung [Update 2026]" — https://armitafibri.com/biaya-masuk-sd-di-bandung/
A parent's survey of Bandung-area primary schools collected over 2019–2024. Each school keeps the year the blog states
for it; where no year is stated we use 2024/2025 (the blog's own reference year) with yearAssumed. Only figures
written in the text are used (many details are in images we cannot read). Comment-section anecdotes are not used."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

SRC = {"title": "Biaya Masuk SD di Bandung [Update 2026] (blog Armita Fibri)", "url": "https://armitafibri.com/biaya-masuk-sd-di-bandung/", "published": "2026-02-15"}
CHK = "2026-11-22"
def C(year, assumed=False): return dict(level="SD", year=year, source=SRC, checked=CHK, **({"yearAssumed": True} if assumed else {}))

upsert("sdit-al-mumtaz-cileunyi", name="SDIT Al Mumtaz Cileunyi", city="Kabupaten Bandung", district="Cileunyi", religion="Islam",
       address="Jl. Pesantren No.1A, Cimekar, Cileunyi, Kabupaten Bandung",
       registrationFee=300_000, entryFee={"min": 6_000_000, "max": 9_000_000}, tuition={"amount": 450_000, "period": "month"},
       otherFees=[fee("Dana program (per tahun)", "Programme fee (per year)", 1_300_000), fee("Seragam laki-laki", "Uniforms (boys)", 800_000), fee("Seragam perempuan", "Uniforms (girls)", 1_000_000)],
       notes=L("Uang pangkal = infak bangunan; sumber mencantumkan Rp6.000.000 dan juga Rp9.000.000. Alumni TK Sukahaji diskon Rp1.000.000. Total masuk sekitar Rp11.550.000 (laki-laki) / Rp11.750.000 (perempuan).",
               "Entry fee = building infaq; the source lists both Rp6,000,000 and Rp9,000,000. TK Sukahaji alumni get Rp1,000,000 off. Total on entry about Rp11,550,000 (boys) / Rp11,750,000 (girls)."), **C("2024/2025"))
upsert("sd-plus-ar-rahmat-cileunyi", name="SD Plus Ar-Rahmat Cileunyi", city="Kabupaten Bandung", district="Cileunyi", religion="Islam",
       address="Jl. Villa Bandung Indah No.5, Cileunyi, Kabupaten Bandung",
       tuition={"amount": 400_000, "period": "month"},
       otherFees=[fee("Buku (per tahun)", "Books (per year)", 400_000), fee("Kegiatan (per semester)", "Activities (per semester)", 500_000)],
       notes=L("Uang pangkal tidak dicantumkan.", "Entry fee not listed."), **C("2024/2025"))
upsert("sdit-q-ta-hamasah-cileunyi", name="SDIT Q-Ta Hamasah Cileunyi", city="Kabupaten Bandung", district="Cileunyi", religion="Islam",
       address="Jl. Villa Bandung Indah, Kp. Manjah Beureum, Cileunyi Kulon, Kabupaten Bandung",
       registrationFee=350_000, entryFee={"min": 5_000_000}, tuition={"amount": 360_000, "period": "month"},
       otherFees=[fee("Psikotes", "Psychological test", 150_000), fee("Seragam laki-laki", "Uniforms (boys)", 800_000), fee("Seragam perempuan", "Uniforms (girls)", 875_000), fee("Buku paket", "Textbooks", 650_000)],
       notes=L("Total masuk Rp8.000.000 (laki-laki) / Rp8.075.000 (perempuan). Biaya tahunan buku dan kegiatan sekitar Rp1.850.000. Jemputan dan katering mingguan Rp50.000.",
               "Total on entry Rp8,000,000 (boys) / Rp8,075,000 (girls). Yearly books and activities about Rp1,850,000. Weekly transport and catering Rp50,000."), **C("2021/2022"))
upsert("sdit-insan-teladan-cileunyi", name="SDIT Insan Teladan Cileunyi", city="Kabupaten Bandung", district="Cileunyi", religion="Islam",
       address="Komplek DPR Blok F No.20, Cileunyi Kulon, Kabupaten Bandung",
       registrationFee=380_000, entryFee={"min": 5_897_000},
       otherFees=[fee("Pengembangan kurikulum", "Curriculum development", 1_035_000), fee("Kesiswaan", "Student affairs", 1_272_000), fee("Intrakurikuler", "Intracurricular", 379_000), fee(*UNIFORM, 1_249_000)],
       notes=L("Uang pangkal = pengembangan dan pemeliharaan sarana prasarana. Total masuk Rp9.832.000.", "Entry fee = facilities development & maintenance. Total on entry Rp9,832,000."), **C("2024/2025", True))
upsert("sd-al-masoem-jatinangor", name="SD Al Ma'soem Jatinangor", city="Kabupaten Sumedang", district="Jatinangor", religion="Islam",
       address="Jl. Raya Cipacing No.22, Jatinangor, Kabupaten Sumedang", phone="(022) 7798204", website="http://almasoem.sch.id",
       entryFee={"min": 9_400_000}, tuition={"amount": 900_000, "period": "month"},
       notes=L("Program full day. Biaya masuk Rp9.400.000 belum termasuk seragam dan buku Rp1.500.000 (total Rp10.900.000). SPP belum termasuk katering.",
               "Full-day programme. Entry Rp9,400,000 excluding uniforms and books Rp1,500,000 (total Rp10,900,000). Tuition excludes catering."), **C("2023/2024"))
upsert("sd-tunas-unggul-bandung", name="SD Tunas Unggul Bandung", city="Kota Bandung", district="Mandalajati",
       address="Jl. Pasir Impun No.94, Mandalajati, Kota Bandung", phone="(022) 87788664",
       entryFee={"min": 34_775_000}, tuition={"amount": 1_375_000, "period": "month"},
       notes=L("Rp34.775.000 adalah uang pangkal beserta biaya lain-lain.", "Rp34,775,000 is the entry fee plus other charges."), **C("2022/2023"))
upsert("sd-terpadu-krida-nusantara-bandung", name="SD Terpadu Krida Nusantara Bandung", city="Kota Bandung", district="Cibiru",
       address="Jl. Desa Cipadung, Cibiru, Kota Bandung", phone="(022) 7830509",
       registrationFee=300_000, entryFee={"min": 12_500_000}, tuition={"amount": 600_000, "period": "month"},
       notes=L("Biaya pendidikan Rp12.500.000 mencakup uang pangkal, seragam, buku, outdoor, dan SPP Juli. SPP termasuk makan siang/snack. Total masuk Rp13.400.000.",
               "Education fee Rp12,500,000 covers entry fee, uniforms, books, outdoor programme and July tuition. Tuition includes lunch/snacks. Total on entry Rp13,400,000."), **C("2024/2025", True))
upsert("sdit-imam-bukhari-jatinangor", name="SDIT Imam Bukhari Jatinangor", city="Kabupaten Sumedang", district="Jatinangor", religion="Islam",
       address="Jl. Caringin Km 20,5, Sayang, Jatinangor, Kabupaten Sumedang",
       entryFee={"min": 13_000_000, "max": 14_000_000}, tuition={"amount": 570_000, "period": "month"},
       notes=L("Total biaya masuk sekitar Rp13–14 juta. Biaya bulanan Rp570.000 tanpa jemputan, Rp820.000 dengan jemputan.", "Total on entry about Rp13–14 million. Monthly Rp570,000 without transport, Rp820,000 with transport."), **C("2022/2023"))
upsert("sd-insan-karim-cibiru", name="SD Insan Karim Cibiru", city="Kota Bandung", district="Cibiru",
       address="Jl. Pandan Wangi 10, Cibiru Wetan, Bandung",
       entryFee={"min": 7_000_000},
       notes=L("Sumber: total biaya masuk tahun 2019 \"sekitar 7 juta rupiah kurang dikit\" (perkiraan).", "Source: total entry cost in 2019 \"just under Rp7 million\" (approximate)."), **C("2019/2020"))
upsert("sd-al-azhar-cairo-bandung", name="SD Al Azhar Cairo Bandung", city="Kabupaten Bandung", district="Cileunyi", religion="Islam",
       address="Kp. Manjah Beureum, Cileunyi Wetan, Cileunyi, Kabupaten Bandung",
       entryFee={"min": 18_000_000, "max": 23_000_000},
       notes=L("Sumber: biaya masuk 2019 sekitar Rp23 juta, atau sekitar Rp18 juta dengan diskon pendaftaran awal (perkiraan).", "Source: 2019 entry cost about Rp23 million, or about Rp18 million with an early-registration discount (approximate)."), **C("2019/2020"))
upsert("sekolah-pribadi-bandung", name="Sekolah Pribadi Bandung", city="Kota Bandung", district="Cibeunying Kaler", curriculum=["Cambridge"],
       address="Jl. PHH. Mustofa No.41, Neglasari, Cibeunying Kaler, Kota Bandung",
       entryFee={"min": 45_000_000}, tuition={"amount": 5_000_000, "period": "month"},
       otherFees=[fee("Uang tahunan", "Annual fee", 14_000_000)], **C("2024/2025", True))
upsert("salman-al-farisi-bandung", name="Sekolah Salman Al Farisi Bandung", city="Kota Bandung", district="Coblong", religion="Islam",
       address="Jl. Tubagus Ismail VIII Atas, Sekeloa, Coblong, Kota Bandung",
       registrationFee=700_000, entryFee={"min": 26_000_000, "max": 28_000_000}, tuition={"amount": 1_800_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_450_000), fee("Uang kegiatan", "Activity fee", 2_806_000)],
       notes=L("Uang pangkal Rp28.000.000 (umum) / Rp26.000.000 (lulusan TK Salman Al Farisi). Total masuk Rp34.056.000 / Rp32.056.000. Diskon Rp2.000.000 jika membayar sampai 31 Januari; diskon saudara kandung Rp750.000 (SD/SMP).",
               "Entry fee Rp28,000,000 (general) / Rp26,000,000 (TK Salman Al Farisi graduates). Total on entry Rp34,056,000 / Rp32,056,000. Rp2,000,000 off if paid by 31 January; sibling discount Rp750,000 (SD/SMP)."), **C("2024/2025"))
print("ok")
