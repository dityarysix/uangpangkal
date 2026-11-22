"""theAsianparent "SD Swasta di Bogor" (7 Jul 2022) and "SD Swasta di Medan" (8 Jul 2022): -> 2022/2023 (assumed). New schools only."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
BG = {"title": "Daftar SD Swasta di Bogor dan Biayanya (theAsianparent)", "url": "https://id.theasianparent.com/sd-swasta-di-bogor", "published": "2022-07-07"}
MD = {"title": "Daftar SD Swasta di Medan dan Biayanya (theAsianparent)", "url": "https://id.theasianparent.com/sd-swasta-di-medan", "published": "2022-07-08"}
N = ("Dari artikel 2022; tahun ajaran tidak disebut, kemungkinan sudah berubah.", "From a 2022 article; academic year not stated, likely outdated.")
M = lambda a: {"amount": a, "period": "month"}
def s(slug, name, city, district, address, source, religion=None, note=("", ""), **f):
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year="2022/2023", yearAssumed=True, source=source, checked=CHK,
           notes=L((note[0] + " " + N[0]).strip(), (note[1] + " " + N[1]).strip()), **f)
KBG, KOB = "Kabupaten Bogor", "Kota Bogor"
s("sd-al-azhar-syifa-budi-bogor", "SD Al-Azhar Syifa Budi Bogor", KOB, "Bogor Selatan", "Jl. Nirwana Residence, Mulyaharja, Bogor Selatan, Kota Bogor", BG, "Islam",
  ("Uang pangkal = biaya pengembangan/gedung.", "Entry = development/building fee."), registrationFee=600_000, entryFee={"min": 30_700_000}, tuition=M(1_700_000))
s("sd-salman-al-farisi-cibinong", "SD Salman Al Farisi Cibinong", KBG, "Cibinong", "Jl. Raya Setu Cikaret, Cibinong, Kabupaten Bogor", BG, "Islam",
  ("Total biaya awal sekitar Rp18 jutaan; rincian uang pangkal tidak disebut.", "Initial total around Rp18M; entry fee not itemised."),
  registrationFee=250_000, tuition=M(740_000), otherFees=[fee("Kegiatan tahunan", "Annual activities", 1_500_000)])
s("sdit-al-hidayah-cibinong", "SDIT Al Hidayah Cibinong", KBG, "Cibinong", "Jl. KSR Dadi Kusmayadi, Cibinong, Kabupaten Bogor", BG, "Islam",
  ("Uang pangkal = biaya bangunan Rp7,5 juta + sarpras Rp2,7 juta. Total sekitar Rp13 jutaan.", "Entry = building Rp7.5M + facilities Rp2.7M. Total about Rp13M."),
  entryFee={"min": 10_200_000}, tuition=M(625_000),
  otherFees=[fee("Pengembangan pendidikan 1 tahun", "Education development (1 year)", 1_800_000), fee("Seragam putra", "Uniforms (boys)", 420_000), fee("Seragam putri", "Uniforms (girls)", 785_000), fee(*BOOKS, 900_000)])
s("an-nahl-islamic-school-gunung-putri", "An-Nahl Islamic School", KBG, "Gunung Putri", "Jl. Raya Ciangsana KM 7, Gunung Putri, Kabupaten Bogor", BG, "Islam", ("Buku Rp700 ribu–Rp1 juta.", "Books Rp700k–Rp1M."),
  entryFee={"min": 30_000_000}, tuition=M(1_900_000),
  otherFees=[fee(*UNIFORM, 1_400_000), fee("Kegiatan tahunan", "Annual activities", 2_300_000), fee("Program parenting", "Parenting programme", 200_000), fee("Kegiatan orang tua", "Parent activities", 150_000)])
s("kinderfield-highfield-bogor", "Kinderfield Highfield Bogor", KOB, None, "Jl. Lawang Gintung, Kota Bogor", BG, None, ("Buku dan kegiatan Rp4–5 juta per tahun; uang penerimaan termasuk seragam.", "Books and activities Rp4–5M per year; acceptance fee includes uniforms."),
  entryFee={"min": 32_500_000}, tuition={"amount": 7_800_000, "period": "quarter"}, otherFees=[fee("Tes pendaftaran", "Entrance test", 500_000), fee("Uang penerimaan", "Acceptance fee", 2_000_000)])
s("sdit-al-madinah-cibinong", "SDIT Al-Madinah Cibinong", KBG, "Cibinong", "Jl. Sukahati, Karadenan, Cibinong, Kabupaten Bogor", BG, "Islam",
  ("Uang pangkal termasuk buku dan bahan seragam; SPP termasuk makan siang.", "Entry includes books and uniform fabric; tuition includes lunch."), website="https://sekolahalmadinah.com/",
  registrationFee=250_000, entryFee={"min": 20_800_000}, tuition=M(1_200_000))
s("sd-labs-school-kaizen-bogor", "SD Labs School Kaizen", KBG, "Gunung Putri", "Perumahan Bumi Mutiara, Bojong Kulur, Gunung Putri, Kabupaten Bogor", BG, "Islam",
  ("Uang pangkal termasuk seragam, infaq gedung, buku paket 1 tahun, psikotes.", "Entry includes uniforms, building donation, 1 year of textbooks, psychological test."),
  registrationFee=300_000, entryFee={"min": 15_000_000}, tuition=M(850_000), otherFees=[fee("Daftar ulang", "Re-registration", 3_000_000)])

MED = "Kota Medan"
s("namira-international-islamic-school-medan", "Namira International Islamic School Medan", MED, "Medan Selayang", "Jl. Setiabudi Pasar 1 No.76, Tanjung Sari, Medan Selayang, Kota Medan", MD, "Islam",
  ("Biaya pendaftaran Rp3.225.000 (siswa Namira) / Rp6.975.000 (siswa baru).", "Registration Rp3,225,000 (Namira students) / Rp6,975,000 (new students)."), registrationFee=6_975_000)
s("sd-sutomo-1-medan", "SD Sutomo 1 Medan", MED, "Medan Perjuangan", "Jl. Jambi No.40B / Jl. M.H. Thamrin No.55, Medan", MD, None, ("Uang pangkal = biaya pembangunan.", "Entry = building fee."),
  registrationFee=300_000, entryFee={"min": 3_000_000})
s("bina-insan-mandiri-medan", "Sekolah Bina Insan Mandiri Medan", MED, "Medan Timur", "Jl. Bambu II No.62, Durian, Medan Timur, Kota Medan", MD, None, ("Hanya uang sekolah bulanan yang disebut.", "Only the monthly fee is given."), tuition=M(1_250_000))
s("perguruan-harapan-mandiri-medan", "Perguruan Harapan Mandiri Medan", MED, "Medan Johor", "Jl. Brigjend Zein Hamid No.40, Titi Kuning, Medan Johor, Kota Medan", MD, None,
  registrationFee=1_600_000, tuition=M(465_000), otherFees=[fee("ADM I", "Admin I", 465_000), fee(*UNIFORM, 630_000), fee("Pramuka", "Scouts", 180_000)])
