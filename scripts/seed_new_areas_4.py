"""New areas, batch 4 — official fee documents.
- SIT Ulil Albab Batam: SPMB T.A. 2027-2028 fee images (RA/TKIT, SDIT, SMPIT, SMAIT full day).
- Medan Independent School (MIS): Tuition Payment Policy 2026–2027 PDF.
- Singapore Indonesia School (SIS) Palembang: School Fee Structure 2026–2027 PDF."""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"

# ---------- SIT Ulil Albab Batam
UA = {"title": "SPMB Tahun Pelajaran 2027–2028 — SIT Ulil Albab Batam (situs resmi, tabel biaya)", "url": "https://ulilalbab-batam.com/"}
UAC = dict(name="SIT Ulil Albab Batam", city="Kota Batam", district="Sekupang", address="Tiban Utara No.1, Patam Lestari, Sekupang, Kota Batam (kampus juga di Batu Aji)",
           religion="Islam", website="https://ulilalbab-batam.com/", phone="0822-7776-0866", curriculum=["Nasional"], year="2027/2028", source=UA, checked=CHK)
WAVES = "Gelombang 1 bayar DPI + pendaftaran s.d. 25 Okt 2026, gelombang 2 s.d. 25 Nov 2026, gelombang 3 s.d. 25 Des 2026."
WAVES_EN = "Wave 1: pay DPI + registration by 25 Oct 2026; wave 2 by 25 Nov 2026; wave 3 by 25 Dec 2026."
upsert("sit-ulil-albab-batam", level="TK", registrationFee=400_000, entryFee={"min": 2_850_000, "max": 3_800_000}, tuition={"amount": 650_000, "period": "month"},
       otherFees=[fee("Komite/majalah per bulan", "Committee/magazine per month", 50_000), fee("Kegiatan per tahun", "Activities per year", 1_300_000), fee("Peralatan per tahun", "Equipment per year", 1_000_000),
                  fee("Mutu per tahun", "Quality fee per year", 300_000), fee("Asuransi per tahun", "Insurance per year", 20_000), fee(*UNIFORM, 1_200_000)],
       notes=L(f"RA Anak Harapan Ulil Albab. DPI (dana pengembangan institusi) normal Rp3.800.000; diskon gelombang 1/2/3 = 25%/20%/10%. Total normal Rp8.720.000. {WAVES}",
               f"RA Anak Harapan Ulil Albab. Institutional development fee (DPI) Rp3,800,000 normal; wave 1/2/3 discounts 25%/20%/10%. Normal total Rp8,720,000. {WAVES_EN}"), **UAC)
upsert("sit-ulil-albab-batam", level="SD", registrationFee=400_000, entryFee={"min": 11_050_000, "max": 13_000_000}, tuition={"amount": 850_000, "period": "month"},
       otherFees=[fee("Komite per bulan", "Committee per month", 20_000), fee("Kegiatan per tahun", "Activities per year", 1_150_000), fee("Buku per tahun", "Books per year", 1_180_000),
                  fee("Mutu per tahun", "Quality fee per year", 400_000), fee("Seragam (lengkap)", "Uniforms (full set)", 2_100_000)],
       notes=L("DPI normal Rp13.000.000; gelombang 1 diskon 15% (Rp11.050.000). Diskon Rp1.000.000 untuk alumni TKIT Ulil Albab. Kelas ber-AC. SPP disesuaikan saat naik ke kelas 4. Total normal Rp19.100.000.",
               "DPI Rp13,000,000 normal; wave 1 15% off (Rp11,050,000). Rp1,000,000 off for TKIT Ulil Albab alumni. Air-conditioned classes. Tuition is adjusted from grade 4. Normal total Rp19,100,000."), **UAC)
upsert("sit-ulil-albab-batam", level="SMP", registrationFee=300_000, entryFee={"min": 1_800_000, "max": 6_000_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee("Ekskul per bulan", "Extracurricular per month", 75_000), fee("Komite per tahun", "Committee per year", 200_000), fee("Kegiatan per tahun", "Activities per year", 1_250_000),
                  fee("Buku per tahun", "Books per year", 775_000), fee("Orientasi", "Orientation", 200_000), fee("Labor/perpustakaan", "Lab/library", 750_000), fee("Mutu per tahun", "Quality fee per year", 500_000),
                  fee("Seragam putra", "Uniforms (boys)", 2_300_000), fee("Seragam putri", "Uniforms (girls)", 2_700_000)],
       notes=L("DPI normal Rp6.000.000; gelombang 1 (1–10 Okt 2026) diskon 70%, gelombang 2 (11 Okt–20 Nov 2026) 25%, gelombang 3 10%. Diskon Rp1.000.000 untuk alumni SDIT Ulil Albab. Total normal Rp13.150.000 (putra) / Rp13.550.000 (putri).",
               "DPI Rp6,000,000 normal; wave 1 (1–10 Oct 2026) 70% off, wave 2 (11 Oct–20 Nov 2026) 25%, wave 3 10%. Rp1,000,000 off for SDIT Ulil Albab alumni. Normal total Rp13,150,000 (boys) / Rp13,550,000 (girls)."), **UAC)
upsert("sit-ulil-albab-batam", level="SMA", registrationFee=300_000, entryFee={"min": 7_000_000, "max": 10_000_000}, tuition={"amount": 1_150_000, "period": "month"},
       otherFees=[fee("Ekskul per bulan", "Extracurricular per month", 100_000), fee("DPS (dana pengembangan siswa) per tahun", "Student development fee per year", 4_500_000),
                  fee("Orientasi & tes penjurusan", "Orientation & stream test", 400_000), fee("Kartu digital pelajar", "Digital student card", 120_000), fee("Cover rapor", "Report cover", 120_000),
                  fee("Seragam putra (6 stel)", "Uniforms boys (6 sets)", 2_400_000), fee("Seragam putri (6 stel)", "Uniforms girls (6 sets)", 2_880_000)],
       notes=L("Full day jalur reguler. DPI normal Rp10.000.000; gelombang 1/2/3 diskon 30%/20%/10%. Diskon Rp1.000.000 untuk alumni SMPIT Ulil Albab. Total normal Rp19.090.000 (putra). Tersedia juga program boarding.",
               "Full-day regular track. DPI Rp10,000,000 normal; wave 1/2/3 discounts 30%/20%/10%. Rp1,000,000 off for SMPIT Ulil Albab alumni. Normal total Rp19,090,000 (boys). A boarding programme is also offered."), **UAC)
for lv in ("TK", "SD", "SMP", "SMA"):
    add_admission("sit-ulil-albab-batam", {"level": lv, "academicYear": "2027/2028", "period": L(WAVES, WAVES_EN),
        "steps": [L("Daftar online di ppdb.ulilalbab-batam.com", "Register online at ppdb.ulilalbab-batam.com"), L("Bayar uang pendaftaran dan DPI sesuai batas gelombang (pendaftaran batal jika belum dibayar)", "Pay registration and DPI by the wave deadline (unpaid registrations are cancelled)"),
                  L("Ikuti observasi/tes" + (" (tambahan observasi kematangan sekolah bagi usia < 6 tahun 6 bulan)" if lv == "SD" else ""), "Attend the observation/test" + (" (extra school-readiness assessment if under 6 years 6 months)" if lv == "SD" else "")),
                  L("Pengumuman dan daftar ulang", "Results and re-registration")],
        "documents": [], "notes": L("Jika tidak diterima, biaya dikembalikan 100%. Mundur sebelum 1 Juli 2027: potongan 50%; setelahnya tidak dikembalikan. Jalur prestasi (olimpiade, peringkat 1–3, hafalan ≥ 3 juz) mendapat bebas DPI atau cashback.",
                                    "If not accepted, fees are refunded in full. Withdrawal before 1 July 2027: 50% deduction; after that, no refund. Achievement tracks (olympiads, top-3 rank, ≥ 3 juz memorised) get DPI waivers or cashback."),
        "source": UA, "checked": CHK})

# ---------- Medan Independent School (official 2026–2027)
MIS = {"title": "Tuition Payment Policy 2026–2027 — Medan Independent School (PDF resmi)", "url": "https://mismedan.org/wp-content/uploads/2026/05/2026-2027-Tuition-Fee-Policy.pdf"}
MN = ("Biaya pendaftaran Rp45.000.000 sekali untuk siswa baru (K3 ke atas). Capital fee Rp25.000.000 per tahun (wajib). Kurs dihitung Rp18.000/USD dan disesuaikan tiap term. Diskon sibling 5%.",
      "One-time registration fee Rp45,000,000 for new students (K3 and above). Capital fee Rp25,000,000 per year (mandatory). Rate based on IDR 18,000/USD, adjusted each term. 5% sibling discount.")
for lv, amt, rng_id, rng_en in [
    ("TK", 56_606_000, "Tuition tahunan K1–K2 Rp56.606.000; K3 Rp108.723.000.", "Annual tuition K1–K2 Rp56,606,000; K3 Rp108,723,000."),
    ("SD", 171_668_000, "Tuition tahunan Grade 1–2 Rp171.668.000; Grade 3–4 Rp206.001.000; Grade 5–6 Rp240.335.000.", "Annual tuition Grades 1–2 Rp171,668,000; 3–4 Rp206,001,000; 5–6 Rp240,335,000."),
    ("SMP", 257_501_000, "Tuition tahunan Grade 7–8 Rp257.501.000; Grade 9 Rp274.668.000.", "Annual tuition Grades 7–8 Rp257,501,000; Grade 9 Rp274,668,000."),
    ("SMA", 274_668_000, "Tuition tahunan Grade 10 Rp274.668.000; Grade 11–12 (IB DP) Rp286.112.000. Biaya ujian IB DP sekitar Rp18.000.000.", "Annual tuition Grade 10 Rp274,668,000; Grades 11–12 (IB DP) Rp286,112,000. IB DP exam fees about Rp18,000,000."),
]:
    upsert("medan-independent-school", name="Medan Independent School", city="Kota Medan", district="Medan Tuntungan", address="Jl. Jamin Ginting Km 10 / Jl. Tali Air No.5, Mangga, Medan Tuntungan, Kota Medan",
           website="https://mismedan.org", curriculum=["IB", "Internasional"], level=lv, year="2026/2027", source=MIS, checked=CHK,
           **({"registrationFee": 45_000_000} if lv != "TK" else {}), tuition={"amount": amt, "period": "year"}, otherFees=[fee("Capital fee per tahun", "Capital fee per year", 25_000_000)],
           notes=L(rng_id + " " + MN[0], rng_en + " " + MN[1]))

# ---------- SIS Palembang (official 2026–2027)
SIS = {"title": "SIS Palembang School Fee Structure 2026–2027 (PDF resmi)", "url": "https://sisschools.org/assets/tuition-fee/SIS-Palembang-School-Fee.pdf"}
SN = ("Development fee dibayar sekali di awal masuk (lumpsum), besarnya tergantung kelas masuk. Tuition bisa dibayar bulanan, per semester, atau tahunan.",
      "Development fee is paid once on entry (lump sum) and depends on the entry grade. Tuition can be paid monthly, per semester or yearly.")
for lv, reg, dmin, dmax, tui, id_, en_ in [
    ("TK", 1_500_000, 6_000_000, 23_600_000, 22_560_000, "Kindergarten 1: development Rp12.000.000, tuition Rp22.560.000/tahun. Nursery 1 Rp23,6 jt + Rp19,2 jt; K2 Rp6 jt + Rp23,64 jt.", "Kindergarten 1: development Rp12,000,000, tuition Rp22,560,000/yr. Nursery 1 Rp23.6M + Rp19.2M; K2 Rp6M + Rp23.64M."),
    ("SD", 2_000_000, 6_600_000, 39_600_000, 28_320_000, "Primary 1: development Rp39.600.000, tuition Rp28.320.000/tahun (total Rp67,92 jt). Primary 6: Rp6,6 jt + Rp34,98 jt.", "Primary 1: development Rp39,600,000, tuition Rp28,320,000/yr (total Rp67.92M). Primary 6: Rp6.6M + Rp34.98M."),
    ("SMP", 2_500_000, 18_000_000, 36_000_000, 35_700_000, "Secondary 1: development Rp36.000.000, tuition Rp35.700.000/tahun (total Rp71,7 jt). Secondary 3: Rp18 jt + Rp41,7 jt.", "Secondary 1: development Rp36,000,000, tuition Rp35,700,000/yr (total Rp71.7M). Secondary 3: Rp18M + Rp41.7M."),
    ("SMA", 2_500_000, 9_000_000, 20_000_000, 47_700_000, "Junior College 1: development Rp20.000.000, tuition Rp47.700.000/tahun. Secondary 4: Rp9 jt + Rp44,7 jt.", "Junior College 1: development Rp20,000,000, tuition Rp47,700,000/yr. Secondary 4: Rp9M + Rp44.7M."),
]:
    upsert("singapore-indonesia-school-palembang", name="Singapore Indonesia School (SIS) Palembang", city="Kota Palembang", website="https://sisschools.org", phone="(0711) 562 6778 / +62 811-7133-331",
           curriculum=["Cambridge", "Internasional"], level=lv, year="2026/2027", source=SIS, checked=CHK,
           registrationFee=reg, entryFee={"min": dmin, "max": dmax}, tuition={"amount": tui, "period": "year"}, notes=L(id_ + " " + SN[0], en_ + " " + SN[1]))
