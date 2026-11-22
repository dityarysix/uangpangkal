"""Seed data transcribed by hand from:
Popmama, "13 Daftar Biaya Masuk SD di Jakarta Selatan & Pusat 2026/2027" (10 Nov 2025).
Every figure below is copied from the article; nothing is estimated.
Run: python3 scripts/seed_popmama_sd_jaksel_jakpus.py
"""
from seedlib import L, fee, upsert, UNIFORM, ACTIVITY
SRC = {
    "title": "13 Daftar Biaya Masuk SD di Jakarta Selatan & Pusat 2026/2027 (Popmama)",
    "url": "https://www.popmama.com/big-kid/6-9-years-old/daftar-biaya-masuk-sd-di-jakarta-selatan-pusat-2026-2027-00-8zdst-pntnk3",
    "published": "2025-11-10",
}
CHECKED = "2026-11-22"

BOOKS = ("Buku paket", "Textbooks")

schools = [
 dict(slug="sd-pangudi-luhur-jakarta", name="SD Pangudi Luhur", city="Jakarta Selatan", district="Cilandak",
      address="Jl. H. Nawi Raya No.21, Gandaria Selatan, Cilandak, Jakarta Selatan",
      fee=dict(registrationFee=175_000, entryFee={"min": 22_000_000, "max": 26_000_000},
               tuition={"amount": 1_300_000, "period": "month"},
               notes=L("Tiga paket: A — UPP+DPP Rp26.000.000 & uang sekolah Rp1.300.000/bln; B — Rp24.000.000 & Rp1.400.000; C — Rp22.000.000 & Rp1.500.000. Belum termasuk buku dan seragam.",
                       "Three packages: A — entry Rp26,000,000 & tuition Rp1,300,000/mo; B — Rp24,000,000 & Rp1,400,000; C — Rp22,000,000 & Rp1,500,000. Excludes books and uniforms."))),
 dict(slug="citra-kasih-don-bosco-pondok-indah", name="Sekolah Citra Kasih Don Bosco Pondok Indah", city="Jakarta Selatan", district="Cilandak",
      address="Jl. Duta Indah, Pondok Indah, Cilandak Barat, Jakarta Selatan",
      fee=dict(registrationFee=500_000, entryFee={"min": 24_000_000, "max": 32_000_000},
               tuition={"amount": 2_200_000, "period": "month"},
               notes=L("Uang pangkal Rp32.000.000, diskon 25% menjadi Rp24.000.000 (berlaku s/d 30 November 2025). Belum termasuk uang kegiatan ±Rp3–4 juta/tahun, seragam ±Rp300–350 ribu/stel, buku ±Rp1–1,2 juta/tahun.",
                       "Entry fee Rp32,000,000, 25% discount to Rp24,000,000 (valid until 30 November 2025). Excludes activity fee ~Rp3–4M/year, uniforms ~Rp300–350k/set, books ~Rp1–1.2M/year."))),
 dict(slug="sd-islam-tunas-mandiri-jagakarsa", name="SD Islam Tunas Mandiri", city="Jakarta Selatan", district="Jagakarsa", religion="Islam",
      address="Jl. M. Kahfi II Gg. Masjid An-Nur No.8, Srengseng Sawah, Jagakarsa, Jakarta Selatan",
      fee=dict(entryFee={"min": 23_000_000}, tuition={"amount": 1_500_000, "period": "month"},
               otherFees=[fee(*ACTIVITY, 2_645_000), fee(*UNIFORM, 1_400_000), fee(*BOOKS, 1_100_000), fee("Komite", "School committee", 400_000)])),
 dict(slug="sekolah-islam-harapan-ibu", name="Sekolah Islam Harapan Ibu", city="Jakarta Selatan", district="Kebayoran Lama", religion="Islam",
      address="Jl. H. Banan No.1, Pondok Pinang, Kebayoran Lama, Jakarta Selatan",
      fee=dict(entryFee={"min": 12_900_000}, tuition={"amount": 2_050_000, "period": "month"},
               otherFees=[fee("Biaya perawatan pengembangan", "Development & maintenance fee", 15_500_000), fee("POMG (persatuan orang tua murid & guru)", "Parent–teacher association", 300_000)])),
 dict(slug="sd-santo-bellarminus-menteng", name="SD Santo Bellarminus", city="Jakarta Pusat", district="Menteng",
      address="Jl. Lombok No.58, Gondangdia, Menteng, Jakarta Pusat",
      fee=dict(registrationFee=300_000, entryFee={"min": 12_000_000}, tuition={"amount": 1_500_000, "period": "month"},
               notes=L("Uang kegiatan ±Rp4.000.000/tahun; buku dan seragam ±Rp3.000.000.",
                       "Activity fee ~Rp4,000,000/year; books and uniforms ~Rp3,000,000."))),
 dict(slug="tunas-bangsa-christian-school-gunung-sahari", name="Tunas Bangsa Christian School", city="Jakarta Pusat", district="Sawah Besar", religion="Kristen",
      address="Jl. Gunung Sahari XII No.11, Gunung Sahari Utara, Sawah Besar, Jakarta Pusat",
      fee=dict(registrationFee=200_000, entryFee={"min": 10_500_000}, tuition={"amount": 1_100_000, "period": "month"},
               otherFees=[fee("Dana operasional tahunan", "Annual operating fee", 1_750_000)],
               notes=L("Biaya gelombang kedua, berlaku Juni–Desember 2025.", "Second-wave fees, valid June–December 2025."))),
 dict(slug="sekolah-hati-suci-tanah-abang", name="Sekolah Hati Suci", city="Jakarta Pusat", district="Tanah Abang",
      address="Jl. Hati Suci No.2, Kampung Bali, Tanah Abang, Jakarta Pusat",
      fee=dict(registrationFee=100_000, entryFee={"min": 8_800_000}, tuition={"amount": 1_000_000, "period": "month"},
               otherFees=[fee(*ACTIVITY, 800_000), fee("Seragam kotak", "Checked uniform", 129_000), fee("Baju olahraga", "Sports uniform", 190_000)])),
 dict(slug="perguruan-cikini", name="Perguruan Cikini", city="Jakarta Pusat", district="Menteng",
      address="Jl. Cikini Raya No.74-76, Cikini, Menteng, Jakarta Pusat",
      fee=dict(registrationFee=365_000, entryFee={"min": 15_500_000}, tuition={"amount": 1_200_000, "period": "month"},
               otherFees=[fee(*ACTIVITY, 4_000_000), fee("Uang perlengkapan", "Supplies", 4_000_000)])),
 dict(slug="sd-swasta-ratih-cempaka-putih", name="SD Swasta Ratih", city="Jakarta Pusat", district="Cempaka Putih",
      address="Jl. Murdai No.1, Cempaka Putih Barat, Jakarta Pusat",
      fee=dict(year="2025/2026", registrationFee=250_000, entryFee={"min": 1_500_000}, tuition={"amount": 400_000, "period": "month"},
               otherFees=[fee("Sarana dan prasarana", "Facilities fee", 1_350_000), fee(*UNIFORM, 500_000), fee(*ACTIVITY, 2_000_000)],
               notes=L("Menurut sumber, ini biaya tahun ajaran berjalan (2025/2026); biaya 2026/2027 diperkirakan tidak jauh berbeda. Uang pangkal = uang gedung.",
                       "Per the source these are current-year (2025/2026) fees; 2026/2027 fees were expected to be similar. Entry fee = building fee."))),
 dict(slug="sdit-kaffah-islamic-school-senen", name="SDIT Kaffah Islamic School", city="Jakarta Pusat", district="Senen", religion="Islam",
      address="Jl. Pramuka 16 No.549A, Paseban, Senen, Jakarta Pusat",
      fee=dict(registrationFee=500_000, entryFee={"min": 11_800_000}, tuition={"amount": 750_000, "period": "month"},
               otherFees=[fee("Kegiatan siswa", "Student activities", 3_950_000)],
               notes=L("Biaya pendaftaran = biaya observasi dan riset.", "Registration fee = observation & assessment fee."))),
 dict(slug="sdit-al-abrar-bendungan-hilir", name="SDIT Al-Abrar", city="Jakarta Pusat", district="Tanah Abang", religion="Islam",
      address="Jl. Bendungan Hilir No.148, Bendungan Hilir, Tanah Abang, Jakarta Pusat",
      fee=dict(registrationFee=270_000, entryFee={"min": 6_100_000}, tuition={"amount": 375_000, "period": "month"},
               otherFees=[fee("Foto dan rapor", "Photos & report book", 200_000), fee(*UNIFORM, 1_605_000), fee(*ACTIVITY, 865_000)])),
 dict(slug="sd-muhammadiyah-1-jakarta", name="SD Muhammadiyah 1 Jakarta", city="Jakarta Pusat", district="Kemayoran", religion="Islam",
      address="Jl. Garuda No.33, Gunung Sahari Selatan, Kemayoran, Jakarta Pusat",
      fee=dict(registrationFee=100_000, entryFee={"min": 9_500_000}, tuition={"amount": 500_000, "period": "month"},
               notes=L("Uang pangkal = Infaq Pembangunan Pendidikan (IPP). Buku dan seragam ±Rp2.000.000.",
                       "Entry fee = Infaq Pembangunan Pendidikan (IPP). Books and uniforms ~Rp2,000,000."))),
 dict(slug="sdit-cempaka-ria", name="SDIT Cempaka Ria", city="Jakarta Pusat", district="Cempaka Putih", religion="Islam",
      address="Jl. Rawasari Timur 1, Cempaka Putih Timur, Jakarta Pusat",
      fee=dict(registrationFee=30_000, entryFee={"min": 3_200_000}, tuition={"amount": 450_000, "period": "month"},
               otherFees=[fee("Ujian PTS dan PAT", "Mid- and end-of-year exams", 400_000), fee("UKS", "School health unit", 200_000),
                          fee(*UNIFORM, 850_000), fee(*BOOKS, 1_150_000), fee("Uang kegiatan (1 tahun)", "Activity fee (1 year)", 800_000),
                          fee("Coding (1 tahun)", "Coding (1 year)", 780_000), fee("Outing class", "Outing class", 700_000), fee("Rapor", "Report book", 150_000)],
               notes=L("Uang pangkal = uang gedung.", "Entry fee = building fee."))),
]

for s in schools:
    f = s.pop("fee")
    slug = s.pop("slug")
    upsert(slug, level="SD", year=f.pop("year", "2026/2027"), source=SRC, checked=CHECKED, **s, **f)
    print("wrote", slug)
