"""Semarang Raya schools.
- Sekolah Islam Nurus Sunnah Semarang, official SPMB page for 2027/2028 (registration fee only): https://nurussunnah.sch.id/ppdb/
Deliberately NOT used: theasianparent 2022 list (fees from 2018–2020, too old to be useful) and undated "sekitar" figures."""
from seedlib import L, upsert

NS = {"title": "SPMB Sekolah Islam Nurus Sunnah Semarang TP 2027/2028 (situs resmi)", "url": "https://nurussunnah.sch.id/ppdb/"}
upsert("sekolah-islam-nurus-sunnah-semarang", name="Sekolah Islam Nurus Sunnah Semarang", city="Kota Semarang", district="Tembalang", religion="Islam",
       address="Jl. Bulusan Utara Raya No.12, Bulusan, Tembalang, Kota Semarang", website="https://nurussunnah.sch.id",
       level="SD", year="2027/2028", source=NS, checked="2026-11-22", registrationFee=275_000,
       notes=L("Program SD Reguler (target hafalan 3 juz) dan SD Tahfidz (12 juz). Situs hanya mencantumkan biaya pendaftaran; ada potongan untuk siswa berprestasi. Uang pangkal dan SPP tidak dipublikasikan. Pendaftaran dibuka 20 Agustus 2025 hingga kuota terpenuhi.",
               "Regular SD (3 juz memorisation target) and Tahfidz SD (12 juz). The site only lists the registration fee; discounts for high achievers. Entry fee and tuition are not published. Registration opened 20 August 2025 until places are filled."))
print("ok")
