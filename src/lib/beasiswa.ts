/**
 * Scholarship info (panel on the home page + full page /beasiswa/).
 * Every item is summarised from the provider's OWN page, read on BEASISWA_CHECKED:
 *   PIP        https://pip.kemendikdasmen.go.id/
 *   KIP Kuliah https://kip-kuliah.kemdiktisaintek.go.id/
 *   Garuda     https://beasiswagaruda.kemdiktisaintek.go.id/ (+ official "Buku Panduan Pendaftaran Beasiswa Garuda 2027" PDF)
 *   Djarum     https://djarumbeasiswaplus.org/about-us (the site blocks automated access; the owner supplied a screenshot of the page)
 *   TELADAN    https://www.tanotofoundation.org/initiative/teladan/
 *   BCA PPBP/PPTI + Bakti BCA: official BCA press releases on bca.co.id (karir.bca.co.id/beasiswa-bca is the registration page)
 * Not included: Beasiswa Bank Indonesia and SatuBeasiswa (sites block automated access); do not bypass blocks.
 * Rules: official source only, no figure that is not on the official page, summary <=150 chars, status <=80 chars,
 * texts first drafted by Haiku and verified against the page. Update BEASISWA_CHECKED when pages are re-read.
 * `state` = registration situation on BEASISWA_CHECKED: open | unknown (no schedule on page) | closed.
 */
import type { Lang } from './i18n';
type T = Record<Lang, string>;

export const BEASISWA_CHECKED = '2026-11-26';

export type Scholarship = {
  name: string; url: string; group: 'siswa' | 'mahasiswa'; state: 'open' | 'unknown' | 'closed';
  level: T; summary: T; status: T;
};

/** Order = display order (open first, then unknown, then closed). */
export const BEASISWA: Scholarship[] = [
  {
    name: 'Beasiswa Garuda 2027 (Kemdiktisaintek, didanai LPDP)', url: 'https://beasiswagaruda.kemdiktisaintek.go.id/', group: 'siswa', state: 'open',
    level: { id: 'Siswa kelas 12 SMA/SMK/MA atau sederajat', en: 'Grade 12 SMA/SMK/MA students or equivalent' },
    summary: { id: 'Beasiswa S1 di perguruan tinggi terbaik dunia (didanai LPDP): SPP, biaya pendaftaran, tunjangan buku, dan dana pendukung termasuk biaya hidup.', en: 'Bachelor’s scholarship at top universities worldwide (LPDP-funded): tuition, registration, book allowance, and support funds incl. living costs.' },
    status: { id: 'Pendaftaran dibuka 12 November 2026 - 4 Januari 2027', en: 'Applications open 12 November 2026 - 4 January 2027' },
  },
  {
    name: 'PIP (Kemendikdasmen)', url: 'https://pip.kemendikdasmen.go.id/', group: 'siswa', state: 'unknown',
    level: { id: 'SMA/SMK (juga SD dan SMP)', en: 'SMA/SMK (also SD and SMP)' },
    summary: { id: 'Bantuan uang tunai dari pemerintah bagi peserta didik dari keluarga miskin atau rentan miskin untuk membiayai pendidikan.', en: 'Cash aid from the government for students from poor or near-poor families, to help pay for their education.' },
    status: { id: 'Nominal dan jadwal pendaftaran tidak tertulis di halaman utama.', en: 'Amounts and registration dates are not stated on the home page.' },
  },
  {
    name: 'KIP Kuliah (Kemdiktisaintek)', url: 'https://kip-kuliah.kemdiktisaintek.go.id/', group: 'siswa', state: 'unknown',
    level: { id: 'Calon mahasiswa (lulusan SMA/SMK)', en: 'Prospective university students (SMA/SMK leavers)' },
    summary: { id: 'Memberi akses ke pendidikan tinggi bagi siswa di seluruh Indonesia melalui jalur SNBP, UTBK-SNBT, dan seleksi mandiri PTN/PTS.', en: 'Gives students across Indonesia access to higher education through SNBP, UTBK-SNBT, and independent PTN and PTS selection.' },
    status: { id: 'Halaman utama memuat jadwal 2026; jadwal 2027 belum tertulis.', en: 'The home page lists 2026 dates; 2027 dates are not stated.' },
  },
  {
    name: 'Djarum Beasiswa Plus (Djarum Foundation)', url: 'https://djarumbeasiswaplus.org/', group: 'mahasiswa', state: 'unknown',
    level: { id: 'Beasiswa prestasi untuk mahasiswa', en: 'Merit scholarship for university students' },
    summary: { id: 'Beasiswa prestasi sejak 1984 untuk mahasiswa berpotensi tinggi, disertai dana pendidikan, pelatihan soft skills, dan jejaring.', en: 'Merit scholarship since 1984 for high-potential university students, with education funding, soft skills training, and networking.' },
    status: { id: 'Jadwal pendaftaran tidak tertulis di halaman ini; cek situs resmi.', en: 'Registration schedule is not stated on this page; check the official website.' },
  },
  {
    name: 'TELADAN (Tanoto Foundation)', url: 'https://www.tanotofoundation.org/initiative/teladan/', group: 'mahasiswa', state: 'closed',
    level: { id: 'Perguruan tinggi (S1)', en: 'University (S1)' },
    summary: { id: 'Program kepemimpinan untuk mahasiswa S1 (usia 18-22 tahun) di universitas mitra, dengan bantuan biaya kuliah penuh dan uang saku.', en: 'Leadership program for S1 students aged 18-22 at partner universities, covering full tuition and a living allowance.' },
    status: { id: 'Pendaftaran 2027 berakhir 7 September 2026; jadwal berikutnya belum tertulis.', en: '2027 registration ended September 7, 2026; next schedule not stated.' },
  },
  {
    name: 'Beasiswa PPBP dan PPTI BCA 2027 (BCA)', url: 'https://karir.bca.co.id/beasiswa-bca', group: 'siswa', state: 'closed',
    level: { id: 'Siswa kelas 11 dan 12 SMA/SMK, serta lulusan SMA/SMK yang berencana kuliah pada 2027', en: 'Grade 11 and 12 SMA/SMK students, and SMA/SMK graduates planning to start university in 2027' },
    summary: { id: 'Pendidikan 2,5 tahun di BCA Learning Institute, Sentul, Bogor, tanpa biaya kuliah. Dapat uang saku, asrama, dan peluang ditawari kerja di BCA.', en: '2.5-year study at BCA Learning Institute, Sentul, Bogor, with no tuition fees. Includes allowance, dormitory and a possible job offer at BCA.' },
    status: { id: 'Pendaftaran 13 April - 20 Oktober 2026 (sudah berakhir)', en: 'Applications 13 April - 20 October 2026 (closed)' },
  },
  {
    name: 'Beasiswa Bakti BCA 2027 (BCA)', url: 'https://www.bca.co.id/en/tentang-bca/media-riset/pressroom/siaran-pers/2026/08/10/04/11/beasiswa-bakti-bca-2027-resmi-dibuka-komitmen-cetak-talenta-muda', group: 'mahasiswa', state: 'closed',
    level: { id: 'Mahasiswa S1 semester 3 di PTN Indonesia', en: 'Semester 3 undergraduate students at state universities in Indonesia' },
    summary: { id: 'Dana pendidikan berupa uang saku dan bantuan biaya kuliah, program orientasi, dan jaringan alumni. Ada tiga kategori seleksi.', en: 'Education funds (living allowance and tuition aid), orientation program and alumni network. Three categories: financial, academic, non-academic.' },
    status: { id: 'Pendaftaran 3 Agustus - 30 September 2026 (sudah berakhir)', en: 'Applications 3 August - 30 September 2026 (closed)' },
  },
];

export const BEASISWA_UI = {
  heading: { id: 'Info Beasiswa', en: 'Scholarship info' } as T,
  official: { id: 'Situs resmi →', en: 'Official site →' } as T,
  seeAll: { id: 'Lihat semua beasiswa →', en: 'See all scholarships →' } as T,
  open: { id: 'Dibuka', en: 'Open' } as T,
  closed: { id: 'Ditutup', en: 'Closed' } as T,
  note: { id: 'Dirangkum dari situs resmi penyedia, diperiksa 26 November 2026. Syarat dan jadwal dapat berubah; selalu cek situs resminya.', en: 'Summarised from each provider’s official site, checked 26 November 2026. Terms and dates may change; always check the official site.' } as T,
  pageTitle: { id: 'Info Beasiswa SMA dan Kuliah: Ringkasan dari Situs Resmi', en: 'Scholarships for SMA and University: Summaries from Official Sites' } as T,
  pageDesc: { id: 'Ringkasan beasiswa untuk siswa SMA/SMK dan mahasiswa (PIP, KIP Kuliah, Garuda, Djarum, TELADAN, BCA), dengan tautan ke situs resmi penyedia dan status pendaftaran.', en: 'Scholarship summaries for SMA/SMK students and university students (PIP, KIP Kuliah, Garuda, Djarum, TELADAN, BCA), with links to each provider’s official site and registration status.' } as T,
  groupSiswa: { id: 'Untuk siswa SMA/SMK dan calon mahasiswa', en: 'For SMA/SMK students and prospective university students' } as T,
  groupMahasiswa: { id: 'Untuk mahasiswa', en: 'For university students' } as T,
  intro: { id: 'Setiap ringkasan ditulis dari halaman resmi penyedia beasiswa. Kami tidak menyalin angka dari media atau agregator; jika nominal atau jadwal tidak tertulis di halaman resmi, kami menyatakannya demikian.', en: 'Each summary is written from the scholarship provider’s own page. We do not copy figures from media or aggregators; if an amount or date is not on the official page, we say so.' } as T,
  home: { id: 'Beranda', en: 'Home' } as T,
};
