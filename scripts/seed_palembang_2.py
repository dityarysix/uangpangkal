"""Palembang Raya, round 2.
- Sekolah Alam Palembang (SaPa), official PPDB page for Tahun Pelajaran 2026-2027 (TK, SD, SMP, SMA).
- Kanya.ID, "Rekomendasi SD Swasta di Medan dan Palembang" (21 Oct 2021): -> 2021/2022 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM

CHK = "2026-11-22"
SAPA = {"title": "Pendaftaran Sekolah Alam Palembang TP 2026-2027 (situs resmi)", "url": "https://sekolahalampalembang.com/pendaftaran-sekolah-alam-palembang/"}
C = dict(name="Sekolah Alam Palembang (SAPA)", city="Kota Palembang", district="Jakabaring", address="Jl. Harapan No.101, Silaberanti, Jakabaring, Kota Palembang",
         website="https://sekolahalampalembang.com", year="2026/2027", source=SAPA, checked=CHK)
NOTE = L("Uang pembangunan dibayar sekali, tanpa daftar ulang. Tersedia beasiswa untuk anak dhuafa.", "Building fee paid once, no re-registration. Scholarships available for underprivileged children.")
for lv, dev, uni, spp, test in [("TK", 6_000_000, 1_000_000, 850_000, None), ("SD", 18_000_000, 2_000_000, 950_000, None),
                                ("SMP", 19_000_000, 2_500_000, 1_000_000, 500_000), ("SMA", 20_000_000, 2_500_000, 1_050_000, 750_000)]:
    upsert("sekolah-alam-palembang", level=lv, registrationFee=350_000, entryFee={"min": dev}, tuition={"amount": spp, "period": "month"},
           otherFees=[fee(*UNIFORM, uni)] + ([fee("Tes bakat minat", "Aptitude test", test)] if test else []), notes=NOTE, **C)

KY = {"title": "Rekomendasi SD Swasta di Medan dan Palembang, Serta Informasi Biayanya (Kanya.ID)", "url": "https://www.kanya.id/read/037476/rekomendasi-sd-swasta-di-medan-dan-palembang-serta-informasi-biayanya", "published": "2021-10-21"}
KN = L("Dari artikel 2021; kemungkinan sudah berubah.", "From a 2021 article; likely outdated.")
for slug, name, city, district, addr, pmin, pmax, spp in [
    ("sd-islam-khalifah-annizam-palembang", "SD Islam Khalifah Annizam Palembang", "Kota Palembang", "Alang-Alang Lebar", "Jl. Hasanudin No.6, Talang Kelapa, Alang-Alang Lebar, Kota Palembang", 16_360_000, None, 800_000),
    ("sdit-menara-fitrah-indralaya", "SDIT Menara Fitrah Indralaya", "Ogan Ilir", "Indralaya", "Jl. Lintas Timur Km 35, Indralaya, Ogan Ilir", 8_000_000, 9_000_000, 550_000),
    ("sd-islam-al-alifah-palembang", "SD Islam Al-Alifah Palembang", "Kota Palembang", "Jakabaring", "Jl. Pangeran Ratu, Jakabaring, Kota Palembang", 13_050_000, None, 640_000),
    ("sd-islam-cendikia-faiha-palembang", "SD Islam Cendikia Faiha Palembang", "Kota Palembang", "Sukarami", "Jl. Perindustrian II, Komplek Sukarami Gardena, Kota Palembang", 9_700_000, None, 435_000),
]:
    upsert(slug, name=name, city=city, district=district, address=addr, religion="Islam", level="SD", year="2021/2022", yearAssumed=True, source=KY, checked=CHK,
           entryFee={"min": pmin, **({"max": pmax} if pmax else {})}, tuition={"amount": spp, "period": "month"}, notes=KN)
