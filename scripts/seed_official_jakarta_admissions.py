"""Official admission information for large Jakarta schools.
- HighScope Indonesia Kelapa Gading: campus page with procedures and 2025/2026 fee tables (images)
  https://highscope.or.id/en/network-of-school/shi-kelapa-gading/5
- BINUS SCHOOL Simprug: the school's OpenApply listing (steps from simprug.binus.sch.id/how-to-apply/)
  https://search.openapply.com/schools/1416"""
from seedlib import L, upsert, add_admission

CHK = "2026-11-22"
HS = {"title": "SHI Kelapa Gading — Admissions & Fee Structure 2025/2026 (situs resmi HighScope Indonesia)", "url": "https://highscope.or.id/en/network-of-school/shi-kelapa-gading/5"}
HSS = dict(name="Sekolah HighScope Indonesia Kelapa Gading", city="Jakarta Utara", website="https://highscope.or.id", year="2025/2026", source=HS, checked=CHK)
upsert("highscope-indonesia-kelapa-gading", level="SD", registrationFee=300_000, entryFee={"min": 69_000_000}, tuition={"amount": 5_600_000, "period": "month"},
       notes=L("Enrollment fee kelas 1–6. SPP Grade K–5 Rp5.600.000/bulan; Grade 6 Rp5.900.000/bulan. Biaya pendaftaran = formulir aplikasi; observasi kelas Rp500.000; deposit Rp5.000.000.",
               "Enrolment fee for grades 1–6. Tuition grades K–5 Rp5,600,000/month; grade 6 Rp5,900,000/month. Registration = application form; class observation Rp500,000; deposit Rp5,000,000."), **HSS)
upsert("highscope-indonesia-kelapa-gading", level="SMP", registrationFee=300_000, entryFee={"min": 62_000_000}, tuition={"amount": 5_900_000, "period": "month"},
       notes=L("Enrollment fee kelas 7–9. Observasi & tes Rp500.000; deposit Rp5.000.000.", "Enrolment fee for grades 7–9. Observation & test Rp500,000; deposit Rp5,000,000."), **HSS)
COMMON_NOTE = L("Semua biaya tidak dapat dikembalikan bila orang tua membatalkan pendaftaran sendiri.", "All fees are non-refundable if parents cancel the enrolment themselves.")
add_admission("highscope-indonesia-kelapa-gading", {"level": "SD", "academicYear": "2025/2026",
    "steps": [L("Bagian admission (AAO) menjadwalkan observasi kelas (biaya Rp500.000).", "The admissions office (AAO) schedules a class observation (Rp500,000)."),
              L("AAO menginformasikan hasil observasi; siswa diterima mendapat surat penerimaan.", "AAO shares the observation result; accepted students receive an acceptance letter."),
              L("Bayar deposit Rp5.000.000 atau langsung lunas enrollment fee.", "Pay a Rp5,000,000 deposit or the full enrolment fee."),
              L("Beli formulir aplikasi Rp300.000 di AAO, lengkapi dan kembalikan.", "Buy the application form (Rp300,000) at AAO, complete and return it."),
              L("Lunasi enrollment fee dan serahkan bukti bayar ke bagian keuangan.", "Pay the enrolment fee and hand the payment slip to Finance.")],
    "test": L("Observasi kelas.", "Class observation."),
    "notes": L("Usia: kelas 1 minimal 6 tahun sebelum 1 November; kelas 2 minimal 7 tahun; kelas 3 ke atas minimal 8 tahun. " + COMMON_NOTE["id"],
               "Age: grade 1 at least 6 before 1 November; grade 2 at least 7; grade 3+ at least 8. " + COMMON_NOTE["en"]),
    "source": HS, "checked": CHK})
add_admission("highscope-indonesia-kelapa-gading", {"level": "SMP", "academicYear": "2025/2026",
    "steps": [L("AAO menjadwalkan observasi kelas, wawancara, psikotes, dan Basic Competency Test (biaya Rp500.000).", "AAO schedules class observation, interview, psychological test and Basic Competency Test (Rp500,000)."),
              L("AAO menginformasikan hasil; siswa diterima mendapat surat penerimaan.", "AAO shares the result; accepted students receive an acceptance letter."),
              L("Bayar deposit Rp5.000.000 atau langsung lunas enrollment fee.", "Pay a Rp5,000,000 deposit or the full enrolment fee."),
              L("Beli formulir aplikasi Rp300.000, lengkapi dan kembalikan ke AAO.", "Buy the application form (Rp300,000), complete and return it to AAO."),
              L("Serahkan bukti pelunasan enrollment fee ke bagian keuangan.", "Hand the enrolment fee payment slip to Finance.")],
    "test": L("Observasi kelas, wawancara, psikotes, dan Basic Competency Test.", "Class observation, interview, psychological test and Basic Competency Test."),
    "notes": L("Kelas 7: lulus SD/kelas 6. Kelas 8–9: lulus kelas 7/8 di sekolah sebelumnya. " + COMMON_NOTE["id"], "Grade 7: completed primary school. Grades 8–9: passed grade 7/8 at the previous school. " + COMMON_NOTE["en"]),
    "source": HS, "checked": CHK})

BN = {"title": "BINUS SCHOOL Simprug — Admissions Process (OpenApply, dari simprug.binus.sch.id/how-to-apply)", "url": "https://search.openapply.com/schools/1416"}
upsert("binus-school-simprug", name="BINUS School Simprug", city="Jakarta Selatan", curriculum=["IB"], phone="Admissions +62 21 7243663", level="SMP",
       year="2026/2027", source={"title": "11 Daftar Biaya Masuk SMP di Jakarta Selatan Tahun Ajaran 2026/2027 (Popmama)",
       "url": "https://www.popmama.com/big-kid/10-12-years-old/daftar-biaya-masuk-smp-di-jakarta-selatan-tahun-ajaran-2026-2027-00-bbqjr-87t30t", "published": "2025-12-12"},
       checked=CHK, entryFee={"min": 192_000_000}, tuition={"amount": 49_800_000, "period": "quarter"})
add_admission("binus-school-simprug", {"academicYear": "2027/2028",
    "steps": [L("Beli formulir pendaftaran dari bagian admission (transfer/debit).", "Buy the registration form from Admissions (transfer/debit)."),
              L("Kode voucher dikirim lewat email.", "A voucher code is sent by email."),
              L("Daftar dan verifikasi email di binus.edu/admissions, lalu lengkapi data registrasi.", "Sign up and verify your email at binus.edu/admissions, then complete the registration details."),
              L("Pilih jadwal tes masuk dan isi booking form dengan kode voucher.", "Choose an entrance test date and fill in the booking form with the voucher code."),
              L("Unggah semua dokumen yang diminta dan tunggu verifikasi.", "Upload all required documents and wait for verification."),
              L("Unduh kartu tes dan dokumen pendukung.", "Download the test card and supporting documents."),
              L("Ikuti tes masuk dan serahkan dokumen pendukung yang sudah diisi ke bagian admission.", "Attend the entrance test and hand in the completed supporting documents.")],
    "test": L("Tes masuk (entrance test).", "Entrance test."),
    "notes": L("Halaman tidak menyebut tahun ajaran; prosedur yang berlaku per November 2026. Kurikulum IB (PYP, MYP, DP) dan nasional. Kontak admission: +62 21 7243663.",
               "The page does not state the academic year; procedure as of November 2026. IB (PYP, MYP, DP) and national curriculum. Admissions: +62 21 7243663."),
    "source": BN, "checked": CHK})
print("ok")
