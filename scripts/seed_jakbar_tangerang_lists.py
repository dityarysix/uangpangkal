"""Orami "SD Swasta Jakarta Barat" (4 Oct 2023) -> 2023/2024 assumed;
theAsianparent "SD Swasta di Tangerang" (7 Jul 2022) -> 2022/2023 assumed. New schools only."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
OJB = {"title": "Rekomendasi SD Swasta di Jakarta Barat dan Biayanya (Orami)", "url": "https://www.orami.co.id/magazine/sd-swasta-jakarta-barat", "published": "2023-10-04"}
TAP = {"title": "Daftar SD Swasta di Tangerang dan Biayanya (theAsianparent)", "url": "https://id.theasianparent.com/sd-swasta-di-tangerang", "published": "2022-07-07"}
N = ("Perkiraan dari artikel; tahun ajaran tidak disebut.", "Approximate figures from an article; academic year not stated.")
def s(slug, name, city, district, address, source, year, religion=None, note=None, **f):
    nid, nen = note or ("", "")
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year=year, yearAssumed=True, source=source, checked=CHK,
           notes=L((nid + " " + N[0]).strip(), (nen + " " + N[1]).strip()), **f)
M = lambda a: {"amount": a, "period": "month"}
JB = "Jakarta Barat"
Y = "2023/2024"
s("sdit-fajrul-islam-kalideres", "SDIT Fajrul Islam Kalideres", JB, "Kalideres", "Jl. Tanjung Pura 3 No.48, Pegadungan, Kalideres, Jakarta Barat", OJB, Y, "Islam",
  ("Artikel menyebut \"biaya pendaftaran Rp5,2 juta\"; dicatat sebagai biaya masuk.", "The article says \"registration fee Rp5.2M\"; recorded as the entry cost."), entryFee={"min": 5_200_000}, tuition=M(320_000))
s("al-azhar-kembangan", "Sekolah Islam Al Azhar Kembangan", JB, "Kembangan", "Kompleks Unilever, Jl. H. Sa'aba, Meruya Selatan, Kembangan, Jakarta Barat", OJB, Y, "Islam",
  ("SDI Al Azhar 8 Kembangan. Biaya masuk sekitar Rp30 jutaan termasuk formulir Rp400.000.", "SDI Al Azhar 8 Kembangan. Entry cost around Rp30M including the Rp400,000 form."),
  registrationFee=400_000, entryFee={"min": 30_000_000}, tuition=M(1_200_000))
s("sekolah-bisa-jakarta", "Sekolah BISA Jakarta", JB, "Kembangan", "Jl. H. Sa'aba No.25A, Joglo, Kembangan, Jakarta Barat", OJB, Y, None,
  ("Uang pangkal sudah termasuk perlengkapan; SPP termasuk makan siang.", "Entry fee includes supplies; tuition includes lunch."), registrationFee=500_000, entryFee={"min": 20_000_000}, tuition=M(1_450_000))
s("sekolah-narada-jakarta", "Sekolah Narada", JB, "Cengkareng", "Perumahan Kosambi Baru, Jl. Kosambi Baru No.9, Duri Kosambi, Cengkareng, Jakarta Barat", OJB, Y, "Buddha", None,
  registrationFee=300_000, entryFee={"min": 28_800_000}, tuition=M(2_950_000), otherFees=[fee(*UNIFORM, 900_000)])
s("sekolah-providentia-jakarta", "Sekolah Providentia", JB, "Kebon Jeruk", "Jl. Kedoya Raya No.2, Kedoya Utara, Kebon Jeruk, Jakarta Barat", OJB, Y, "Kristen", None,
  registrationFee=100_000, entryFee={"min": 4_500_000}, tuition=M(725_000), otherFees=[fee("Kegiatan per tahun", "Activities per year", 1_900_000), fee(*UNIFORM, 650_000)])
s("tunas-muda-school-jakarta", "Tunas Muda School", JB, "Kembangan", "Jl. Meruya Utara No.71, Meruya Utara, Kembangan, Jakarta Barat", OJB, Y, "Katolik", ("Sekolah IB. SPP per 3 bulan.", "IB school. Tuition per 3 months."),
  curriculum=["IB", "Internasional"], entryFee={"min": 90_000_000}, tuition={"amount": 21_700_000, "period": "quarter"})
s("ananda-islamic-school-jakarta", "Ananda Islamic School", JB, "Kalideres", "Jl. Tanjung Pura No.34, Pegadungan, Kalideres, Jakarta Barat", OJB, Y, "Islam", None,
  registrationFee=650_000, entryFee={"min": 24_300_000}, tuition=M(1_200_000), otherFees=[fee("Kegiatan siswa per tahun", "Student activities per year", 3_000_000), fee("Perlengkapan sekolah", "School supplies", 3_000_000)])

Y = "2022/2023"
s("citra-bangsa-school-tangerang", "Citra Bangsa School Tangerang", "Kota Tangerang", None, "Jl. Raya Prabu Kiansantang, Kota Tangerang", TAP, Y, None, None, registrationFee=250_000, entryFee={"min": 9_000_000})
s("sdit-tunas-harapan-ilahi-tangerang", "SDIT Tunas Harapan Ilahi Tangerang", "Kota Tangerang", "Cipondoh", "Jl. Tugu Karya II No.3, Cipondoh Makmur, Cipondoh, Kota Tangerang", TAP, Y, "Islam",
  ("Uang pangkal = dana pembangunan.", "Entry fee = building fund."), website="https://www.sdit.thi.or.id/", registrationFee=450_000, entryFee={"min": 12_500_000}, tuition=M(850_000),
  otherFees=[fee("Kegiatan siswa per bulan", "Student activities per month", 175_000), fee("Komite per bulan", "Committee per month", 15_000), fee("Buku paket", "Textbooks", 1_000_000), fee("Perlengkapan (seragam dll.)", "Supplies (uniforms etc.)", 1_800_000)])
s("sd-islam-al-azhar-bsd", "SD Islam Al Azhar BSD", "Tangerang Selatan", "Serpong", None, TAP, Y, "Islam", None,
  entryFee={"min": 28_800_000}, tuition=M(1_600_000), otherFees=[fee("Kegiatan siswa", "Student activities", 2_400_000)])
s("sdk-penabur-gading-serpong", "SDK BPK Penabur Gading Serpong", "Kabupaten Tangerang", "Kelapa Dua", "Jl. Kelapa Gading Barat Raya, Gading Serpong, Kabupaten Tangerang", TAP, Y, "Kristen", None,
  registrationFee=350_000, entryFee={"min": 24_900_000}, tuition=M(2_800_000), otherFees=[fee("Psikotes", "Psychological test", 270_000), fee(*ACTIVITY, 1_000_000), fee("Perlengkapan", "Supplies", 2_500_000)])
