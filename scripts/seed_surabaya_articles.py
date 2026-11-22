"""Surabaya SD articles (figures verbatim; approximations labelled):
- IDN Times, "Biaya Masuk SD Swasta di Surabaya 24/25, Seharga DP Rumah" (31 Oct 2024) -> 2024/2025 as titled.
- Akurat, "10 SD Swasta Terbaik di Surabaya 2025: Biaya, Fasilitas, dan Keunggulannya" (16 Dec 2025) -> 2025/2026, yearAssumed, estimates.
- Mamikita, "7 SD Swasta di Surabaya Terbaik, Lengkap dengan Rincian Biayanya" (25 Feb 2024) -> 2024/2025, yearAssumed."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS

CHK = "2026-11-22"
IDN = {"title": "Biaya Masuk SD Swasta di Surabaya 24/25, Seharga DP Rumah (IDN Times)", "url": "https://www.idntimes.com/life/family/biaya-masuk-sd-swasta-di-surabaya-2024-2025-seharga-dp-rumah-01-7cxy7-0dtrhr", "published": "2024-10-31"}
AK = {"title": "10 SD Swasta Terbaik di Surabaya 2025: Biaya, Fasilitas, dan Keunggulannya (Akurat)", "url": "https://www.akurat.co/pendidikan/824267/10-sd-swasta-terbaik-di-surabaya-2025-biaya-fasilitas-dan-keunggulannya", "published": "2025-12-16"}
MK = {"title": "7 SD Swasta di Surabaya Terbaik, Lengkap dengan Rincian Biayanya (Mamikita)", "url": "https://mamikita.com/sd-swasta-di-surabaya/", "published": "2024-02-25"}
I = dict(city="Surabaya", level="SD", year="2024/2025", source=IDN, checked=CHK)
A = dict(city="Surabaya", level="SD", year="2025/2026", yearAssumed=True, source=AK, checked=CHK)
M = dict(city="Surabaya", level="SD", year="2024/2025", yearAssumed=True, source=MK, checked=CHK)
EST = L("Perkiraan biaya menurut sumber.", "Estimated fees according to the source.")

upsert("sd-muhammadiyah-4-pucang-surabaya", name="SD Muhammadiyah 4 Pucang Surabaya", religion="Islam", curriculum=["Cambridge"], website="https://mudipat.co",
       entryFee={"min": 16_500_000, "max": 17_000_000}, tuition={"amount": 1_450_000, "period": "month"},
       otherFees=[fee("Biaya kegiatan sekolah (reguler)", "School activity fee (regular)", 3_850_000), fee("Seragam & perlengkapan putra", "Uniforms & supplies (boys)", 2_970_000), fee("Seragam & perlengkapan putri", "Uniforms & supplies (girls)", 3_810_000)],
       notes=L("Program reguler: DPP Rp16,5 juta, SPP Rp1,45 juta, BKS Rp3,85 juta (total masuk putra Rp24,7 juta / putri Rp25,6 juta). Program Cambridge: DPP Rp17 juta, SPP Rp1,75 juta, BKS Rp4,61 juta (total Rp26,335 juta / Rp27,175 juta).",
               "Regular programme: development fee Rp16.5M, tuition Rp1.45M, activity fee Rp3.85M (total on entry boys Rp24.7M / girls Rp25.6M). Cambridge programme: Rp17M, Rp1.75M, Rp4.61M (total Rp26.335M / Rp27.175M)."), **I)
upsert("sekolah-alam-insan-mulia-surabaya", name="Sekolah Alam Insan Mulia (SAIM) Surabaya", religion="Islam", curriculum=["Sekolah Alam"],
       entryFee={"min": 26_000_000}, tuition={"amount": 2_160_000, "period": "month"},
       otherFees=[fee("Daftar ulang", "Re-registration", 3_800_000), fee("Iuran Forsaim", "Forsaim contribution", 10_000)],
       notes=L("Bisa dicicil: pembayaran awal Rp10.410.000 lalu 5 termin @Rp3.120.000.", "Can be paid in instalments: Rp10,410,000 upfront then 5 instalments of Rp3,120,000."), **I)
upsert("sekolah-alam-insan-mulia-surabaya", name="Sekolah Alam Insan Mulia (SAIM) Surabaya", registrationFee=350_000, entryFee={"min": 20_000_000},
       tuition={"amount": 1_800_000, "period": "month"}, notes=EST, **A)
upsert("sd-al-hikmah-surabaya", name="SD Al Hikmah Surabaya", religion="Islam",
       entryFee={"min": 34_000_000}, otherFees=[fee("Dana pengembangan pendidikan", "Education development fund", 2_850_000), fee("Biaya penyelenggaraan pendidikan", "Education operating fee", 2_200_000)],
       notes=L("Uang pangkal = infaq. Total Rp39,05 juta belum termasuk seragam dan buku.", "Entry fee = infaq. Total Rp39.05 million excluding uniforms and books."), **I)
upsert("sd-al-hikmah-surabaya", name="SD Al Hikmah Surabaya", registrationFee=500_000, entryFee={"min": 30_500_000}, tuition={"amount": 1_900_000, "period": "month"},
       otherFees=[fee("Biaya pengembangan pendidikan", "Education development fee", 2_500_000)], notes=L("Uang pangkal = infaq.", "Entry fee = infaq."), **M)
upsert("sd-khadijah-2-surabaya", name="SD Khadijah 2 Surabaya", religion="Islam", address="Jl. Darmo Permai Selatan V/61-63, Surabaya",
       registrationFee=400_000, entryFee={"min": 9_500_000}, tuition={"amount": 700_000, "period": "month"},
       otherFees=[fee("Uang kegiatan per tahun", "Activity fee per year", 900_000), fee("Buku per tahun", "Books per year", 1_250_000), fee("Seragam putra", "Uniforms (boys)", 1_400_000),
                  fee("Seragam putri", "Uniforms (girls)", 1_500_000), fee("Kegiatan ICP", "ICP activities", 1_700_000)],
       notes=L("Uang pangkal = infaq. Total kelas reguler Rp14.150.000 (putra) / Rp14.250.000 (putri); kelas ICP Rp15.850.000 / Rp15.950.000. Inden Rp1.000.000 memberi potongan infaq Rp1.000.000 (sampai 30 September 2024).",
               "Entry fee = infaq. Regular class total Rp14,150,000 (boys) / Rp14,250,000 (girls); ICP class Rp15,850,000 / Rp15,950,000. An Rp1,000,000 early deposit gave Rp1,000,000 off the infaq (until 30 September 2024)."), **I)
upsert("sd-khadijah-surabaya", name="SD Khadijah Surabaya", religion="Islam",
       registrationFee=400_000, entryFee={"min": 11_000_000}, tuition={"amount": 700_000, "period": "month"},
       otherFees=[fee("Biaya kegiatan", "Activity fee", 1_700_000), fee(*UNIFORM, 1_700_000), fee(*BOOKS, 1_000_000)],
       notes=L("Uang pangkal = infaq. Sumber tidak menyebut kampus.", "Entry fee = infaq. The source does not name the campus."), **M)
upsert("sekolah-ciputra-surabaya", name="Sekolah Ciputra Surabaya", curriculum=["IB"], address="Citra Raya, Surabaya Barat", website="https://sekolahciputra.sch.id",
       entryFee={"min": 21_250_000, "max": 68_500_000}, tuition={"amount": 61_910_000, "period": "year"},
       notes=L("DPP SD Rp21.250.000–Rp68.500.000; SPP tahunan Rp61.910.000–Rp68.110.000 (tergantung kelas).", "SD development fee Rp21,250,000–Rp68,500,000; annual tuition Rp61,910,000–Rp68,110,000 (depending on grade)."), **I)
upsert("sekolah-ciputra-surabaya", name="Sekolah Ciputra Surabaya", registrationFee=2_500_000, entryFee={"min": 92_990_000}, tuition={"amount": 70_900_000, "period": "year"},
       notes=L(EST["id"] + " Uang pangkal = development fee.", EST["en"] + " Entry fee = development fee."), **A)
upsert("sdit-at-taqwa-2-surabaya", name="SDIT At-Taqwa 2 Surabaya", district="Wiyung", religion="Islam", address="Jl. Griya Babatan Mukti, Wiyung, Surabaya", website="https://sekolahattaqwa.sch.id",
       entryFee={"min": 7_875_000}, tuition={"amount": 980_000, "period": "month"},
       otherFees=[fee("Dana pengembangan pendidikan", "Education development fund", 1_800_000), fee("Uang peralatan", "Supplies", 1_700_000), fee(*UNIFORM, 1_300_000)],
       notes=L("Uang pangkal = infaq jariyah.", "Entry fee = infaq jariyah."), **I)
upsert("surabaya-european-school", name="Surabaya European School (SES)", curriculum=["Internasional"],
       registrationFee=39_900_000, otherFees=[fee("Total biaya tahunan (perkiraan, maks.)", "Total annual cost (estimate, max.)", 271_000_000)],
       notes=L(EST["id"] + " Total biaya tahunan Rp269–271 juta.", EST["en"] + " Total annual cost Rp269–271 million."), **A)
upsert("sd-katolik-santo-yosef-surabaya", name="SD Katolik Santo Yosef Surabaya", religion="Katolik",
       entryFee={"min": 7_000_000}, tuition={"amount": 700_000, "period": "month"}, notes=EST, **A)
upsert("sd-islam-al-azhar-35-surabaya", name="SD Islam Al Azhar 35 Surabaya", registrationFee=400_000, entryFee={"min": 31_000_000},
       tuition={"amount": 2_200_000, "period": "month"}, notes=EST, **A)
upsert("surabaya-intercultural-school", name="Surabaya Intercultural School (SIS)", registrationFee=20_000_000, entryFee={"min": 30_000_000},
       notes=L(EST["id"] + " Pendaftaran sekitar Rp20 juta, uang gedung Rp30 juta, SPP tahunan \"relatif tinggi\".", EST["en"] + " Registration about Rp20M, building fee Rp30M, annual tuition \"relatively high\"."), **A)
print("ok")
