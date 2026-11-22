"""KalderaNews, "Inilah 10 SMP Swasta Terbaik di Yogyakarta, Lengkap dengan Kisaran Biaya Sekolahnya" (8 Jun 2025).
Ranges are as published. Year not stated -> 2025/2026, yearAssumed. Skipped: SMP Budi Utama (no figures)."""
from seedlib import L, fee, upsert

SRC = {"title": "10 SMP Swasta Terbaik di Yogyakarta dengan Kisaran Biaya (KalderaNews)", "url": "https://www.kalderanews.com/2025/06/08/inilah-10-smp-swasta-terbaik-di-yogyakarta-lengkap-dengan-kisaran-biaya-sekolahnya/", "published": "2025-06-08"}
C = dict(level="SMP", year="2025/2026", yearAssumed=True, source=SRC, checked="2026-11-22")
SEM = L("Kisaran biaya pendidikan per semester menurut sumber; ditambah biaya tahunan dan kegiatan.", "Education fee range per semester according to the source; plus annual and activity fees.")

upsert("smp-pangudi-luhur-1-yogyakarta", name="SMP Pangudi Luhur 1 Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Katolik",
       address="Jl. Timoho II No.29, Muja Muju, Umbulharjo, Yogyakarta",
       tuition={"amount": 8_000_000, "period": "semester"}, notes=L(SEM["id"] + " Rp8–12 juta per semester.", SEM["en"] + " Rp8–12 million per semester."), **C)
upsert("smp-stella-duce-1-yogyakarta", name="SMP Stella Duce 1 Yogyakarta", city="Kota Yogyakarta", district="Gondokusuman", religion="Katolik",
       address="Jl. Jenderal Sudirman No.115, Gondokusuman, Yogyakarta",
       entryFee={"min": 10_000_000, "max": 15_000_000}, tuition={"amount": 600_000, "period": "month"},
       notes=L("SPP Rp600–900 ribu per bulan (kisaran).", "Tuition Rp600–900 thousand per month (range)."), **C)
upsert("smpit-abu-bakar-yogyakarta", name="SMPIT Abu Bakar Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Islam",
       address="Jl. Veteran No.48, Umbulharjo, Yogyakarta",
       entryFee={"min": 10_000_000, "max": 15_000_000}, tuition={"amount": 800_000, "period": "month"},
       notes=L("Biaya masuk sesuai program. SPP Rp800 ribu–Rp1 juta per bulan (kisaran).", "Entry fee depends on the programme. Tuition Rp800 thousand–Rp1 million per month (range)."), **C)
upsert("smp-muhammadiyah-2-yogyakarta", name="SMP Muhammadiyah 2 Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Islam",
       address="Jl. Kapas II No.7A, Semaki, Yogyakarta",
       entryFee={"min": 2_800_000}, tuition={"amount": 450_000, "period": "month"},
       otherFees=[fee("Infak", "Infaq", 1_750_000), fee("Dana tahunan", "Annual fee", 3_800_000)],
       notes=L("Uang pangkal = dana pengembangan.", "Entry fee = development fund."), **C)
upsert("smpit-masjid-syuhada-yogyakarta", name="SMPIT Masjid Syuhada Yogyakarta", city="Kota Yogyakarta", district="Gondokusuman", religion="Islam",
       address="Jl. I Dewa Nyoman Oka No.28, Kotabaru, Yogyakarta",
       registrationFee=50_000, tuition={"amount": 470_000, "period": "month"}, **C)
upsert("smp-bpk-penabur-yogyakarta", name="SMP BPK Penabur Yogyakarta", city="Sleman", district="Depok", religion="Kristen",
       address="Jl. Ring Road Utara, Condongcatur, Sleman",
       tuition={"amount": 9_000_000, "period": "semester"}, notes=L(SEM["id"] + " Rp9–14 juta per semester.", SEM["en"] + " Rp9–14 million per semester."), **C)
upsert("smp-islam-al-azhar-26-yogyakarta", name="SMP Islam Al Azhar 26 Yogyakarta", city="Sleman", district="Mlati", religion="Islam",
       tuition={"amount": 7_000_000, "period": "semester"},
       notes=L(SEM["id"] + " Rp7–11 juta per semester. Lokasi menurut data sekolah: Mlati, Sleman.", SEM["en"] + " Rp7–11 million per semester. Location per school registry: Mlati, Sleman."), **C)
upsert("sekolah-bina-anak-sholeh-yogyakarta", name="Sekolah Bina Anak Sholeh (BIAS) Yogyakarta", city="Kota Yogyakarta", district="Umbulharjo", religion="Islam",
       address="Jl. Mendung Warih, Giwangan, Umbulharjo, Yogyakarta",
       notes=L("Sumber tidak mencantumkan biaya SMP BIAS.", "The source does not list fees for BIAS junior high."), **C)
print("ok")
