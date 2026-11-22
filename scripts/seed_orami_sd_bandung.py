"""Orami, "7 SD Swasta di Bandung, Ada Kurikulum Internasional" (1 Jul 2025).
Only schools with specific figures. Year not stated; published July 2025 -> 2025/2026, yearAssumed.
Skipped: SD Lab Percontohan UPI (university lab school) and Singapore Intercultural School (only wide ranges)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

SRC = {"title": "7 SD Swasta di Bandung, Ada Kurikulum Internasional (Orami)", "url": "https://www.orami.co.id/magazine/sd-swasta-di-bandung", "published": "2025-07-01"}
C = dict(city="Kota Bandung", level="SD", year="2025/2026", yearAssumed=True, source=SRC, checked="2026-11-22")

upsert("global-prestasi-school-bandung", name="Global Prestasi School Bandung", district="Cidadap", curriculum=["Cambridge"],
       address="Allegro Altura Complex, Jl. Citra Green, Ciumbuleuit, Cidadap, Kota Bandung",
       registrationFee=600_000, entryFee={"min": 40_000_000}, tuition={"amount": 10_950_000, "period": "quarter"},
       otherFees=[fee(*BOOKS, 2_500_000), fee(*UNIFORM, 1_600_000), fee("Biaya kegiatan", "Activity fee", 3_650_000)],
       notes=L("Uang pangkal = biaya pengembangan. Daftar ulang Rp200.000–Rp400.000.", "Entry fee = development fee. Re-registration Rp200,000–Rp400,000."), **C)
upsert("sd-islam-al-azhar-36-bandung", name="SD Islam Al Azhar 36 Bandung", district="Lengkong", religion="Islam",
       address="Jl. Palasari No.9, Lengkong, Kota Bandung",
       registrationFee=400_000, entryFee={"min": 28_000_000}, tuition={"amount": 1_300_000, "period": "month"},
       otherFees=[fee("Uang jamiyyah", "Parents' association (jamiyyah)", 250_000)], **C)
upsert("sd-assalaam-bandung", name="SD Assalaam Bandung", district="Regol", religion="Islam",
       address="Jl. Sasak Gantung No.1-4, Balonggede, Regol, Kota Bandung", phone="0838-0400-7400",
       tuition={"amount": 2_250_000, "period": "month"},
       otherFees=[fee("Buku (per tahun)", "Books (per year)", 1_795_000), fee("Seragam (pembayaran awal)", "Uniforms (initial payment)", 1_350_000)],
       notes=L("Sumber menyebut \"SPP (Sumbangan Pengembangan Pendidikan)\" Rp2.250.000 per bulan; uang pangkal tidak dicantumkan.",
               "The source lists \"SPP (education development contribution)\" Rp2,250,000 per month; entry fee not listed."), **C)
upsert("sd-bpi-bandung", name="SD BPI Bandung", district="Lengkong",
       address="Jl. Halimun No.40, Lengkong, Kota Bandung", phone="(022) 7301460",
       registrationFee=300_000, otherFees=[fee("Biaya kegiatan per tahun", "Activity fee per year", 4_025_000)],
       notes=L("Uang pangkal dan SPP tidak dicantumkan sumber.", "Entry fee and tuition not listed by the source."), **C)
upsert("sd-mutiara-bunda-bandung", name="SD Mutiara Bunda Bandung", district="Arcamanik", religion="Islam",
       address="Jl. Arcamanik Endah No.3, Sukamiskin, Arcamanik, Kota Bandung", phone="0812-8008-2116",
       otherFees=[fee("Biaya tahunan (tertinggi)", "Annual package (highest)", 49_900_000)],
       notes=L("Biaya tahunan Rp44.400.000–Rp49.900.000, sudah mencakup pendaftaran, daftar ulang, biaya pengembangan, kegiatan per semester, dan iuran bulanan. Gelombang pertama Rp44.400.000–Rp47.900.000.",
               "Annual package Rp44,400,000–Rp49,900,000, covering registration, re-registration, development fee, semester activities and monthly fees. First wave Rp44,400,000–Rp47,900,000."), **C)
print("ok")
