"""Official SPMB pages, academic year 2027/2028 (figures verbatim):
- Santa Maria Ursulin (Surabaya & Sidoarjo): https://ppdb.sanmarosu-jatim.sch.id/profile/<UNIT>
- SMP SIG (Semen Gresik): https://ppdb.smpsemengresik.sch.id/"""
from seedlib import L, fee, upsert

CHK = "2026-11-22"
def SM(unit): return {"title": f"SPMB Santa Maria {unit.replace('-', ' ').title()} TA 2027/2028 (situs resmi)", "url": f"https://ppdb.sanmarosu-jatim.sch.id/profile/{unit}"}
SBY = dict(name="Sekolah Santa Maria Surabaya", city="Surabaya", religion="Katolik", address="Jl. Raya Darmo No.49, Surabaya",
           website="https://ppdb.sanmarosu-jatim.sch.id", year="2027/2028", checked=CHK)
PAYNOTE = ("Potongan 5% jika uang pengembangan dibayar lunas (plus 1 pasang seragam olahraga); potongan 5% jika SPP 1 tahun dilunasi Juli–Agustus 2027. Belum termasuk seragam.",
           "5% off if the development fee is paid in full (plus one free sports uniform); 5% off if a full year's tuition is paid in July–August 2027. Uniforms not included.")
upsert("sekolah-santa-maria-surabaya", level="KB", source=SM("KB-SURABAYA"), registrationFee=250_000, entryFee={"min": 15_000_000},
       tuition={"amount": 1_100_000, "period": "month"}, otherFees=[fee("Uang kegiatan", "Activity fee", 2_200_000)],
       notes=L("Uang pengembangan/gedung dibayar sekali, berlaku sampai lulus TK B. SPP disesuaikan saat masuk TK A. " + PAYNOTE[0],
               "The development/building fee is paid once and covers up to TK B graduation. Tuition is adjusted on entering TK A. " + PAYNOTE[1]), **SBY)
upsert("sekolah-santa-maria-surabaya", level="TK", source=SM("TK-SURABAYA"), registrationFee=250_000, entryFee={"min": 11_000_000},
       tuition={"amount": 1_150_000, "period": "month"}, otherFees=[fee("Uang kegiatan TK A", "Activity fee TK A", 2_800_000), fee("Uang kegiatan TK B", "Activity fee TK B", 3_000_000)],
       notes=L("Uang pengembangan/gedung dibayar sekali, berlaku sampai lulus TK B. " + PAYNOTE[0], "The development/building fee is paid once and covers up to TK B graduation. " + PAYNOTE[1]), **SBY)
upsert("sekolah-santa-maria-surabaya", level="SD", source=SM("SD-SURABAYA"), registrationFee=275_000, entryFee={"min": 16_200_000, "max": 17_200_000},
       tuition={"amount": 1_250_000, "period": "month"}, otherFees=[fee("Uang kegiatan", "Activity fee", 2_440_000)],
       notes=L("Jalur khusus (dari TK Santa Maria Surabaya / TK Santa Maria II Sidoarjo): UPP Rp16.200.000, SPP Rp1.250.000. Jalur peminatan (TK lain, daftar s.d. 9 Agustus 2026): Rp16.700.000, SPP Rp1.275.000. Jalur umum: Rp17.200.000, SPP Rp1.300.000. Potongan Rp300.000 untuk pendaftar awal tertentu; potongan keluarga Rp500.000. " + PAYNOTE[0] + " Belum termasuk buku paket.",
               "Special track (from TK Santa Maria Surabaya / TK Santa Maria II Sidoarjo): development fee Rp16,200,000, tuition Rp1,250,000. Interest track (other kindergartens, registered by 9 August 2026): Rp16,700,000, tuition Rp1,275,000. General track: Rp17,200,000, tuition Rp1,300,000. Rp300,000 off for certain early registrants; Rp500,000 family discount. " + PAYNOTE[1] + " Textbooks not included."), **SBY)
upsert("sekolah-santa-maria-surabaya", level="SMA", source=SM("SMA-SURABAYA"), registrationFee=350_000, entryFee={"min": 19_300_000},
       tuition={"amount": 2_300_000, "period": "month"}, otherFees=[fee("Uang kegiatan 1 tahun kelas X", "Grade 10 activity fee (1 year)", 3_300_000)],
       notes=L("Biaya jalur umum II. Belum termasuk seragam.", "General track II fees. Uniforms not included."), **SBY)

SDA = dict(name="Sekolah Santa Maria II Sidoarjo", city="Sidoarjo", religion="Katolik", website="https://ppdb.sanmarosu-jatim.sch.id", year="2027/2028", checked=CHK)
SIB = ("Ada saudara kandung yang masuk di tahun yang sama: potongan uang pengembangan Rp500.000 per keluarga. Potongan 5% jika SPP 1 tahun dilunasi Juli–Agustus 2027.",
       "Sibling entering the same year: Rp500,000 off the development fee per family. 5% off if a full year's tuition is paid in July–August 2027.")
upsert("sekolah-santa-maria-ii-sidoarjo", level="KB", source=SM("KB-SIDOARJO"), registrationFee=200_000, entryFee={"min": 6_375_000, "max": 8_000_000},
       tuition={"amount": 700_000, "period": "month"}, otherFees=[fee("Uang kegiatan KB A", "Activity fee KB A", 1_000_000), fee("Uang kegiatan KB B", "Activity fee KB B", 1_400_000)],
       notes=L("Uang sarana dan pengembangan: early bird / jalur expo Rp6.375.000; gelombang 1 Rp7.500.000; gelombang 2 Rp8.000.000. Seragam ± Rp500.000. " + SIB[0],
               "Facilities & development fee: early bird / expo track Rp6,375,000; wave 1 Rp7,500,000; wave 2 Rp8,000,000. Uniforms ~Rp500,000. " + SIB[1]), **SDA)
upsert("sekolah-santa-maria-ii-sidoarjo", level="TK", source=SM("TK-SIDOARJO"), registrationFee=200_000, entryFee={"min": 5_950_000, "max": 7_500_000},
       tuition={"amount": 750_000, "period": "month"}, otherFees=[fee("Uang kegiatan TK A", "Activity fee TK A", 1_600_000), fee("Uang kegiatan TK B", "Activity fee TK B", 1_700_000)],
       notes=L("Uang sarana dan pengembangan: early bird / jalur expo Rp5.950.000; gelombang 1 Rp7.000.000; gelombang 2 Rp7.500.000 (berlaku sampai lulus TK B). Seragam ± Rp500.000. " + SIB[0],
               "Facilities & development fee: early bird / expo track Rp5,950,000; wave 1 Rp7,000,000; wave 2 Rp7,500,000 (covers up to TK B). Uniforms ~Rp500,000. " + SIB[1]), **SDA)
upsert("sekolah-santa-maria-ii-sidoarjo", level="SD", source=SM("SD-SIDOARJO"), registrationFee=225_000, entryFee={"min": 9_000_000, "max": 10_000_000},
       tuition={"amount": 855_000, "period": "month"}, otherFees=[fee("Uang kegiatan", "Activity fee", 1_850_000), fee("Seragam (perkiraan)", "Uniforms (approx.)", 900_000), fee("Buku (perkiraan)", "Books (approx.)", 650_000)],
       notes=L("Gelombang 1: jalur khusus (dari TK Santa Maria) Rp9.000.000 dengan SPP Rp855.000; jalur umum Rp10.000.000 dengan SPP Rp900.000. Gelombang 2 jalur khusus Rp10.000.000, SPP Rp900.000. Potongan 5% jika uang pengembangan lunas. " + SIB[0],
               "Wave 1: special track (from TK Santa Maria) Rp9,000,000 with tuition Rp855,000; general track Rp10,000,000 with tuition Rp900,000. Wave 2 special track Rp10,000,000, tuition Rp900,000. 5% off if the development fee is paid in full. " + SIB[1]), **SDA)
upsert("sekolah-santa-maria-ii-sidoarjo", level="SMP", source=SM("SMP-SIDOARJO"), registrationFee=250_000, entryFee={"min": 10_000_000},
       tuition={"amount": 900_000, "period": "month"}, otherFees=[fee("Uang kegiatan", "Activity fee", 1_905_000), fee("Seragam (perkiraan)", "Uniforms (approx.)", 1_000_000)],
       notes=L("Gelombang II: jalur khusus SPP Rp900.000; jalur umum SPP Rp950.000. Uang pengembangan bisa dicicil (50% lalu 5 kali angsuran); lunas dapat potongan 5% dan 1 stel seragam olahraga. " + SIB[0],
               "Wave II: special track tuition Rp900,000; general track Rp950,000. Development fee can be paid in instalments (50%, then 5 monthly payments); paying in full gets 5% off and a sports uniform. " + SIB[1]), **SDA)

SIG = {"title": "SPMB SMP SIG (Semen Gresik) TA 2027/2028 (situs resmi)", "url": "https://ppdb.smpsemengresik.sch.id/"}
upsert("smp-sig-semen-gresik", name="SMP SIG (Semen Gresik)", city="Gresik", district="Kebomas", address="Kebomas, Gresik", website="https://ppdb.smpsemengresik.sch.id",
       level="SMP", year="2027/2028", source=SIG, checked=CHK, registrationFee=0, entryFee={"min": 6_350_000, "max": 7_500_000},
       notes=L("Biaya masuk normal Rp7.500.000; potongan menurut gelombang dan kategori (mis. gelombang 1 Rp7.000.000; anak keluarga SIG gelombang 1 Rp6.350.000) plus gratis SPP 1–3 bulan. Gratis formulir, seragam, ekstrakurikuler, ujian, dan daftar ulang kenaikan kelas. Besaran SPP tidak dicantumkan.",
               "Normal entry fee Rp7,500,000; discounts by wave and category (e.g. wave 1 Rp7,000,000; SIG employees' children in wave 1 Rp6,350,000) plus 1–3 months' free tuition. Free form, uniforms, extracurriculars, exams and annual re-registration. Monthly tuition not listed."))
print("ok")
