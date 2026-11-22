"""Official SPMB pages, academic year 2027/2028 (figures verbatim):
- SMAIT Pesantren Nururrahman Depok: https://spmb.smaitpnr.sch.id/ (address from school directories)
- SMP IT Masjid Syuhada Yogyakarta: official SPMB post 2027/2028"""
from seedlib import L, fee, upsert, add_admission

CHK = "2026-11-22"
NR = {"title": "SPMB SMAIT Pesantren Nururrahman TP 2027/2028 (situs resmi)", "url": "https://spmb.smaitpnr.sch.id/"}
upsert("smait-pesantren-nururrahman-depok", name="SMAIT Pesantren Nururrahman Depok", city="Depok", district="Pancoran Mas", religion="Islam",
       address="Jl. Raya Sawangan Km 2, Pancoran Mas, Depok", level="SMA", year="2027/2028", source=NR, checked=CHK,
       registrationFee=400_000, entryFee={"min": 14_000_000}, tuition={"amount": 850_000, "period": "month"},
       otherFees=[fee("Uang kesiswaan per tahun", "Student affairs per year", 3_000_000), fee("Iuran air minum per tahun", "Drinking water per year", 300_000),
                  fee("Asrama pesantren tahfidz", "Tahfidz boarding", 1_500_000)],
       notes=L("Total biaya siswa reguler Rp18.550.000. Gratis pendaftaran untuk calon santri berprestasi (S&K berlaku). Alamat menurut direktori sekolah.",
               "Total for regular students Rp18,550,000. Free registration for high achievers (T&Cs apply). Address from school directories."))

SY = {"title": "Pendaftaran Murid Baru SMP IT Masjid Syuhada TA 2027/2028 (situs resmi)", "url": "https://smpitmasjidsyuhada.sch.id/2026/uncategorized/pendaftaran-murid-baru-smp-it-masjid-syuhada-tahun-ajaran-2027-2028/"}
upsert("smpit-masjid-syuhada-yogyakarta", name="SMPIT Masjid Syuhada Yogyakarta", city="Kota Yogyakarta", website="https://smpitmasjidsyuhada.sch.id",
       level="SMP", year="2027/2028", source=SY, checked=CHK,
       registrationFee=100_000, entryFee={"min": 1_500_000, "max": 5_000_000}, tuition={"amount": 570_000, "period": "month"},
       otherFees=[fee("Dana kegiatan", "Activity fund", 3_500_000), fee("Kain seragam & atribut (putra)", "Uniform fabric & badges (boys)", 1_096_700),
                  fee("Kain seragam & atribut (putri)", "Uniform fabric & badges (girls)", 1_406_000), fee("Buku pelajaran", "Textbooks", 750_000), fee("Komite (per bulan)", "Committee (per month)", 30_000)],
       notes=L("Dana pengembangan (sekali selama sekolah): gelombang inden Rp1.500.000; gelombang 1 Rp2.500.000 (potongan 50%); gelombang 2 Rp3.750.000 (potongan 25%); gelombang 3 Rp5.000.000. Biaya lain: Rp5.946.700 (putra) / Rp6.256.000 (putri).",
               "Development fund (once): early wave Rp1,500,000; wave 1 Rp2,500,000 (50% off); wave 2 Rp3,750,000 (25% off); wave 3 Rp5,000,000. Other costs: Rp5,946,700 (boys) / Rp6,256,000 (girls)."))
add_admission("smpit-masjid-syuhada-yogyakarta", {"level": "SMP", "academicYear": "2027/2028",
    "steps": [L("Isi formulir pendaftaran SPMB 2027/2028 secara online.", "Fill in the SPMB 2027/2028 form online."),
              L("Ikuti wawancara sesuai jadwal gelombang pendaftaran.", "Attend the interview on your wave's schedule."),
              L("Bayar dana pengembangan dan biaya lain sesuai gelombang.", "Pay the development fund and other fees for your wave.")],
    "documents": [L("Gelombang 3: fotokopi ijazah dan Surat Keterangan Nilai TKA (khusus DIY) yang dilegalisir, 1 lembar", "Wave 3: certified copies of the primary certificate and TKA score letter (DIY only), 1 each")],
    "test": L("Wawancara.", "Interview."), "source": SY, "checked": CHK})
print("ok")
