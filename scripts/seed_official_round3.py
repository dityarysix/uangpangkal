"""Official 2027/2028 pages (figures verbatim):
- Daarul Qur'an (Daqu) SPMB: https://ppdb.daqu.sch.id/ — campuses inside our areas only.
- Al-Fath School Indonesia tuition 2027/2028: https://alfathschoolindonesia.sch.id/tuition-fee/
- Yayasan Al Ma'soem (Jatinangor) SD & SMA 2027-2028 articles summarising their brochures.
- SMP Muhammadiyah 3 Waru ("SMP Mugaru"), Sidoarjo: https://spmb.smpmugaru.sch.id/en/biaya
- Al Azhar Kembangan and Sekolah Kreativa Bogor: admission periods only (no fees published)."""
from seedlib import L, fee, upsert, add_admission, ensure_school

CHK = "2026-11-22"
DQ = {"title": "SPMB Daarul Qur'an TA 2027/2028 — biaya per unit (situs resmi)", "url": "https://ppdb.daqu.sch.id/"}
PROMO = ("Uang pangkal normal Rp{n}; promo periode indent Rp{p} (selama kuota tersedia; gelombang berikutnya disesuaikan).",
         "Normal entry fee Rp{n}; early (indent) promotion Rp{p} (while places last; later waves are priced differently).")
def dq(slug, name, city, district, level, reg, normal, promo, spp, extra=("", "")):
    n_id, p_id = f"{normal:,}".replace(",", "."), f"{promo:,}".replace(",", ".")
    upsert(slug, name=name, city=city, district=district, religion="Islam", website="https://ppdb.daqu.sch.id",
           level=level, year="2027/2028", source=DQ, checked=CHK, registrationFee=reg,
           entryFee={"min": promo, "max": normal}, tuition={"amount": spp, "period": "month"},
           notes=L(PROMO[0].format(n=n_id, p=p_id) + extra[0], PROMO[1].format(n=f"{normal:,}", p=f"{promo:,}") + extra[1]))
dq("daqu-kalibata", "Sekolah Daarul Qur'an Kalibata", "Jakarta Selatan", "Pancoran", "TK", 500_000, 11_500_000, 8_050_000, 1_500_000, (" KB-TK; diskon 30%.", " Playgroup/kindergarten; 30% off."))
dq("daqu-kalibata", "Sekolah Daarul Qur'an Kalibata", "Jakarta Selatan", "Pancoran", "SD", 500_000, 21_000_000, 10_500_000, 1_650_000, (" Hemat 50%.", " 50% saving."))
dq("daqu-bassura-jakarta-timur", "KB-TK Daarul Qur'an Bassura", "Jakarta Timur", "Jatinegara", "TK", 500_000, 11_500_000, 8_050_000, 1_700_000, (" KB-TK; diskon 30%.", " Playgroup/kindergarten; 30% off."))
dq("daqu-ketapang-tangerang", "Sekolah Daarul Qur'an Ketapang Tangerang", "Kota Tangerang", "Cipondoh", "SD", 500_000, 29_300_000, 14_650_000, 1_750_000, (" Hemat 50% (Juli–Oktober 2026).", " 50% saving (July–October 2026)."))
dq("daqu-ketapang-tangerang", "Sekolah Daarul Qur'an Ketapang Tangerang", "Kota Tangerang", "Cipondoh", "TK", 500_000, 11_450_000, 8_015_000, 1_150_000, (" KB-TK Daqu Tangerang; diskon 30%.", " Daqu Tangerang playgroup/kindergarten; 30% off."))
for lvl in ("SMP", "SMA"):
    upsert("daqu-ketapang-tangerang", name="Sekolah Daarul Qur'an Ketapang Tangerang", city="Kota Tangerang", district="Cipondoh", religion="Islam",
           level=lvl, year="2027/2028", source=DQ, checked=CHK, registrationFee=350_000, entryFee={"min": 7_480_000}, tuition={"amount": 650_000, "period": "month"},
           notes=L("Fullday non-asrama (biaya reguler). Pesantren (asrama) Daqu Tangerang: formulir Rp500.000, uang pangkal Rp30.000.000 (promo indent Rp15.000.000), SPP Rp2.700.000/bulan.",
                   "Day school, non-boarding (regular fees). Daqu Tangerang boarding: form Rp500,000, entry Rp30,000,000 (indent promo Rp15,000,000), tuition Rp2,700,000/month."))
    upsert("daqu-cikarang", name="Sekolah Daarul Qur'an Cikarang", city="Kabupaten Bekasi", religion="Islam",
           level=lvl, year="2027/2028", source=DQ, checked=CHK, registrationFee=350_000, entryFee={"min": 7_480_000}, tuition={"amount": 650_000, "period": "month"},
           notes=L("Fullday non-asrama (biaya reguler). Pesantren (asrama) Daqu Cikarang: formulir Rp500.000, uang pangkal Rp30.000.000 (promo indent Rp15.000.000), SPP Rp2.700.000/bulan.",
                   "Day school, non-boarding (regular fees). Daqu Cikarang boarding: form Rp500,000, entry Rp30,000,000 (indent promo Rp15,000,000), tuition Rp2,700,000/month."))
dq("daqu-semarang-banyumanik", "Sekolah Daarul Qur'an Semarang", "Kota Semarang", "Banyumanik", "TK", 500_000, 10_500_000, 5_250_000, 850_000, (" KB-TK.", " Playgroup/kindergarten."))
dq("daqu-semarang-banyumanik", "Sekolah Daarul Qur'an Semarang", "Kota Semarang", "Banyumanik", "SD", 500_000, 17_500_000, 8_750_000, 1_000_000)
upsert("smp-daqu-ungaran", name="SMP Daarul Qur'an Ungaran", city="Kabupaten Semarang", district="Ungaran", religion="Islam", website="https://ppdb.daqu.sch.id",
       level="SMP", year="2027/2028", source=DQ, checked=CHK, registrationFee=350_000, entryFee={"min": 3_500_000}, tuition={"amount": 250_000, "period": "month"},
       notes=L("Fullday non-asrama.", "Day school, non-boarding."))

AF = {"title": "Tuition Fee 2027/2028 — Al-Fath School Indonesia (situs resmi)", "url": "https://alfathschoolindonesia.sch.id/tuition-fee/"}
AFS = dict(name="Al-Fath School Indonesia", city="Tangerang Selatan", district="Ciputat Timur", religion="Islam", website="https://alfathschoolindonesia.sch.id",
           year="2027/2028", source=AF, checked=CHK, registrationFee=350_000)
DON = ("Sumbangan tahunan min. Rp500.000–maks. Rp2.000.000. ", "Annual donation min. Rp500,000–max. Rp2,000,000. ")
upsert("al-fath-school-indonesia", level="KB", entryFee={"min": 11_000_000}, tuition={"amount": 1_435_000, "period": "month"},
       otherFees=[fee("Uang media (per bulan)", "Media fee (per month)", 160_000), fee("Iuran PTA (per tahun)", "PTA (per year)", 175_000), fee("Seragam (per tahun)", "Uniforms (per year)", 200_000),
                  fee("Daftar ulang KB kecil ke KB besar", "Re-registration (KB small to big)", 1_000_000)], notes=L(DON[0], DON[1]), **AFS)
upsert("al-fath-school-indonesia", level="TK", entryFee={"min": 13_000_000, "max": 14_000_000}, tuition={"amount": 1_633_800, "period": "month"},
       otherFees=[fee("Uang media (per bulan)", "Media fee (per month)", 170_000), fee("Seragam (per tahun)", "Uniforms (per year)", 675_000), fee("Komputer (per tahun)", "Computer (per year)", 700_000),
                  fee("Daftar ulang TK A ke TK B", "Re-registration (TK A to TK B)", 1_250_000)],
       notes=L(DON[0] + "Uang pangkal TK A Rp14.000.000; TK B Rp13.000.000.", DON[1] + "Entry fee TK A Rp14,000,000; TK B Rp13,000,000."), **AFS)
upsert("al-fath-school-indonesia", level="SD", entryFee={"min": 25_000_000}, tuition={"amount": 2_563_300, "period": "month"},
       otherFees=[fee("Uang media (per bulan)", "Media fee (per month)", 170_000), fee("Seragam (per tahun)", "Uniforms (per year)", 1_000_000), fee("Komputer (per tahun)", "Computer (per year)", 700_000),
                  fee("Buku (per tahun)", "Books (per year)", 550_000), fee("Cambridge Test English (per tahun)", "Cambridge English test (per year)", 1_400_000)], notes=L(DON[0], DON[1]), **AFS)
for lvl, uni, cam in (("SMP", 1_650_000, 1_700_000), ("SMA", 1_450_000, 1_800_000)):
    upsert("al-fath-school-indonesia", level=lvl, entryFee={"min": 26_000_000}, tuition={"amount": 2_590_150, "period": "month"},
           otherFees=[fee("Uang media (per bulan)", "Media fee (per month)", 250_000), fee("Iuran PTA (per tahun)", "PTA (per year)", 225_000), fee("Seragam (per tahun)", "Uniforms (per year)", uni),
                      fee("Komputer (per tahun)", "Computer (per year)", 700_000), fee("Buku (per tahun)", "Books (per year)", 925_000), fee("Cambridge Test English (per tahun)", "Cambridge English test (per year)", cam)],
           notes=L(DON[0], DON[1]), **AFS)

MS_SD = {"title": "Berapa Biaya Masuk SD Al Ma'soem Bandung TA 2027–2028 (situs resmi Yayasan Al Ma'soem)", "url": "https://almasoem.sch.id/berapa-biaya-masuk-sd-al-masoem-bandung-tahun-ajaran-2027-2028-dan-apa-saja-komponennya/"}
MS_SMA = {"title": "Berapa Biaya Masuk SMA Al Ma'soem Bandung TA 2027–2028 (situs resmi Yayasan Al Ma'soem)", "url": "https://almasoem.sch.id/berapa-biaya-masuk-sma-al-masoem-bandung-tahun-ajaran-2027-2028-2/"}
MSS = dict(name="Sekolah Al Ma'soem Jatinangor", city="Kabupaten Sumedang", district="Jatinangor", religion="Islam", address="Jl. Raya Cipacing No.22, Jatinangor, Kabupaten Sumedang",
           website="https://almasoem.sch.id", year="2027/2028", checked=CHK)
upsert("sd-al-masoem-jatinangor", level="SD", source=MS_SD, otherFees=[fee("Total biaya masuk gelombang 1", "Total entry cost, wave 1", 12_985_000), fee("Kelengkapan siswa", "Student supplies", 1_110_000), fee("KPAM", "KPAM", 150_000)],
       tuition={"amount": 1_245_000, "period": "month"},
       notes=L("Total biaya masuk per gelombang (termasuk registrasi Rp730.000 dan DPP dengan keringanan berbeda): gelombang 1 Rp12.985.000; gelombang 2 Rp13.640.000; gelombang 3 Rp14.295.000; gelombang 4 Rp14.950.000; extra gelombang Rp15.605.000 (keringanan DPP 0%). Seragam dan buku dapat dihitung terpisah.",
               "Total entry cost by wave (incl. Rp730,000 registration and the DPP with different discounts): wave 1 Rp12,985,000; wave 2 Rp13,640,000; wave 3 Rp14,295,000; wave 4 Rp14,950,000; extra wave Rp15,605,000 (no DPP discount). Uniforms and books may be extra."), registrationFee=730_000, **MSS)
upsert("sd-al-masoem-jatinangor", level="SMA", source=MS_SMA, registrationFee=750_000, tuition={"amount": 1_600_000, "period": "month"},
       otherFees=[fee("Total biaya masuk gelombang 1", "Total entry cost, wave 1", 19_500_000), fee("KPAM", "KPAM", 200_000), fee("Kelengkapan siswa", "Student supplies", 1_300_000),
                  fee("Tambahan boarding", "Boarding supplement", 11_400_000)],
       notes=L("Total biaya masuk SMA reguler: gelombang 1 Rp19.500.000 (DPP -20%, mulai 1 Agustus 2026); gelombang 2 Rp20.525.000 (Oktober 2026); gelombang 3 Rp21.550.000 (Januari 2027); gelombang 4 Rp22.575.000 (April 2027); extra gelombang Rp23.600.000. Kelas internasional mulai sekitar Rp23.885.000.",
               "Total SMA entry cost (regular): wave 1 Rp19,500,000 (DPP −20%, from 1 August 2026); wave 2 Rp20,525,000 (October 2026); wave 3 Rp21,550,000 (January 2027); wave 4 Rp22,575,000 (April 2027); extra wave Rp23,600,000. International class from about Rp23,885,000."), **MSS)

MG = {"title": "Biaya SPMB SMP Muhammadiyah 3 Waru (SMP Mugaru) TA 2027/2028 (situs resmi)", "url": "https://spmb.smpmugaru.sch.id/en/biaya"}
upsert("smp-muhammadiyah-3-waru-sidoarjo", name="SMP Muhammadiyah 3 Waru (Mugaru) Sidoarjo", city="Sidoarjo", district="Waru", religion="Islam",
       address="Jl. Kol. Sugiono 105, Kureksari, Waru, Sidoarjo", website="https://smpmugaru.sch.id", level="SMP", year="2027/2028", source=MG, checked=CHK,
       entryFee={"min": 3_000_000, "max": 7_000_000}, tuition={"amount": 425_000, "period": "month"},
       otherFees=[fee("Biaya kegiatan (Excellence)", "Activities (Excellence)", 4_600_000), fee("Biaya kegiatan (M-ICO)", "Activities (M-ICO)", 5_450_000),
                  fee("Seragam putra", "Uniforms (boys)", 2_285_000), fee("Seragam putri", "Uniforms (girls)", 2_685_000), fee("EPP (M-ICO)", "EPP (M-ICO)", 2_500_000)],
       notes=L("Uang pangkal = DPP Rp7.000.000; periode inden potongan DPP Rp4.000.000 (+ potongan khusus lulusan sekolah Islam). Program Excellence SPP Rp425.000; M-ICO Rp525.000. Total normal: M-ICO Rp17.760.000 (putra) / Rp18.160.000 (putri); Excellence Rp14.310.000 / Rp14.710.000. Total inden: M-ICO putra Rp13.760.000; Excellence Rp10.310.000 / Rp10.710.000.",
               "Entry fee = DPP Rp7,000,000; early (indent) period gets Rp4,000,000 off (plus an extra discount for Islamic-school graduates). Excellence tuition Rp425,000; M-ICO Rp525,000. Normal totals: M-ICO Rp17,760,000 (boys) / Rp18,160,000 (girls); Excellence Rp14,310,000 / Rp14,710,000. Indent totals: M-ICO boys Rp13,760,000; Excellence Rp10,310,000 / Rp10,710,000."))

AK = {"title": "PMB Al Azhar Kembangan TP 2027/2028 (situs resmi)", "url": "https://pmb.alazhar-kembangan.sch.id/"}
ensure_school("al-azhar-kembangan", name="Sekolah Islam Al Azhar Kembangan", city="Jakarta Barat", district="Kembangan", levels=["TK", "SD", "SMP", "SMA"], religion="Islam",
              address="Jl. H. Saaba Raya, Komp. Unilever, Meruya Selatan, Kembangan, Jakarta Barat", website="https://pmb.alazhar-kembangan.sch.id")
add_admission("al-azhar-kembangan", {"academicYear": "2027/2028",
    "period": L("Pendaftaran murid baru 7 September 2026–29 Juni 2027 untuk TKI Al Azhar 9, SDI Al Azhar 8, SMPI Al Azhar 10 (termasuk jalur prestasi non-tes), dan SMA Islam Al Azhar 20 Kembangan.",
                "Registration 7 September 2026–29 June 2027 for TKI Al Azhar 9, SDI Al Azhar 8, SMPI Al Azhar 10 (incl. a no-test achievement track) and SMA Islam Al Azhar 20 Kembangan."),
    "steps": [L("Daftar online dan bayar uang pendaftaran Rp500.000 via Bank Syariah Indonesia.", "Register online and pay the Rp500,000 registration fee via Bank Syariah Indonesia."),
              L("Tunggu jadwal observasi.", "Wait for the observation schedule.")],
    "test": L("Observasi.", "Observation."), "notes": L("SD: usia minimal 6 tahun pada Juli 2027. Besaran uang pangkal dan SPP tidak terbaca di halaman.", "SD: minimum age 6 by July 2027. Entry fee and tuition amounts are not shown on the page."),
    "source": AK, "checked": CHK})

KV = {"title": "Penerimaan Murid Baru 2027/2028 — Sekolah Kreativa Bogor (situs resmi)", "url": "https://sekolahkreativa.sch.id/"}
ensure_school("sekolah-kreativa-bogor", name="Sekolah Kreativa Bogor", city="Kota Bogor", levels=["KB", "TK", "SD", "SMP"], religion="Islam",
              address="KB-TK: Jl. Johar Raya No.38, Taman Yasmin; SD: Jl. Kranji Ujung No.71, Sukaresmi; SMP: Jl. Raya Munjul, Kayu Manis — Kota Bogor",
              phone="KB-TK 0819-9994-4038 · SD 0815-7474-3744", website="https://sekolahkreativa.sch.id")
add_admission("sekolah-kreativa-bogor", {"academicYear": "2027/2028",
    "period": L("SPMB 28 September–7 November 2026; early bird (28 September–3 Oktober 2026) potongan uang pangkal Rp500.000; diskon jalur prestasi SMP 50%; tarif khusus alumni.",
                "Admissions 28 September–7 November 2026; early bird (28 September–3 October 2026) Rp500,000 off the entry fee; 50% off for the SMP achievement track; special alumni rates."),
    "notes": L("Sekolah inklusi dengan kuota khusus anak berkebutuhan khusus di setiap jenjang. Besaran biaya tidak dicantumkan.", "Inclusive school with places reserved for children with special needs at every level. Fee amounts are not published."),
    "source": KV, "checked": CHK})
print("ok")
