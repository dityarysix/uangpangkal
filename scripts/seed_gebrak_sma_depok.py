"""Gebrak.id, "8 SMA Swasta Akreditasi A di Depok dengan Biaya Masuk Mulai Rp2,7 Juta" (compiled 12 Jun 2026).
Fees for the 2026/2027 intake (assumed from the article's timing)."""
from seedlib import L, upsert

CHK = "2026-11-22"
SRC = {"title": "Tak Lolos SMA Negeri? Ini 8 SMA Swasta Akreditasi A di Depok dengan Biaya Masuk Mulai Rp2,7 Juta (Gebrak.id)", "url": "https://www.gebrak.id/2026/06/tak-lolos-sma-negeri-ini-8-sma-swasta.html", "published": "2026-06-12"}
N = L("Uang pangkal dan SPP dari tabel artikel (dirangkum 12 Juni 2026). Konfirmasi ke sekolah.", "Entry fee and tuition from the article's table (compiled 12 June 2026). Confirm with the school.")
for slug, name, district, addr, pmin, pmax, smin, rel in [
    ("sma-yapan-indonesia-depok", "SMA Yapan Indonesia Depok", "Sawangan", "Jl. Raya Muchtar No.50, Sawangan Baru, Depok", 6_750_000, None, 500_000, None),
    ("sma-pgri-depok", "SMA PGRI Depok", "Pancoran Mas", "Jl. Pemuda, Belimbing 3 No.2, Pancoran Mas, Depok", 6_060_000, None, 270_000, None),
    ("sma-yadika-12-depok", "SMA Yadika 12 Depok", "Limo", "Jl. Limo Raya Blok Isan No.20, Meruyung, Limo, Depok", 9_500_000, None, 850_000, None),
    ("sma-muhammadiyah-4-depok", "SMA Muhammadiyah 4 Depok", "Pancoran Mas", "Jl. Masjid Al Hukama No.21, Parung Bingung, Rangkapan Jaya Baru, Pancoran Mas, Depok", 12_000_000, None, 500_000, "Islam"),
    ("sma-perjuangan-terpadu-depok", "SMA Perjuangan Terpadu Depok", "Pancoran Mas", "Jl. Raya Sawangan No.1, Rangkapan Jaya Baru, Pancoran Mas, Depok", 14_550_000, None, 850_000, None),
    ("sma-citra-negara-depok", "SMA Citra Negara Depok", "Beji", "Jl. Kemiri Jaya II No.99, Tanah Baru, Beji, Depok", 6_000_000, None, 500_000, None),
    ("sma-putra-bangsa-depok", "SMA Putra Bangsa Depok", "Beji", "Jl. Kedondong No.3, Kemiri Muka, Beji, Depok", 5_300_000, 7_250_000, 300_000, None),
    ("sma-arrahman-depok", "SMA Arrahman Depok", "Cipayung", "Jl. Masjid Al Ittihad No.35, Bojong Pondok Terong, Cipayung, Depok", 2_750_000, None, 300_000, "Islam"),
]:
    notes = N if slug != "sma-putra-bangsa-depok" else L("SPP Rp300.000–Rp500.000/bulan. " + N["id"], "Tuition Rp300,000–Rp500,000/month. " + N["en"])
    upsert(slug, name=name, city="Depok", district=district, address=addr, religion=rel, level="SMA", year="2026/2027", yearAssumed=True, source=SRC, checked=CHK,
           entryFee={"min": pmin, **({"max": pmax} if pmax else {})}, tuition={"amount": smin, "period": "month"}, notes=notes)
