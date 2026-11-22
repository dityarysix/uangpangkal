"""SMPIT Nidaul Hikmah Salatiga — official SPMB page, Tahun Ajaran 2026/2027."""
from seedlib import L, upsert, add_admission
CHK = "2026-11-22"
SRC = {"title": "SPMB SMPIT Nidaul Hikmah Salatiga TA 2026/2027 (situs resmi)", "url": "https://ppdb.smpitnh.sch.id/"}
upsert("smpit-nidaul-hikmah-salatiga", name="SMPIT Nidaul Hikmah Salatiga", city="Salatiga", religion="Islam", website="https://ppdb.smpitnh.sch.id/",
       level="SMP", year="2026/2027", source=SRC, checked=CHK, registrationFee=200_000, entryFee={"min": 6_400_000, "max": 12_100_000}, tuition={"amount": 420_000, "period": "month"},
       notes=L("Fullday School: biaya awal tahun Rp6.400.000, IPP Rp420.000 (total awal Rp7.020.000); kuota 32 putra/32 putri. Vila Qur'an (boarding, tahfidz 30 juz): biaya awal tahun Rp12.100.000, IPP Rp1.250.000, uang saku & tabungan Rp250.000 (total Rp13.600.000). Cashback gelombang 1 (1 Sep–31 Des 2025): Rp500.000, alumni SDIT Nidaul Hikmah Rp1.500.000. IPP diasumsikan per bulan.",
               "Full-day School: start-of-year fee Rp6,400,000, IPP Rp420,000 (initial total Rp7,020,000); quota 32 boys/32 girls. Vila Qur'an (boarding, 30-juz memorisation): start-of-year Rp12,100,000, IPP Rp1,250,000, pocket money & savings Rp250,000 (total Rp13,600,000). Wave 1 cashback (1 Sep–31 Dec 2025): Rp500,000, SDIT Nidaul Hikmah alumni Rp1,500,000. IPP assumed to be monthly."))
add_admission("smpit-nidaul-hikmah-salatiga", {"level": "SMP", "academicYear": "2026/2027",
    "steps": [L("Transfer biaya pendaftaran Rp200.000 (gratis bagi yang sudah inden)", "Transfer the Rp200,000 registration fee (free for those who pre-booked)"), L("Konfirmasi pendaftaran", "Confirm registration"), L("Tes seleksi dan wawancara", "Selection test and interview")],
    "documents": [], "source": SRC, "checked": CHK})
