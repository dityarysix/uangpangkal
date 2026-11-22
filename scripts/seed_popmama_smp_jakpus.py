"""Popmama, "9 Daftar Biaya Masuk SMP di Jakarta Pusat Tahun Ajaran 2026/2027" (11 Dec 2025).
Figures copied verbatim from the article."""
from seedlib import L, fee, upsert

SRC = {"title": "9 Daftar Biaya Masuk SMP di Jakarta Pusat Tahun Ajaran 2026/2027 (Popmama)",
       "url": "https://www.popmama.com/big-kid/10-12-years-old/biaya-masuk-smp-di-jakarta-pusat-tahun-ajaran-2026-2027-00-bbqjr-hzfm3q",
       "published": "2025-12-11"}
C = dict(city="Jakarta Pusat", level="SMP", year="2026/2027", source=SRC, checked="2026-11-22")

upsert("sekolah-bunda-mulia-petojo", name="Sekolah Bunda Mulia Petojo", district="Gambir",
       address="Jl. A.M. Sangaji No.20, Petojo Utara, Gambir, Jakarta Pusat", website="https://sbm.sch.id",
       entryFee={"min": 7_500_000, "max": 8_500_000}, tuition={"amount": 1_300_000, "period": "month"},
       notes=L("Kelas reguler: uang sekolah Rp1.300.000/bulan. Kelas bilingual: Rp2.500.000/bulan. Uang pangkal sama untuk keduanya.",
               "Regular class: tuition Rp1,300,000/month. Bilingual class: Rp2,500,000/month. Same entry fee for both."), **C)
upsert("smpi-al-ihsan-kebon-kacang", name="SMPI Al Ihsan Kebon Kacang", district="Tanah Abang", religion="Islam",
       address="Jl. Kebon Kacang 9 No.57, Kebon Kacang, Tanah Abang, Jakarta Pusat", phone="(021) 3103313 / 0812-8897-1305",
       entryFee={"min": 1_675_000}, tuition={"amount": 225_000, "period": "month"},
       notes=L("Uang pangkal = uang gedung dan lain-lain.", "Entry fee = building fee and other items."), **C)
upsert("smpit-al-mubarak-cempaka-putih", name="SMPIT Al Mubarak", district="Cempaka Putih", religion="Islam",
       address="Jl. Pramuka Sari III No.24, Rawasari, Cempaka Putih, Jakarta Pusat", phone="0895-1703-6100",
       entryFee={"min": 15_000_000}, tuition={"amount": 750_000, "period": "month"},
       notes=L("Sumber menyebut: registrasi Rp15.000.000 (setelah tes); SPP Rp750.000/bulan; sudah termasuk pangkal, buku, dan seragam.",
               "Source states: registration Rp15,000,000 (after the test); tuition Rp750,000/month; includes entry fee, books and uniforms."), **C)
upsert("perguruan-advent-menteng", name="Perguruan Advent Menteng", district="Menteng", religion="Kristen",
       address="Jl. Sawo No.27, Menteng, Jakarta Pusat", phone="0813-7060-6868", website="https://adventmenteng.sch.id",
       tuition={"amount": 850_000, "period": "month"},
       otherFees=[fee("Uang tahunan (tahun pertama)", "Annual fee (first year)", 22_350_000), fee("Makan siang per bulan", "Lunch per month", 275_000)],
       notes=L("Tidak ada uang pangkal terpisah; sekolah memungut uang tahunan.", "No separate entry fee; the school charges an annual fee."), **C)
upsert("perguruan-cikini", name="Perguruan Cikini", district="Menteng",
       address="Jl. Cikini Raya No.74-76, Cikini, Menteng, Jakarta Pusat", phone="(021) 3144374 / 0815-1905-3664",
       entryFee={"min": 18_700_000}, tuition={"amount": 1_770_000, "period": "month"},
       otherFees=[fee("Uang buku", "Books", 1_800_000)], **C)
upsert("smp-1-pskd", name="SMP 1 PSKD", district="Senen",
       address="Jl. Diponegoro No.80, Senen, Jakarta Pusat", phone="(021) 3904418 / 0821-8888-7753",
       registrationFee=150_000, tuition={"amount": 746_000, "period": "month"},
       otherFees=[fee("Biaya pengembangan (per tahun)", "Development fee (per year)", 2_500_000)], **C)
upsert("sekolah-kristen-saint-john-kemayoran", name="Sekolah Kristen Saint John", district="Kemayoran", religion="Kristen",
       address="Jl. Bungur Besar Raya No.82A, Gunung Sahari, Kemayoran, Jakarta Pusat", phone="(021) 4213645 / 0878-7818-7068",
       entryFee={"min": 6_000_000}, tuition={"amount": 1_100_000, "period": "month"},
       otherFees=[fee("Uang kegiatan", "Activity fee", 2_000_000)],
       notes=L("Uang pangkal sebelum diskon; ada diskon untuk pendaftaran dan pelunasan lebih awal.", "Entry fee before discount; discounts for early registration and payment."), **C)
upsert("universal-school-kemayoran", name="Universal School Kemayoran", district="Kemayoran", curriculum=["Nasional Plus"],
       address="Jl. Ruas D7, Blok D6 No.2, Kota Baru Kemayoran, Jakarta Pusat", phone="(021) 6542654 / 0857-8888-6488", website="https://universalschool.id",
       tuition={"amount": 2_500_000, "period": "month"},
       otherFees=[fee("Uang paket tahunan (National Plus)", "Annual package (National Plus)", 28_000_000)],
       notes=L("National Plus: uang paket tahunan Rp28.000.000, SPP Rp2.500.000/bulan. Intensive English: Rp31.000.000 dan Rp3.000.000/bulan.",
               "National Plus: annual package Rp28,000,000, tuition Rp2,500,000/month. Intensive English: Rp31,000,000 and Rp3,000,000/month."), **C)
upsert("smp-van-lith-jakarta", name="SMP Van Lith Jakarta", district="Kemayoran", religion="Katolik",
       address="Jl. Gunung Sahari No.91, Gunung Sahari Selatan, Kemayoran, Jakarta Pusat", phone="(021) 42877726 / 0821-1211-0074",
       entryFee={"min": 7_600_000}, tuition={"amount": 835_000, "period": "month"},
       notes=L("Uang pangkal = Uang Perawatan Gedung (UPG). Tersedia diskon gelombang pertama.", "Entry fee = building maintenance fee (UPG). First-wave discount available."), **C)
print("ok smp jakpus")
