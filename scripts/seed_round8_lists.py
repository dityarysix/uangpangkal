"""Round 8 lists.
- SobatSekolah, "Cek Biaya Sekolah di Depok, dari Termurah sampai Termahal" (23 Apr 2024): -> 2024/2025 (assumed; one school's waves Sep 2023–Apr 2024).
- Nakita, "Biaya Masuk SD Swasta Semarang" (26 Mar 2024): -> 2024/2025 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
SOB = {"title": "Cek Biaya Sekolah di Depok, dari Termurah sampai Termahal (SobatSekolah)", "url": "https://sobatsekolah.com/pendidikan/biaya-sekolah-di-depok/", "published": "2024-04-23"}
NAK = {"title": "Biaya Masuk SD Swasta Semarang, Tentukan Pilihan Terbaik untuk Anak! (Nakita)", "url": "https://nakita.grid.id/read/024050247/biaya-masuk-sd-swasta-semarang-tentukan-pilihan-terbaik-untuk-anak?page=all", "published": "2024-03-26"}
N = ("Dari artikel; tahun ajaran tidak disebut.", "From an article; academic year not stated.")
M = lambda a: {"amount": a, "period": "month"}
def s(slug, name, city, district, address, source, note=("", ""), religion="Islam", level="SD", **f):
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level=level, year="2024/2025", yearAssumed=True, source=source, checked=CHK,
           notes=L((note[0] + " " + N[0]).strip(), (note[1] + " " + N[1]).strip()), **f)
D = "Depok"
s("sekolah-al-irsyad-al-islamiyyah-depok", "Sekolah Al Irsyad Al Islamiyyah Depok", D, "Sukmajaya", "Jl. Lesung Raya No.290, Abadijaya, Sukmajaya, Depok", SOB, ("Uang pangkal = biaya awal pengembangan.", "Entry = initial development fee."),
  registrationFee=150_000, entryFee={"min": 13_000_000}, tuition=M(600_000), otherFees=[fee(*UNIFORM, 850_000), fee(*BOOKS, 1_150_000), fee("Kegiatan per tahun", "Activities per year", 1_500_000)])
s("sekolah-alam-indonesia-depok", "Sekolah Alam Indonesia Depok", D, "Sukmajaya", "Jl. Raden Saleh / Jl. Studio Alam TVRI No.78x, Sukmajaya, Depok", SOB,
  ("DPP Rp9–15 juta; operasional tahunan Rp3,5–4,5 juta; biaya guru per bulan SD Rp800 ribu (TK Rp700 ribu).", "Development fee Rp9–15M; annual operations Rp3.5–4.5M; monthly teacher fee SD Rp800k (TK Rp700k)."), religion=None,
  registrationFee=500_000, entryFee={"min": 9_000_000, "max": 15_000_000}, tuition=M(800_000), otherFees=[fee("Operasional tahunan (min.)", "Annual operations (min.)", 3_500_000)])
upsert("smp-prestasi-global-depok", name="Sekolah Prestasi Global Depok", city=D, district="Pancoran Mas", level="SD", year="2024/2025", yearAssumed=True, source=SOB, checked=CHK, religion="Islam",
       registrationFee=300_000, entryFee={"min": 20_000_000}, tuition=M(1_200_000),
       notes=L("Biaya pengembangan pendidikan (uang pangkal, kegiatan tahunan, seragam, buku paket) Rp20.000.000. " + N[0], "Education development fee (entry, annual activities, uniforms, textbooks) Rp20,000,000. " + N[1]))
s("al-fauzien-islamic-school-depok", "Al Fauzien Islamic School Depok", D, "Pancoran Mas", None, SOB, ("Perlengkapan setahun Rp1,02 juta; dana kesehatan Rp95.000.", "Annual supplies Rp1.02M; health fund Rp95,000."),
  entryFee={"min": 24_500_000}, tuition=M(1_150_000), otherFees=[fee("Seragam 5 stel", "Uniforms (5 sets)", 1_140_000), fee("Kegiatan siswa", "Student activities", 1_050_000)])
s("sdit-darul-abidin-depok", "SDIT Darul Abidin Depok", D, "Beji", "Jl. Karet Hijau No.23, Beji, Depok", SOB, ("Gelombang I Rp35.000.000, gelombang II Rp36.500.000.", "Wave I Rp35,000,000, wave II Rp36,500,000."),
  registrationFee=350_000, entryFee={"min": 35_000_000, "max": 36_500_000}, tuition=M(1_600_000))
s("global-islamic-labschool-depok", "Global Islamic LabSchool Depok", D, None, "Jl. Raya KSU-Kalimulya No.67, Depok", SOB, ("Artikel menyebut \"uang pendaftaran Rp30.050.000\"; dicatat sebagai biaya masuk.", "The article says \"registration Rp30,050,000\"; recorded as the entry cost."),
  registrationFee=400_000, entryFee={"min": 30_050_000}, tuition=M(1_600_000))
s("sekolah-ummul-quro-depok", "Sekolah Ummul Quro Depok", D, "Beji", "Jl. Mandor Sanim, Kukusan, Beji, Depok", SOB,
  ("Paket masuk gelombang I (Sep–Des 2023) Rp30.395.000, gelombang II (Jan–Apr 2024) Rp31.395.000. Jalur tes inklusi +Rp375.000.", "Entry package wave I (Sep–Dec 2023) Rp30,395,000, wave II (Jan–Apr 2024) Rp31,395,000. Inclusion test track +Rp375,000."),
  registrationFee=450_000, entryFee={"min": 30_395_000, "max": 31_395_000}, tuition=M(1_700_000))
s("sdit-al-haraki-depok", "SDIT Al-Haraki Depok", D, "Pancoran Mas", None, SOB, ("Uang pangkal = investasi biaya pendidikan.", "Entry = education investment fee."), registrationFee=600_000, entryFee={"min": 30_850_000}, tuition=M(1_850_000))
s("sekolah-islam-fitrah-al-fikri-depok", "Sekolah Islam Fitrah Al Fikri Depok", D, "Sukmajaya", "Jl. Raden Saleh No.2A, Sukmajaya, Depok", SOB, ("", ""),
  registrationFee=600_000, entryFee={"min": 30_870_000}, tuition=M(1_890_000), otherFees=[fee("Uang tahunan", "Annual fee", 2_750_000), fee(*UNIFORM, 850_000), fee("Komite", "Committee", 240_000)])
s("sd-hj-isriati-baiturrahman-1-semarang", "SD Hj. Isriati Baiturrahman 1 Semarang", "Kota Semarang", "Semarang Tengah", "Jl. Pandanaran No.126, Pekunden, Semarang Tengah, Kota Semarang", NAK,
  ("Uang pangkal = sumbangan pendidikan.", "Entry = education contribution."), entryFee={"min": 9_000_000}, tuition=M(850_000),
  otherFees=[fee("Administrasi", "Administration", 2_745_000), fee(*UNIFORM, 1_339_000), fee("Paket buku", "Book package", 2_946_000), fee("Komite per bulan", "Committee per month", 50_000)])
