"""Gudangberita, "Viral! Biaya Sekolah SD Swasta di Batam Tembus Rp 50 Juta" (17 Aug 2025).
Figures from a parent's Instagram survey of schools, stated as academic year 2024/2025."""
from seedlib import L, upsert
CHK = "2026-11-22"
GB = {"title": "Viral! Biaya Sekolah SD Swasta di Batam Tembus Rp 50 Juta, Warganet Heboh (Gudangberita)", "url": "https://gudangberita.co.id/viral-biaya-sekolah-sd-swasta-di-batam-tembus-rp-50-juta-warganet-heboh/", "published": "2025-08-17"}
N = ("Data TA 2024/2025 dari survei pribadi orang tua (unggahan Instagram) yang dikutip media; uang pangkal umumnya sudah termasuk seragam, buku, dan fasilitas. Konfirmasi ke sekolah.",
     "2024/2025 figures from a parent's own survey (Instagram post) quoted by the outlet; entry fees usually include uniforms, books and facilities. Confirm with the school.")
for slug, name, rel, pmin, pmax, spp, extra in [
    ("sekolah-mondial-batam", "Sekolah Mondial Batam", None, 49_470_000, 49_870_000, 2_980_000, ("Uang pangkal Rp49.470.000 (putra) / Rp49.870.000 (putri).", "Entry fee Rp49,470,000 (boys) / Rp49,870,000 (girls).")),
    ("australian-intercultural-school-batam", "Australian Intercultural School (AIS) Batam", None, 21_450_000, None, 2_450_000, ("", "")),
    ("sd-yos-sudarso-batam", "SD Yos Sudarso Batam", "Katolik", 9_850_000, None, 630_000, ("", "")),
    ("sekolah-yehonala-batam", "Sekolah Yehonala Batam", "Kristen", 24_900_000, None, 1_400_000, ("", "")),
    ("monte-sienna-school-batam", "Monte Sienna School Batam", None, 50_000_000, None, None, ("Disebut \"Sekolah Montesiana\"; uang pangkal \"sekitar Rp50 jutaan\", SPP tidak disebut. Berlokasi di Sungai Jodoh, Batu Ampar.", "Listed as \"Sekolah Montesiana\"; entry fee \"around Rp50 million\", tuition not given. Located in Sungai Jodoh, Batu Ampar.")),
]:
    upsert(slug, name=name, city="Kota Batam", religion=rel, level="SD", year="2024/2025", source=GB, checked=CHK,
           entryFee={"min": pmin, **({"max": pmax} if pmax else {})}, **({"tuition": {"amount": spp, "period": "month"}} if spp else {}),
           notes=L((extra[0] + " " + N[0]).strip(), (extra[1] + " " + N[1]).strip()))
