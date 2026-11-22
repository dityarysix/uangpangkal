"""Official PPDB site of Nurul Fikri Islamic School, Depok — academic year 2027/2028.
Fees:      https://ppdb.nurulfikri.sch.id/biaya
Schedule:  https://ppdb.nurulfikri.sch.id/jadwal
Rules:     https://ppdb.nurulfikri.sch.id/syarat
Figures copied verbatim. SPP amounts are not published on the site."""
from seedlib import L, fee, upsert, add_admission

FEES = {"title": "Biaya Pendidikan TA 2027/2028 — PPDB Nurul Fikri Islamic School (situs resmi)", "url": "https://ppdb.nurulfikri.sch.id/biaya"}
JADWAL = {"title": "Jadwal Tes TA 2027/2028 — PPDB Nurul Fikri Islamic School (situs resmi)", "url": "https://ppdb.nurulfikri.sch.id/jadwal"}
CHECKED = "2026-11-22"
SLUG = "nurul-fikri-islamic-school-depok"
SCHOOL = dict(name="Nurul Fikri Islamic School Depok", city="Depok", district="Cimanggis", religion="Islam",
              address="Jl. Tugu Raya No.61, Tugu, Cimanggis, Depok", phone="+62 872 0645 / psb@nurulfikri.sch.id",
              website="https://ppdb.nurulfikri.sch.id")
C = dict(year="2027/2028", source=FEES, checked=CHECKED, **SCHOOL)

ONE_OFF = L("Dana pengembangan (uang pangkal) dan dana pendidikan dibayar satu kali selama di jenjang tersebut; dana pendidikan termasuk sarana dan bahan ajar tahun pertama. SPP dibayar mulai Juli dan belum termasuk katering dan antar jemput; besaran SPP tidak dicantumkan di situs. ",
            "The development fund (entry fee) and education fund are paid once per school level; the education fund covers first-year facilities and learning materials. Tuition starts in July and excludes catering and transport; the tuition amount is not published on the site. ")

def reg_note(ext, inte, staff):
    return (f"Biaya pendaftaran: Rp{ext:,} (dari luar Nurul Fikri), Rp{inte:,} (dari Nurul Fikri), Rp{staff:,} (anak pegawai).".replace(",", "."),
            f"Registration: Rp{ext:,} (external), Rp{inte:,} (from Nurul Fikri), Rp{staff:,} (staff children).")

def entry(level, reg, dev, edu, boys, girls, extra=("", "")):
    rid, ren = reg_note(*reg)
    upsert(SLUG, level=level, registrationFee=reg[0],
           entryFee={"min": dev[0], **({"max": dev[1]} if len(dev) > 1 else {})},
           otherFees=[fee("Dana pendidikan (sekali bayar)", "Education fund (one-off)", edu[0]),
                      fee("Seragam putra", "Uniforms (boys)", boys), fee("Seragam putri", "Uniforms (girls)", girls)],
           notes=L(ONE_OFF["id"] + extra[0] + rid, ONE_OFF["en"] + extra[1] + ren), **C)

entry("TK", (500_000, 400_000, 250_000), (6_000_000, 9_000_000), (9_000_000,), 1_400_000, 1_700_000,
      ("PG/TK A: dana pengembangan Rp9.000.000, dana pendidikan Rp9.000.000. TK B: Rp6.000.000 dan Rp8.000.000. ",
       "Playgroup/TK A: development fund Rp9,000,000, education fund Rp9,000,000. TK B: Rp6,000,000 and Rp8,000,000. "))
entry("SD", (650_000, 500_000, 325_000), (22_500_000,), (14_000_000,), 2_000_000, 2_600_000)
entry("SMP", (850_000, 550_000, 425_000), (22_500_000,), (16_000_000,), 2_100_000, 3_000_000)
entry("SMA", (900_000, 550_000, 450_000), (22_500_000,), (16_000_000,), 2_200_000, 3_000_000)

# ---- Admission (from /jadwal and /syarat) ----
STEPS = [L("Daftar online di ppdb.nurulfikri.sch.id.", "Register online at ppdb.nurulfikri.sch.id."),
         L("Bayar biaya pendaftaran.", "Pay the registration fee."),
         L("Unggah dokumen maksimal 5 hari setelah pembayaran.", "Upload documents within 5 days of payment."),
         L("Ikuti seleksi sesuai jadwal (offline).", "Attend the selection on the scheduled date (in person)."),
         L("Pengumuman hasil, lalu daftar ulang dengan membayar biaya pendidikan.", "Results are announced; then re-register by paying the education fees.")]
DOCS = [L("Scan Kartu Keluarga", "Scan of the family card (Kartu Keluarga)"), L("Scan akta kelahiran", "Scan of the birth certificate")]
HEALTH = L("Surat keterangan sehat dari dokter (tinggi & berat badan, tekanan darah, penyakit kronis, alergi), diunggah sebelum seleksi",
           "Doctor's health certificate (height, weight, blood pressure, chronic illness, allergies), uploaded before the selection")
SRC_ADM = {"title": "Jadwal Tes & Syarat Pendaftaran TA 2027/2028 — PPDB Nurul Fikri Islamic School (situs resmi)", "url": "https://ppdb.nurulfikri.sch.id/jadwal"}
WAVES = ("Pendaftaran online dibuka 8 Agustus 2026. Siswa dari luar Nurul Fikri: gelombang I {g1}; gelombang II seleksi 14 November 2026 (pengumuman 26 November); gelombang III seleksi 5 Desember 2026 (pengumuman 17 Desember). Gelombang II dan III hanya dibuka jika kuota masih tersedia.",
         "Online registration opened 8 August 2026. External applicants: wave I {g1en}; wave II selection 14 November 2026 (results 26 November); wave III selection 5 December 2026 (results 17 December). Waves II and III open only if places remain.")

def adm(level, g1, g1en, docs, test_id, test_en, notes=None):
    add_admission(SLUG, {"level": level, "academicYear": "2027/2028",
        "period": L(WAVES[0].format(g1=g1), WAVES[1].format(g1en=g1en)),
        "steps": STEPS, "documents": DOCS + docs, "test": L(test_id, test_en),
        **({"notes": notes} if notes else {}), "source": SRC_ADM, "checked": CHECKED})

adm("TK", "seleksi 17 Oktober 2026", "selection 17 October 2026", [],
    "Observasi (dibantu psikolog) dan wawancara orang tua.", "Observation (with a psychologist) and parent interview.",
    L("Usia: PG lahir Juli 2023–Juni 2024; TK A lahir Juli 2022–Juni 2023; TK B lahir Juli 2021–Juni 2022.",
      "Age: Playgroup born July 2023–June 2024; TK A born July 2022–June 2023; TK B born July 2021–June 2022."))
adm("SD", "seleksi 17–18 Oktober 2026", "selection 17–18 October 2026", [HEALTH],
    "Psikotes dan wawancara orang tua; tes akademik untuk siswa pindahan.", "Psychological test and parent interview; academic test for transfer students.",
    L("Usia minimal 5 tahun 10 bulan pada Juli 2027 (lahir paling lambat Oktober 2021).", "Minimum age 5 years 10 months in July 2027 (born no later than October 2021)."))
adm("SMP", "seleksi 10, 11, 17 dan 18 Oktober 2026", "selection 10, 11, 17 and 18 October 2026",
    [L("Scan rapor SD kelas 4 dan 5; nilai PAI, Bahasa Indonesia, Matematika, IPA, IPS diinput di situs", "Scan of grade 4 and 5 report cards; enter Islamic studies, Indonesian, maths, science and social studies grades on the site"), HEALTH],
    "Psikotes, tes potensi akademik (matematika, literasi, IPA, IPS), wawancara orang tua dan wawancara siswa.",
    "Psychological test, academic aptitude test (maths, literacy, science, social studies), parent interview and student interview.")
adm("SMA", "seleksi 26–27 September dan 3, 4, 10, 11 Oktober 2026", "selection 26–27 September and 3, 4, 10, 11 October 2026",
    [L("Scan rapor SMP kelas 7 dan 8; nilai PAI, Bahasa Indonesia, Bahasa Inggris, Matematika, IPA, IPS diinput di situs", "Scan of grade 7 and 8 report cards; enter Islamic studies, Indonesian, English, maths, science and social studies grades on the site"),
     HEALTH, L("Hasil tes bebas narkoba (AMP, MET, COC, THC) dari RS, klinik, atau laboratorium", "Drug test result (AMP, MET, COC, THC) from a hospital, clinic or lab")],
    "Psikotes, tes potensi akademik (matematika, literasi, IPA, IPS), wawancara orang tua dan wawancara siswa.",
    "Psychological test, academic aptitude test (maths, literacy, science, social studies), parent interview and student interview.")
print("ok nurul fikri")
