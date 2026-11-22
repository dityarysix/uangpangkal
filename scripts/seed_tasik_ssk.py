"""Tribun Jabar, "Daftar SMA/SMK Swasta Kerja Sama di Kota dan Kabupaten Tasikmalaya, Alternatif SPMB Jabar 2026".
Admission-only records (no school fee published): SSK partner status, how to apply, and the Jabar province subsidy."""
from seedlib import L, ensure_school, add_admission
import re

CHK = "2026-11-22"
SRC = {"title": "Daftar SMA/SMK Swasta Kerja Sama di Kota dan Kabupaten Tasikmalaya, Alternatif SPMB Jabar 2026 (Tribun Jabar)", "url": "https://jabar.tribunnews.com/jabar-istimewa/1176922/daftar-smasmk-swasta-kerja-sama-di-kota-dan-kabupaten-tasikmalaya-alternatif-spmb-jabar-2026"}
def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
ADM = lambda: {"level": "SMA", "academicYear": "2026/2027",
    "period": L("SPMB Jabar 2026 (Juni 2026).", "SPMB Jabar 2026 (June 2026)."),
    "steps": [L("Daftar melalui portal SPMB Jabar dan pilih sekolah berstatus SSK (sekolah swasta kerja sama)", "Register on the SPMB Jabar portal and choose a school with SSK (partner private school) status"),
              L("Kuota SSK per sekolah 1 rombel; siswa yang diterima mendapat bantuan Pemprov Jabar", "Each SSK school has a quota of one class; admitted students get Jabar province aid")],
    "documents": [], "notes": L("Sekolah swasta kerja sama (SSK) SPMB Jabar 2026. Siswa SSK mendapat bantuan Pemprov Jabar: beasiswa Rp100.000/bulan dan uang bangunan Rp1.500.000/tahun (total Rp2,7 juta). Biaya sekolah tidak dipublikasikan; tanyakan ke sekolah.",
                                 "SPMB Jabar 2026 partner private school (SSK). SSK students get Jabar province aid: Rp100,000/month scholarship and Rp1,500,000/year building fee (Rp2.7M total). School fees are not published; ask the school."),
    "source": SRC, "checked": CHK}
for name, city, rel in [
    ("SMA Pasundan 1 Tasikmalaya", "Kota Tasikmalaya", None), ("SMA Islamic Leader School Tasikmalaya", "Kota Tasikmalaya", "Islam"), ("SMAS Pasundan 2 Tasikmalaya", "Kota Tasikmalaya", None),
    ("SMA Pancasila Tasikmalaya", "Kota Tasikmalaya", None), ("SMA IT At-Taufiq Al-Islamy Tasikmalaya", "Kota Tasikmalaya", "Islam"), ("SMA Plus Nashrul Haq Tasikmalaya", "Kota Tasikmalaya", "Islam"),
    ("SMA Islam Ibnu Siena Tasikmalaya", "Kota Tasikmalaya", "Islam"), ("SMAS Muhammadiyah Tasikmalaya", "Kota Tasikmalaya", "Islam"),
    ("SMAS PGRI 43 Singaparna", "Kabupaten Tasikmalaya", None), ("SMA Alhidayah Puspahiang", "Kabupaten Tasikmalaya", "Islam"), ("SMAS KHZ. Mustafa Tasikmalaya", "Kabupaten Tasikmalaya", "Islam"),
    ("SMAS Pesantren Cintawana", "Kabupaten Tasikmalaya", "Islam"), ("SMAS Muhammadiyah Singaparna", "Kabupaten Tasikmalaya", "Islam"), ("SMA Islam Cipasung", "Kabupaten Tasikmalaya", "Islam"),
    ("SMA Serbabakti Tasikmalaya", "Kabupaten Tasikmalaya", None), ("SMA YAB Sukaratu", "Kabupaten Tasikmalaya", None), ("SMA Al Mukrom Tasikmalaya", "Kabupaten Tasikmalaya", "Islam"),
    ("SMA Islam Cipicung Tasikmalaya", "Kabupaten Tasikmalaya", "Islam"),
]:
    slug = slugify(name)
    ensure_school(slug, name=name, city=city, levels=["SMA"], religion=rel)
    add_admission(slug, ADM())
