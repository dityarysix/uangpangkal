"""Solo Raya schools.
- SD Islam Al Fattah Surakarta, official post for 2027/2028:
  https://sdislamalfattah.com/blog/2026/08/12/penerimaan-murid-baru-tahun-pelajaran-2027-2028-sd-islam-al-fattah-surakarta/
- SD Muhammadiyah Alam Surya Mentari (Sekolah Alam Solo), official SPMB 2027/2028 page (registration fee only):
  https://www.sekolahalamsolo.sch.id/p/info-pendaftaran.html
- Mamikita, "7 SD Swasta di Solo, Lengkap Dengan Rincian Biayanya" (28 Feb 2024): only schools whose location is clear.
  Year not stated -> 2024/2025, yearAssumed. Skipped: schools without a clear location, and a homeschooling programme."""
from seedlib import L, fee, upsert, add_admission, UNIFORM

CHK = "2026-11-22"
AF = {"title": "Penerimaan Murid Baru TP 2027/2028 SD Islam Al Fattah Surakarta (situs resmi)",
      "url": "https://sdislamalfattah.com/blog/2026/08/12/penerimaan-murid-baru-tahun-pelajaran-2027-2028-sd-islam-al-fattah-surakarta/", "published": "2026-08-12"}
upsert("sd-islam-al-fattah-surakarta", name="SD Islam Al Fattah Surakarta", city="Surakarta (Solo)", district="Banjarsari", religion="Islam",
       address="Jl. Menteri Supeno No.16A, Manahan, Banjarsari, Surakarta", website="https://sdislamalfattah.com",
       level="SD", year="2027/2028", source=AF, checked=CHK,
       registrationFee=200_000, entryFee={"min": 5_000_000}, tuition={"amount": 300_000, "period": "month"},
       notes=L("Uang pangkal = biaya kelengkapan murid baru (tunai atau diangsur sesuai kesepakatan saat wawancara), termasuk seragam lengkap 5 stel dan buku paket 1 tahun. Biaya bulanan disebut infaq pendidikan; Rp300.000 adalah angka untuk kelas 1 tahun 2026/2027 dan sudah mencakup buku paket. Tidak ada biaya daftar ulang.",
               "Entry fee = new-student package (cash or instalments agreed at the interview), including 5 full uniform sets and a year of textbooks. The monthly fee is called an education infaq; Rp300,000 is the figure for grade 1 in 2026/2027 and covers textbooks. No re-registration fees."))
add_admission("sd-islam-al-fattah-surakarta", {"level": "SD", "academicYear": "2027/2028",
    "steps": [L("Isi formulir pendaftaran dan bayar biaya pendaftaran Rp200.000.", "Fill in the registration form and pay the Rp200,000 registration fee."),
              L("Ikuti tes seleksi (jadwal diinformasikan kemudian).", "Attend the selection test (date to be announced)."),
              L("Jika diterima, bayar biaya kelengkapan murid baru.", "If accepted, pay the new-student package fee.")],
    "documents": [L("Fotokopi akta kelahiran (1 lembar)", "Copy of birth certificate (1)"), L("Fotokopi Kartu Keluarga (1 lembar)", "Copy of family card (1)"),
                  L("Fotokopi ijazah TK/RA (tidak wajib)", "Copy of kindergarten certificate (optional)")],
    "test": L("Tes kesiapan belajar (calon murid) dan wawancara orang tua/wali.", "School-readiness test (child) and parent/guardian interview."),
    "notes": L("Usia minimal 6 tahun per 1 Juli 2027.", "Minimum age 6 by 1 July 2027."), "source": AF, "checked": CHK})

ASM = {"title": "Info Pendaftaran SPMB 2027/2028 — SD Muhammadiyah Alam Surya Mentari (situs resmi)", "url": "https://www.sekolahalamsolo.sch.id/p/info-pendaftaran.html"}
upsert("sd-muhammadiyah-alam-surya-mentari-surakarta", name="SD Muhammadiyah Alam Surya Mentari Surakarta", city="Surakarta (Solo)", district="Laweyan",
       religion="Islam", curriculum=["Sekolah Alam"], address="Jl. Mangga VI, Jajar, Laweyan, Surakarta", website="https://www.sekolahalamsolo.sch.id",
       level="SD", year="2027/2028", source=ASM, checked=CHK, registrationFee=300_000,
       notes=L("Situs hanya mencantumkan biaya pendaftaran; uang pangkal dan SPP tidak dipublikasikan.", "The site only lists the registration fee; entry fee and tuition are not published."))

MK = {"title": "7 SD Swasta di Solo, Lengkap Dengan Rincian Biayanya (Mamikita)", "url": "https://mamikita.com/7-sd-swasta-di-solo-lengkap-dengan-rincian-biayanya/", "published": "2024-02-28"}
C = dict(level="SD", year="2024/2025", yearAssumed=True, source=MK, checked=CHK)
upsert("sd-lazuardi-kamila-surakarta", name="SD Lazuardi Kamila Surakarta", city="Surakarta (Solo)", religion="Islam",
       registrationFee=325_000, entryFee={"min": 9_750_000}, tuition={"amount": 750_000, "period": "month"},
       otherFees=[fee("Uang semester", "Semester fee", 1_300_000), fee(*UNIFORM, 750_000)], **C)
upsert("sd-muhammadiyah-pk-kottabarat-surakarta", name="SD Muhammadiyah Program Khusus Kottabarat Surakarta", city="Surakarta (Solo)", religion="Islam",
       entryFee={"min": 11_750_000, "max": 12_750_000}, tuition={"amount": 1_400_000, "period": "month"},
       notes=L("Biaya masuk mencakup uang pengembangan, seragam, dan pengembangan laboratorium. SPP mencakup fieldtrip, outing, kemah, LKSD, katering, snack, dan ekstrakurikuler.",
               "Entry fee covers development, uniforms and lab development. Tuition covers field trips, outings, camp, workbooks, catering, snacks and extracurriculars."), **C)
upsert("sd-mim-pk-kartasura", name="SD MIM PK Kartasura", city="Sukoharjo", district="Kartasura", religion="Islam",
       otherFees=[fee("Paket biaya tahun pertama", "First-year fee package", 9_000_000)],
       notes=L("Sekolah inklusi. Sumber menyebut dana Rp9.000.000 sudah termasuk seragam, SPP, tes MIR, kegiatan operasional, dan buku selama setahun.",
               "Inclusive school. The source says Rp9,000,000 covers uniforms, tuition, MIR test, operations and books for a year."), **C)
print("ok")
