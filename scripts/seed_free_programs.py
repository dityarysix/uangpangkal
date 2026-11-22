"""Government partner/free private-school programmes (thin areas).
- Banten "Sekolah Gratis" for SMA/SMK/SKh swasta, SPMB Banten 2026/2027: registration, SPP, building fee and LKS are paid by the province
  for students admitted through the programme. Lists from Sindonews (Kota Serang) and Tribun Banten (Kota Cilegon), both citing Dindikbud Banten.
- Pekanbaru: 16 SMP swasta mitra SPMB 2025/2026 (Koran Jakarta, 2 Jul 2025): free for students admitted through the programme (BOSDA)."""
from seedlib import L, upsert

CHK = "2026-11-22"
SN = {"title": "Daftar 783 Sekolah Gratis di Banten 2026, SPP hingga Biaya LKS Ditanggung (Sindonews)", "url": "https://edukasi.sindonews.com/read/1701797/212/daftar-783-sekolah-gratis-di-banten-2026-spp-hingga-biaya-lks-ditanggung-1777518261"}
TB = {"title": "Daftar Sekolah SMA/SMK/SKh Swasta Gratis di Kota Cilegon untuk SPMB Banten 2026/2027 (Tribun Banten)", "url": "https://banten.tribunnews.com/cilegon/154863/daftar-sekolah-smasmkskh-swasta-gratis-di-kota-cilegon-untuk-spmb-banten-20262027"}
BN = L("Sekolah peserta program Sekolah Gratis Pemprov Banten (SPMB 2026/2027): biaya pendaftaran, SPP, biaya bangunan, dan LKS ditanggung provinsi bagi siswa yang diterima lewat program ini. Biaya untuk siswa di luar program bisa berbeda; tanyakan ke sekolah.",
       "Part of Banten province's free private-school programme (SPMB 2026/2027): registration, tuition, building fee and worksheets are paid by the province for students admitted through the programme. Fees outside the programme may differ; ask the school.")
FREE = dict(registrationFee=0, entryFee={"min": 0}, tuition={"amount": 0, "period": "month"})
def slugify(s):
    import re
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
for name, rel in [("SMAS Citra Al-Alawiyah", "Islam"), ("SMAS Al Kautsar Curug", "Islam"), ("SMAS Plus Al-Khairiyah Kasemen", "Islam"), ("SMAS Al Mubarok Kota Serang", "Islam"),
                  ("SMAS PGRI 1 Kota Serang", None), ("SMAS Maulana Yusuf Kota Serang", "Islam"), ("SMAS Nurul Islam Kota Serang", "Islam"), ("SMAS Muhammadiyah Kota Serang", "Islam"),
                  ("SMAS Nur El Bantany Kota Serang", "Islam"), ("SMAS Ardaniah", "Islam"), ("SMAS Nurrurohman", "Islam"), ("SMAS Agro Taktakan", None), ("SMA IT Nurudz Dzikri", "Islam"),
                  ("SMAS Al Huda", "Islam"), ("SMAS IT Darussalam Pipitan", "Islam")]:
    nm = name if "Serang" in name else name + " Kota Serang"
    upsert(slugify(nm), name=nm, city="Kota Serang", religion=rel, level="SMA", year="2026/2027", source=SN, checked=CHK, notes=BN, **FREE)
for name, rel in [("SMAS Al Khairiyah 3 Cilegon", "Islam"), ("SMA Al-Fath Cilegon", "Islam"), ("MAS Al Khairiyah 4 Cilegon", "Islam"), ("SMAS Al Khairiyah 1 Cilegon", "Islam"),
                  ("SMAS Maflahul Ummah Cilegon", "Islam"), ("MAS Al Munawaroh Cilegon", "Islam"), ("SMAS Muhammadiyah Cilegon", "Islam"), ("SMAS Al Ishlah Cilegon", "Islam")]:
    upsert(slugify(name), name=name, city="Cilegon", religion=rel, level="SMA", year="2026/2027", source=TB, checked=CHK, notes=BN, **FREE)

KJ = {"title": "Pekanbaru Sediakan 16 SMP Swasta Gratis bagi yang Tidak Lulus SPMB (Koran Jakarta)", "url": "https://koran-jakarta.com/2025-07-02/pekanbaru-sediakan-16-smp-swasta-gratis-bagi-yang-tidak-lulus-spmb", "published": "2025-07-02"}
PN = L("SMP swasta mitra SPMB Pemkot Pekanbaru 2025/2026: gratis (dibiayai BOS daerah) bagi siswa yang tidak lolos SMP negeri dan diterima lewat program ini. Pada 2026 program diperluas menjadi 23 sekolah. Biaya untuk siswa di luar program bisa berbeda; tanyakan ke sekolah.",
       "Pekanbaru city SPMB partner SMP 2025/2026: free (funded by regional BOS) for students not placed in public SMPs and admitted through the programme. Expanded to 23 schools in 2026. Fees outside the programme may differ; ask the school.")
for slug, name, dist, rel in [
    ("smp-islam-ylpi-pekanbaru", "SMP Islam YLPI Pekanbaru", "Sukajadi", "Islam"), ("smp-telekomunikasi-pekanbaru", "SMP Telekomunikasi Pekanbaru", "Bina Widya", None),
    ("smp-taruna-satria-pekanbaru", "SMP Taruna Satria Pekanbaru", "Tuah Madani", None), ("smp-tri-bhakti-pekanbaru", "SMP Tri Bhakti Pekanbaru", "Payung Sekaki", None),
    ("smp-masmur-pekanbaru", "SMP Masmur Pekanbaru", "Sukajadi", "Kristen"), ("smp-muhammadiyah-5-pekanbaru", "SMP Muhammadiyah 5 Pekanbaru", "Rumbai Pesisir", "Islam"),
    ("smpit-badrul-islam-pekanbaru", "SMPIT Badrul Islam Pekanbaru", "Bina Widya", "Islam"), ("smp-plus-terpadu-pekanbaru", "SMP Plus Terpadu Pekanbaru", "Bina Widya", None),
    ("smp-tunas-karya-pekanbaru", "SMP Tunas Karya Pekanbaru", "Sukajadi", None), ("smp-widya-graha-pekanbaru", "SMP Widya Graha Pekanbaru", "Bukit Raya", None),
    ("smp-dwi-sejahtera-pekanbaru", "SMP Dwi Sejahtera Pekanbaru", "Marpoyan Damai", None), ("smp-yabri-terpadu-pekanbaru", "SMP YABRI Terpadu Pekanbaru", None, None),
    ("smp-nurul-falah-kulim-pekanbaru", "SMP Nurul Falah Kulim Pekanbaru", None, "Islam"), ("smp-pekerti-mulya-pekanbaru", "SMP Pekerti Mulya Pekanbaru", None, None),
    ("smp-plus-ath-thoiba-pekanbaru", "SMP Plus Ath Thoiba Pekanbaru", None, "Islam"), ("smp-islam-nurul-hidayah-pekanbaru", "SMP Islam Nurul Hidayah Pekanbaru", None, "Islam"),
]:
    upsert(slug, name=name, city="Kota Pekanbaru", district=dist, religion=rel, level="SMP", year="2025/2026", source=KJ, checked=CHK, notes=PN, **FREE)
