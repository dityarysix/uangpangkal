"""GoBekasi, "Mau Daftarin Anak Sekolah Dasar? Ini 5 SD Swasta Populer di Bekasi dan Biayanya" (26 Oct 2025).
The article says these schools opened registration for 2026/2027. Figures copied verbatim."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

SRC = {"title": "5 SD Swasta Populer di Bekasi dan Biayanya (GoBekasi)",
       "url": "https://gobekasi.id/2025/10/26/mau-daftarin-anak-sekolah-dasar-ini-5-sd-swasta-populer-di-bekasi-dan-biayanya/",
       "published": "2025-10-26"}
C = dict(city="Kota Bekasi", level="SD", year="2026/2027", source=SRC, checked="2026-11-22")

upsert("global-prestasi-school-bekasi", name="Global Prestasi School Bekasi", curriculum=["Cambridge"],
       address="Jl. K.H. Noer Alie No.10B, Bekasi",
       registrationFee=600_000, entryFee={"min": 60_000_000}, tuition={"amount": 12_900_000, "period": "quarter"},
       otherFees=[fee("Uang aktivitas", "Activity fee", 3_870_000), fee(*BOOKS, 2_500_000), fee(*UNIFORM, 1_600_000)],
       notes=L("Uang pangkal untuk 6 tahun. SPP Rp12.900.000 per 3 bulan atau Rp47.300.000 per tahun.", "Entry fee covers 6 years. Tuition Rp12,900,000 per quarter or Rp47,300,000 per year."), **C)
upsert("global-insani-islamic-school-bekasi", name="Global Insani Islamic School Bekasi", district="Medan Satria", religion="Islam",
       address="Jl. Duta Bumi Raya No.1, Pejuang, Bekasi",
       registrationFee=500_000, entryFee={"min": 25_000_000}, **C)
upsert("sd-islam-al-azhar-44-summarecon-bekasi", name="SD Islam Al-Azhar 44 Summarecon Bekasi", district="Bekasi Utara", religion="Islam",
       address="Jl. Bulevar Utara Blok L, Marga Mulya, Bekasi Utara, Kota Bekasi",
       registrationFee=850_000, entryFee={"min": 38_500_000}, tuition={"amount": 2_350_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 2_550_000), fee(*BOOKS, 2_450_000), fee("ATK", "Stationery", 950_000)], **C)
upsert("sekolah-victory-plus-bekasi", name="Sekolah Victory Plus Bekasi", district="Rawalumbu",
       address="Citra Niaga Raya Blok AO 1-14, Kemang Pratama, Bekasi",
       registrationFee=500_000, entryFee={"min": 15_334_000}, tuition={"amount": 17_850_000, "period": "quarter"},
       notes=L("Sumber menyebut uang pangkal Rp15.334.000 per tahun.", "The source lists the entry fee as Rp15,334,000 per year."), **C)
upsert("sekolah-alam-bekasi", name="Sekolah Alam Bekasi", district="Jatisampurna", curriculum=["Sekolah Alam"],
       address="Jl. Raya Hankam No.99, Jatiranggon, Jatisampurna, Kota Bekasi",
       registrationFee=650_000, entryFee={"min": 25_000_000}, tuition={"amount": 1_400_000, "period": "month"},
       otherFees=[fee(*UNIFORM, 600_000), fee("Parents orientation", "Parents' orientation", 1_400_000), fee("Program pembelajaran 1 tahun", "One-year learning programme", 5_000_000)], **C)
print("ok")
