"""Semarang Raya schools.
- Sekolah Islam Nurus Sunnah Semarang, official SPMB page for 2027/2028 (registration fee only): https://nurussunnah.sch.id/ppdb/
Deliberately NOT used: theasianparent 2022 list (fees from 2018–2020, too old to be useful) and undated "sekitar" figures."""
from seedlib import L, fee, upsert, add_admission

NS = {"title": "SPMB Sekolah Islam Nurus Sunnah Semarang TP 2027/2028 (situs resmi)", "url": "https://nurussunnah.sch.id/ppdb/"}
upsert("sekolah-islam-nurus-sunnah-semarang", name="Sekolah Islam Nurus Sunnah Semarang", city="Kota Semarang", district="Tembalang", religion="Islam",
       address="Jl. Bulusan Utara Raya No.12, Bulusan, Tembalang, Kota Semarang", website="https://nurussunnah.sch.id",
       level="SD", year="2027/2028", source=NS, checked="2026-11-22", registrationFee=275_000,
       notes=L("Program SD Reguler (target hafalan 3 juz) dan SD Tahfidz (12 juz). Situs hanya mencantumkan biaya pendaftaran; ada potongan untuk siswa berprestasi. Uang pangkal dan SPP tidak dipublikasikan. Pendaftaran dibuka 20 Agustus 2025 hingga kuota terpenuhi.",
               "Regular SD (3 juz memorisation target) and Tahfidz SD (12 juz). The site only lists the registration fee; discounts for high achievers. Entry fee and tuition are not published. Registration opened 20 August 2025 until places are filled."))
print("ok")

# ---- Nakita, "Biaya Masuk SD Swasta Semarang, Tentukan Pilihan Terbaik untuk Anak!" (26 Mar 2024) ----
NK = {"title": "Biaya Masuk SD Swasta Semarang, Tentukan Pilihan Terbaik untuk Anak! (Nakita)", "url": "https://nakita.grid.id/read/024050247/biaya-masuk-sd-swasta-semarang-tentukan-pilihan-terbaik-untuk-anak?page=all", "published": "2024-03-26"}
NKC = dict(city="Kota Semarang", level="SD", year="2024/2025", yearAssumed=True, source=NK, checked="2026-11-22")
REC = L("Sumber merangkum dari berbagai sumber tanpa tahun ajaran; sebagian angka di artikel yang sama berasal dari tahun lebih lama.", "The source compiles figures from various sources without academic years; some figures in the same article are older.")
upsert("sd-islam-al-azhar-25-semarang", name="SD Islam Al Azhar 25 Semarang", district="Semarang Barat", religion="Islam",
       address="Jl. WR. Supratman Kav. 31-32, Gisikdrono, Semarang Barat, Kota Semarang",
       entryFee={"min": 20_000_000}, tuition={"amount": 1_000_000, "period": "month"}, notes=REC, **NKC)
upsert("sdit-bina-amal-semarang", name="SDIT Bina Amal Semarang", district="Semarang Selatan", religion="Islam",
       address="Jl. Kyai Saleh, Mugassari, Semarang Selatan, Kota Semarang",
       registrationFee=150_000, tuition={"amount": 250_000, "period": "month"},
       notes=L(REC["id"] + " Uang pangkal tidak dicantumkan.", REC["en"] + " Entry fee not listed."), **NKC)

# ---- SMP Mah'ad Islam Semarang, official PPDB page 2025/2026 ----
MI = {"title": "PPDB SMP Mah'ad Islam Semarang TA 2025/2026 (situs resmi)", "url": "https://smp.mahadislam.sch.id/ppdb-smp-mahad-islam-semarang-2024-2025/"}
upsert("smp-mahad-islam-semarang", name="SMP Mah'ad Islam Semarang", city="Kota Semarang", religion="Islam",
       address="Jl. Citarum Selatan No.9, Bugangan, Kota Semarang", website="https://smp.mahadislam.sch.id",
       level="SMP", year="2025/2026", source=MI, checked="2026-11-22", registrationFee=50_000,
       otherFees=[fee("Paket seragam", "Uniform package", 500_000)],
       notes=L("Besaran infaq pendidikan tidak tercantum di halaman. Potongan infaq 30% bila kakak masih bersekolah di SMP Ma'had Islam; 50% untuk lulusan SD Ma'had Islam.",
               "The education infaq amount is not shown on the page. 30% off the infaq if an older sibling attends; 50% off for SD Ma'had Islam graduates."))
add_admission("smp-mahad-islam-semarang", {"level": "SMP", "academicYear": "2025/2026",
    "steps": [L("Ambil dan isi formulir di panitia PPDB (Rp50.000).", "Get and fill in the form from the admissions committee (Rp50,000)."),
              L("Serahkan berkas pendaftaran.", "Hand in the registration documents."),
              L("Ikuti seleksi/wawancara.", "Attend the selection/interview."),
              L("Diterima bila syarat lengkap, uang paket dan infaq pendidikan lunas, dan lolos seleksi.", "Accepted once documents are complete, the package and infaq are paid, and the selection is passed.")],
    "documents": [L("Fotokopi ijazah SD/MI", "Copy of primary school certificate"), L("Pas foto 3x4 (2 lembar)", "3x4 photos (2)"),
                  L("Fotokopi Kartu Keluarga", "Copy of family card"), L("Fotokopi piagam (bila ada)", "Copies of certificates (if any)")],
    "source": MI, "checked": "2026-11-22"})
print("ok semarang 2")
