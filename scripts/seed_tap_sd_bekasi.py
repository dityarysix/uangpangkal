"""theAsianparent, "16 SD Swasta di Bekasi, Lengkap dengan Kisaran Biaya Sekolahnya" (updated 12 Aug 2026).
No academic year stated -> 2026/2027, yearAssumed, with a caution note (the list may carry older figures)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

SRC = {"title": "16 SD Swasta di Bekasi, Lengkap dengan Kisaran Biaya Sekolahnya (theAsianparent)", "url": "https://id.theasianparent.com/sd-swasta-di-bekasi", "published": "2026-08-12"}
C = dict(city="Kota Bekasi", level="SD", year="2026/2027", yearAssumed=True, source=SRC, checked="2026-11-22")
CAU = ("Sumber tidak menyebut tahun ajaran (artikel diperbarui Agustus 2026); angka bisa berasal dari tahun sebelumnya. ",
       "The source does not state the academic year (article updated August 2026); figures may be from earlier years. ")
def n(i="", e=""): return L(CAU[0] + i, CAU[1] + e)

upsert("sd-islam-al-azhar-44-summarecon-bekasi", name="SD Islam Al-Azhar 44 Summarecon Bekasi", registrationFee=400_000, entryFee={"min": 33_000_000},
       tuition={"amount": 1_950_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_550_000), fee(*BOOKS, 1_750_000), fee("Alat tulis", "Stationery", 750_000), fee("Iuran jamiyah", "Parents' association", 350_000)],
       notes=n("Uang pangkal = uang gedung / biaya pengembangan pendidikan.", "Entry fee = building / education development fee."), **C)
upsert("al-ihsan-islamic-school-bekasi", name="Al Ihsan Islamic School Bekasi", district="Bekasi Selatan", religion="Islam", address="Jaka Setia, Bekasi Selatan",
       registrationFee=350_000, entryFee={"min": 18_500_000}, tuition={"amount": 950_000, "period": "month"},
       otherFees=[fee("Dana kegiatan belajar mengajar", "Teaching & learning fund", 5_000_000)], notes=n(), **C)
upsert("salsabila-islamic-school-bekasi", name="Salsabila Islamic School Bekasi", district="Bekasi Timur", religion="Islam", address="Jl. Ki Mangunsarkoro 30, Bekasi Jaya, Bekasi Timur",
       registrationFee=400_000, entryFee={"min": 14_500_000},
       otherFees=[fee("Observasi & psikotes", "Observation & psych test", 350_000), fee("Administrasi pendidikan per tahun", "Education administration per year", 7_200_000),
                  fee("Iuran komite per tahun", "Committee per year", 250_000), fee("Infaq pendidikan", "Education infaq", 500_000)], notes=n(), **C)
upsert("sekolah-alam-bekasi", name="Sekolah Alam Bekasi", district="Jatisampurna", entryFee={"min": 20_000_000}, tuition={"amount": 950_000, "period": "month"},
       otherFees=[fee("Biaya program pembelajaran", "Learning programme fee", 3_500_000)], notes=n("Disebut juga SD Alam Bekasi (SASI).", "Also called SD Alam Bekasi (SASI)."), **C)
upsert("sdit-al-ikhlas-bekasi", name="SDIT Al Ikhlas Bekasi", district="Bekasi Selatan", religion="Islam", address="Perum Masnaga, Jl. Nakula 6C, Jaka Setia, Bekasi Selatan",
       entryFee={"min": 12_000_000}, tuition={"amount": 550_000, "period": "month"}, notes=n(), **C)
upsert("islamic-green-school-bekasi", name="Islamic Green School Bekasi", district="Mustikajaya", religion="Islam", address="Jl. Cipete Raya No.113, Mustikasari, Mustikajaya, Kota Bekasi",
       entryFee={"min": 10_000_000, "max": 17_000_000}, tuition={"amount": 1_000_000, "period": "month"},
       notes=n("Reguler: uang pangkal Rp10 juta, SPP Rp1 juta. Siswa berkebutuhan khusus: Rp17 juta, SPP Rp2,5–3,5 juta.", "Regular: entry Rp10M, tuition Rp1M. Special-needs students: Rp17M, tuition Rp2.5–3.5M."), **C)
upsert("sdit-global-insan-madani-bekasi", name="SDIT Global Insan Madani Bekasi", religion="Islam", address="Jl. Sumur Binong 29, Kota Bekasi",
       registrationFee=250_000, entryFee={"min": 4_200_000}, tuition={"amount": 495_000, "period": "month"},
       otherFees=[fee("Pengembangan SDM", "Staff development", 270_000), fee("Kesehatan siswa", "Student health", 100_000), fee("Seragam 6 pasang", "Uniforms (6 sets)", 1_200_000),
                  fee("Buku paket satu tahun", "Textbooks (1 year)", 1_400_000), fee("Kegiatan satu tahun", "Activities (1 year)", 1_850_000)],
       notes=n("SPP termasuk iuran komite.", "Tuition includes the committee fee."), **C)
upsert("sd-al-azhar-9-kemang-pratama-bekasi", name="SD Al Azhar 9 Kemang Pratama Bekasi", district="Rawalumbu", religion="Islam",
       address="Perumahan Kemang Pratama, Jl. Mitra / Jl. Duta Raya, Bojong Rawalumbu, Rawalumbu, Kota Bekasi",
       registrationFee=350_000, entryFee={"min": 32_000_000}, tuition={"amount": 1_700_000, "period": "month"}, notes=n(), **C)
upsert("sdit-thariq-bin-ziyad-bekasi", name="SDIT Thariq Bin Ziyad Bekasi", district="Rawalumbu", religion="Islam",
       address="Perum Pondok Hijau Permai, Jl. Raya Pd. Hijau Permai No.23, Pengasinan, Rawalumbu, Kota Bekasi",
       registrationFee=300_000, entryFee={"min": 11_850_000}, tuition={"amount": 850_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_800_000), fee("Paket pengembangan kompetensi & buku", "Competency development & books", 3_140_000)], notes=n(), **C)
upsert("sd-advent-bekasi", name="SD Advent Bekasi", religion="Kristen", address="Jl. Sersan Aswan 3, Margahayu, Bekasi",
       registrationFee=175_000, entryFee={"min": 4_000_000}, tuition={"amount": 550_000, "period": "month"},
       notes=n("SPP termasuk biaya kegiatan.", "Tuition includes activities."), **C)
upsert("sd-strada-budi-luhur-bekasi", name="SD Strada Budi Luhur Bekasi", district="Bekasi Timur", religion="Katolik", address="Jl. Persikasi 164, Margahayu, Bekasi Timur",
       registrationFee=50_000, notes=n("Pendaftaran Rp50.000 untuk calon siswa dari luar sekolah Strada (gratis dari sekolah Strada). Uang pangkal dan SPP ditentukan lewat wawancara keuangan.",
                                       "Registration Rp50,000 for applicants from outside Strada schools (free for Strada feeders). Entry fee and tuition are set at a financial interview."), **C)
upsert("global-prestasi-school-bekasi", name="Global Prestasi School Bekasi", registrationFee=600_000, entryFee={"min": 25_000_000}, tuition={"amount": 2_800_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_500_000), fee("Buku (mulai)", "Books (from)", 2_500_000), fee("Biaya aktivitas", "Activity fee", 2_800_000)],
       notes=n("Angka ini berbeda jauh dengan sumber GoBekasi (uang pangkal Rp60 juta untuk 6 tahun, SPP Rp12,9 juta per 3 bulan); konfirmasi ke sekolah.",
               "These figures differ a lot from the GoBekasi source (entry Rp60M for 6 years, tuition Rp12.9M per quarter); confirm with the school."), **C)
upsert("sekolah-victory-plus-bekasi", name="Sekolah Victory Plus Bekasi", registrationFee=500_000, entryFee={"min": 52_500_000}, tuition={"amount": 44_700_000, "period": "year"},
       notes=n("SPP per tahun sudah termasuk biaya kegiatan dan lain-lain.", "Annual tuition includes activities etc."), **C)
upsert("sd-kinderfield-bekasi", name="SD Kinderfield Bekasi", district="Rawalumbu", address="Jl. Caringin Raya 88, Bojong Menteng, Rawalumbu, Kota Bekasi",
       entryFee={"min": 38_500_000}, tuition={"amount": 2_600_000, "period": "month"}, notes=n(), **C)
upsert("binus-school-bekasi", name="BINUS School Bekasi", address="Jl. Saraswati No.1, Bumiwedari, Vida, Kota Bekasi",
       registrationFee=300_000, entryFee={"min": 23_000_000, "max": 45_000_000}, tuition={"amount": 2_800_000, "period": "month"}, notes=n(), **C)
upsert("nassa-school-bekasi", name="Nassa School Bekasi", district="Pondok Melati", address="Jl. Bojong Nangka II No.38, Jatirahayu, Pondok Melati, Kota Bekasi",
       registrationFee=500_000, entryFee={"min": 6_300_000}, tuition={"amount": 472_500, "period": "month"}, notes=n(), **C)
print("ok")
