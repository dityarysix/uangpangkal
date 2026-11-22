"""New areas, batch 3 — official SPMB 2027/2028 pages.
- SIT Al Auliya Balikpapan (Samarinda Raya): fee tables per unit, external vs internal.
- Yayasan Islam Ibadurrahman Ciruas (Serang Raya): totals per period + components + SPP."""
from seedlib import L, fee, upsert, add_admission, UNIFORM

CHK = "2026-11-22"

# ---------- SIT Al Auliya Balikpapan
AA = {"title": "SPMB Online SIT Al Auliya Balikpapan TA 2027/2028 (situs resmi)", "url": "https://spmb.al-auliya.sch.id/"}
AAC = dict(name="SIT Al Auliya Balikpapan", city="Balikpapan", district="Balikpapan Utara", address="Jl. MT. Haryono No.137 RT 43, Graha Indah, Balikpapan Utara, Kota Balikpapan",
           religion="Islam", website="https://spmb.al-auliya.sch.id/", year="2027/2028", source=AA, checked=CHK)
def aa(level, reg, ext, intl, spp, others, nid, nen):
    upsert("sit-al-auliya-balikpapan", level=level, registrationFee=reg, entryFee={"min": intl, "max": ext}, tuition={"amount": spp, "period": "month"},
           otherFees=[fee(*o) for o in others], notes=L(nid, nen), **AAC)
aa("KB", 200_000, 2_000_000, 2_000_000, 800_000, [("Dana kegiatan per tahun", "Activities per year", 600_000), ("APE", "Educational play equipment", 500_000), ("Komite", "Committee", 300_000), ("Dana kesehatan", "Health fund", 50_000), ("Seragam", "Uniforms", 1_000_000)],
   "KBIT 1. Total Rp5.450.000. Daycare: uang pangkal Rp1.000.000, SPP Rp1.100.000/bulan.", "KBIT 1. Total Rp5,450,000. Daycare: entry Rp1,000,000, Rp1,100,000/month.")
aa("TK", 200_000, 4_000_000, 2_000_000, 850_000, [("Perlengkapan dan APE", "Supplies and play equipment", 1_000_000), ("Seragam", "Uniforms", 1_100_000), ("Dana kegiatan", "Activities", 1_400_000), ("Komite sekolah", "School committee", 360_000), ("Dana kesehatan", "Health fund", 50_000)],
   "TKIT 1 dan TKIT 2 (sama). Uang pangkal Rp4.000.000 (eksternal) / Rp2.000.000 (internal, tanpa biaya administrasi). Total Rp8.960.000 / Rp6.760.000.", "TKIT 1 and TKIT 2 (same). Entry Rp4,000,000 (external) / Rp2,000,000 (internal, no admin fee). Total Rp8,960,000 / Rp6,760,000.")
aa("SD", 350_000, 15_000_000, 11_500_000, 1_450_000, [("Perlengkapan dan buku (laki-laki)", "Supplies and books (boys)", 3_850_000), ("Perlengkapan dan buku (perempuan)", "Supplies and books (girls)", 4_050_000), ("Dana kegiatan", "Activities", 800_000), ("Komite sekolah", "School committee", 350_000)],
   "SDIT 1: uang pangkal Rp13.000.000 (eksternal) / Rp11.500.000 (internal), SPP Rp1.450.000. SDIT 2: Rp15.000.000 / Rp14.000.000, SPP Rp1.600.000.", "SDIT 1: entry Rp13,000,000 (external) / Rp11,500,000 (internal), tuition Rp1,450,000. SDIT 2: Rp15,000,000 / Rp14,000,000, tuition Rp1,600,000.")
aa("SMP", 350_000, 18_000_000, 14_500_000, 1_600_000, [("Biaya operasional sekolah (3 tahun)", "School operations (3 years)", 3_700_000), ("Komite per tahun", "Committee per year", 350_000), ("Perlengkapan putra", "Supplies (boys)", 2_420_000), ("Perlengkapan putri", "Supplies (girls)", 2_620_000)],
   "Fullday: uang pangkal Rp16.000.000 (eksternal) / Rp14.500.000 (internal), SPP Rp1.600.000. Boarding: Rp18.000.000 / Rp16.500.000, SPP Rp2.750.000, operasional 3 tahun Rp4.500.000.", "Full-day: entry Rp16,000,000 (external) / Rp14,500,000 (internal), tuition Rp1,600,000. Boarding: Rp18,000,000 / Rp16,500,000, tuition Rp2,750,000, 3-year operations Rp4,500,000.")
aa("SMA", 350_000, 13_000_000, 11_500_000, 1_650_000, [("Seragam (laki-laki)", "Uniforms (boys)", 2_600_000), ("Seragam (perempuan)", "Uniforms (girls)", 3_150_000), ("Dana kegiatan", "Activities", 3_700_000), ("Komite sekolah", "School committee", 350_000)],
   "Uang pangkal Rp13.000.000 (eksternal) / Rp11.500.000 (internal). Total laki-laki Rp21.650.000 / Rp20.150.000.", "Entry Rp13,000,000 (external) / Rp11,500,000 (internal). Boys' total Rp21,650,000 / Rp20,150,000.")

# ---------- Yayasan Islam Ibadurrahman (Serang)
IB = {"title": "SPMB 2027/2028 — Yayasan Islam Ibadurrahman Ciruas (situs resmi)", "url": "https://spmb.ibadurrahman.sch.id/"}
PER = L("Early Bird 1: 10 Okt–12 Des 2026; Early Bird 2: 2 Jan–21 Mar 2027; normal: Apr–Jun 2027.", "Early Bird 1: 10 Oct–12 Dec 2026; Early Bird 2: 2 Jan–21 Mar 2027; normal: Apr–Jun 2027.")
def ib(slug, name, city, district, address, level, infaq, kbm, sarpra, seragam, komite, spp, eb1, normal, extra_id="", extra_en=""):
    upsert(slug, name=name, city=city, district=district, address=address, religion="Islam", website="https://spmb.ibadurrahman.sch.id/", phone="+62 8591 0650 0225",
           level=level, year="2027/2028", source=IB, checked=CHK,
           entryFee={"min": infaq + sarpra - (normal - eb1), "max": infaq + sarpra}, tuition={"amount": spp, "period": "month"},
           otherFees=[fee("KBM & kegiatan per tahun", "Learning & activities per year", kbm), fee(*UNIFORM, seragam)] + ([fee("Komite", "Committee", komite)] if komite else []),
           notes=L(f"Total SPMB: Early Bird 1 Rp{eb1:,} / normal Rp{normal:,} (SPP bulanan di luar total). Uang pangkal = infaq bangunan Rp{infaq:,} + sarpra Rp{sarpra:,} (harga normal); diskon early bird dihitung dari total. {extra_id}".replace(",", ".").strip(),
                   f"Total admission cost: Early Bird 1 Rp{eb1:,} / normal Rp{normal:,} (monthly tuition separate). Entry fee = building donation Rp{infaq:,} + facilities Rp{sarpra:,} (normal price); the early-bird discount applies to the total. {extra_en}".strip()))
    add_admission(slug, {"level": level, "academicYear": "2027/2028", "period": PER,
        "steps": [L("Pilih unit dan jalur pendaftaran", "Choose the unit and admission track"), L("Isi formulir pendaftaran", "Fill in the registration form"), L("Unggah dokumen sesuai jalur", "Upload documents for the chosen track"),
                  L("Selesaikan pembayaran tagihan SPMB", "Pay the admission invoice"), L("Verifikasi dan seleksi (tes/observasi)", "Verification and selection (test/observation)")],
        "documents": [], "source": IB, "checked": CHK})
CIR = dict(city="Kabupaten Serang", district="Ciruas")
ib("ibadurrahman-ciruas-serang", "Sekolah Islam Ibadurrahman Ciruas Serang", address="Kp. Kubangawan RT 002/RW 002, Citerep, Ciruas, Kabupaten Serang (RA & SDIT); Perum Bumi Ciruas Blok C8 No.14–15, Ranjeng, Ciruas (SMPIT & SMAIT)", level="TK",
   infaq=3_000_000, kbm=2_000_000, sarpra=1_000_000, seragam=850_000, komite=0, spp=400_000, eb1=4_850_000, normal=6_850_000, extra_id="RAIT Waladun Sholih.", extra_en="RAIT Waladun Sholih.", **CIR)
ib("ibadurrahman-ciruas-serang", "Sekolah Islam Ibadurrahman Ciruas Serang", address=None, level="SD", infaq=5_000_000, kbm=2_200_000, sarpra=2_450_000, seragam=1_200_000, komite=100_000, spp=700_000, eb1=8_950_000, normal=10_950_000, extra_id="SDIT Ibadurrahman.", extra_en="SDIT Ibadurrahman.", **CIR)
ib("ibadurrahman-ciruas-serang", "Sekolah Islam Ibadurrahman Ciruas Serang", address=None, level="SMP", infaq=5_000_000, kbm=2_600_000, sarpra=2_000_000, seragam=1_200_000, komite=100_000, spp=650_000, eb1=8_900_000, normal=10_900_000,
   extra_id="SMPIT Ibadurrahman. Asrama putri: tambahan Rp450.000/bulan.", extra_en="SMPIT Ibadurrahman. Girls' boarding: extra Rp450,000/month.", **CIR)
ib("ibadurrahman-ciruas-serang", "Sekolah Islam Ibadurrahman Ciruas Serang", address=None, level="SMA", infaq=3_500_000, kbm=2_400_000, sarpra=1_350_000, seragam=1_300_000, komite=100_000, spp=600_000, eb1=6_650_000, normal=8_650_000,
   extra_id="SMAIT Ibadurrahman. Asrama putri: tambahan Rp450.000/bulan.", extra_en="SMAIT Ibadurrahman. Girls' boarding: extra Rp450,000/month.", **CIR)
DH = dict(city="Kota Serang", district="Cipocok Jaya")
ib("daarul-huffazh-ibadurrahman-serang", "Daarul Huffazh Ibadurrahman Serang", address="Jl. Raya Pandeglang KM 04 RT 05/RW 01, Dalung, Cipocok Jaya, Kota Serang", level="TK",
   infaq=3_000_000, kbm=1_900_000, sarpra=1_200_000, seragam=400_000, komite=50_000, spp=400_000, eb1=4_550_000, normal=6_550_000, extra_id="TK Qur'an.", extra_en="Qur'an kindergarten.", **DH)
ib("daarul-huffazh-ibadurrahman-serang", "Daarul Huffazh Ibadurrahman Serang", address=None, level="SD", infaq=5_000_000, kbm=2_800_000, sarpra=1_500_000, seragam=600_000, komite=100_000, spp=500_000, eb1=8_000_000, normal=10_000_000, extra_id="SD Qur'an.", extra_en="Qur'an primary school.", **DH)
