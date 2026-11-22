"""Sekolah Dian Harapan (SDH) network — campuses inside uangpangkal.com's nine areas.

Campus list & admission contacts: https://www.sdh.sch.id/admissions (network admission procedure, tests, age rules)
Fees: Popmama "20 Biaya Sekolah SMP Swasta Jabodetabek 2025" (8 Dec 2024) gives ONE approximate range for
"Sekolah Dian Harapan" without naming a campus. It is applied to every campus with a clear note.
Campuses outside our areas (Karawang, Jember, Makassar, etc.) are skipped.
SDH Bandung is skipped until its city (Kota/Kabupaten Bandung) is confirmed."""
from seedlib import L, fee, upsert, add_admission, UNIFORM, BOOKS

FEE_SRC = {"title": "20 Biaya Sekolah SMP Swasta Jabodetabek 2025 (Popmama)",
           "url": "https://www.popmama.com/big-kid/10-12-years-old/20-biaya-sekolah-smp-swasta-jabodetabek-2025-00-58r8y-pymtjw",
           "published": "2024-12-08"}
ADM_SRC = {"title": "Admissions — Sekolah Dian Harapan (situs resmi)", "url": "https://www.sdh.sch.id/admissions"}
CHECKED = "2026-11-22"

CAMPUSES = [
    # slug suffix, display name, city, district, address, contact
    ("lippo-village", "Lippo Village", "Kabupaten Tangerang", "Kelapa Dua", "Lippo Village, Kabupaten Tangerang", "admission.sdhlippovillage@sdh.or.id / +62 8577 3000 560"),
    ("global-bintaro", "Global Bintaro", "Tangerang Selatan", None, "Bintaro, Tangerang Selatan", "admission.sdhglobalbintaro@sdh.or.id / +62 812 6018 8882"),
    ("daan-mogot", "Daan Mogot", "Jakarta Barat", None, "Daan Mogot, Jakarta Barat", "admission.sdhdaanmogot@sdh.or.id / +62 812 8484 8969"),
    ("east-jakarta", "East Jakarta", "Jakarta Timur", None, None, "admission.sdheastjakarta@sdh.or.id / +62 822 6018 8887"),
    ("cikarang", "Cikarang", "Kabupaten Bekasi", "Cikarang Selatan", "Lippo Cikarang, Kabupaten Bekasi", "admission.sdhcikarang@sdh.or.id / +62 8788 1295 565"),
    ("bogor", "Bogor", "Kota Bogor", "Bogor Tengah", "Lippo Plaza Keboen Raya Lt. 4–5, Jl. Pajajaran No.27, Babakan, Bogor Tengah, Kota Bogor", "admission.sdhbogor@sdh.or.id / +62 8151 3045 336"),
    ("sentul", "Sentul", "Kabupaten Bogor", "Babakan Madang", "Komplek Bellanova Country Mall, Sentul, Kabupaten Bogor", "admission.sdhsentul@sdh.or.id / +62 812 1688 8852"),
    ("depok", "Depok", "Depok", None, None, "admission.sdhdepok@sdh.or.id / +62 815 8830 656"),
    ("surabaya", "Surabaya", "Surabaya", None, None, "admission.sdhsurabaya@sdh.or.id / +62 812 9868 8881"),
    ("jogja", "Jogja", "Kota Yogyakarta", None, "Lippo Plaza Jogja, Yogyakarta", "admission.sdhjogja@sdh.or.id / +62 822 6018 8883"),
    ("jogja-north-campus", "Jogja North Campus", "Sleman", None, "Sleman (kampus kedua SDH Jogja, dibuka Juli 2026)", "admission.sdhjogja@sdh.or.id / +62 822 6018 8883"),
]

NETWORK_NOTE = L("Rentang biaya ini berlaku untuk jaringan Sekolah Dian Harapan secara umum menurut sumber, bukan khusus kampus ini, dan disebut sebagai perkiraan (\"sekitar\"). Uang pangkal = DPP. Tanyakan biaya kampus ini langsung ke bagian admission.",
                 "This fee range is given by the source for the Sekolah Dian Harapan network in general, not specifically this campus, and is approximate. Entry fee = DPP. Ask this campus's admissions office for its exact fees.")

ADM = {
    "TK": ("Observasi dan wawancara orang tua.", "Observation and parent interview.",
           "Kelas K1/K2/K3: usia minimal 3/4/5 tahun per 30 September.", "K1/K2/K3: minimum age 3/4/5 by 30 September."),
    "SD": ("Kelas 1: psikotes, wawancara siswa & orang tua. Kelas 2–6: psikotes, Matematika, Bahasa Inggris, Bahasa Indonesia, wawancara siswa & orang tua.",
           "Grade 1: psychological test, student & parent interview. Grades 2–6: psychological test, maths, English, Indonesian, student & parent interview.",
           "Kelas 1: usia minimal 6 tahun per 30 September.", "Grade 1: minimum age 6 by 30 September."),
    "SMP": ("Psikotes, Matematika, Bahasa Inggris, Bahasa Indonesia, wawancara siswa & orang tua.", "Psychological test, maths, English, Indonesian, student & parent interview.", None, None),
    "SMA": ("Psikotes, Matematika, Bahasa Inggris, Bahasa Indonesia, wawancara siswa & orang tua.", "Psychological test, maths, English, Indonesian, student & parent interview.", None, None),
}
STEPS = [L("Daftar online melalui situs SDH.", "Register online via the SDH website."),
         L("Unggah dokumen (atau serahkan langsung ke kampus).", "Upload documents (or hand in hard copies at the campus)."),
         L("Bagian admission menginformasikan jadwal tes masuk; tes bisa di kampus atau online.", "Admissions informs you of the entrance test date; tests can be on campus or online.")]
DOCS = [L("Scan/fotokopi akta kelahiran", "Scan/copy of birth certificate"), L("Scan/fotokopi Kartu Keluarga", "Scan/copy of family card (Kartu Keluarga)"),
        L("Dua pas foto terbaru 3x4", "Two recent 3x4 photos"), L("Satu salinan rapor tahun terakhir", "One copy of last year's report card")]

for suffix, label, city, district, address, contact in CAMPUSES:
    slug = f"sekolah-dian-harapan-{suffix}"
    upsert(slug, name=f"Sekolah Dian Harapan {label}", city=city, district=district, address=address, phone=contact,
           religion="Kristen", website="https://www.sdh.sch.id",
           level="SMP", year="2025/2026", yearAssumed=True, source=FEE_SRC, checked=CHECKED,
           registrationFee=350_000, entryFee={"min": 14_000_000, "max": 22_000_000}, tuition={"amount": 1_375_000, "period": "month"},
           otherFees=[fee(*UNIFORM, 1_000_000), fee(*BOOKS, 1_500_000)],
           notes=L(NETWORK_NOTE["id"] + " SPP Rp1.375.000–Rp2.700.000/bulan.", NETWORK_NOTE["en"] + " Tuition Rp1,375,000–Rp2,700,000/month."))
    for level, (tid, ten, nid, nen) in ADM.items():
        add_admission(slug, {"level": level, "academicYear": "2027/2028",
            "steps": STEPS, "documents": DOCS, "test": L(tid, ten),
            **({"notes": L(nid, nen)} if nid else {}),
            "period": L("Pendaftaran online dibuka. Situs tidak menyebut tahun ajaran; ini prosedur yang berlaku per November 2026.",
                        "Online registration is open. The site does not state the academic year; this is the procedure in effect as of November 2026."),
            "source": ADM_SRC, "checked": CHECKED})
print("ok", len(CAMPUSES))
