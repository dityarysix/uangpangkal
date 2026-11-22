"""Official 2027/2028 pages:
- Yayasan Darut Taqwa (Pondok Pesantren Ngalah), Sengonagung, Purwosari, Kab. Pasuruan: https://ppdb.daruttaqwa.or.id/
- SMA Muhammadiyah 1 Taman, Sidoarjo: https://ppdb.smam1ta.sch.id/biaya
Skipped: PMDI (Palima, Serang — outside our areas)."""
from seedlib import L, fee, upsert, add_admission

CHK = "2026-11-22"
DT = {"title": "PPDB Periode 2027-2028 — Yayasan Darut Taqwa (situs resmi)", "url": "https://ppdb.daruttaqwa.or.id/"}
DTS = dict(name="Yayasan Darut Taqwa (Ngalah) Pasuruan", city="Kabupaten Pasuruan", district="Purwosari", religion="Islam",
           address="Jl. Pesantren Ngalah, Sengonagung, Purwosari, Kabupaten Pasuruan", website="https://ppdb.daruttaqwa.or.id",
           year="2027/2028", source=DT, checked=CHK)
POND = ("Biaya awal sekolah sesuai lembaga (rincian komponen tidak ditampilkan). Bila sekaligus mondok di Pondok Pesantren Ngalah ditambah biaya pondok Rp2.400.000. ",
        "Initial school payment by institution (component breakdown not shown). Boarding at Pondok Pesantren Ngalah adds Rp2,400,000. ")
upsert("yayasan-darut-taqwa-pasuruan", level="SD", entryFee={"min": 782_000, "max": 851_000},
       notes=L(POND[0] + "MI Darut Taqwa (setara SD): laki-laki Rp782.000, perempuan Rp851.000.", POND[1] + "MI Darut Taqwa (primary): boys Rp782,000, girls Rp851,000."), **DTS)
upsert("yayasan-darut-taqwa-pasuruan", level="SMP", entryFee={"min": 3_300_000},
       notes=L(POND[0] + "MTs Darut Taqwa 02 dan SMP Bhinneka Tunggal Ika: Rp3.300.000 (dengan pondok Rp5.700.000).", POND[1] + "MTs Darut Taqwa 02 and SMP Bhinneka Tunggal Ika: Rp3,300,000 (with boarding Rp5,700,000)."), **DTS)
upsert("yayasan-darut-taqwa-pasuruan", level="SMA", entryFee={"min": 3_400_000},
       notes=L(POND[0] + "MA dan SMA Darut Taqwa (bahasa & budaya, IPS, MIPA): Rp3.400.000 (dengan pondok Rp5.800.000).", POND[1] + "MA and SMA Darut Taqwa (languages, social sciences, science): Rp3,400,000 (with boarding Rp5,800,000)."), **DTS)
upsert("yayasan-darut-taqwa-pasuruan", level="SMK", entryFee={"min": 3_750_000},
       notes=L(POND[0] + "SMK Darut Taqwa (mis. bisnis daring, DKV): Rp3.750.000 (dengan pondok Rp6.150.000).", POND[1] + "SMK Darut Taqwa (e.g. online business, visual design): Rp3,750,000 (with boarding Rp6,150,000)."), **DTS)
add_admission("yayasan-darut-taqwa-pasuruan", {"academicYear": "2027/2028",
    "period": L("Daftar online lewat aplikasi Ngalah Mobile sampai 30 Juni 2027.", "Register online in the Ngalah Mobile app until 30 June 2027."),
    "steps": [L("Masuk aplikasi dengan nomor WhatsApp wali (kode dikirim via WhatsApp) dan isi pendaftaran.", "Log in to the app with the guardian's WhatsApp number (code sent via WhatsApp) and register."),
              L("Bila tidak bisa daftar sendiri, datang ke kantor panitia (Sabtu–Kamis 08.00–14.00), Kantor Yayasan Darut Taqwa lt. 3, area Duta Swalayan.", "If you cannot register yourself, visit the committee office (Sat–Thu 08:00–14:00), Yayasan Darut Taqwa office, 3rd floor, Duta Swalayan area.")],
    "notes": L("Alumni MI, MTs, dan SMP Darut Taqwa mendapat potongan biaya pendaftaran Rp100.000.", "Alumni of the foundation's MI, MTs and SMP get Rp100,000 off registration."), "source": DT, "checked": CHK})

SM = {"title": "Biaya Pendaftaran SPMB SMA Muhammadiyah 1 Taman TA 2027/2028 (situs resmi)", "url": "https://ppdb.smam1ta.sch.id/biaya"}
upsert("sma-muhammadiyah-1-taman-sidoarjo", name="SMA Muhammadiyah 1 Taman Sidoarjo", city="Sidoarjo", district="Taman", religion="Islam",
       address="Jl. Raya Ketegan No.35, Taman, Sidoarjo", website="https://ppdb.smam1ta.sch.id", level="SMA", year="2027/2028", source=SM, checked=CHK,
       entryFee={"min": 10_000_000}, tuition={"amount": 800_000, "period": "month"},
       otherFees=[fee("Uang kegiatan (Excellent/Tahfidz)", "Activity fee (Excellent/Tahfidz)", 4_250_000), fee("Uang kegiatan (M-ICO)", "Activity fee (M-ICO)", 6_750_000),
                  fee("Seragam laki-laki", "Uniforms (boys)", 1_800_000), fee("Seragam perempuan", "Uniforms (girls)", 2_100_000),
                  fee("Student exchange Singapura–Malaysia (opsional)", "Singapore–Malaysia student exchange (optional)", 10_000_000)],
       notes=L("SPP Juli 2027: Excellent Class Rp800.000; M-ICO Rp1.200.000; Tahfidz Rp1.000.000. Total laki-laki: Rp16.975.000 / Rp19.875.000 / Rp17.175.000; perempuan: Rp17.275.000 / Rp20.175.000 / Rp17.475.000.",
               "July 2027 tuition: Excellent Class Rp800,000; M-ICO Rp1,200,000; Tahfidz Rp1,000,000. Totals for boys: Rp16,975,000 / Rp19,875,000 / Rp17,175,000; girls: Rp17,275,000 / Rp20,175,000 / Rp17,475,000."))
print("ok")
