"""Popmama, "11 Daftar Biaya Masuk SMP di Jakarta Selatan Tahun Ajaran 2026/2027" (12 Dec 2025).
Figures copied verbatim from the article."""
from seedlib import L, fee, upsert

SRC = {"title": "11 Daftar Biaya Masuk SMP di Jakarta Selatan Tahun Ajaran 2026/2027 (Popmama)",
       "url": "https://www.popmama.com/big-kid/10-12-years-old/daftar-biaya-masuk-smp-di-jakarta-selatan-tahun-ajaran-2026-2027-00-bbqjr-87t30t",
       "published": "2025-12-12"}
C = dict(area="jabodetabek", city="Jakarta Selatan", level="SMP", year="2026/2027", source=SRC, checked="2026-11-22")
WAVE = L("Terdapat diskon gelombang.", "Early-wave discounts available.")

upsert("al-jabr-islamic-school", name="Al Jabr Islamic School", district="Cilandak", religion="Islam", curriculum=["Nasional Plus"],
       address="Jl. Bango II No.38, Pondok Labu, Cilandak, Jakarta Selatan", phone="(021) 75913675", website="https://aljabrislamicschool.sch.id",
       entryFee={"min": 40_000_000}, tuition={"amount": 10_950_000, "period": "quarter"},
       otherFees=[fee("Biaya akademik per tahun", "Academic fee per year", 5_000_000)], **C)
upsert("sekolah-adik-irma", name="Sekolah Adik Irma", district="Tebet",
       address="Jl. Tebet Barat IV, Rawa Bilal, Tebet, Jakarta Selatan", phone="(021) 830 9287 / 0813-8008-5063", website="https://adikirma.com",
       entryFee={"min": 14_500_000}, tuition={"amount": 1_700_000, "period": "month"}, **C)
upsert("al-ihsan-kebagusan", name="Sekolah Al-Ihsan Kebagusan", district="Pasar Minggu", religion="Islam",
       address="Jl. Baung IV No.43, Kebagusan, Pasar Minggu, Jakarta Selatan", phone="(021) 7813033 / 0857-1826-7914", website="https://al-ihsankebagusan.sch.id",
       registrationFee=300_000, entryFee={"min": 20_000_000}, **C)
upsert("azhari-islamic-school-lebak-bulus", name="Azhari Islamic School Lebak Bulus", district="Cilandak", religion="Islam",
       address="Jl. Pertanian Raya No.43, Lebak Bulus, Jakarta Selatan", phone="(021) 7699289 / 0812-9580-1894",
       entryFee={"min": 32_000_000}, tuition={"amount": 2_100_000, "period": "month"},
       otherFees=[fee("Buku & kegiatan (tahunan)", "Books & activities (yearly)", 8_000_000)],
       notes=L("Uang pangkal = admission fee. SPP Juli 2026.", "Entry fee = admission fee. Tuition as of July 2026."), **C)
upsert("bakti-mulya-400", name="Sekolah Bakti Mulya 400", district="Kebayoran Lama", curriculum=["Cambridge"],
       address="Jl. R.A. Kartini, Pondok Pinang, Kebayoran Lama, Jakarta Selatan", phone="(021) 7653627 / 0813-9895-4600", website="https://baktimulya400.sch.id",
       entryFee={"min": 47_500_000, "max": 53_500_000}, tuition={"amount": 9_750_000, "period": "quarter"},
       notes=L("Program Cambridge/SKS: uang pangkal Rp47.500.000, SPP Rp9.750.000 per 3 bulan. Program boarding: uang pangkal Rp53.500.000, SPP Rp28.500.000 per 3 bulan.",
               "Cambridge/accelerated programme: entry Rp47,500,000, tuition Rp9,750,000 per quarter. Boarding: entry Rp53,500,000, tuition Rp28,500,000 per quarter."), **C)
upsert("binus-school-simprug", name="BINUS School Simprug", district="Kebayoran Lama", curriculum=["Internasional"],
       address="Jl. Sultan Iskandar Muda Kav. G-8, Kebayoran Lama, Jakarta Selatan", phone="0811-9700-6969", website="https://simprug.binus.sch.id",
       entryFee={"min": 192_000_000}, tuition={"amount": 49_800_000, "period": "quarter"}, **C)
upsert("madina-islamic-school-tebet", name="Madina Islamic School Tebet", district="Tebet", religion="Islam",
       address="Jl. Tebet Dalam IV No.1, Tebet Barat, Jakarta Selatan", phone="(021) 8312311 / 0821-2308-0368",
       entryFee={"min": 36_500_000}, tuition={"amount": 4_000_000, "period": "month"},
       otherFees=[fee("Uang tahunan", "Annual fee", 11_350_000)], **C)
upsert("mentari-intercultural-school-jakarta", name="Mentari Intercultural School Jakarta", district="Kebayoran Baru",
       address="Jl. H. Jian No.6, Cipete Utara, Kebayoran Baru, Jakarta Selatan", phone="(021) 72794870 / 0878-7773-7937", website="https://mentarischool.com",
       entryFee={"min": 98_000_000}, tuition={"amount": 9_850_000, "period": "month"},
       notes=L("Uang pangkal = uang pengembangan.", "Entry fee = development fee."), **C)
upsert("sekolah-islam-harapan-ibu", name="Sekolah Islam Harapan Ibu", district="Kebayoran Lama", religion="Islam",
       address="Jl. H. Banan No.1, Pondok Pinang, Kebayoran Lama, Jakarta Selatan", phone="(021) 7591122 / 0811-8992-413", website="https://harapanibu.sch.id",
       entryFee={"min": 8_300_000}, tuition={"amount": 1_750_000, "period": "month"},
       otherFees=[fee("Biaya perawatan pengembangan", "Development & maintenance fee", 14_000_000)], notes=WAVE, **C)
upsert("bpk-penabur-tirtamarta-pondok-indah", name="Sekolah Tirtamarta BPK Penabur Pondok Indah", religion="Kristen",
       address="Jl. Sekolah Kencana IV, Pondok Indah, Jakarta Selatan", phone="(021) 7656615 / 0851-7533-8161",
       entryFee={"min": 28_000_000, "max": 30_000_000}, tuition={"amount": 3_650_000, "period": "month"}, **C)
upsert("smp-yasporbi-ii", name="SMP Yasporbi II", district="Pasar Minggu",
       address="Jl. AUP, Komplek Perumahan Bank Indonesia, Pasar Minggu, Jakarta Selatan", phone="(021) 7801835 / 0813-7892-4422", website="https://yasporbi.sch.id",
       entryFee={"min": 15_500_000}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee("Uang kegiatan setahun", "Activity fee (yearly)", 4_800_000)], notes=WAVE, **C)
print("ok smp jaksel")
