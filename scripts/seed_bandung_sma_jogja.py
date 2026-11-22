"""- Akurat, "Rekomendasi SMA Swasta Terbaik di Bandung" (5 Aug 2026): -> 2026/2027 (assumed).
- Mojok, "Sekolah Mahal di Jogja, Ada Rupa Ada Harga" (1 Jul 2021): -> 2021/2022 (assumed)."""
from seedlib import L, fee, upsert, UNIFORM

CHK = "2026-11-22"
AK = {"title": "Rekomendasi SMA Swasta Terbaik di Bandung: Lengkap dengan Biaya dan Fasilitas (Akurat)", "url": "https://akurat.co/pendidikan/879727/rekomendasi-sma-swasta-terbaik-di-bandung-lengkap-dengan-biaya-dan-fasilitas", "published": "2026-08-05"}
N = ("Perkiraan dari artikel; tahun ajaran tidak disebut.", "Approximate figures from an article; academic year not stated.")
def s(slug, name, city, district, note, religion=None, **f):
    upsert(slug, name=name, city=city, district=district, religion=religion, level="SMA", year="2026/2027", yearAssumed=True, source=AK, checked=CHK,
           notes=L((note[0] + " " + N[0]).strip(), (note[1] + " " + N[1]).strip()), **f)
KB = "Kota Bandung"
s("smak-1-bpk-penabur-bandung", "SMAK 1 BPK Penabur Bandung", KB, None,
  ("Biaya pendaftaran (paket masuk) sekitar Rp15,5 juta untuk Kelas Unggulan dan Rp13,3 juta untuk Kelas Nasional.", "Admission package about Rp15.5M (Excellence class) and Rp13.3M (National class)."),
  religion="Kristen", entryFee={"min": 13_300_000, "max": 15_500_000})
s("sma-al-irsyad-satya-bandung", "SMA Al-Irsyad Satya", "Kabupaten Bandung Barat", "Padalarang",
  ("Biaya tahunan Rp28–50 juta tergantung program.", "Annual fees Rp28–50M depending on programme."), religion="Islam", tuition={"amount": 28_000_000, "period": "year"})
s("sma-santo-aloysius-1-bandung", "SMA Santo Aloysius 1 Bandung", KB, None, ("SPP bulanan sekitar Rp3 juta. Lokasi di Jl. Sultan Agung.", "Monthly tuition about Rp3M. Located on Jl. Sultan Agung."), religion="Katolik",
  tuition={"amount": 3_000_000, "period": "month"})
s("smak-2-bpk-penabur-bandung", "SMAK 2 BPK Penabur Bandung", KB, None, ("Disebut \"SMA BPK 2 Penabur\". Biaya pendaftaran sekitar Rp6,2 juta termasuk SPP bulan pertama.", "Listed as \"SMA BPK 2 Penabur\". Admission about Rp6.2M incl. first month's tuition."),
  religion="Kristen", entryFee={"min": 6_200_000}, tuition={"amount": 500_000, "period": "month"})
s("sma-santa-angela-bandung", "SMA Santa Angela Bandung", KB, None, ("SPP bulanan sekitar Rp2,5 juta.", "Monthly tuition about Rp2.5M."), religion="Katolik", tuition={"amount": 2_500_000, "period": "month"})

MJ = {"title": "Sekolah Mahal di Jogja, Ada Rupa Ada Harga (Mojok)", "url": "https://mojok.co/liputan/susul/sekolah-mahal-di-jogja-ada-rupa-ada-harga/", "published": "2021-07-01"}
upsert("olifant-school-yogyakarta", name="Olifant School Yogyakarta", city="Sleman", district="Depok", address="Jl. Cendrawasih, Demangan Baru, Condongcatur, Depok, Sleman", level="TK", year="2021/2022", yearAssumed=True,
       source=MJ, checked=CHK, entryFee={"min": 15_000_000}, otherFees=[fee("Experiential activities per tahun", "Experiential activities per year", 3_350_000), fee(*UNIFORM, 750_000), fee("Daftar ulang (naik kelas)", "Re-registration (next grade)", 2_750_000)],
       notes=L("Olifant Preschool. Joining fee Rp15.000.000; total biaya awal Rp21.400.000 termasuk SPP Juli. Artikel 2021, kemungkinan sudah berubah.", "Olifant Preschool. Joining fee Rp15,000,000; initial total Rp21,400,000 incl. July tuition. 2021 article, likely outdated."))
