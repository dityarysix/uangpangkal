"""New areas, batch 2 — official pages.
- SIT Bina Insani (YABICA), Kabupaten Serang: PMB 2027/2028 fee tables (TK/PG, SD, SMP, SMA).
- Pondok Pesantren Darussalam Rajapolah, Kabupaten Tasikmalaya: PSB 2026–2027 rincian biaya masuk.
- SDIT Mutiara Insani, Delanggu, Klaten (Solo Raya): SPMB 2027/2028 post (16 Sep 2026)."""
from seedlib import L, fee, upsert, ensure_school, add_admission, UNIFORM, BOOKS

CHK = "2026-11-22"

# ---------- SIT Bina Insani Serang
BI = {"title": "PMB SIT Bina Insani T.A. 2027/2028 (situs resmi YABICA)", "url": "https://pmbsit.yabica.com/"}
BIC = dict(name="SIT Bina Insani Serang", city="Kabupaten Serang", district="Waringinkurung", address="Jl. Raya Waringinkurung Km. 4, Kabupaten Serang, Banten",
           religion="Islam", website="https://pmbsit.yabica.com/", phone="0817-6560-665", curriculum=["Nasional"], year="2027/2028", source=BI, checked=CHK)
def bi(level, spp, kbm, infaq, sapra, note_id="", note_en=""):
    total = spp + kbm + infaq + sapra + 100_000
    upsert("sit-bina-insani-serang", level=level, registrationFee=100_000, entryFee={"min": infaq + sapra}, tuition={"amount": spp, "period": "month"},
           otherFees=[fee("KBM", "Learning activities (KBM)", kbm), fee("Komite", "Committee", 100_000)],
           notes=L(f"Uang pangkal = infaq pembangunan Rp{infaq:,} + sapra Rp{sapra:,}. Total awal Rp{total:,} (termasuk SPP bulan pertama). {note_id}".replace(",", ".").strip(),
                   f"Entry fee = building donation Rp{infaq:,} + facilities Rp{sapra:,}. Initial total Rp{total:,} (incl. first month's tuition). {note_en}".strip()), **BIC)
bi("KB", 500_000, 1_500_000, 2_300_000, 1_000_000, "Play Group. TKIT Bina Insani 2: SPP Rp300.000 + KBM Rp1.500.000 saja.", "Play group. TKIT Bina Insani 2: only tuition Rp300,000 + KBM Rp1,500,000.")
bi("TK", 500_000, 1_500_000, 2_300_000, 1_000_000, "TK A. TKIT Bina Insani 2: SPP Rp300.000 + KBM Rp1.500.000 saja.", "TK A. TKIT Bina Insani 2: only tuition Rp300,000 + KBM Rp1,500,000.")
bi("SD", 950_000, 1_600_000, 6_600_000, 4_200_000, "Sama untuk SDIT Bina Insani dan SDIT Bina Insani 2.", "Same for SDIT Bina Insani and SDIT Bina Insani 2.")
bi("SMP", 950_000, 3_000_000, 6_600_000, 3_200_000, "SMPIT Al Masykar Bina Insani, fullday. Boarding: SPP Rp1.750.000 (total Rp14.650.000).", "SMPIT Al Masykar Bina Insani, full-day. Boarding: tuition Rp1,750,000 (total Rp14,650,000).")
bi("SMA", 500_000, 2_750_000, 2_800_000, 1_500_000, "SMAIT Bina Insani, fullday. Boarding: SPP Rp1.000.000 (total Rp8.150.000).", "SMAIT Bina Insani, full-day. Boarding: tuition Rp1,000,000 (total Rp8,150,000).")
for lv in ("TK", "SD"):
    add_admission("sit-bina-insani-serang", {"level": lv, "academicYear": "2027/2028", "period": L("Dibuka 1 Oktober 2026.", "Opened 1 October 2026."),
        "steps": [L("Isi dan lengkapi formulir pendaftaran online, unggah persyaratan", "Fill in the online form and upload the requirements"), L("Bayar biaya pendaftaran Rp100.000", "Pay the Rp100,000 registration fee"),
                  L("Ikuti tes observasi dan wawancara orang tua sesuai jadwal", "Attend the observation test and parent interview as scheduled"), L("Lihat hasil observasi sesuai jadwal", "Check the observation results on the scheduled date")],
        "documents": [L("Fotokopi akta kelahiran", "Copy of birth certificate"), L("Fotokopi Kartu Keluarga", "Copy of family card")], "source": BI, "checked": CHK})

# ---------- Darussalam Rajapolah, Kab. Tasikmalaya
DS = {"title": "Rincian Biaya Masuk PSB 2026–2027 — Pondok Pesantren Darussalam Rajapolah (situs resmi)", "url": "https://psb.darussalam-tasik.or.id/informasi_rincian-biaya-masuk_pg-3.html"}
for lv in ("SMP", "SMA"):
    upsert("pesantren-darussalam-rajapolah-tasikmalaya", name="Pondok Pesantren Darussalam Rajapolah Tasikmalaya", city="Kabupaten Tasikmalaya", district="Rajapolah",
           address="Narunggul, Tanjungpura, Rajapolah, Kabupaten Tasikmalaya", phone="0821-2632-7799", religion="Islam", website="https://www.darussalam-tasik.or.id",
           level=lv, year="2026/2027", source=DS, checked=CHK, registrationFee=200_000, entryFee={"min": 1_000_000},
           otherFees=[fee("Total pembiayaan awal tahun", "Total start-of-year payment", 4_000_000)],
           notes=L("Pesantren (boarding) dengan sekolah formal SMP dan SMA. Uang pangkal = infaq pengembangan pondok dan uang pangkal Rp1.000.000. Total awal tahun Rp4.000.000 sudah termasuk uang makan Rp550.000 dan syahriyah Rp235.000, kegiatan, kesehatan, dll.",
                   "Boarding pesantren with formal SMP and SMA. Entry fee = development donation and entry fee Rp1,000,000. The Rp4,000,000 start-of-year total includes meals Rp550,000 and syahriyah Rp235,000, activities, health, etc."))
    add_admission("pesantren-darussalam-rajapolah-tasikmalaya", {"level": lv, "academicYear": "2026/2027",
        "steps": [L(i, e) for i, e in [("Isi formulir PSB online", "Fill in the online admission form"), ("Bayar biaya pendaftaran dan konfirmasi pembayaran", "Pay the registration fee and confirm payment"),
                  ("Dapatkan ID dan PIN, login akun PSB, cetak formulir", "Get an ID and PIN, log in, print the form"), ("Ikuti tes masuk", "Take the entrance test"),
                  ("Lihat hasil penerimaan", "Check the result"), ("Daftar ulang, setor berkas, bayar biaya sekolah", "Re-register, submit documents, pay school fees")]],
        "documents": [], "source": DS, "checked": CHK})

# ---------- SDIT Mutiara Insani Klaten (Solo Raya)
MI = {"title": "SPMB SDIT Mutiara Insani Tahun Ajaran 2027/2028 Dibuka (situs resmi)", "url": "https://sditmutiarainsani.sch.id/spmb-sdit-mutiara-insani-tahun-ajaran-2027-2028-dibuka-saatnya-menyiapkan-pendidikan-terbaik-untuk-ananda/", "published": "2026-09-16"}
upsert("sdit-mutiara-insani-klaten", name="SDIT Mutiara Insani Klaten", city="Klaten", district="Delanggu", address="Jl. Kaswari, Gatak, Delanggu, Klaten", religion="Islam", website="https://sditmutiarainsani.sch.id",
       level="SD", year="2027/2028", source=MI, checked=CHK, registrationFee=200_000, entryFee={"min": 5_250_000, "max": 6_250_000}, tuition={"amount": 325_000, "period": "month"},
       otherFees=[fee(*BOOKS, 1_000_000), fee("Perpustakaan", "Library", 200_000), fee("Seragam putra", "Uniforms (boys)", 795_000), fee("Seragam putri", "Uniforms (girls)", 942_000)],
       notes=L("Uang pangkal = infaq pendidikan Rp1.000.000 + infaq pengembangan pilihan Rp4.250.000 / Rp4.750.000 / Rp5.250.000. Diskon 20% infaq pengembangan untuk lulusan TKIT Mutiara Insani. Kuota 2 rombel × 28 siswa.",
               "Entry fee = education donation Rp1,000,000 + development donation option Rp4,250,000 / Rp4,750,000 / Rp5,250,000. 20% development-donation discount for TKIT Mutiara Insani graduates. Quota 2 classes × 28."))
add_admission("sdit-mutiara-insani-klaten", {"level": "SD", "academicYear": "2027/2028",
    "period": L("Gelombang I: 19–24 Okt 2026 (TKIT Mutiara Insani/se-yayasan), 26–31 Okt 2026 (TK lain); gelombang II: 23–26 Nov 2026.", "Wave I: 19–24 Oct 2026 (TKIT Mutiara Insani/foundation), 26–31 Oct 2026 (other kindergartens); wave II: 23–26 Nov 2026."),
    "steps": [L("Datang ke sekolah, ambil nomor antrean", "Come to the school and take a queue number"), L("Bayar biaya pendaftaran Rp200.000 dan isi formulir online", "Pay the Rp200,000 registration fee and fill in the online form"),
              L("Serahkan berkas pendaftaran", "Hand in the documents")],
    "documents": [L("Fotokopi rapor TK semester gasal 2026/2027 dilegalisir", "Legalised copy of the kindergarten report (odd semester 2026/2027)"), L("Fotokopi akta kelahiran (2 lembar)", "Copies of birth certificate (2)"),
                  L("Fotokopi Kartu Keluarga (2 lembar)", "Copies of family card (2)"), L("Foto 3×4 (2 lembar)", "3×4 photos (2)")],
    "source": MI, "checked": CHK})
