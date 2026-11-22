"""Round 6, 2027/2028 fees.
- YPM Al Fitrah Bandung (official pages per unit).
- SDIT Uswatun Hasanah Cimahi (official PMB page, "Biaya Masuk ... 2027/2028").
- IDN Times Jogja, "Biaya SD Muhammadiyah Sapen dan MSUS 2027/2028" (3 Aug 2026), from the school's SPMB graphic."""
from seedlib import L, fee, upsert, add_admission, UNIFORM

CHK = "2026-11-22"
def afsrc(unit):
    return {"title": f"Pendaftaran {unit} Al Fitrah TA 2027/2028 — YPM Al Fitrah (situs resmi)", "url": f"https://ypmalfitrah.sch.id/pendaftaran-{unit.lower()}-al-fitrah/"}
AF = dict(name="Sekolah Islam Terpadu Al Fitrah Bandung", city="Kota Bandung", district="Buahbatu", address="Jl. Merkuri Timur No.1, Margahayu Raya, Kota Bandung", religion="Islam",
          website="https://ypmalfitrah.sch.id", year="2027/2028", checked=CHK)
AFN = ("Keringanan Rp1.000.000 untuk pendaftaran 12 Agustus–26 Oktober 2026. Bisa dicicil 4 kali (s.d. Mei 2027).", "Rp1,000,000 off for registrations 12 August–26 October 2026. Can be paid in 4 instalments (until May 2027).")
for level, unit, reg, spp, ppd, dev, total, ext_id, ext_en in [
    ("KB", "TKIT", 250_000, 550_000, 1_900_000, 3_550_000, 6_000_000, "Kelas KOBER (kelompok belajar).", "KOBER (play group) class."),
    ("SD", "SDIT", 500_000, 990_000, 5_642_000, 18_208_000, 24_840_000, "Pendaftaran termasuk psikotes. Usia 6 tahun pada Juli.", "Registration includes the psychological test. Age 6 by July."),
    ("SMP", "SMPIT", 400_000, 950_000, 6_875_000, 15_275_000, 23_100_000, "", ""),
    ("SMA", "SMAIT", 350_000, 950_000, 5_930_000, 11_570_000, 18_450_000, "Halaman menulis \"SPP bulan Juli 2026\", kemungkinan salah ketik (periode pendaftaran 2026 untuk tahun ajaran 2027/2028).", "The page says \"July 2026 tuition\", probably a typo (registration in 2026 is for 2027/2028)."),
]:
    upsert("sit-al-fitrah-bandung", level=level, source=afsrc(unit), registrationFee=reg, entryFee={"min": dev}, tuition={"amount": spp, "period": "month"},
           otherFees=[fee("Biaya penyelenggaraan pendidikan (kegiatan 1 tahun, buku, seragam)", "Education provision fee (1 year of activities, books, uniforms)", ppd)],
           notes=L(f"{unit}. Uang pangkal = biaya pengembangan pendidikan. Total uang pangkal + SPP Juli Rp{total:,}. {ext_id} {AFN[0]}".replace(",", "."), f"{unit}. Entry fee = education development fee. Total with July tuition Rp{total:,}. {ext_en} {AFN[1]}"), **AF)

US = {"title": "PMB SDIT Uswatun Hasanah Cimahi — Biaya Masuk 2027/2028 (situs resmi)", "url": "https://www.sdituswahcimahi.sch.id/pmb-sdituswahcimahi/"}
upsert("sdit-uswatun-hasanah-cimahi", name="SDIT Uswatun Hasanah Cimahi", city="Cimahi", district="Cimahi Tengah", address="Jl. MK. Wiganda Sasmita No.19A, Cimahi Tengah, Kota Cimahi", religion="Islam",
       website="https://www.sdituswahcimahi.sch.id", level="SD", year="2027/2028", source=US, checked=CHK,
       registrationFee=300_000, entryFee={"min": 11_000_000, "max": 13_000_000}, tuition={"amount": 600_000, "period": "month"},
       notes=L("Uang pangkal = infaq pendidikan Rp13.000.000; diskon Rp2.000.000 (gelombang 1) / Rp1.000.000 (gelombang 2). Pendaftaran = administrasi tes psikolog. Uang kegiatan tahunan ditetapkan awal pembelajaran.",
               "Entry fee = education donation Rp13,000,000; Rp2,000,000 off (wave 1) / Rp1,000,000 off (wave 2). Registration = psychological test fee. Annual activity fee set at the start of the year."))
add_admission("sdit-uswatun-hasanah-cimahi", {"level": "SD", "academicYear": "2027/2028", "steps": [L("Datang ke kantor Tata Usaha sekolah atau daftar online", "Visit the school office or register online"), L("Bayar Rp300.000 untuk tes psikolog", "Pay Rp300,000 for the psychological test")],
    "documents": [L("Akta kelahiran (usia minimal 6 tahun pada Juli)", "Birth certificate (minimum age 6 by July)")], "source": US, "checked": CHK})

IDN = {"title": "Biaya SD Muhammadiyah Sapen dan MSUS 2027/2028, Segini Bedanya! (IDN Times Jogja)", "url": "https://jogja.idntimes.com/news/jogja/biaya-sd-muhammadiyah-sapen-dan-msus-2027-2028-segini-bedanya-00-yplq6-795z4h", "published": "2026-08-03"}
SP_ADM = {"level": "SD", "academicYear": "2027/2028", "steps": [L("Daftar/inden melalui aplikasi Super Sapen sesuai jadwal", "Register/pre-book through the Super Sapen app on schedule")], "documents": [],
          "notes": L("Peminat sangat tinggi; antrean inden disebut sudah sampai tahun ajaran 2033.", "Very high demand; the pre-booking queue reportedly reaches the 2033 intake."), "source": IDN, "checked": CHK}
upsert("sd-muhammadiyah-sapen-yogyakarta", name="SD Muhammadiyah Sapen Yogyakarta", city="Kota Yogyakarta", district="Gondokusuman", address="Jl. Bimokurdo No.33, Sapen, Demangan, Gondokusuman, Kota Yogyakarta",
       religion="Islam", website="https://www.sdmuhsapen-yog.sch.id", level="SD", year="2027/2028", source=IDN, checked=CHK, tuition={"amount": 1_240_000, "period": "month"},
       otherFees=[fee("Total biaya awal (putra)", "Initial total (boys)", 23_740_000), fee("Total biaya awal (putri)", "Initial total (girls)", 23_890_000)],
       notes=L("Jalur reguler kampus utama. Rincian per komponen tidak dimuat di artikel; total biaya awal dari grafis SPMB resmi.", "Regular track, main campus. The article doesn't itemise the components; totals are from the official SPMB graphic."))
add_admission("sd-muhammadiyah-sapen-yogyakarta", SP_ADM)
upsert("muhammadiyah-sapen-universal-school-bantul", name="Muhammadiyah Sapen Universal School (MSUS)", city="Bantul", district="Kasihan", address="Jl. Brawijaya, Gatak, Tamantirto, Kasihan, Bantul",
       religion="Islam", curriculum=["Nasional", "Cambridge"], level="SD", year="2027/2028", source=IDN, checked=CHK,
       registrationFee=1_000_000, entryFee={"min": 18_000_000}, tuition={"amount": 1_840_000, "period": "month"},
       otherFees=[fee("Biaya kegiatan per tahun", "Activities per year", 9_335_000), fee("Seragam putra", "Uniforms (boys)", 2_165_000), fee("Seragam putri", "Uniforms (girls)", 2_315_000)],
       notes=L("Pengembangan sekolah Rp18.000.000. Biaya bulanan termasuk snack dan makan siang. Total biaya awal Rp31.340.000 (putra) / Rp31.490.000 (putri). Dibuka Juli 2026; Kurikulum Nasional + pengayaan Cambridge dan pendekatan IB.",
               "School development fee Rp18,000,000. Monthly fee includes snacks and lunch. Initial total Rp31,340,000 (boys) / Rp31,490,000 (girls). Opened July 2026; national curriculum with Cambridge enrichment and an IB approach."))
add_admission("muhammadiyah-sapen-universal-school-bantul", SP_ADM)
