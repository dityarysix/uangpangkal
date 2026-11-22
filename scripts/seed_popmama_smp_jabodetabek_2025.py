"""Popmama, "20 Biaya Sekolah SMP Swasta Jabodetabek 2025" (8 Dec 2024).
Only schools whose city is clear and not already covered by newer data. The article does not state the
academic year; published Dec 2024 for the 2025 intake -> 2025/2026, yearAssumed=True. Figures verbatim."""
from seedlib import L, fee, upsert, UNIFORM, ACTIVITY, BOOKS

SRC = {"title": "20 Biaya Sekolah SMP Swasta Jabodetabek 2025 (Popmama)",
       "url": "https://www.popmama.com/big-kid/10-12-years-old/20-biaya-sekolah-smp-swasta-jabodetabek-2025-00-58r8y-pymtjw",
       "published": "2024-12-08"}
C = dict(level="SMP", year="2025/2026", yearAssumed=True, source=SRC, checked="2026-11-22")

upsert("smp-islam-raden-patah-depok", name="SMP Islam Raden Patah Depok", city="Depok", religion="Islam", website="https://radenpatah.sch.id",
       registrationFee=400_000, entryFee={"min": 11_000_000, "max": 13_000_000}, tuition={"amount": 700_000, "period": "month"}, **C)
upsert("budi-cendekia-islamic-school-depok", name="Budi Cendekia Islamic School Depok", city="Depok", religion="Islam", website="https://bcischool.sch.id",
       address="Jl. Boulevard, Kalimulya, Grand Depok City, Depok",
       registrationFee=750_000, entryFee={"min": 19_750_000}, tuition={"amount": 2_100_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 1_800_000), fee("OSIS & Pramuka", "Student council & scouts", 200_000)], **C)
upsert("smp-nasional-plus-tunas-global-depok", name="SMP Nasional Plus Tunas Global Depok", city="Depok", curriculum=["Nasional Plus"], website="https://tunasglobaldepok.com",
       registrationFee=500_000, entryFee={"min": 15_000_000}, tuition={"amount": 1_750_000, "period": "month"},
       otherFees=[fee("Uang gedung", "Building fee", 15_000_000), fee(*UNIFORM, 2_385_000), fee("Uang kegiatan (per tahun)", "Activity fee (per year)", 3_500_000),
                  fee("Uang perlengkapan (per tahun)", "Supplies (per year)", 2_000_000)], **C)
upsert("smpit-al-haraki-depok", name="SMPIT Al Haraki Depok", city="Depok", religion="Islam", website="https://smp.alharaki.sch.id",
       registrationFee=550_003, entryFee={"min": 32_500_000}, tuition={"amount": 1_850_000, "period": "month"},
       notes=L("Uang pangkal = investasi biaya pendidikan.", "Entry fee = education investment fee."), **C)
upsert("charis-global-school-cikarang", name="Charis Global School Lippo Cikarang", city="Kabupaten Bekasi", district="Cikarang Selatan", curriculum=["Nasional Plus"],
       address="Lippo Cikarang, Kabupaten Bekasi", website="https://charisglobalschool.com",
       registrationFee=500_000, entryFee={"min": 21_800_000}, tuition={"amount": 2_300_000, "period": "month"},
       otherFees=[fee(*BOOKS, 2_680_000)],
       notes=L("Sumber menyebut angka sebagai perkiraan (\"sekitar\"). Uang pangkal = DPP.", "The source gives these figures as approximate. Entry fee = DPP."), **C)
upsert("sekolah-kesatuan-bogor", name="Sekolah Kesatuan Bogor", city="Kota Bogor", website="https://sekolah-kesatuan.sch.id",
       registrationFee=250_000, entryFee={"min": 14_000_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Tes masuk", "Entrance test", 100_000), fee(*BOOKS, 1_200_000)], **C)
upsert("smpit-insantama-bogor", name="SMPIT Insantama Bogor", city="Kota Bogor", district="Bogor Barat", religion="Islam",
       address="Jl. Hegarmanah IV No.47, Gunungbatu, Bogor Barat, Kota Bogor", phone="(0251) 8363973", website="https://insantama.sch.id",
       registrationFee=600_000, entryFee={"min": 25_000_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Parenting", "Parenting programme", 800_000), fee("Seragam putra", "Uniforms (boys)", 1_530_000), fee("Seragam putri", "Uniforms (girls)", 1_790_000)],
       notes=L("Uang pangkal = infaq pengembangan. Alamat dari direktori sekolah.", "Entry fee = development infaq. Address from school directories."), **C)
print("ok")
