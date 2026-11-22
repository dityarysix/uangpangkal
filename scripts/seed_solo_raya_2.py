"""Solo Raya, older data (labelled with the stated year):
- Sapamama / Playdate Soloraya, "Info Biaya Sekolah Dasar (SD) di Kota Solo dan Sekitarnya (Solo Raya)" (17 Nov 2021):
  the article states these are 2022/2023 fees.
- Nakita, "Daftar Biaya 3 Sekolah SMP Swasta di Solo Tahun Ajaran 2023-2024"."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

CHK = "2026-11-22"
SP = {"title": "Info Biaya SD di Kota Solo dan Solo Raya dari Playdate Soloraya (blog Sapamama)", "url": "https://www.sapamama.com/2021/11/info-biaya-sekolah-dasar-sd-di-kota.html", "published": "2021-11-17"}
C = dict(level="SD", year="2022/2023", source=SP, checked=CHK, religion="Islam")
KOTA = "Surakarta (Solo)"

upsert("sd-al-azhar-syifa-budi-solo", name="SD Al Azhar Syifa Budi Solo", city=KOTA, district="Laweyan",
       address="Jl. Haryo Panular No.64, Panularan, Laweyan, Surakarta", phone="(0271) 725306",
       registrationFee=350_000, entryFee={"min": 9_000_000}, tuition={"amount": 625_000, "period": "month"},
       otherFees=[fee("Sumbangan pengembangan", "Development contribution", 4_500_000), fee("Uang kegiatan 1 tahun", "Activities (1 year)", 1_420_000),
                  fee("Uang buku 1 tahun", "Books (1 year)", 1_500_000), fee("Seragam putra", "Uniforms (boys)", 750_000), fee("Seragam putri", "Uniforms (girls)", 890_000)],
       notes=L("Pendaftaran Rp300.000 untuk alumni TK ASBS. SPP Juli 2022. Total putra Rp17.795.000 / putri Rp17.935.000.", "Registration Rp300,000 for TK ASBS alumni. July 2022 tuition. Total boys Rp17,795,000 / girls Rp17,935,000."), **C)
upsert("sd-muhammadiyah-pk-kottabarat-surakarta", name="SD Muhammadiyah Program Khusus Kottabarat Surakarta", city=KOTA, district="Laweyan",
       address="Jl. Dr. Moewardi No.24, Purwosari, Laweyan, Surakarta", phone="(0271) 712158",
       entryFee={"min": 11_500_000, "max": 12_500_000}, tuition={"amount": 1_500_000, "period": "month"},
       notes=L("Total biaya masuk termasuk SPP Juli 2022, buku, seragam, kegiatan. SPP normal Rp1.500.000 (saat pandemi Rp850.000), termasuk katering, snack, kegiatan/ekskul.",
               "Total entry cost includes July 2022 tuition, books, uniforms, activities. Normal tuition Rp1,500,000 (Rp850,000 during the pandemic), incl. catering, snacks, activities."), **C)
upsert("sd-lazuardi-kamila-surakarta", name="SD Lazuardi Kamila Surakarta", city=KOTA, district="Banjarsari", address="Jl. Monumen 45 No.11, Setabelan, Banjarsari, Surakarta",
       entryFee={"min": 12_450_000}, tuition={"amount": 700_000, "period": "month"},
       notes=L("Gelombang 1 (hingga 31 Desember 2021), belum termasuk buku.", "Wave 1 (until 31 December 2021), excluding books."), **C)
upsert("sd-tamirul-islam-surakarta", name="SD Ta'mirul Islam Surakarta", city=KOTA, district="Laweyan", address="Jl. Dr. Wahidin No.36, Bumi, Laweyan, Surakarta", phone="(0271) 724020",
       entryFee={"min": 6_000_000}, tuition={"amount": 400_000, "period": "month"},
       otherFees=[fee("Seragam & buku putra", "Uniforms & books (boys)", 1_750_000), fee("Seragam & buku putri", "Uniforms & books (girls)", 2_000_000),
                  fee("Biaya program per bulan", "Programme fee per month", 50_000), fee("Lab (kelas digital sains)", "Lab (digital science class)", 500_000), fee("Snack per bulan", "Snacks per month", 60_000)],
       notes=L("Kelas reguler SPP Rp400.000; tahfidz dan digital sains Rp500.000.", "Regular class tuition Rp400,000; tahfidz and digital science Rp500,000."), **C)
upsert("mi-tamirul-islam-surakarta", name="MI Ta'mirul Islam Surakarta", city=KOTA, district="Laweyan", phone="(0271) 8000760",
       registrationFee=300_000, entryFee={"min": 6_000_000}, tuition={"amount": 500_000, "period": "month"},
       otherFees=[fee("Seragam putra", "Uniforms (boys)", 1_000_000), fee("Seragam putri", "Uniforms (girls)", 1_250_000), fee("Snack per bulan", "Snacks per month", 72_000)],
       notes=L("Madrasah Ibtidaiyah (setara SD). SPP minimal; infaq sukarela.", "Madrasah Ibtidaiyah (equivalent to SD). Minimum tuition; voluntary infaq."), **C)
upsert("sdict-al-abidin-surakarta", name="SDICT Al Abidin Surakarta", city=KOTA, district="Banjarsari", address="Jl. Bone Barat Utama, Banyuanyar, Banjarsari, Surakarta", phone="0857-3554-9969",
       entryFee={"min": 6_500_000, "max": 12_000_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 850_000), fee("Paket pembelajaran digital", "Digital learning package", 800_000)],
       notes=L("Sekolah coding. BPI tahap 1: gelombang khusus Rp6.500.000–Rp7.000.000, reguler Rp12.000.000; lalu 3 tahap BPI @Rp2.000.000 (Juli 2023, 2024, 2025). Wakaf pendidikan pilihan Rp500 ribu–>Rp1,5 juta.",
               "Coding school. Entry stage 1: special waves Rp6,500,000–Rp7,000,000, regular Rp12,000,000; then 3 further payments of Rp2,000,000 (July 2023, 2024, 2025). Optional endowment Rp500k–>Rp1.5M."), **C)
upsert("charis-institute-surakarta", name="Charis Institute Surakarta", city=KOTA, district="Banjarsari", address="Jl. Monginsidi No.28, Gilingan, Banjarsari, Surakarta",
       entryFee={"min": 1_600_000, "max": 2_300_000},
       notes=L("Biaya masuk gelombang 1 Rp1.600.000; gelombang 2 Rp1.800.000; gelombang 3 Rp2.300.000; termasuk uang gedung, daftar ulang, seragam, dan buku tulis. SPP didiskusikan dengan sekolah.",
               "Entry fee wave 1 Rp1,600,000; wave 2 Rp1,800,000; wave 3 Rp2,300,000; includes building fee, re-registration, uniforms and exercise books. Tuition is discussed with the school."),
       **{**C, "religion": "Kristen"})
upsert("sd-muhammadiyah-alam-surya-mentari-surakarta", name="SD Muhammadiyah Alam Surya Mentari Surakarta", city=KOTA,
       entryFee={"min": 12_500_000}, notes=L("Total biaya masuk.", "Total entry cost."), **C)
upsert("sdit-insan-mulia-surakarta", name="SDIT Insan Mulia Surakarta", city=KOTA, phone="(0271) 732373",
       registrationFee=250_000, entryFee={"min": 6_600_000}, tuition={"amount": 450_000, "period": "month"},
       otherFees=[fee("Seragam putra", "Uniforms (boys)", 550_000), fee("Seragam putri", "Uniforms (girls)", 650_000), fee("Uang kegiatan per semester", "Activities per semester", 600_000)],
       notes=L("SPP minimal.", "Minimum tuition."), **C)
upsert("sd-muhammadiyah-plus-malangjiwan-colomadu", name="SD Muhammadiyah Plus Malangjiwan Colomadu", city="Karanganyar", district="Colomadu",
       address="Ngerangan, Gawanan Barat, Colomadu, Karanganyar",
       registrationFee=125_000, entryFee={"min": 2_750_000, "max": 3_250_000}, tuition={"amount": 437_000, "period": "month"},
       otherFees=[fee("Wakaf tunai pembangunan (min.)", "Building endowment (min.)", 1_500_000), fee("Perlengkapan 1 tahun (seragam, tas, alat tulis)", "Supplies for 1 year (uniforms, bag, stationery)", 2_750_000),
                  fee("Katering per bulan", "Catering per month", 283_000)],
       notes=L("Pendaftaran Rp125.000 (inden) / Rp250.000. Dana pengembangan pilihan I–III: Rp2.750.000–Rp3.250.000; wakaf Rp1.500.000–Rp1.700.000. SPP = infaq pendidikan bulanan.",
               "Registration Rp125,000 (early) / Rp250,000. Development fund options I–III: Rp2,750,000–Rp3,250,000; endowment Rp1,500,000–Rp1,700,000. Tuition = monthly education infaq."), **C)
upsert("sd-muhammadiyah-palur", name="SD Muhammadiyah Program Khusus Palur", city="Sukoharjo", district="Mojolaban",
       address="Jl. Raya Palur No.243, Kedung Aron, Palur, Mojolaban, Sukoharjo", phone="(0271) 825937",
       tuition={"amount": 250_000, "period": "month"},
       otherFees=[fee("Kegiatan per bulan", "Activities per month", 75_000), fee("Makan per bulan", "Meals per month", 110_000), fee("Seragam putra", "Uniforms (boys)", 900_000),
                  fee("Seragam putri", "Uniforms (girls)", 1_000_000), fee("Paket buku", "Books", 800_000), fee("Tas & alat tulis", "Bag & stationery", 200_000)],
       notes=L("Total masuk paket A: Rp6.850.000 (putra) / Rp6.950.000 (putri); paket B: Rp7.350.000 / Rp7.450.000 (komponen B Rp5.000.000).", "Total on entry, package A: Rp6,850,000 (boys) / Rp6,950,000 (girls); package B: Rp7,350,000 / Rp7,450,000 (B component Rp5,000,000)."), **C)
upsert("sd-muhammadiyah-al-kautsar-kartasura", name="SD Muhammadiyah Al Kautsar Kartasura", city="Sukoharjo", district="Kartasura",
       address="Jl. Cendana Raya No.3, Gumpang, Kartasura, Sukoharjo", phone="(0271) 7652590",
       registrationFee=300_000, entryFee={"min": 6_000_000}, tuition={"amount": 500_000, "period": "month"},
       otherFees=[fee("Seragam putra", "Uniforms (boys)", 900_000), fee("Seragam putri", "Uniforms (girls)", 1_000_000), fee("Makan per bulan", "Meals per month", 110_000),
                  fee("Buku 1 tahun", "Books (1 year)", 950_000), fee("Ta'aruf siswa baru", "New-student orientation", 250_000), fee("Kegiatan 1 tahun", "Activities (1 year)", 1_900_000)],
       notes=L("Uang pangkal = infaq minimal. SPP minimal.", "Entry fee = minimum infaq. Minimum tuition."), **C)
upsert("sekolah-alam-aminah-sukoharjo", name="Sekolah Alam Aminah Sukoharjo", city="Sukoharjo", district="Baki", curriculum=["Sekolah Alam"],
       address="Jl. Raya Baki, Gawok, Sukoharjo", phone="0856-4091-8948",
       registrationFee=100_000, entryFee={"min": 2_000_000}, tuition={"amount": 400_000, "period": "month"},
       otherFees=[fee("Seragam putra", "Uniforms (boys)", 500_000), fee("Seragam putri", "Uniforms (girls)", 600_000), fee("Buku per semester", "Books per semester", 550_000)],
       notes=L("SPP termasuk uang makan. Total Rp3.550.000 (putra) / Rp3.650.000 (putri).", "Tuition includes meals. Total Rp3,550,000 (boys) / Rp3,650,000 (girls)."), **C)
upsert("sekolah-alam-bengawan-solo", name="Sekolah Alam Bengawan Solo", city="Klaten", district="Juwiring", curriculum=["Sekolah Alam"],
       address="Panjangan, Gondangsari, Juwiring, Klaten", phone="0895-0242-8222",
       entryFee={"min": 3_000_000}, tuition={"amount": 150_000, "period": "month"}, notes=L("Dana pengembangan minimal.", "Minimum development fund."), **C)

NK = {"title": "Daftar Biaya 3 Sekolah SMP Swasta di Solo Tahun Ajaran 2023-2024 (Nakita)", "url": "https://nakita.grid.id/read/023694707/daftar-biaya-3-sekolah-smp-swasta-di-solo-tahun-ajaran-2023-2024?page=all"}
N = dict(level="SMP", year="2023/2024", source=NK, checked=CHK, religion="Islam")
upsert("smp-islam-al-abidin-surakarta", name="SMP Islam Al Abidin Surakarta", city=KOTA, district="Banjarsari", address="Jl. Tarumanegara No.3, Banyuanyar, Banjarsari, Surakarta",
       registrationFee=300_000, entryFee={"min": 12_000_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_000_000), fee(*BOOKS, 500_000)],
       notes=L("Uang pangkal = biaya pengembangan institusi. Wakaf pendidikan pilihan Rp500 ribu–>Rp1,5 juta. Program ICP, tahfidz, ICT.", "Entry fee = institutional development fee. Optional endowment Rp500k–>Rp1.5M. ICP, tahfidz and ICT programmes."), **N)
upsert("smpit-nur-hidayah-surakarta", name="SMPIT Nur Hidayah Surakarta", city=KOTA, district="Banjarsari", address="Jl. Kahuripan Utara, Sumber, Banjarsari, Surakarta",
       phone="(0271) 743416", website="https://smpitnurhidayahsolo.sch.id",
       entryFee={"min": 13_500_000}, tuition={"amount": 850_000, "period": "month"},
       otherFees=[fee("Wakaf pendidikan", "Education endowment", 1_500_000), fee("Seragam putra", "Uniforms (boys)", 1_000_000), fee("Seragam putri", "Uniforms (girls)", 1_200_000),
                  fee("Kegiatan awal masuk", "Orientation activities", 500_000), fee(*BOOKS, 400_000)],
       notes=L("Total putra Rp17.750.000 / putri Rp17.950.000. Boarding sekitar Rp22,25 juta (putra) / Rp22,45 juta (putri).", "Total boys Rp17,750,000 / girls Rp17,950,000. Boarding about Rp22.25M (boys) / Rp22.45M (girls)."), **N)
upsert("insan-cendekia-boarding-school-sukoharjo", name="Insan Cendekia Boarding School Sukoharjo", city="Sukoharjo", district="Baki",
       address="Jl. Ovensari, Kadilangu, Baki, Sukoharjo", phone="(0271) 6727303",
       registrationFee=350_000, entryFee={"min": 10_200_000}, tuition={"amount": 2_600_000, "period": "month"},
       otherFees=[fee("Buku dan kegiatan", "Books and activities", 3_600_000), fee(*UNIFORM, 1_100_000)], notes=L("Total Rp17.500.000.", "Total Rp17,500,000."), **N)
print("ok")
