"""Official SPMB fee table of Rabbaanii Islamic School, wave 1 for academic year 2027/2028 (after discount).
https://rabbaanii.sch.id/spmb/biaya — main campus Cikarang Timur (Kab. Bekasi); boarding campus Ciwidey (Kab. Bandung)."""
from seedlib import L, upsert, add_admission

SRC = {"title": "Biaya Pendidikan SPMB Rabbaanii — Gelombang 1 TA 2027/2028 (situs resmi)", "url": "https://rabbaanii.sch.id/spmb/biaya"}
CHK = "2026-11-22"
COMMON = ("Biaya gelombang 1 setelah diskon (biaya sebelum diskon ada di sorotan Instagram @rabbaanii_official). Uang pangkal sudah termasuk seragam 5 stel (TK 4 stel), buku paket tahun pertama, SPP Juli 2027, dan uang tahunan. DP minimal 25%, sisa maks. 4 bulan. Uang pangkal tidak dapat dikembalikan bila mengundurkan diri.",
          "Wave 1 prices after discount (pre-discount prices are in the @rabbaanii_official Instagram highlights). The entry fee includes 5 uniform sets (TK: 4), first-year textbooks, July 2027 tuition and the annual fee. Minimum 25% down payment, the rest within 4 months. Non-refundable if you withdraw.")
CIK = dict(name="Rabbaanii Islamic School Cikarang", city="Kabupaten Bekasi", district="Cikarang Timur", religion="Islam",
           address="Jl. Cimandiri 8B RT.06/08, Graha Asri, Jatireja, Cikarang Timur, Kabupaten Bekasi", phone="CS 0853-1364-2033",
           website="https://rabbaanii.sch.id", year="2027/2028", source=SRC, checked=CHK)
def n(i, e): return L(COMMON[0] + " " + i, COMMON[1] + " " + e)

upsert("rabbaanii-islamic-school-cikarang", level="TK", registrationFee=250_000, entryFee={"min": 5_050_000, "max": 5_300_000},
       tuition={"amount": 270_000, "period": "month"},
       notes=n("TKIT: uang pangkal Rp5.300.000 (umum) / Rp5.050.000 (alumni/keluarga RIS); uang tahunan Rp1.800.000.",
               "TKIT: entry Rp5,300,000 (general) / Rp5,050,000 (alumni/family); annual fee Rp1,800,000."), **CIK)
upsert("rabbaanii-islamic-school-cikarang", level="SD", registrationFee=500_000, entryFee={"min": 16_500_000, "max": 22_500_000},
       tuition={"amount": 725_000, "period": "month"},
       notes=n("SDIT reguler: uang pangkal Rp18.000.000 (umum) / Rp16.500.000 (alumni/keluarga), SPP Rp725.000. Kelas Inggris: Rp22.500.000 / Rp21.000.000, SPP Rp1.250.000. Uang tahunan Rp2.500.000.",
               "SDIT regular: entry Rp18,000,000 (general) / Rp16,500,000 (alumni/family), tuition Rp725,000. English class: Rp22,500,000 / Rp21,000,000, tuition Rp1,250,000. Annual fee Rp2,500,000."), **CIK)
upsert("rabbaanii-islamic-school-cikarang", level="SMP", registrationFee=500_000, entryFee={"min": 16_700_000, "max": 29_800_000},
       tuition={"amount": 750_000, "period": "month"},
       notes=n("SMPSI fullday: Rp18.200.000 (umum) / Rp16.700.000 (alumni), SPP Rp750.000; kelas Inggris Rp22.500.000 / Rp21.000.000, SPP Rp1.250.000; uang tahunan Rp2.500.000. Boarding (IBS) putra: Rp29.800.000 / Rp27.800.000; putri: Rp24.800.000 / Rp22.800.000; SPP Rp3.300.000; uang tahunan Rp3.500.000.",
               "SMPSI day school: Rp18,200,000 (general) / Rp16,700,000 (alumni), tuition Rp750,000; English class Rp22,500,000 / Rp21,000,000, tuition Rp1,250,000; annual fee Rp2,500,000. Boarding (IBS) boys: Rp29,800,000 / Rp27,800,000; girls: Rp24,800,000 / Rp22,800,000; tuition Rp3,300,000; annual fee Rp3,500,000."), **CIK)
upsert("rabbaanii-islamic-school-cikarang", level="SMA", registrationFee=500_000, entryFee={"min": 14_500_000, "max": 35_300_000},
       tuition={"amount": 650_000, "period": "month"},
       notes=n("SMAI Putri fullday: Rp16.500.000 (umum) / Rp14.500.000 (alumni), SPP Rp650.000; kelas Inggris Rp22.500.000 / Rp21.500.000, SPP Rp1.250.000; uang tahunan Rp3.500.000. Boarding (IBS) putra: Rp35.300.000 / Rp33.300.000; putri: Rp30.300.000 / Rp28.300.000; SPP Rp3.300.000; uang tahunan Rp4.000.000.",
               "SMAI girls' day school: Rp16,500,000 (general) / Rp14,500,000 (alumni), tuition Rp650,000; English class Rp22,500,000 / Rp21,500,000, tuition Rp1,250,000; annual fee Rp3,500,000. Boarding (IBS) boys: Rp35,300,000 / Rp33,300,000; girls: Rp30,300,000 / Rp28,300,000; tuition Rp3,300,000; annual fee Rp4,000,000."), **CIK)

BDG = dict(name="Rabbaanii Islamic Boarding School Bandung (Ciwidey)", city="Kabupaten Bandung", district="Ciwidey", religion="Islam",
           phone="CS 0853-1364-2033", website="https://rabbaanii.sch.id", year="2027/2028", source=SRC, checked=CHK)
upsert("rabbaanii-ibs-bandung-ciwidey", level="SMP", registrationFee=500_000, entryFee={"min": 22_800_000, "max": 24_800_000},
       tuition={"amount": 3_300_000, "period": "month"},
       notes=n("Boarding khusus putra. Uang pangkal Rp24.800.000 (umum) / Rp22.800.000 (alumni/keluarga). Uang tahunan Rp3.500.000.",
               "Boys' boarding only. Entry Rp24,800,000 (general) / Rp22,800,000 (alumni/family). Annual fee Rp3,500,000."), **BDG)
upsert("rabbaanii-ibs-bandung-ciwidey", level="SMA", registrationFee=500_000, entryFee={"min": 28_300_000, "max": 30_300_000},
       tuition={"amount": 3_300_000, "period": "month"},
       notes=n("Boarding khusus putra. Uang pangkal Rp30.300.000 (umum) / Rp28.300.000 (alumni/keluarga). Uang tahunan Rp4.000.000.",
               "Boys' boarding only. Entry Rp30,300,000 (general) / Rp28,300,000 (alumni/family). Annual fee Rp4,000,000."), **BDG)
for slug in ("rabbaanii-islamic-school-cikarang", "rabbaanii-ibs-bandung-ciwidey"):
    add_admission(slug, {"academicYear": "2027/2028",
        "period": L("Gelombang 1 mulai 15 September 2026; tes online 16 Oktober dan tes offline 17 Oktober 2026.", "Wave 1 from 15 September 2026; online test 16 October and in-person test 17 October 2026."),
        "steps": [L("Daftar online di rabbaanii.sch.id dan bayar formulir.", "Register online at rabbaanii.sch.id and pay the form fee."),
                  L("Ikuti tes online dan offline sesuai jadwal gelombang.", "Take the online and in-person tests on the wave's dates."),
                  L("Daftar ulang: bayar DP uang pangkal minimal 25%.", "Re-register by paying at least 25% of the entry fee.")],
        "notes": L("Untuk pindahan dan pengajuan subsidi/beasiswa hubungi CS 0853-1364-2033.", "For transfers and subsidy/scholarship requests contact CS 0853-1364-2033."),
        "source": SRC, "checked": CHK})
print("ok")
