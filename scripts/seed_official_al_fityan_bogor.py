"""Official fee flyers (PDF) of Al-Fityan School Bogor, academic year 2027/2028.
https://alfityanbogor.sch.id/biaya/  — one PDF per level, uploaded September 2026.
Figures read from the flyers. Struck-through prices are shown as the normal price in notes."""
from seedlib import L, fee, upsert

BASE = "https://alfityanbogor.sch.id/wp-content/uploads/2026/09/Biaya-{}-TP.-2027-2028.pdf"
SCHOOL = dict(name="Al-Fityan School Bogor", city="Kabupaten Bogor", district="Cileungsi", religion="Islam",
              address="Cileungsi, Kabupaten Bogor, Jawa Barat 16820", phone="0813-8051-5414", website="https://alfityanbogor.sch.id")
C = dict(year="2027/2028", checked="2026-11-22", **SCHOOL)
def src(level): return {"title": f"Biaya PPDB {level} Al-Fityan Bogor TP 2027/2028 (brosur resmi)", "url": BASE.format(level)}
ONE_OFF = ("Building fee dan sarana prasarana dibayar satu kali selama bersekolah di unit ini; kegiatan pendidikan dibayar sekali setahun; iuran komite termasuk tagihan SPP bulanan. ",
           "Building fee and facilities fee are paid once per school level; the education activities fee once a year; the committee fee is included in the monthly tuition bill. ")

upsert("al-fityan-school-bogor", level="TK", source=src("TK"), registrationFee=300_000,
       entryFee={"min": 2_200_000, "max": 2_800_000}, tuition={"amount": 575_000, "period": "month"},
       otherFees=[fee("Sarana prasarana (Play Group / TK A)", "Facilities fee (Playgroup / TK A)", 2_000_000), fee("Sarana prasarana (TK B)", "Facilities fee (TK B)", 1_500_000),
                  fee("Iuran komite (per bulan)", "Committee fee (per month)", 25_000), fee("Kegiatan pendidikan (Play Group / TK A, per tahun)", "Education activities (Playgroup / TK A, per year)", 1_800_000),
                  fee("Kegiatan pendidikan (TK B, per tahun)", "Education activities (TK B, per year)", 2_400_000), fee("Peralatan KBM / buku paket", "Learning materials / textbooks", 950_000),
                  fee("Seragam putra", "Uniforms (boys)", 900_000), fee("Seragam putri", "Uniforms (girls)", 920_000)],
       notes=L(ONE_OFF[0] + "Building fee: Play Group & TK A Rp2.800.000, TK B Rp2.200.000. Total masuk TK B putra Rp8.550.000; Play Group/TK A putra Rp9.050.000.",
               ONE_OFF[1] + "Building fee: Playgroup & TK A Rp2,800,000, TK B Rp2,200,000. Total on entry: TK B boys Rp8,550,000; Playgroup/TK A boys Rp9,050,000."), **C)
upsert("al-fityan-school-bogor", level="SD", source=src("SD"), registrationFee=300_000,
       entryFee={"min": 6_000_000}, tuition={"amount": 1_200_000, "period": "month"},
       otherFees=[fee("Sarana prasarana (sekali bayar)", "Facilities fee (one-off)", 3_000_000), fee("Iuran komite (per bulan)", "Committee fee (per month)", 25_000),
                  fee("Kegiatan pendidikan (per tahun)", "Education activities (per year)", 2_500_000), fee("Peralatan KBM / buku paket", "Learning materials / textbooks", 1_365_000),
                  fee("Seragam putra", "Uniforms (boys)", 1_230_000), fee("Seragam putri", "Uniforms (girls)", 1_450_000)],
       notes=L(ONE_OFF[0] + "SPP sudah termasuk makan siang. Total masuk: putra Rp15.320.000, putri Rp15.540.000. Promo bebas biaya pendaftaran untuk 50 pendaftar pertama.",
               ONE_OFF[1] + "Tuition includes lunch. Total on entry: boys Rp15,320,000, girls Rp15,540,000. Registration fee waived for the first 50 applicants."), **C)
upsert("al-fityan-school-bogor", level="SMP", source=src("SMP"), registrationFee=300_000,
       entryFee={"min": 3_000_000}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee("Sarana prasarana (full day, sekali bayar)", "Facilities fee (day school, one-off)", 2_500_000), fee("Iuran komite (per bulan)", "Committee fee (per month)", 30_000),
                  fee("Kegiatan pendidikan (per tahun)", "Education activities (per year)", 3_500_000), fee("Buku paket", "Textbooks", 2_000_000),
                  fee("Seragam putra", "Uniforms (boys)", 1_500_000), fee("Seragam putri", "Uniforms (girls)", 1_830_000)],
       notes=L(ONE_OFF[0] + "Building fee Rp3.000.000 (diskon dari Rp5.000.000). Full day: sarana prasarana Rp2.500.000 (dari Rp3.000.000), SPP Rp1.500.000 termasuk makan siang. Boarding: sarana prasarana Rp3.000.000 (dari Rp3.500.000), SPP Rp2.500.000 termasuk makan 3x, laundry, dan asrama. Total masuk full day putra Rp14.030.000; boarding putra Rp15.530.000.",
               ONE_OFF[1] + "Building fee Rp3,000,000 (discounted from Rp5,000,000). Day school: facilities Rp2,500,000 (from Rp3,000,000), tuition Rp1,500,000 incl. lunch. Boarding: facilities Rp3,000,000 (from Rp3,500,000), tuition Rp2,500,000 incl. 3 meals, laundry and boarding. Total on entry: day school boys Rp14,030,000; boarding boys Rp15,530,000."), **C)
upsert("al-fityan-school-bogor", level="SMA", source=src("SMA"), registrationFee=300_000,
       entryFee={"min": 0}, tuition={"amount": 1_500_000, "period": "month"},
       otherFees=[fee("Sarana prasarana (full day, sekali bayar)", "Facilities fee (day school, one-off)", 2_500_000), fee("Iuran komite (per bulan)", "Committee fee (per month)", 30_000),
                  fee("Kegiatan pendidikan (per tahun)", "Education activities (per year)", 3_500_000), fee("Buku paket", "Textbooks", 2_300_000),
                  fee("Seragam putra", "Uniforms (boys)", 1_550_000), fee("Seragam putri", "Uniforms (girls)", 1_830_000)],
       notes=L(ONE_OFF[0] + "Building fee gratis (normal Rp5.000.000). Full day: sarana prasarana Rp2.500.000 (dari Rp3.000.000), SPP Rp1.500.000 termasuk makan siang. Boarding: sarana prasarana Rp3.000.000 (dari Rp3.500.000), SPP Rp2.300.000 termasuk makan 3x, laundry, dan asrama. Total masuk full day putra Rp11.380.000; boarding putra Rp12.680.000.",
               ONE_OFF[1] + "Building fee waived (normally Rp5,000,000). Day school: facilities Rp2,500,000 (from Rp3,000,000), tuition Rp1,500,000 incl. lunch. Boarding: facilities Rp3,000,000 (from Rp3,500,000), tuition Rp2,300,000 incl. 3 meals, laundry and boarding. Total on entry: day school boys Rp11,380,000; boarding boys Rp12,680,000."), **C)
print("ok")
