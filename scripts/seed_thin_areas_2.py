"""Thin areas, round 2.
- Prokal, "Daftar 13 SMP Swasta di Balikpapan yang Dapat Subsidi SPP dan Uang Pangkal" (14 Jun 2025): partner schools of
  the Balikpapan SPMB 2025/2026, where the city pays uang pangkal Rp1.5M and SPP Rp150k/month per subsidised student.
- MIAS Tasikmalaya, official "Info PSB 2027/2028" page (SMPIT-TQ, SMAIT-TQ)."""
from seedlib import L, fee, upsert, add_admission

CHK = "2026-11-22"
PK = {"title": "Tak Lolos Sekolah Negeri? Ini Daftar 13 SMP Swasta di Balikpapan yang Dapat Subsidi SPP dan Uang Pangkal (Prokal)", "url": "https://www.prokal.co/kalimantan-timur/1776140044/tak-lolos-sekolah-negeri-ini-daftar-13-smp-swasta-di-balikpapan-yang-dapat-subsidi-spp-dan-uang-pangkal", "published": "2025-06-14"}
N = L("Sekolah mitra SPMB Pemkot Balikpapan 2025/2026: untuk siswa yang diterima lewat program ini, uang pangkal Rp1.500.000 dan SPP Rp150.000/bulan dibayar Pemkot (gratis bagi orang tua). Biaya untuk siswa di luar program bisa berbeda; tanyakan ke sekolah. Program berlanjut di 2026/2027 dengan 15 sekolah.",
      "Balikpapan city SPMB partner school 2025/2026: for students admitted through this programme, the city pays the Rp1,500,000 entry fee and Rp150,000/month tuition (free for parents). Fees outside the programme may differ; ask the school. The programme continued in 2026/2027 with 15 schools.")
for slug, name, rel, addr in [
    ("smp-pgri-4-balikpapan", "SMP PGRI 4 Balikpapan", None, "Jl. Indrakila 3, Balikpapan"),
    ("salp-plus-nurul-khairat-balikpapan", "SALP Plus Nurul Khairat Balikpapan", "Islam", "Jl. Sepinggan Baru RT.46, Balikpapan"),
    ("smp-wiyata-mandala-balikpapan", "SMP Wiyata Mandala Balikpapan", None, "Jl. Prona Gang 5 RT.24 No.99, Balikpapan"),
    ("smp-pgri-7-balikpapan", "SMP PGRI 7 Balikpapan", None, "Jl. Bukit Pelajar 1 RT.39, Sidodadi Baru Ulu, Balikpapan"),
    ("smp-al-ula-balikpapan", "SMP Al Ula Balikpapan", "Islam", "Jl. Bukit Pelajar RT.38 No.20, Balikpapan"),
    ("smpit-acsadlyah-manuntung-balikpapan", "SMPIT Acsadlyah Manuntung Balikpapan", "Islam", "Jl. Pandan Sari RT.20 No.137, Margasari, Balikpapan"),
    ("mts-ibnu-khaldun-balikpapan", "MTs Ibnu Khaldun Balikpapan", "Islam", "Jl. Semai RT.13, Margasari, Balikpapan"),
    ("smp-pgri-2-balikpapan", "SMP PGRI 2 Balikpapan", None, "Jl. Mayjen D.I. Panjaitan, Sumber Rejo, Balikpapan"),
    ("smp-sabilal-muhtadin-balikpapan", "SMP Sabilal Muhtadin Balikpapan", "Islam", "Jl. Pangeran Antasari RT.62 No.31, Karang Rejo, Balikpapan"),
    ("mts-sabilal-muhtadin-balikpapan", "MTs Sabilal Muhtadin Balikpapan", "Islam", "Jl. Pangeran Antasari RT.62 No.31, Karang Rejo, Balikpapan"),
    ("smp-ypi-balikpapan", "SMP YPI Balikpapan", None, "Jl. Telaga Sari RT.41 No.1, Balikpapan"),
    ("smp-simar-pancasila-balikpapan", "SMP Simar Pancasila Balikpapan", None, "Jl. Telaga Sari RT.31 No.13, Balikpapan"),
    ("smp-al-hasan-balikpapan", "SMP Al Hasan Balikpapan", "Islam", "Jl. Telaga Sari RT.31 No.14, Balikpapan"),
]:
    upsert(slug, name=name, city="Balikpapan", address=addr, religion=rel, level="SMP", year="2025/2026", source=PK, checked=CHK,
           entryFee={"min": 1_500_000}, tuition={"amount": 150_000, "period": "month"}, notes=N)

MI = {"title": "Info PSB 2027/2028 — MIAS Tasikmalaya (situs resmi)", "url": "https://psb.miastasikmalaya.com/"}
MC = dict(name="MIAS Tasikmalaya", city="Kota Tasikmalaya", district="Cihideung", address="Jl. Terusan BCA No.11, Tuguraja, Cihideung, Tasikmalaya", religion="Islam",
          website="https://psb.miastasikmalaya.com/", year="2027/2028", source=MI, checked=CHK, registrationFee=500_000, entryFee={"min": 13_500_000, "max": 20_000_000}, tuition={"amount": 1_750_000, "period": "month"})
for lv, unit in (("SMP", "SMPIT-TQ"), ("SMA", "SMAIT-TQ")):
    upsert("mias-tasikmalaya", level=lv, notes=L(f"{unit}. Biaya awal masuk Rp20.000.000 (eksternal) / Rp13.500.000 (lulusan MIAS). Halaman menulis alamat \"Kab. Tasikmalaya\"; Kec. Cihideung termasuk Kota Tasikmalaya.",
                                                 f"{unit}. Initial entry Rp20,000,000 (external) / Rp13,500,000 (MIAS graduates). The page says \"Kab. Tasikmalaya\"; Cihideung district is in Kota Tasikmalaya."), **MC)
    add_admission("mias-tasikmalaya", {"level": lv, "academicYear": "2027/2028", "steps": [L("Transfer uang pendaftaran Rp500.000 dan isi formulir (pilih jenjang; SMP: program Reguler/TQ)", "Transfer the Rp500,000 registration fee and fill in the form (choose level; SMP: Regular/TQ programme)"), L("Ikuti seleksi; pengumuman kelulusan 30 September 2026 dan 2 November 2026", "Take the selection; results on 30 September 2026 and 2 November 2026")],
        "documents": [], "source": MI, "checked": CHK})
