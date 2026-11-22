"""New areas, batch 1 (Medan, Makassar, Palembang, Pekanbaru, Padang).
Sources:
- Lembar Kerja Untuk Anak, "Biaya Masuk Sekolah Dasar di Medan Tahun Ajaran Baru 2026" (29 Sep 2026): year stated as 2026 -> 2026/2027 (assumed).
- HaiBunda city lists (Oct 2023, Medan / Pekanbaru / Makassar): no year stated -> 2023/2024 (assumed).
- Orami, "4 Sekolah Internasional di Makassar" (19 Jun 2025): no year stated -> 2025/2026 (assumed).
- Akurat Sumsel, SD swasta Palembang (23 Apr 2026): estimates -> 2026/2027 (assumed).
- Official: SMA Santo Yoseph Medan SPMB 2026/2027; SMPIT Al Furqon Palembang SPMB 2026/2027; Perguruan Islam Al-Amjad Medan SPMB 2027/2028 (admission only).
- Sumbarbisnis, SMPIT Surau Minang Padang SPMB 2027/2028 (2 Nov 2026).
- Sekolah Dian Harapan network admission procedure (Medan, Makassar campuses; no campus fees published).
Skipped: wartamakassar.com list (fees for public schools, unverifiable details)."""
from seedlib import L, fee, upsert, ensure_school, add_admission, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
MEDAN = "Kota Medan"

# ---------- Medan: Lembar Kerja Untuk Anak
LK = {"title": "Biaya Masuk Sekolah Dasar di Medan Tahun Ajaran Baru 2026 (Lembar Kerja Untuk Anak)", "url": "https://lembarkerjauntukanak.com/biaya-masuk-sekolah-dasar-di-medan/", "published": "2026-09-29"}
LKC = dict(level="SD", year="2026/2027", yearAssumed=True, source=LK, checked=CHK)
LKN = L("Angka dari artikel blog (tahun ajaran 2026); konfirmasi ke sekolah.", "Figures from a blog article (academic year 2026); confirm with the school.")
for slug, name, district, addr, rel, pangkal, spp, period in [
    ("sdit-siti-hajar-medan", "SDIT Siti Hajar Medan", "Medan Tuntungan", "Jl. Paya Bundung, Simpang Selayang, Medan Tuntungan, Kota Medan", "Islam", 7_000_000, 900_000, "month"),
    ("sd-jabal-rahmah-mulia-medan", "SD Jabal Rahmah Mulia Medan", "Medan Sunggal", "Jl. Balai Desa No.24 H, Sunggal, Medan", "Islam", 8_500_000, 520_000, "month"),
    ("perguruan-islam-al-ulum-terpadu-medan", "Perguruan Islam Al-Ulum Terpadu Medan", "Medan Area", "Jl. Puri No.154/346, Kota Matsum II, Medan Area, Kota Medan", "Islam", 7_000_000, 575_000, "month"),
    ("sd-shafiyyatul-amaliyyah-medan", "SD Shafiyyatul Amaliyyah Medan", "Medan Sunggal", "Jl. Setia Budi No.191, Tanjung Rejo, Medan Sunggal, Kota Medan", "Islam", 14_000_000, 1_300_000, "month"),
    ("sd-al-azhar-medan-johor", "SD Al-Azhar Medan Johor", "Medan Johor", "Jl. Pintu Air IV No.214, Kwala Bekala, Medan Johor, Kota Medan", "Islam", 10_000_000, 900_000, "month"),
    ("singapore-international-school-medan", "Singapore International School Medan", "Medan Tuntungan", "Jl. Jamin Ginting Km 8,5, Mangga, Medan Tuntungan, Kota Medan", None, 28_000_000, 66_000_000, "year"),
    ("highscope-indonesia-medan", "HighScope Indonesia Medan", "Medan Baru", "Kompleks Citra Garden Blok B12, Jl. Citra Garden No.5, Titi Rantai, Medan Baru, Kota Medan", None, 25_000_000, 3_300_000, "month"),
    ("prime-one-school-medan", "Prime One School Medan", "Medan Amplas", "Jl. Jenderal Besar A.H. Nasution No.88A, Harjosari II, Medan Amplas, Kota Medan", None, 15_000_000, 2_750_000, "month"),
    ("chandra-kumala-school-medan", "Chandra Kumala School Medan", "Medan Baru", "Jl. Letjen S Parman, Petisah Hulu, Medan Baru, Kota Medan", None, 7_500_000, 2_000_000, "month"),
]:
    upsert(slug, name=name, city=MEDAN, district=district, address=addr, religion=rel,
           entryFee={"min": pangkal}, tuition={"amount": spp, "period": period}, notes=LKN, **LKC)

# ---------- Medan: HaiBunda (2023)
HBM = {"title": "20 SD Negeri dan Swasta Medan Akreditasi A, Lengkap dengan Alamat & Estimasi Biaya (HaiBunda)", "url": "https://www.haibunda.com/parenting/20231024093600-61-319347/20-sd-negeri-dan-swasta-medan-akreditasi-a-lengkap-dengan-alamat-estimasi-biaya", "published": "2023-10-25"}
HBC = dict(level="SD", year="2023/2024", yearAssumed=True, checked=CHK)
HBN = L("Estimasi biaya dari artikel 2023; tahun ajaran tidak disebut.", "Estimated fees from a 2023 article; academic year not stated.")
upsert("sd-harapan-1-medan", name="SD Harapan 1 Medan", city=MEDAN, district="Medan Maimun", address="Jl. Imam Bonjol No.32, Medan Maimun, Kota Medan", religion="Islam",
       source=HBM, registrationFee=250_000, entryFee={"min": 3_010_000}, tuition={"amount": 650_000, "period": "month"},
       otherFees=[fee("Uang sarana pendidikan per tahun", "Education facilities fee per year", 1_050_000)], notes=HBN, **HBC)
upsert("medan-independent-school", name="Medan Independent School", city=MEDAN, district="Medan Tuntungan", address="Jl. Tali Air No.5, Mangga, Medan Tuntungan, Kota Medan",
       curriculum=["IB", "Internasional"], source=HBM, registrationFee=35_000_000, tuition={"amount": 197_400_000, "period": "year"},
       otherFees=[fee("Biaya pengembangan per tahun", "Development fee per year", 12_400_000)],
       notes=L("Biaya registrasi dibayar sekali saat masuk. " + HBN["id"], "Registration fee is paid once on entry. " + HBN["en"]), **HBC)

# ---------- Medan: official pages
SY = {"title": "Detail SPMB 2026/2027 — SMA Swasta Santo Yoseph Medan (situs resmi)", "url": "https://www.smastyosephmedan.com/ppdb/1"}
upsert("sma-santo-yoseph-medan", name="SMA Swasta Santo Yoseph Medan", city=MEDAN, district="Medan Tuntungan", address="Jl. Flamboyan Raya No.139, Tanjung Selamat, Medan Tuntungan, Kota Medan",
       religion="Katolik", website="https://www.smastyosephmedan.com", level="SMA", year="2026/2027", source=SY, checked=CHK,
       registrationFee=200_000, entryFee={"min": 1_850_000}, tuition={"amount": 500_000, "period": "month"},
       otherFees=[fee("Perlengkapan sekolah", "School supplies", 150_000), fee("Baju olahraga", "Sports uniform", 185_000), fee("Baju kotak-kotak", "Checked uniform", 170_000),
                  fee("Baju batik", "Batik uniform", 160_000), fee("Uang OSIS per tahun", "Student council fee per year", 240_000)],
       notes=L("Total gelombang 1 Rp3.455.000. Potongan 50% uang pangkal untuk lulusan SMP Santo Yoseph dan SMP Deli Murni Sukamaju, serta juara umum 1–3 kelas IX.",
               "Wave 1 total Rp3,455,000. 50% entry-fee reduction for graduates of SMP Santo Yoseph and SMP Deli Murni Sukamaju, and for top-3 overall in grade 9."))
add_admission("sma-santo-yoseph-medan", {"level": "SMA", "academicYear": "2026/2027", "steps": [],
    "documents": [L("Fotokopi surat permandian (1 lembar)", "Copy of baptism certificate (1)"), L("Surat tanda lulus (1 lembar)", "Graduation letter (1)"), L("Ijazah asli SMP dan fotokopi (2 lembar)", "Original SMP diploma and 2 copies")],
    "source": SY, "checked": CHK})

AJ = {"title": "Pendaftaran Siswa Baru Al-Amjad 2027/2028 (situs resmi)", "url": "https://www.perguruanalamjad.com/daftar"}
ensure_school("perguruan-islam-al-amjad-medan", name="Perguruan Islam Al-Amjad Medan", city=MEDAN, levels=["KB", "TK", "SD", "SMP", "SMA"], district="Medan Sunggal",
              address="Jl. Merpati No.81 (Ringroad), Sei Sikambing B, Medan Sunggal, Kota Medan", religion="Islam", website="https://www.perguruanalamjad.com", phone="061 4256 5253 / 0811 682 7787")
AJ_DOCS = [L("Fotokopi akta kelahiran", "Copy of birth certificate"), L("Fotokopi kartu keluarga", "Copy of family card"), L("Pas foto 3x4 (4 lembar)", "3x4 photos (4)")]
AJ_STEPS = [L("Pra-registrasi online di spmb.alamjad.sch.id atau langsung di sekolah (gratis, tidak mengikat)", "Online pre-registration at spmb.alamjad.sch.id or at the school (free, non-binding)"),
            L("Tim sekolah menghubungi untuk jadwal kedatangan", "The school contacts you to schedule a visit"),
            L("Registrasi di sekolah dan bayar uang pendaftaran (kursi baru terjamin setelah ini)", "Register at the school and pay the registration fee (seat secured only after this)"),
            L("Seleksi: calon murid dan orang tua hadir bersama", "Selection day: applicant and parents attend together")]
AJ_PERIOD = L("Dibuka sejak open house 24 Oktober 2026. Early bird (diskon uang pangkal) sampai 31 Januari 2027; diskon sibling bisa digabung.",
              "Open since the open house on 24 October 2026. Early-bird entry-fee discount until 31 January 2027; sibling discount can be combined.")
for lv, tid, ten, docid, docen in [
    ("TK", "Observasi tumbuh kembang, kemandirian, kesiapan belajar; wawancara orang tua. Usia PG 3, TK-A 4, TK-B 5 tahun per 31 Juli 2027.", "Observation of development, independence, readiness; parent interview. Age: PG 3, TK-A 4, TK-B 5 by 31 July 2027.", "Rapor TK terakhir (bila ada)", "Latest kindergarten report (if any)"),
    ("SD", "Tanpa tes akademik: observasi kesiapan belajar dan wawancara orang tua. Usia minimal 6 tahun per 31 Juli 2027.", "No academic test: readiness observation and parent interview. Minimum age 6 by 31 July 2027.", "Rapor TK terakhir (bila ada)", "Latest kindergarten report (if any)"),
    ("SMP", "Seleksi akademik mata pelajaran inti, sikap, dan keislaman; wawancara orang tua.", "Academic test in core subjects, attitude and Islamic knowledge; parent interview.", "Rapor kelas 5 SD semester 2", "Grade 5 semester 2 report"),
    ("SMA", "Seleksi akademik mata pelajaran inti, sikap, dan keislaman; wawancara orang tua.", "Academic test in core subjects, attitude and Islamic knowledge; parent interview.", "Rapor kelas 8 SMP semester 2", "Grade 8 semester 2 report"),
]:
    add_admission("perguruan-islam-al-amjad-medan", {"level": lv, "academicYear": "2027/2028", "period": AJ_PERIOD, "steps": AJ_STEPS,
        "documents": AJ_DOCS + [L(docid, docen)], "test": L(tid, ten), "source": AJ, "checked": CHK})

# ---------- Sekolah Dian Harapan Medan & Makassar (admission procedure only)
SDH = {"title": "Admissions — Sekolah Dian Harapan (situs resmi)", "url": "https://www.sdh.sch.id/admissions"}
SDH_STEPS = [L("Daftar online melalui situs SDH.", "Register online via the SDH website."),
             L("Unggah dokumen (atau serahkan langsung ke kampus).", "Upload documents (or hand in hard copies at the campus)."),
             L("Bagian admission menginformasikan jadwal tes masuk; tes bisa di kampus atau online.", "Admissions informs you of the entrance test date; tests can be on campus or online.")]
SDH_DOCS = [L("Scan/fotokopi akta kelahiran", "Scan/copy of birth certificate"), L("Scan/fotokopi Kartu Keluarga", "Scan/copy of family card (Kartu Keluarga)"),
            L("Dua pas foto terbaru 3x4", "Two recent 3x4 photos"), L("Satu salinan rapor tahun terakhir", "One copy of last year's report card")]
SDH_TEST = {"SD": L("Kelas 1: psikotes, wawancara siswa & orang tua. Kelas 2–6: psikotes, Matematika, Bahasa Inggris, Bahasa Indonesia, wawancara.", "Grade 1: psychological test, student & parent interview. Grades 2–6: psychological test, maths, English, Indonesian, interview."),
            "SMP": L("Psikotes, Matematika, Bahasa Inggris, Bahasa Indonesia, wawancara siswa & orang tua.", "Psychological test, maths, English, Indonesian, student & parent interview.")}
for slug, name, city, district, addr in [
    ("sekolah-dian-harapan-medan", "Sekolah Dian Harapan Medan", MEDAN, "Medan Petisah", "Lippo Plaza, Jl. Imam Bonjol No.6, Petisah Tengah, Medan Petisah, Kota Medan"),
    ("sekolah-dian-harapan-makassar", "Sekolah Dian Harapan Makassar", "Kota Makassar", "Tamalate", "Jl. Gunung Agung No.201, Tanjung Merdeka, Tamalate, Kota Makassar"),
]:
    ensure_school(slug, name=name, city=city, levels=["SD", "SMP"], district=district, address=addr, religion="Kristen", website="https://www.sdh.sch.id")
    for lv in ("SD", "SMP"):
        add_admission(slug, {"level": lv, "academicYear": "2027/2028", "steps": SDH_STEPS, "documents": SDH_DOCS, "test": SDH_TEST[lv],
            "period": L("Prosedur jaringan SDH per November 2026; situs tidak menyebut tahun ajaran. Biaya kampus tidak dipublikasikan.", "SDH network procedure as of November 2026; the site does not state the year. Campus fees are not published."),
            "source": SDH, "checked": CHK})

# ---------- Makassar: HaiBunda (2023)
MKS = "Kota Makassar"
HBK = {"title": "30 SD Negeri dan Swasta Makassar Akreditasi Terbaik Beserta Alamat & Estimasi Biaya (HaiBunda)", "url": "https://www.haibunda.com/parenting/20231027101549-61-320556/30-sd-negeri-swasta-makassar-akreditasi-terbaik-beserta-alamat-estimasi-biaya", "published": "2023-10-27"}
K = dict(level="SD", year="2023/2024", yearAssumed=True, source=HBK, checked=CHK)
upsert("al-akhyar-islamic-school-makassar", name="Al-Akhyar Islamic School Makassar", city=MKS, district="Biringkanaya", address="Jl. Arung Teko No.99, Sudiang, Biringkanaya, Kota Makassar", religion="Islam",
       entryFee={"min": 13_000_000}, tuition={"amount": 750_000, "period": "month"}, otherFees=[fee("Infaq kegiatan", "Activities donation", 1_000_000)],
       notes=L("Uang pangkal Rp3.000.000 + infaq sarana prasarana Rp10.000.000. " + HBN["id"], "Entry fee Rp3,000,000 + facilities donation Rp10,000,000. " + HBN["en"]), **K)
upsert("sdit-al-fatih-makassar", name="SDIT Al-Fatih Makassar", city=MKS, district="Makassar", address="Jl. Domba No.12, Maricaya, Makassar, Kota Makassar", religion="Islam",
       registrationFee=350_000, entryFee={"min": 20_500_000}, tuition={"amount": 1_235_000, "period": "month"},
       otherFees=[fee("Observasi", "Observation", 400_000), fee("Seragam putra", "Uniforms (boys)", 1_725_000), fee("Seragam putri", "Uniforms (girls)", 1_375_000),
                  fee("Buku paket", "Textbooks", 1_250_000), fee("Dana kegiatan", "Activities", 1_150_000), fee("Komite per tahun", "Committee fee per year", 250_000)], notes=HBN, **K)
upsert("sdit-ar-rahmah-makassar", name="SDIT Ar-Rahmah Makassar", city=MKS, district="Tamalanrea", address="Perumahan Dosen Unhas, Jl. Al-Ikhlas I Blok H, Tamalanrea Jaya, Kota Makassar", religion="Islam",
       entryFee={"min": 1_220_000}, tuition={"amount": 280_000, "period": "month"},
       otherFees=[fee("Praktikum", "Practicals", 500_000), fee("Kesiswaan", "Student affairs", 850_000), fee("Buku dan lembar kerja", "Books and worksheets", 1_100_000), fee("Seragam 3 pasang", "Uniforms (3 sets)", 750_000)],
       notes=L("Uang masuk = biaya fasilitas pendidikan. " + HBN["id"], "Entry = education facilities fee. " + HBN["en"]), **K)
upsert("sekolah-islam-ar-raafi-makassar", name="Sekolah Islam Ar-Raafi Makassar", city=MKS, district="Rappocini", address="Jl. Sultan Alauddin No.307b, Gunung Sari, Rappocini, Kota Makassar", religion="Islam",
       tuition={"amount": 250_000, "period": "month"}, notes=L("Infaq jariyah Rp250.000/bulan (full day). " + HBN["id"], "Monthly donation Rp250,000 (full day). " + HBN["en"]), **K)
upsert("sd-runiah-makassar", name="SD Runiah Makassar", city=MKS, district="Mariso", address="Jl. Gagak No.25, Mariso, Kota Makassar",
       registrationFee=300_000, notes=L("Sekolah inklusi. Hanya biaya pendaftaran yang disebut. " + HBN["id"], "Inclusive school. Only the registration fee is given. " + HBN["en"]), **K)

# ---------- Makassar: Orami international schools (2025)
ORM = {"title": "4 Sekolah Internasional di Makassar, Lengkap dengan Biaya! (Orami)", "url": "https://www.orami.co.id/magazine/sekolah-internasional-di-makassar", "published": "2025-06-19"}
O = dict(level="SD", year="2025/2026", yearAssumed=True, source=ORM, checked=CHK)
ON = L("Kisaran biaya dari artikel; jenjang tidak dirinci. Konfirmasi ke sekolah.", "Fee range from an article; level not specified. Confirm with the school.")
upsert("stella-gracia-school-makassar", name="Stella Gracia School Makassar", city=MKS, district="Tamalate", address="Jl. Manunggal 22 No.5, Maccini Sombala, Tamalate, Kota Makassar", religion="Kristen",
       registrationFee=1_000_000, entryFee={"min": 25_000_000}, tuition={"amount": 10_000_000, "period": "quarter"},
       notes=L("SPP Rp10.000.000 per 4 bulan (dicatat per term). Biaya pendaftaran (uang masuk) Rp25.000.000. " + ON["id"], "Tuition Rp10,000,000 per 4 months (shown per term). Joining fee Rp25,000,000. " + ON["en"]), **O)
upsert("makassar-independent-school", name="Makassar Independent School", city=MKS, district="Ujung Pandang", address="Jl. Botolempangan No.19, Sawerigading, Ujung Pandang, Kota Makassar",
       curriculum=["Internasional"], entryFee={"min": 25_000_000}, tuition={"amount": 9_000_000, "period": "quarter"}, notes=ON, **O)
upsert("sekolah-kristen-ipeka-cpi-makassar", name="Sekolah Kristen IPEKA CPI Makassar", city=MKS, address="Perum Citra Land City Losari Blok C-D No.02, Kota Makassar", religion="Kristen",
       entryFee={"min": 75_000_000}, tuition={"amount": 14_000_000, "period": "month"}, notes=L("Angka \"sekitar\". " + ON["id"], "Approximate figures. " + ON["en"]), **O)

# ---------- Palembang: Akurat (2026)
PLG = "Kota Palembang"
AK = {"title": "Daftar Rekomendasi SD Swasta di Palembang Lengkap dengan Estimasi Rincian Biaya Masuknya (Akurat Sumsel)", "url": "https://sumsel.akurat.co/sumsel/850881/daftar-rekomendasi-sd-swasta-di-palembang-lengkap-dengan-estimasi-rincian-biaya-masuknya", "published": "2026-04-23"}
A = dict(level="SD", year="2026/2027", yearAssumed=True, source=AK, checked=CHK)
AN = L("Estimasi kisaran dari artikel; konfirmasi ke sekolah.", "Estimated range from an article; confirm with the school.")
for slug, name, rel, pmin, pmax, smin, smax in [
    ("sd-islam-al-azhar-cairo-palembang", "SD Islam Al-Azhar Cairo Palembang", "Islam", 15_000_000, 25_000_000, 800_000, 1_500_000),
    ("sdit-bina-ilmi-palembang", "SDIT Bina Ilmi Palembang", "Islam", None, None, 600_000, 1_000_000),
    ("sd-kusuma-bangsa-palembang", "SD Kusuma Bangsa Palembang", None, 15_000_000, 30_000_000, 1_000_000, 2_000_000),
    ("sd-xaverius-1-palembang", "SD Xaverius 1 Palembang", "Katolik", 10_000_000, 25_000_000, 800_000, 1_500_000),
    ("sd-islam-az-zahrah-palembang", "SD Islam Az-Zahrah Palembang", "Islam", 10_000_000, 20_000_000, 700_000, 1_200_000),
    ("sekolah-alam-palembang", "Sekolah Alam Palembang (SAPA)", None, 20_000_000, 22_000_000, 500_000, 500_000),
    ("sekolah-maitreyawira-palembang", "Sekolah Maitreyawira Palembang", "Buddha", 10_000_000, None, 900_000, 1_000_000),
]:
    kw = {}
    if pmin: kw["entryFee"] = {"min": pmin, **({"max": pmax} if pmax else {})}
    rng = f"SPP Rp{smin:,}–Rp{smax:,}/bulan.".replace(",", ".") if smax != smin else ""
    rng_en = f"Tuition Rp{smin:,}–Rp{smax:,}/month." if smax != smin else ""
    upsert(slug, name=name, city=PLG, religion=rel, tuition={"amount": smin, "period": "month"},
           notes=L((rng + " " + AN["id"]).strip(), (rng_en + " " + AN["en"]).strip()), **kw, **A)

# ---------- Palembang: SMPIT Al Furqon (official, 2026/2027)
AF = {"title": "SPMB SMP IT Al Furqon Palembang TP 2026/2027 (situs resmi)", "url": "https://sites.google.com/view/ppdbsmpitalfurqonpalembang/beranda"}
upsert("smpit-al-furqon-palembang", name="SMPIT Al Furqon Palembang", city=PLG, religion="Islam", level="SMP", year="2026/2027", source=AF, checked=CHK,
       entryFee={"min": 17_923_000, "max": 26_303_000}, tuition={"amount": 1_500_000, "period": "month"},
       notes=L("Total biaya masuk (wakaf lahan, uang pangkal, SPP Juli, seragam, kegiatan dan buku 1 tahun): internal fullday Rp17.923.000 / boarding Rp22.338.000; eksternal fullday Rp21.888.000 / boarding Rp26.303.000. SPP fullday Rp1.500.000, boarding Rp3.540.000 per bulan.",
               "Total entry cost (land endowment, entry fee, July tuition, uniforms, 1 year of activities and books): internal full-day Rp17,923,000 / boarding Rp22,338,000; external full-day Rp21,888,000 / boarding Rp26,303,000. Tuition full-day Rp1,500,000, boarding Rp3,540,000 per month."))
add_admission("smpit-al-furqon-palembang", {"level": "SMP", "academicYear": "2026/2027", "period": L("Dibuka 1 September 2025.", "Opened 1 September 2025."),
    "steps": [L("Pelajari informasi pendaftaran dan biaya", "Read the admission and fee information"), L("Mendaftar (langsung di kantor administrasi atau online)", "Register (at the admin office or online)"),
              L("Tes seleksi masuk", "Entrance selection test"), L("Pengumuman kelulusan dan daftar ulang", "Results and re-registration"), L("Pengambilan seragam dan buku", "Collect uniforms and books")],
    "documents": [], "source": AF, "checked": CHK})

# ---------- Pekanbaru: HaiBunda (2023)
PKU = "Kota Pekanbaru"
HBP = {"title": "20 SD Negeri dan Swasta Pekanbaru Akreditasi Terbaik Beserta Alamat & Estimasi Biaya (HaiBunda)", "url": "https://www.haibunda.com/parenting/20231026163120-61-320598/20-sd-negeri-dan-swasta-pekanbaru-akreditasi-terbaik-beserta-alamat-estimasi-biaya", "published": "2023-10-26"}
P = dict(level="SD", year="2023/2024", yearAssumed=True, source=HBP, checked=CHK)
upsert("sd-brilliant-islamic-school-pekanbaru", name="SD Brilliant Islamic School Pekanbaru", city=PKU, district="Tampan", address="Jl. Swakarya B No.30, Tuah Karya, Tampan, Pekanbaru", religion="Islam",
       entryFee={"min": 9_250_000}, notes=L("Estimasi biaya total Rp9.250.000. " + HBN["id"], "Estimated total Rp9,250,000. " + HBN["en"]), **P)
upsert("sd-angkasa-pekanbaru", name="SD Angkasa Pekanbaru", city=PKU, district="Marpoyan Damai", address="Jl. Adi Sucipto, Lanud Roesmin Nurjadin, Maharatu, Marpoyan Damai, Pekanbaru",
       entryFee={"min": 4_500_000}, notes=L("Estimasi biaya total Rp4.500.000. " + HBN["id"], "Estimated total Rp4,500,000. " + HBN["en"]), **P)
upsert("sdit-al-manar-pekanbaru", name="SDIT Al Manar Pekanbaru", city=PKU, district="Marpoyan Damai", address="Gg. Al-Manar, Tengkerang Barat, Marpoyan Damai, Pekanbaru", religion="Islam",
       registrationFee=100_000, entryFee={"min": 3_500_000}, tuition={"amount": 250_000, "period": "month"},
       otherFees=[fee("Biaya pendidikan 1 tahun", "Education fee (1 year)", 600_000), fee("Sarana prasarana", "Facilities", 600_000), fee("Seragam 5 pasang", "Uniforms (5 sets)", 1_000_000)],
       notes=L("Uang masuk = pembangunan. " + HBN["id"], "Entry = building fee. " + HBN["en"]), **P)
upsert("sdit-al-fikri-islamic-green-school-pekanbaru", name="SDIT Al Fikri Islamic Green School Pekanbaru", city=PKU, district="Marpoyan Damai", address="Jl. Merak No.1, Tengkerang Tengah, Marpoyan Damai, Pekanbaru", religion="Islam",
       registrationFee=250_000, entryFee={"min": 10_000_000}, tuition={"amount": 1_000_000, "period": "month"},
       otherFees=[fee("KBM 1 tahun", "Learning activities (1 year)", 4_700_000), fee(*UNIFORM, 1_350_000), fee("Tes IQ", "IQ test", 500_000)], notes=HBN, **P)

# ---------- Padang: SMPIT Surau Minang (2027/2028)
SM = {"title": "SDIT PIS dan SMPIT Surau Minang Buka Pendaftaran Siswa Baru 2027/2028 (Sumbarbisnis)", "url": "https://sumbarbisnis.com/sdit-pis-dan-smpit-surau-minang-buka-pendaftaran-siswa-baru-2027-2028/", "published": "2026-11-02"}
upsert("smpit-surau-minang-padang", name="SMPIT Surau Minang Padang", city="Kota Padang", district="Kuranji", address="Jl. Raya Ampang (belakang Kantor Pos Kuranji), Kota Padang", religion="Islam",
       level="SMP", year="2027/2028", source=SM, checked=CHK, registrationFee=150_000, entryFee={"min": 8_800_000, "max": 8_900_000}, tuition={"amount": 450_000, "period": "month"},
       notes=L("Uang pembangunan Rp8.800.000 (putra) / Rp8.900.000 (putri). Pendaftaran dibuka mulai 11 November 2026.", "Building fee Rp8,800,000 (boys) / Rp8,900,000 (girls). Registration opens 11 November 2026."))
