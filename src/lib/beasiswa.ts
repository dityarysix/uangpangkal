/**
 * Scholarship panel on the home page (SMA and university).
 * Summaries were written from the providers' OWN pages, read on 2026-11-26:
 *   KIP Kuliah  https://kip-kuliah.kemdiktisaintek.go.id/
 *   PIP         https://pip.kemendikdasmen.go.id/
 *   TELADAN     https://www.tanotofoundation.org/initiative/teladan/
 * Not included (no readable official source): Djarum Beasiswa Plus (site returned 403 to automated access),
 * Beasiswa Bank Indonesia (site blocks automated access). Do not bypass; add only from official pages.
 * Update `BEASISWA_CHECKED` whenever the pages are re-read.
 */
import type { Lang } from './i18n';
type T = Record<Lang, string>;

export const BEASISWA_CHECKED = '2026-11-26';

export const BEASISWA: { name: string; url: string; level: T; summary: T; status: T }[] = [
  {
    name: 'PIP (Kemendikdasmen)',
    url: 'https://pip.kemendikdasmen.go.id/',
    level: { id: 'SMA/SMK (juga SD dan SMP)', en: 'SMA/SMK (also SD and SMP)' },
    summary: { id: 'Bantuan uang tunai dari pemerintah bagi peserta didik dari keluarga miskin atau rentan miskin untuk membiayai pendidikan.', en: 'Cash aid from the government for students from poor or near-poor families, to help pay for their education.' },
    status: { id: 'Nominal dan jadwal pendaftaran tidak tertulis di halaman utama.', en: 'Amounts and registration dates are not stated on the home page.' },
  },
  {
    name: 'KIP Kuliah (Kemdiktisaintek)',
    url: 'https://kip-kuliah.kemdiktisaintek.go.id/',
    level: { id: 'Perguruan tinggi', en: 'University' },
    summary: { id: 'Memberi akses ke pendidikan tinggi bagi siswa di seluruh Indonesia melalui jalur SNBP, UTBK-SNBT, dan seleksi mandiri PTN/PTS.', en: 'Gives students across Indonesia access to higher education through SNBP, UTBK-SNBT, and independent PTN and PTS selection.' },
    status: { id: 'Halaman utama memuat jadwal 2026; jadwal 2027 belum tertulis.', en: 'The home page lists 2026 dates; 2027 dates are not stated.' },
  },
  {
    name: 'TELADAN (Tanoto Foundation)',
    url: 'https://www.tanotofoundation.org/initiative/teladan/',
    level: { id: 'Perguruan tinggi (S1)', en: 'University (S1)' },
    summary: { id: 'Program kepemimpinan untuk mahasiswa S1 (usia 18-22 tahun) di universitas mitra, dengan bantuan biaya kuliah penuh dan uang saku.', en: 'Leadership program for S1 students aged 18-22 at partner universities, covering full tuition and a living allowance.' },
    status: { id: 'Pendaftaran 2027 berakhir 7 September 2026; jadwal berikutnya belum tertulis.', en: '2027 registration ended September 7, 2026; next schedule not stated.' },
  },
];

export const BEASISWA_UI = {
  heading: { id: 'Info Beasiswa', en: 'Scholarship info' } as T,
  official: { id: 'Situs resmi →', en: 'Official site →' } as T,
  note: { id: 'Dirangkum dari situs resmi penyedia, diperiksa 26 November 2026. Syarat dan jadwal dapat berubah; selalu cek situs resminya.', en: 'Summarised from each provider’s official site, checked 26 November 2026. Terms and dates may change; always check the official site.' } as T,
};
