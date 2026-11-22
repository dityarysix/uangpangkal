"""City lists round 3 (new schools only).
- HaiBunda Bandung (23 Oct 2023) and Semarang (10 Oct 2023): -> 2023/2024 (assumed).
- Orami "SD Islam Terbaik di Bandung" (28 Nov 2022): -> 2022/2023 (assumed). Figures "bisa berubah".
- Orami "Rekomendasi SD di Malang" (24 Jun 2025): -> 2025/2026 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM, BOOKS, ACTIVITY

CHK = "2026-11-22"
HBB = {"title": "20 SD Negeri dan Swasta Bandung Akreditasi Terbaik Beserta Alamat & Estimasi Biaya (HaiBunda)", "url": "https://www.haibunda.com/parenting/20231023170407-61-319975/20-sd-negeri-dan-swasta-bandung-akreditasi-terbaik-beserta-alamat-estimasi-biaya", "published": "2023-10-23"}
HBS = {"title": "15 SD Swasta Akreditasi Terbaik di Semarang Beserta Alamat & Estimasi Biaya (HaiBunda)", "url": "https://www.haibunda.com/parenting/20231010112944-61-318153/15-sd-swasta-akreditasi-terbaik-di-semarang-beserta-alamat-estimasi-biaya", "published": "2023-10-10"}
ORB = {"title": "SD Islam Terbaik di Bandung (Orami)", "url": "https://www.orami.co.id/magazine/sd-islam-terbaik-di-bandung", "published": "2022-11-28"}
ORM = {"title": "Rekomendasi SD di Malang (Orami)", "url": "https://www.orami.co.id/magazine/rekomendasi-sd-di-malang", "published": "2025-06-24"}
N = ("Perkiraan dari artikel; tahun ajaran tidak disebut.", "Approximate figures from an article; academic year not stated.")
def s(slug, name, city, district, address, source, year, religion="Islam", note=None, **f):
    nid, nen = note or ("", "")
    upsert(slug, name=name, city=city, district=district, address=address, religion=religion, level="SD", year=year, yearAssumed=True, source=source, checked=CHK,
           notes=L((nid + " " + N[0]).strip(), (nen + " " + N[1]).strip()), **f)
M = lambda a: {"amount": a, "period": "month"}
KB = "Kota Bandung"

s("bandung-alliance-intercultural-school", "Bandung Alliance Intercultural School", "Kabupaten Bandung Barat", "Padalarang", "Jl. Bujanggamanik Kav., Jl. Parahyangan Raya No.2, Kertajaya, Padalarang, Kabupaten Bandung Barat", HBB, "2023/2024", "Kristen",
  ("Total tahunan Rp191.000.000 = biaya sekolah Rp171.000.000 + retribusi modal Rp20.000.000.", "Annual total Rp191,000,000 = tuition Rp171,000,000 + capital levy Rp20,000,000."),
  tuition={"amount": 171_000_000, "period": "year"}, otherFees=[fee("Retribusi modal per tahun", "Capital levy per year", 20_000_000)])
s("sd-darul-hikam-bandung", "SD Darul Hikam Bandung", KB, "Coblong", "Jl. Ir. H. Juanda No.285, Dago, Coblong, Kota Bandung", HBB, "2023/2024", "Islam", ("SPP Juli termasuk makan siang.", "July tuition includes lunch."),
  registrationFee=600_000, entryFee={"min": 22_000_000}, tuition=M(1_650_000), otherFees=[fee("Kesiswaan", "Student affairs", 2_250_000), fee(*BOOKS, 1_795_000), fee(*UNIFORM, 1_350_000)])
s("sd-darul-hikam-bandung", "SD Darul Hikam Bandung", KB, "Coblong", None, ORB, "2022/2023", "Islam", None, entryFee={"min": 25_000_000}, tuition=M(1_250_000))
s("sd-marsudirini-semarang", "SD Marsudirini Semarang", "Kota Semarang", "Semarang Tengah", "Jl. Pemuda No.157, Sekayu, Semarang Tengah, Kota Semarang", HBS, "2023/2024", "Katolik",
  ("Hanya biaya pendaftaran yang disebut.", "Only the registration fee is given."), registrationFee=200_000)

for slug, name, city, dist, addr, biaya, spp in [
    ("cendekia-muda-elementary-school-bandung", "Cendekia Muda Elementary School", KB, "Arcamanik", "Jl. Arcamanik Endah No.35, Sukamiskin, Arcamanik, Kota Bandung", 25_000_000, 1_400_000),
    ("sd-cendekia-leadership-bukit-ligar", "SD Cendekia Leadership Bukit Ligar", "Kabupaten Bandung", "Cimenyan", "Jl. Ligar Taqwa No.2, Komp. Bukit Ligar, Cibeunying, Cimenyan, Kabupaten Bandung", 43_000_000, 1_700_000),
    ("bandung-islamic-school", "Bandung Islamic School (BISc)", KB, "Sumur Bandung", "Jl. Van Deventer No.12, Kebon Pisang, Sumur Bandung, Kota Bandung", 27_000_000, 1_350_000),
    ("sd-bintang-madani-bandung", "SD Bintang Madani Bandung", KB, "Arcamanik", "Jl. Terusan Pesantren No.102, Cisaranten Bina Harapan, Arcamanik, Kota Bandung", 32_000_000, 950_000),
]:
    s(slug, name, city, dist, addr, ORB, "2022/2023", "Islam", ("Uang masuk = \"biaya pendidikan\" menurut artikel.", "Entry cost = \"education fee\" in the article."), entryFee={"min": biaya}, tuition=M(spp))
s("sdit-nur-al-rahman-cimahi", "SDIT Nur Al Rahman Cimahi", "Cimahi", None, "Jl. Cihanjuang 77A, Cimahi", ORB, "2022/2023", "Islam",
  ("Artikel menulis \"Rp20.275.0000\" (dibaca Rp20.275.000).", "The article writes \"Rp20.275.0000\" (read as Rp20,275,000)."), entryFee={"min": 20_275_000})
s("arvardia-global-islamic-school-bandung", "Arvardia Global Islamic School", KB, "Arcamanik", "Jl. Cisaranten Kulon Raya No.24, Arcamanik, Kota Bandung", ORB, "2022/2023", "Islam", None, entryFee={"min": 29_468_000})
s("sdit-al-irsyad-bandung", "SDIT Al Irsyad Bandung", KB, "Cibeunying Kaler", "Jl. Al-Irsyad Cikutra, Cibeunying Kaler, Kota Bandung", ORB, "2022/2023", "Islam", None, tuition=M(985_000))
s("sd-islam-nurul-amanah-bandung", "SD Islam Nurul Amanah Bandung", KB, "Arcamanik", "Jl. Sumber Sari No.101, Cisaranten Kulon, Arcamanik, Kota Bandung", ORB, "2022/2023", "Islam", None, tuition=M(425_000))

s("sd-katolik-cor-jesu-malang", "SD Katolik Cor Jesu Malang", "Kota Malang", "Klojen", "Jl. Jaksa Agung Suprapto, Samaan, Klojen, Kota Malang", ORM, "2025/2026", "Katolik",
  ("Pendaftaran Rp75.000–Rp150.000; SPP sekitar Rp500.000.", "Registration Rp75,000–Rp150,000; tuition about Rp500,000."), registrationFee=75_000, tuition=M(500_000))
s("bina-bangsa-school-malang", "Bina Bangsa School Malang", "Kota Malang", "Blimbing", "Jl. Jenderal A. Yani Utara, Polowijen, Blimbing, Kota Malang", ORM, "2025/2026", None,
  ("Biaya tahunan Rp113–203 juta; SPP sekitar Rp8,5 juta/bulan.", "Annual fees Rp113–203M; tuition about Rp8.5M/month."), tuition=M(8_500_000), otherFees=[fee("Biaya tahunan (min.)", "Annual fees (min.)", 113_000_000)])
