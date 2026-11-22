"""Official PPDB page of Birrul Waalidain Bogor (2024/2025): https://birrulwaalidain.sch.id/pages/ppdb
Figures copied verbatim. Older data — shown with the 'older academic year' warning on the site."""
from seedlib import L, fee, upsert, add_admission

SRC = {"title": "Informasi PPDB 2024/2025 — SIT Birrul Waalidain Bogor (situs resmi)", "url": "https://birrulwaalidain.sch.id/pages/ppdb"}
SCHOOL = dict(name="SIT Birrul Waalidain Bogor", city="Kabupaten Bogor", district="Kemang", religion="Islam",
              address="Jl. Raya Salabenda–Semplak No.12, Parakan Jaya, Kemang, Kabupaten Bogor 16310", phone="0251-7535-784 / 0838-0630-4182",
              website="https://birrulwaalidain.sch.id")
C = dict(year="2024/2025", source=SRC, checked="2026-11-22", **SCHOOL)
NOTE = L("Uang pangkal = Dana Sumbangan Pendidikan (DSP). Uang masuk minimal 50% dibayar paling lambat 10 hari setelah diterima; sisanya bisa dicicil. Biaya bersubsidi silang. SPP tidak dicantumkan.",
         "Entry fee = education contribution (DSP). At least 50% of the entry payment is due within 10 days of acceptance; the rest can be paid in instalments. Fees are cross-subsidised. Tuition not listed.")
upsert("sit-birrul-waalidain-bogor", level="TK", registrationFee=500_000, entryFee={"min": 2_650_000},
       otherFees=[fee("Seragam 3 stel", "Uniforms (3 sets)", 600_000), fee("Buku paket 1 semester", "Textbooks (1 semester)", 410_000)], notes=NOTE, **C)
upsert("sit-birrul-waalidain-bogor", level="SD", registrationFee=600_000, entryFee={"min": 5_000_000},
       otherFees=[fee("Bimbingan orientasi & ta'aruf (Mei–Juni)", "Orientation (May–June)", 300_000), fee("Seragam 4 stel", "Uniforms (4 sets)", 960_000), fee("Buku paket 1 tahun", "Textbooks (1 year)", 1_200_000)], notes=NOTE, **C)
upsert("sit-birrul-waalidain-bogor", level="SMP", registrationFee=600_000, entryFee={"min": 4_000_000},
       otherFees=[fee("Bimbingan orientasi & ta'aruf", "Orientation", 300_000), fee("Seragam 4 stel", "Uniforms (4 sets)", 1_100_000), fee("Buku paket 1 tahun", "Textbooks (1 year)", 1_200_000)],
       notes=L(NOTE["id"] + " Santri mondok: sewa tempat tidur, lemari, kasur (3 tahun) Rp3.000.000.", NOTE["en"] + " Boarders: bed, wardrobe and mattress rental (3 years) Rp3,000,000."), **C)
STEPS = [L("Isi buku tamu online.", "Fill in the online guest book."),
         L("Transfer biaya pendaftaran (Rp500.000 TK; Rp600.000 SD & SMP) dan konfirmasi via WhatsApp atau email.", "Transfer the registration fee (Rp500,000 TK; Rp600,000 SD & SMP) and confirm by WhatsApp or email."),
         L("Panitia mengirim undangan tes penjajakan dan wawancara orang tua.", "The committee sends an invitation to the placement test and parent interview."),
         L("Ikuti tes penjajakan di sekolah.", "Attend the placement test at the school."),
         L("Hasil seleksi dikirim; jika diterima, bayar minimal 50% uang masuk dalam 10 hari.", "Results are sent; if accepted, pay at least 50% of the entry fees within 10 days.")]
BASE_DOCS = [L("Formulir pendaftaran", "Registration form"), L("Surat keterangan kelahiran (2 lembar)", "Birth certificate (2 copies)"),
             L("Fotokopi Kartu Keluarga (2 lembar)", "Copy of family card (2 copies)"), L("Surat keterangan sehat dari dokter", "Doctor's health certificate")]
for level, docs, age in [
    ("TK", [], ("Usia per Juni 2024: Play Group 3–4 tahun, TK A 4–5 tahun, TK B 5–6 tahun.", "Age as of June 2024: Playgroup 3–4, TK A 4–5, TK B 5–6.")),
    ("SD", [L("Pas foto 3x4 (4 lembar)", "Passport photos 3x4 (4)")], ("Usia 6–7 tahun pada Juli 2024.", "Age 6–7 in July 2024.")),
    ("SMP", [L("Surat kelakuan baik dari sekolah asal", "Good-conduct letter from previous school"), L("Fotokopi surat keterangan lulus", "Copy of graduation certificate")], ("Usia 12–13 tahun; harus lulus tes penjajakan.", "Age 12–13; must pass the placement test.")),
]:
    add_admission("sit-birrul-waalidain-bogor", {"level": level, "academicYear": "2024/2025",
        "period": L("Dibuka mulai Desember 2023, offline (sekretariat Jl. Salabenda–Semplak No.12) dan online.", "Opened from December 2023, in person (secretariat at Jl. Salabenda–Semplak No.12) and online."),
        "steps": STEPS, "documents": BASE_DOCS + docs,
        "test": L("Tes penjajakan dan wawancara orang tua.", "Placement test and parent interview."),
        "notes": L(age[0], age[1]), "source": SRC, "checked": "2026-11-22"})
print("ok")
