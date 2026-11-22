"""Official fee pages.
- Yayasan Adzkia Sumatera Barat: SPMB Adzkia 2026-2027 fee tables (Padang and Bukittinggi units).
- YKPI Al-Ittihad Pekanbaru: SPMB pages per unit; schedules Oct 2026–May 2027 -> 2027/2028."""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
AD = {"title": "Biaya Pendaftaran SPMB Adzkia 2026-2027 — Yayasan Adzkia Sumatera Barat (situs resmi)", "url": "https://spmb.adzkiasumbar.or.id/index.php?page=biaya"}
QA = ("Biaya belum termasuk seragam (dipesan di Koperasi Adzkia).", "Fees exclude uniforms (ordered from the Adzkia cooperative).")
PDG = dict(name="Sekolah Islam Adzkia Padang", city="Kota Padang", district="Kuranji", address="Jl. Taratak Paneh No.7, Kuranji, Kota Padang (kantor pusat)", religion="Islam",
           website="https://spmb.adzkiasumbar.or.id", phone="(0751) 498 901", year="2026/2027", source=AD, checked=CHK)
upsert("sekolah-islam-adzkia-padang", level="TK", registrationFee=200_000, entryFee={"min": 1_500_000, "max": 3_000_000}, tuition={"amount": 750_000, "period": "month"},
       otherFees=[fee("Uang alat", "Equipment", 2_200_000), fee(*ACTIVITY, 1_000_000), fee("Qardh al-hasan (titipan, dikembalikan setelah tamat)", "Qardh al-hasan deposit (refunded on graduation)", 1_000_000)],
       notes=L("TKIT Adzkia 1, Plus dan 5: pembangunan Rp2.000.000 (1 shift) / Rp2.500.000 (full day), SPP Rp750.000 / Rp1.200.000. TKIT Adzkia 2: pembangunan Rp1.500.000. TKIT Adzkia 3: Rp2.500.000 / Rp3.000.000, SPP Rp800.000 / Rp1.250.000. " + QA[0],
               "TKIT Adzkia 1, Plus and 5: building fee Rp2,000,000 (1 shift) / Rp2,500,000 (full day), tuition Rp750,000 / Rp1,200,000. TKIT Adzkia 2: building Rp1,500,000. TKIT Adzkia 3: Rp2,500,000 / Rp3,000,000, tuition Rp800,000 / Rp1,250,000. " + QA[1]), **PDG)
upsert("sekolah-islam-adzkia-padang", level="SD", registrationFee=300_000, entryFee={"min": 9_000_000}, tuition={"amount": 1_300_000, "period": "month"},
       otherFees=[fee("Uang PBM 1 tahun", "Learning fee (1 year)", 1_750_000), fee("Perlengkapan sekolah", "School supplies", 800_000), fee("Komite", "Committee", 300_000), fee("Qardh al-hasan (titipan, dikembalikan)", "Qardh al-hasan deposit (refundable)", 2_000_000)],
       notes=L("SDIT Adzkia Padang (kampus Kuranji dan Belanti). Pendaftaran Rp200.000 (internal) / Rp300.000 (eksternal). Uang bulanan minimal Rp1.300.000. Total Rp13.150.000 (di luar pendaftaran). " + QA[0],
               "SDIT Adzkia Padang (Kuranji and Belanti campuses). Registration Rp200,000 (internal) / Rp300,000 (external). Minimum monthly fee Rp1,300,000. Total Rp13,150,000 (excl. registration). " + QA[1]), **PDG)
upsert("sekolah-islam-adzkia-padang", level="SMP", registrationFee=300_000, entryFee={"min": 6_500_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Kegiatan 1 tahun", "Activities (1 year)", 3_000_000), fee("Komite", "Committee", 350_000), fee("Qardh al-hasan (titipan, dikembalikan)", "Qardh al-hasan deposit (refundable)", 1_000_000)],
       notes=L("SMPIT Adzkia Padang. Pendaftaran Rp200.000 (internal) / Rp300.000 (eksternal). Total Rp11.050.000 (di luar pendaftaran). " + QA[0], "SMPIT Adzkia Padang. Registration Rp200,000 (internal) / Rp300,000 (external). Total Rp11,050,000 (excl. registration). " + QA[1]), **PDG)
upsert("sekolah-islam-adzkia-padang", level="SMA", registrationFee=200_000, entryFee={"min": 2_500_000}, tuition={"amount": 600_000, "period": "month"},
       notes=L("SMAIP Adzkia. Total Rp3.100.000 (di luar pendaftaran). " + QA[0], "SMAIP Adzkia. Total Rp3,100,000 (excl. registration). " + QA[1]), **PDG)
BKT = dict(name="Sekolah Islam Adzkia Bukittinggi", city="Bukittinggi", religion="Islam", website="https://spmb.adzkiasumbar.or.id", year="2026/2027", source=AD, checked=CHK)
upsert("sekolah-islam-adzkia-bukittinggi", level="TK", registrationFee=150_000, entryFee={"min": 1_500_000}, tuition={"amount": 525_000, "period": "month"},
       otherFees=[fee("Uang alat", "Equipment", 1_500_000), fee(*ACTIVITY, 700_000)], notes=L("TKIT Adzkia Bukittinggi. Total Rp4.225.000 (di luar pendaftaran). " + QA[0], "TKIT Adzkia Bukittinggi. Total Rp4,225,000 (excl. registration). " + QA[1]), **BKT)
upsert("sekolah-islam-adzkia-bukittinggi", level="SD", registrationFee=200_000, entryFee={"min": 5_500_000}, tuition={"amount": 900_000, "period": "month"},
       otherFees=[fee("Uang PBM 1 tahun", "Learning fee (1 year)", 1_500_000), fee("Perlengkapan sekolah", "School supplies", 700_000), fee("Komite", "Committee", 300_000)],
       notes=L("SDIT Adzkia Bukittinggi. Pendaftaran Rp125.000 (internal) / Rp200.000 (eksternal). Uang bulanan minimal Rp900.000. Total Rp8.900.000. " + QA[0], "SDIT Adzkia Bukittinggi. Registration Rp125,000 (internal) / Rp200,000 (external). Minimum monthly Rp900,000. Total Rp8,900,000. " + QA[1]), **BKT)

# ---------- YKPI Al-Ittihad Pekanbaru
def itsrc(unit, path):
    return {"title": f"SPMB {unit} Al-Ittihad — YKPI Al-Ittihad Pekanbaru (situs resmi)", "url": f"https://ykpialittihad.or.id/{path}/"}
IT = dict(name="Sekolah Islam Terpadu Al-Ittihad Pekanbaru", city="Kota Pekanbaru", district="Rumbai", address="Komplek Damar No.608, Lembah Damai, Rumbai, Pekanbaru (sekretariat YKPI Al-Ittihad)",
          religion="Islam", website="https://ykpialittihad.or.id", year="2027/2028", checked=CHK)
def it(level, unit, path, up_u, up_a, spp, sm, sf, book, period_id, period_en, extra_id="", extra_en=""):
    src = itsrc(unit, path)
    of = [fee("Seragam putra", "Uniforms (boys)", sm), fee("Seragam putri", "Uniforms (girls)", sf)] + ([fee(*BOOKS, book)] if book else [])
    upsert("sit-al-ittihad-pekanbaru", level=level, source=src, registrationFee=325_000, entryFee={"min": up_a, "max": up_u}, tuition={"amount": spp, "period": "month"}, otherFees=of,
           notes=L(f"{unit}. Uang pangkal Rp{up_u:,} (umum) / Rp{up_a:,} (alumni). Uang komite sesuai kesepakatan orang tua. {extra_id}".replace(",", ".").strip(),
                   f"{unit}. Entry fee Rp{up_u:,} (general) / Rp{up_a:,} (alumni). Committee fee by parents' agreement. {extra_en}".strip()), **IT)
    add_admission("sit-al-ittihad-pekanbaru", {"level": level, "academicYear": "2027/2028", "period": L(period_id, period_en), "steps": [], "documents": [], "source": src, "checked": CHK})
it("TK", "TKIT", "spmb-tkit-al-ittihad", 8_600_000, 8_600_000, 900_000, 850_000, 900_000, None,
   "Gelombang I: daftar 14 Okt 2026–5 Feb 2027, observasi 6 Feb 2027. Gelombang II: 1 Mar–14 Mei 2027, observasi 15 Mei 2027.", "Wave I: register 14 Oct 2026–5 Feb 2027, observation 6 Feb 2027. Wave II: 1 Mar–14 May 2027, observation 15 May 2027.", "SPP termasuk snack.", "Tuition includes snacks.")
it("SD", "SDIT", "spmb-sdit-al-ittihad", 16_000_000, 14_000_000, 1_400_000, 950_000, 1_175_000, 750_000,
   "Daftar 14 Okt 2026–25 Jan 2027 (internal s.d. 11 Jan); psikotes 16/30 Jan 2027; pengumuman 15/24 Feb 2027.", "Register 14 Oct 2026–25 Jan 2027 (internal until 11 Jan); psychological test 16/30 Jan 2027; results 15/24 Feb 2027.")
it("SMP", "SMPIT", "spmb-smpit-al-ittihad", 14_000_000, 13_000_000, 1_200_000, 1_250_000, 1_975_000, 950_000,
   "Daftar 14 Okt 2026–7 Jan 2027; tes akademik & interview 9 Jan 2027; psikotes 10 Jan 2027; pengumuman 28 Feb 2027.", "Register 14 Oct 2026–7 Jan 2027; academic test & interview 9 Jan 2027; psychological test 10 Jan 2027; results 28 Feb 2027.")
it("SMA", "SMAIT", "spmb-smait-al-ittihad", 15_000_000, 14_000_000, 1_300_000, 1_650_000, 2_200_000, 1_600_000,
   "Gelombang I: 14 Okt–28 Des 2026 (tes 9–10 Jan 2027). Gelombang II: 2 Feb–31 Mar 2027 (tes 3–4 Apr 2027).", "Wave I: 14 Oct–28 Dec 2026 (tests 9–10 Jan 2027). Wave II: 2 Feb–31 Mar 2027 (tests 3–4 Apr 2027).")
MTS = itsrc("MTs", "spmb-mts-al-ittihadiyah")
upsert("mts-al-ittihadiyah-pekanbaru", name="MTs Al-Ittihadiyah Pekanbaru", city="Kota Pekanbaru", religion="Islam", website="https://ykpialittihad.or.id", level="SMP", year="2027/2028", source=MTS, checked=CHK,
       registrationFee=325_000, entryFee={"min": 5_500_000, "max": 11_600_000}, tuition={"amount": 600_000, "period": "month"},
       otherFees=[fee("Seragam putra", "Uniforms (boys)", 1_250_000), fee("Seragam putri", "Uniforms (girls)", 1_675_000), fee(*BOOKS, 800_000)],
       notes=L("Madrasah Tsanawiyah (setara SMP), YKPI Al-Ittihad. Biaya bertingkat menurut penghasilan orang tua: Grade A (> Rp10 jt/bulan) UP Rp11.600.000, SPP Rp1.200.000; Grade B (Rp6–10 jt) UP Rp9.100.000, SPP Rp850.000; Grade C (< Rp6 jt) UP Rp6.000.000, SPP Rp600.000. Alumni: UP lebih rendah Rp500.000–Rp1.000.000.",
               "Madrasah Tsanawiyah (SMP-equivalent), YKPI Al-Ittihad. Fees tiered by parents' income: Grade A (> Rp10M/month) entry Rp11,600,000, tuition Rp1,200,000; Grade B (Rp6–10M) Rp9,100,000, Rp850,000; Grade C (< Rp6M) Rp6,000,000, Rp600,000. Alumni pay Rp500,000–Rp1,000,000 less."))
