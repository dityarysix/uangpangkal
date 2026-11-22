"""Popmama, "Biaya Sekolah SMP di Tangerang & Tangerang Selatan Terbaru" (1 Dec 2025).
Figures copied verbatim. The article does not state the academic year; it was published
during 2026/2027 admissions, so entries are marked 2026/2027 with yearAssumed=True."""
from seedlib import L, fee, upsert, UNIFORM, ACTIVITY, BOOKS

SRC = {"title": "Biaya Sekolah SMP di Tangerang & Tangerang Selatan Terbaru (Popmama)",
       "url": "https://www.popmama.com/big-kid/10-12-years-old/biaya-sekolah-smp-di-tangerang-tangsel-terbaru-orangtua-wajib-cek-00-sdwkg-ccc7f7",
       "published": "2025-12-01"}
C = dict(area="jabodetabek", level="SMP", year="2026/2027", yearAssumed=True, source=SRC, checked="2026-11-22")
TS = "Tangerang Selatan"

upsert("smp-islam-al-azhar-25-setu", name="SMP Islam Al-Azhar 25", city=TS, district="Setu", religion="Islam",
       address="Jl. Kelapa Dua No.50, Babakan, Setu, Tangerang Selatan",
       registrationFee=550_000, entryFee={"min": 27_000_000}, tuition={"amount": 1_825_000, "period": "month"},
       notes=L("Uang sekolah kelas prestasi Rp1.825.000; kelas bilingual Rp1.930.000.", "Tuition: achievement class Rp1,825,000; bilingual class Rp1,930,000."), **C)
upsert("al-fath-school-indonesia", name="Al-Fath School Indonesia", city=TS, district="Ciputat Timur", religion="Islam",
       website="https://alfathschoolindonesia.sch.id",
       registrationFee=350_000, entryFee={"min": 26_000_000}, tuition={"amount": 2_490_150, "period": "month"},
       otherFees=[fee("Uang media (per bulan)", "Media fee (per month)", 250_000), fee("Iuran PTA (per tahun)", "PTA fee (per year)", 225_000),
                  fee("Cambridge Test English (per tahun)", "Cambridge English test (per year)", 1_450_000), fee("Seragam (per tahun)", "Uniforms (per year)", 1_450_000),
                  fee("Komputer (per tahun)", "Computer (per year)", 700_000), fee("Buku (per tahun)", "Books (per year)", 750_000)],
       notes=L("SPP sudah termasuk katering makan siang. Sumbangan min. Rp500.000 – maks. Rp2.000.000/tahun.", "Tuition includes lunch catering. Donation min. Rp500,000 – max. Rp2,000,000/year."), **C)
upsert("technosa-school", name="Technosa School", city=TS, district="Serpong Utara", website="https://www.technosa.sch.id",
       registrationFee=250_000, entryFee={"min": 10_000_000}, tuition={"amount": 875_000, "period": "month"},
       otherFees=[fee(*ACTIVITY, 2_000_000), fee("Seragam (termasuk jas laboratorium)", "Uniforms (incl. lab coat)", 850_000)], **C)
upsert("global-jaya-school", name="Global Jaya School", city=TS, district="Pondok Aren", curriculum=["IB"], website="https://www.globaljaya.com",
       entryFee={"min": 25_000_000}, tuition={"amount": 138_000_000, "period": "year"},
       notes=L("Uang pangkal = SP development fee (1 tahun).", "Entry fee = development fee (1 year)."), **C)
upsert("smp-islam-amalina", name="SMP Islam Amalina", city=TS, district="Pondok Aren", religion="Islam",
       registrationFee=950_000, entryFee={"min": 21_000_000, "max": 24_000_000}, tuition={"amount": 1_100_000, "period": "month"}, **C)
upsert("smp-bhakti-prima-pamulang", name="SMP Bhakti Prima", city=TS, district="Pamulang", website="https://bhaktiprima.sch.id",
       registrationFee=300_000, entryFee={"min": 8_514_300, "max": 10_000_000}, tuition={"amount": 1_014_300, "period": "month"},
       otherFees=[fee(*UNIFORM, 625_000)],
       notes=L("Uang pangkal = uang gedung. Tanpa uang kegiatan; uang buku menyusul.", "Entry fee = building fee. No activity fee; book fee to follow."), **C)
upsert("sekolah-pelita-harapan-lippo-village", name="Sekolah Pelita Harapan Lippo Village", city="Kabupaten Tangerang", district="Kelapa Dua", curriculum=["Internasional"],
       registrationFee=3_000_000,
       otherFees=[fee("1 tahun akademik (sesuai sumber)", "1 academic year (as stated by source)", 284_000_000)], **C)
upsert("sampoerna-academy-bsd", name="Sampoerna Academy BSD", city=TS, district="Serpong", curriculum=["Internasional"], website="https://www.sampoernaacademy.sch.id",
       registrationFee=8_000_000, tuition={"amount": 119_900_000, "period": "year"},
       notes=L("Grade 7 & 8: Rp119.900.000/tahun; Grade 9: Rp135.000.000/tahun. Belum termasuk buku, seragam, field trip.",
               "Grades 7 & 8: Rp119,900,000/year; Grade 9: Rp135,000,000/year. Excludes books, uniforms, field trips."), **C)
upsert("jade-school-serpong", name="Jade School", city=TS, district="Serpong Utara", website="https://www.jade-school.com",
       registrationFee=0, entryFee={"min": 0}, tuition={"amount": 1_700_000, "period": "month"},
       otherFees=[fee("Administrasi per semester (Maret & September)", "Administration per semester (March & September)", 1_500_000)],
       notes=L("Tanpa uang pendaftaran dan uang pangkal. Seragam ± Rp1.000.000; ekskul ± Rp400.000/ekskul; kegiatan maks. Rp1.000.000/kegiatan.",
               "No registration or entry fee. Uniforms ~Rp1,000,000; extracurriculars ~Rp400,000 each; activities up to Rp1,000,000 each."), **C)
upsert("sekolah-athalia", name="Sekolah Athalia", city=TS, district="Serpong Utara",
       registrationFee=400_025, tuition={"amount": 2_600_000, "period": "month"},
       otherFees=[fee("Uang alat & bahan (UAB)", "Tools & materials fee", 3_100_000)],
       notes=L("Sumber juga mencantumkan \"SPP Rp27.000.000\" (kemungkinan uang pangkal; konfirmasi ke sekolah). Perkiraan seragam & buku Rp2.200.000.",
               "The source also lists \"SPP Rp27,000,000\" (probably the entry fee; confirm with the school). Estimated uniforms & books Rp2,200,000."), **C)
upsert("global-islamic-school-serpong", name="Global Islamic School (GIS) Serpong", city=TS, district="Serpong", religion="Islam",
       registrationFee=750_000, entryFee={"min": 34_650_000}, tuition={"amount": 2_200_000, "period": "month"},
       otherFees=[fee("Kegiatan (per tahun)", "Activities (per year)", 4_655_000), fee("Perlengkapan (per tahun)", "Supplies (per year)", 5_865_000), fee("BKOMG (per tahun)", "Parent–teacher body (per year)", 300_000)], **C)
upsert("sekolah-an-nisaa-izada", name="Sekolah An-Nisaa' Izada", city=TS, district="Pondok Aren", religion="Islam", website="https://annisaa-izada.sch.id",
       registrationFee=850_000, entryFee={"min": 37_300_000}, tuition={"amount": 2_885_000, "period": "month"},
       otherFees=[fee("Iuran INSAANI", "INSAANI contribution", 255_000), fee("Perpustakaan", "Library", 300_000)],
       notes=L("Uang pangkal = biaya penerimaan.", "Entry fee = admission fee."), **C)
upsert("sekolah-auliya", name="Sekolah Auliya", city=TS, district="Pondok Aren", religion="Islam", website="https://sekolahauliya.sch.id",
       registrationFee=500_000, entryFee={"min": 40_900_000}, tuition={"amount": 2_400_000, "period": "month"},
       notes=L("Uang pangkal = biaya penerimaan.", "Entry fee = admission fee."), **C)
upsert("millennia-world-school", name="Millennia World School", city=TS, district="Ciputat", curriculum=["Internasional"],
       registrationFee=600_000, entryFee={"min": 21_150_000}, tuition={"amount": 3_400_000, "period": "month"},
       otherFees=[fee("Uang kegiatan (per tahun)", "Activity fee (per year)", 3_300_000), fee(*UNIFORM, 1_550_000)], **C)
print("ok")
