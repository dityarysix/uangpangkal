"""Bali.
- Official: Bali Island School (Fee Schedule SY 2026-2027 PDF), Green School Bali (Tuition & Fees 2026-2027 PDF),
  Canggu Community School (Fees page, 2026-27).
- Lokalfinds, "International Schools in Bali: Official 2026 Fees" (Jul 2026): compiled from each school's
  official schedule (AIS Bali, ProEd, British School of Bali, Sunrise, Pelangi).
- HaiBunda, "20 SD Negeri dan Swasta Denpasar Akreditasi Terbaik" (30 Oct 2023): -> 2023/2024 (assumed)."""
from seedlib import L, fee, upsert

CHK = "2026-11-22"
Y = lambda a: {"amount": a, "period": "year"}

# ---------- Bali Island School (official)
BIS = {"title": "Fee Schedule & Terms School Year 2026-2027 — Bali Island School (PDF resmi)", "url": "https://baliinternationalschool.com/wp-content/uploads/2026/04/Tuition-fees-SY-26-27-updated-16-april.pdf"}
BC = dict(name="Bali Island School (BIS)", city="Kota Denpasar", district="Denpasar Selatan", address="Sanur, Denpasar", website="https://baliinternationalschool.com",
          curriculum=["IB", "Internasional"], year="2026/2027", source=BIS, checked=CHK, registrationFee=2_500_000)
BN = ("Biaya aplikasi Rp2.500.000 (siswa baru). Capital Levy Charge dibayar bersama tagihan pertama. Cicilan 4x menambah 1,5%.", "Application fee Rp2,500,000 (new students). Capital Levy Charge is paid with the first invoice. Paying in 4 instalments adds 1.5%.")
for lv, tui, clc, nid, nen in [
    ("TK", 131_783_000, 22_252_000, "Kindy. Preschool 3 (setengah hari) Rp54.598.000; Preschool 4 Rp70.723.000.", "Kindy. Preschool 3 (half day) Rp54,598,000; Preschool 4 Rp70,723,000."),
    ("SD", 208_952_000, 25_675_000, "Grade 1–2; Grade 3–5 Rp211.921.000; Grade 6 Rp232.578.000 (CLC Rp28.527.000).", "Grades 1–2; Grades 3–5 Rp211,921,000; Grade 6 Rp232,578,000 (CLC Rp28,527,000)."),
    ("SMP", 250_979_000, 28_527_000, "Grade 7–8; Grade 9 Rp252.672.000.", "Grades 7–8; Grade 9 Rp252,672,000."),
    ("SMA", 258_805_000, 28_527_000, "Grade 10; Grade 11–12 (IB DP) Rp301.738.000.", "Grade 10; Grades 11–12 (IB DP) Rp301,738,000."),
]:
    upsert("bali-island-school", level=lv, entryFee={"min": clc}, tuition=Y(tui), notes=L(f"{nid} Uang pangkal = Capital Levy Charge (per tahun ajaran masuk). {BN[0]}", f"{nen} Entry = Capital Levy Charge. {BN[1]}"), **BC)

# ---------- Green School Bali (official)
GS = {"title": "Green School Bali Tuition & Fees Schedule 2026-2027 (PDF resmi)", "url": "https://bali.greenschool.org/wp-content/uploads/sites/2/2026/02/26-27-GSB-Tuition-Fees-Schedule-.docx.pdf"}
GC = dict(name="Green School Bali", city="Badung", district="Abiansemal", address="Jl. Raya Sibang Kaja, Br. Saren, Abiansemal, Badung", website="https://bali.greenschool.org",
          curriculum=["Internasional"], year="2026/2027", source=GS, checked=CHK, registrationFee=4_000_000, entryFee={"min": 36_000_000})
GN = ("Aplikasi Rp4.000.000 + registrasi sekali Rp36.000.000; deposit Rp30.000.000 (dapat dikembalikan). Tuition = pembayaran setahun penuh; bayar per semester +3%, per term +8%. Diskon sibling 5–15%.",
      "Application Rp4,000,000 + one-time registration Rp36,000,000; refundable deposit Rp30,000,000. Tuition = full-year payment; semester payment +3%, termly +8%. Sibling discounts 5–15%.")
for lv, tui, nid, nen in [("TK", 219_176_020, "KG; Pre-K Rp185.445.400.", "KG; Pre-K Rp185,445,400."), ("SD", 249_263_690, "Grade 1–3; Grade 4–5 Rp254.894.600.", "Grades 1–3; Grades 4–5 Rp254,894,600."),
                          ("SMP", 287_350_080, "Grade 6–8.", "Grades 6–8."), ("SMA", 304_468_000, "Grade 9–10; Grade 11–12 Rp328.600.900; biaya service trip SMA Rp7.250.000.", "Grades 9–10; Grades 11–12 Rp328,600,900; high-school service trips Rp7,250,000.")]:
    upsert("green-school-bali", level=lv, tuition=Y(tui), otherFees=[fee("Deposit (dapat dikembalikan)", "Refundable deposit", 30_000_000)], notes=L(f"{nid} {GN[0]}", f"{nen} {GN[1]}"), **GC)

# ---------- Canggu Community School (official)
CCS = {"title": "Fees — Canggu Community School, Compulsory Fee Schedule 2026-2027 (situs resmi)", "url": "https://www.ccsbali.com/admissions/fees"}
CC = dict(name="Canggu Community School (CCS)", city="Badung", district="Kuta Utara", address="Tibubeneng, Canggu, Kuta Utara, Badung", website="https://www.ccsbali.com",
          curriculum=["Cambridge", "IB", "Internasional"], year="2026/2027", source=CCS, checked=CHK, registrationFee=2_500_000)
CN = ("Biaya aplikasi Rp2.500.000. Registrasi Rp17.000.000 (anak pertama) / Rp14.000.000 (anak berikutnya) untuk Year 1–13. Diskon 5% bayar setahun, 2% per semester; diskon sibling.",
      "Application Rp2,500,000. Registration Rp17,000,000 (first child) / Rp14,000,000 (each additional) for Years 1–13. 5% off annual payment, 2% per semester; sibling discount.")
for lv, tui, nid, nen in [("TK", 117_000_000, "Early Years (Preschool–Reception).", "Early Years (Preschool–Reception)."), ("SD", 162_000_000, "Year 1–2; Year 3–6 Rp173.000.000.", "Years 1–2; Years 3–6 Rp173,000,000."),
                          ("SMP", 214_000_000, "Year 7–9.", "Years 7–9."), ("SMA", 243_000_000, "Year 10; Year 11 Rp261.000.000; IB Diploma Year 12–13 Rp272.000.000.", "Year 10; Year 11 Rp261,000,000; IB Diploma Years 12–13 Rp272,000,000.")]:
    upsert("canggu-community-school", level=lv, tuition=Y(tui), **({"entryFee": {"min": 14_000_000, "max": 17_000_000}} if lv != "TK" else {}), notes=L(f"{nid} {CN[0]}", f"{nen} {CN[1]}"), **CC)

# ---------- Lokalfinds (official schedules compiled)
LF = {"title": "International Schools in Bali: Official 2026 Fees (Lokalfinds)", "url": "https://lokalfinds.com/blog/international-schools-bali-2026", "published": "2026-07-01"}
LN = ("Dihimpun Lokalfinds dari jadwal biaya resmi sekolah (Juli 2026).", "Compiled by Lokalfinds from the school's official fee schedule (July 2026).")
def lf(slug, name, city, district, address, level, tui, note, curriculum=None, year="2026/2027", **f):
    upsert(slug, name=name, city=city, district=district, address=address, curriculum=curriculum or ["Internasional"], level=level, year=year, source=LF, checked=CHK,
           tuition=Y(tui), notes=L(note[0] + " " + LN[0], note[1] + " " + LN[1]), **f)
AISN = ("Jadwal tahun kalender 2026 (Jan–Des). Capital Levy Rp20 juta (Foundation)–Rp50 juta (Year 9–12) per tahun; Material & Resources Levy Rp6,4–12,8 juta; aplikasi Rp2 juta, registrasi Rp5 juta, deposit Rp5 juta.",
        "Calendar-year 2026 schedule (Jan–Dec). Annual Capital Levy Rp20M (Foundation)–Rp50M (Years 9–12); Material & Resources Levy Rp6.4–12.8M; application Rp2M, registration Rp5M, deposit Rp5M.")
AIS = dict(name="Australian Independent School (AIS) Bali", city="Kota Denpasar", district=None, address=None, curriculum=["Internasional"], registrationFee=5_000_000)
lf("ais-bali", level="TK", tui=75_930_000, note=("Early Years (full-time). Opsi 3 hari/minggu sekitar Rp45,6 juta. " + AISN[0], "Early Years (full-time). 3-days-a-week option about Rp45.6M. " + AISN[1]), **AIS)
lf("ais-bali", level="SMA", tui=190_720_000, note=("Year 11–12. " + AISN[0], "Years 11–12. " + AISN[1]), **AIS)
PEN = ("Registrasi sekali Rp11.025.000; Development Levy Rp13,125 juta (s.d. Year 6)–Rp15,75 juta (Year 7+); Material Levy Rp15,225 juta; Wellbeing Levy Rp5,25 juta. Diskon: bayar setahun −5%, sibling −5%.",
       "One-time registration Rp11,025,000; Development Levy Rp13.125M (to Year 6)–Rp15.75M (Year 7+); Material Levy Rp15.225M; Wellbeing Levy Rp5.25M. Discounts: annual payment −5%, siblings −5%.")
PE = dict(name="ProEd Global School Umalas", city="Badung", district="Kuta Utara", address="Umalas, Kuta Utara, Badung", curriculum=["Cambridge", "Internasional"], registrationFee=11_025_000)
lf("proed-global-school-umalas", level="TK", tui=92_400_000, note=("Nursery. " + PEN[0], "Nursery. " + PEN[1]), entryFee={"min": 13_125_000}, **PE)
lf("proed-global-school-umalas", level="SMA", tui=202_650_000, note=("Year 9–13. Kampus Nuanu s.d. Rp213.150.000 (Year 10–11). " + PEN[0], "Years 9–13. Nuanu campus up to Rp213,150,000 (Years 10–11). " + PEN[1]), entryFee={"min": 15_750_000}, **PE)
BSN = ("Jadwal 2026-27 masih \"draft\". Tarif tahunan sudah termasuk diskon 5% bayar di muka; termasuk perlengkapan. Aplikasi Rp4 juta, enrolment Rp30 juta per keluarga; makan siang Rp10 juta/term.",
       "2026-27 schedule still marked \"draft\". Annual rate includes the 5% early-payment discount and supplies. Application Rp4M, enrolment Rp30M per family; lunch Rp10M/term.")
BSB = dict(name="The British School of Bali", city="Gianyar", district="Tegallalang", address="Tegallalang, Gianyar", curriculum=["Internasional"], registrationFee=4_000_000, entryFee={"min": 30_000_000})
lf("british-school-of-bali", level="TK", tui=230_000_000, note=("Nursery, Reception. " + BSN[0], "Nursery, Reception. " + BSN[1]), **BSB)
lf("british-school-of-bali", level="SD", tui=240_000_000, note=("Year 1–6. " + BSN[0], "Years 1–6. " + BSN[1]), **BSB)
SUN = ("Tuition per term ×4. Resource Levy tahunan Rp6,5–21,25 juta; registrasi siswa baru Rp10 juta. Semua pembayaran tidak dapat dikembalikan.", "Tuition per term ×4. Annual Resource Levy Rp6.5–21.25M; new-student registration Rp10M. All payments are non-refundable.")
SU = dict(name="Sunrise School Bali", city="Badung", district="Kuta Utara", address="Kerobokan, Kuta Utara, Badung", curriculum=["Internasional"], registrationFee=10_000_000)
lf("sunrise-school-bali", level="TK", tui=49_000_000, note=("Small World setengah hari (Rp12,25 juta/term). " + SUN[0], "Small World half day (Rp12.25M/term). " + SUN[1]), **SU)
lf("sunrise-school-bali", level="SMP", tui=124_000_000, note=("Year 7–9 (Rp31 juta/term). " + SUN[0], "Years 7–9 (Rp31M/term). " + SUN[1]), **SU)
PLN = ("Biaya tahunan all-inclusive (dana pengembangan, sumber belajar, tuition). Registrasi Rp500.000; enrolment siswa baru Rp15 juta; deposit Rp10 juta (dapat dikembalikan).",
       "All-inclusive annual fees (development fund, resources, tuition). Registration Rp500,000; new-student enrolment Rp15M; refundable deposit Rp10M.")
PL = dict(name="Pelangi School Ubud", city="Gianyar", district="Ubud", address="Mas, Ubud, Gianyar", curriculum=["Nasional"], registrationFee=500_000, entryFee={"min": 15_000_000})
lf("pelangi-school-ubud", level="TK", tui=53_250_000, note=("Tiny Tots setengah hari. " + PLN[0], "Tiny Tots half day. " + PLN[1]), **PL)
lf("pelangi-school-ubud", level="SMP", tui=126_900_000, note=("Middle Class 8. " + PLN[0], "Middle Class 8. " + PLN[1]), **PL)

# ---------- HaiBunda Denpasar (2023)
HB = {"title": "20 SD Negeri dan Swasta Denpasar Akreditasi Terbaik Beserta Alamat & Estimasi Biaya (HaiBunda)", "url": "https://www.haibunda.com/parenting/20231030232934-61-319955/20-sd-negeri-dan-swasta-denpasar-akreditasi-terbaik-beserta-alamat-estimasi-biaya", "published": "2023-10-30"}
HN = ("Estimasi dari artikel 2023; tahun ajaran tidak disebut.", "Estimate from a 2023 article; academic year not stated.")
def hb(slug, name, city, district, address, religion=None, note=("", ""), **f):
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year="2023/2024", yearAssumed=True, source=HB, checked=CHK,
           notes=L((note[0] + " " + HN[0]).strip(), (note[1] + " " + HN[1]).strip()), **f)
hb("sdit-albanna-denpasar", "SDIT Albanna Denpasar", "Kota Denpasar", "Denpasar Timur", "Jl. Tukad Yeh Ho III No.16, Dangin Puri Klod, Denpasar Timur", "Islam",
   ("Artikel menulis \"Rp12.000.0000\" (dibaca Rp12.000.000) untuk biaya pengembangan.", "The article writes \"Rp12.000.0000\" (read as Rp12,000,000) for the development fee."),
   entryFee={"min": 12_000_000}, tuition={"amount": 900_000, "period": "month"}, otherFees=[fee("Biaya operasional", "Operational fee", 2_650_000)])
hb("gandhi-memorial-intercontinental-school-bali", "Gandhi Memorial Intercontinental School (GMIS) Bali", "Kota Denpasar", "Denpasar Selatan", "Jl. Tukad Penet No.8A, Renon, Denpasar Selatan", None,
   ("Artikel hanya menyebut \"estimasi biaya Rp67.000.000\".", "The article only gives an \"estimated cost of Rp67,000,000\"."), otherFees=[fee("Estimasi biaya (tidak dirinci)", "Estimated cost (not itemised)", 67_000_000)])
hb("sekolah-lentera-kasih-bali", "Sekolah Lentera Kasih Bali", "Badung", "Kuta Utara", "Jl. Gunung Salak No.88, Kerobokan, Kuta Utara, Badung", "Kristen", ("Biaya formulir.", "Form fee."), registrationFee=200_000)
hb("sd-saraswati-sukawati", "SD Saraswati Sukawati", "Gianyar", "Sukawati", "Jl. Lettu Nengah Duaji, Sukawati, Gianyar", "Hindu",
   ("Uang gedung dibayar sekali untuk 6 tahun.", "Building fee paid once for 6 years."), entryFee={"min": 5_000_000}, tuition={"amount": 380_000, "period": "month"},
   otherFees=[fee("Uang aktivitas per bulan", "Activities per month", 170_000), fee("Uang makan per bulan", "Meals per month", 150_000)])
hb("sd-widiatmika-jimbaran", "SD Widiatmika Jimbaran", "Badung", "Kuta Selatan", "Jl. Raya Kampus Unud, Jimbaran, Kuta Selatan, Badung", "Hindu",
   ("Biaya masuk Rp16.420.000 (alumni TK Widiatmika) / Rp17.420.000 (non-alumni).", "Entry Rp16,420,000 (TK Widiatmika alumni) / Rp17,420,000 (others)."),
   entryFee={"min": 16_420_000, "max": 17_420_000}, tuition={"amount": 1_150_000, "period": "month"})
