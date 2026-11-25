/**
 * Facts for the "Sekolah Swasta Gratis 2027" guide and the home-page side panels.
 * Every statement below comes from the dated source listed in SOURCES (checked 2026-11-25).
 * Update this file (and GUIDE_UPDATED) when new official information is published.
 */
import type { Lang } from './i18n';

export const GUIDE_UPDATED = '2026-11-25';

type T = Record<Lang, string>;

export const SOURCES: { id: string; title: string; org: string; date: string; url: string }[] = [
  { id: 'pojok', title: 'Rp5 Triliun Disiapkan untuk Sekolah Swasta Gratis 2027, Ini Kriterianya', org: 'PojokSatu.id', date: '2026-11-17', url: 'https://pojoksatu.id/edugov/rp5-triliun-disiapkan-untuk-sekolah-swasta-gratis-2027-ini-kriterianya' },
  { id: 'katadata', title: 'Pemerintah Siapkan Rp 5 T untuk Uji Coba Sekolah Gratis Tahun Depan', org: 'Katadata', date: '2026-09-29', url: 'https://katadata.co.id/finansial/makro/6abb6c30d6f6f/pemerintah-siapkan-rp-5-t-untuk-uji-coba-sekolah-gratis-tahun-depan' },
  { id: 'detik-bertahap', title: 'Skenario Bertahap SD-SMP Swasta Gratis, Kemendikdasmen: Anak Putus Sekolah Prioritas', org: 'detikEdu', date: '2025-07-10', url: 'https://www.detik.com/edu/sekolah/d-8004896/skenario-bertahap-sd-smp-swasta-gratis-kemendikdasmen-anak-putus-sekolah-prioritas' },
  { id: 'detik-mk', title: 'MK Putuskan SD-SMP Swasta Gratis', org: 'detikEdu', date: '2025-05-27', url: 'https://www.detik.com/edu/sekolah/d-7936136/mk-putuskan-sd-smp-swasta-gratis' },
  { id: 'banten', title: 'Program Sekolah Gratis Banten menjangkau puluhan ribu siswa', org: 'Journal Arta', date: '2026-11-14', url: 'https://journalarta.com/news/2026/11/14/program-sekolah-gratis-banten-minat-swasta/?all=1' },
  { id: 'dki', title: 'Pemprov DKI Siapkan Rp200 M Lebih untuk Sekolah Swasta Gratis', org: 'Metro TV', date: '2026-04-18', url: 'https://www.metrotvnews.com/read/NQAC0Q8B-pemprov-dki-siapkan-rp200-m-lebih-untuk-sekolah-swasta-gratis' },
];

/** Short facts shown in the home side panels and the guide summary. */
export const QUICK: { text: T; src: string }[] = [
  { text: { id: 'Pemerintah dan DPR menyatakan menganggarkan sekitar Rp5 triliun pada 2027 untuk sekolah swasta gratis; cakupan belum final.', en: 'Government and parliament say they budgeted about Rp5 trillion for free private schools in 2027; scope is not final.' }, src: 'pojok' },
  { text: { id: 'Tidak semua sekolah swasta otomatis gratis. Kemendikdasmen menyusun daftar sasaran; sekolah dengan kurikulum tambahan IB/Cambridge berpotensi tidak masuk.', en: 'Not every private school is automatically free. The ministry is compiling a target list; schools with extra IB/Cambridge curricula may be left out.' }, src: 'pojok' },
  { text: { id: 'Banten 2026/2027: program gratis mencakup 782 SMA, SMK, dan SKh swasta dengan 59.697 siswa.', en: 'Banten 2026/2027: the free program covers 782 private SMA, SMK, and SKh schools with 59,697 students.' }, src: 'banten' },
  { text: { id: 'DKI Jakarta 2026/2027: 103 sekolah swasta digratiskan, anggaran Rp253,6 miliar.', en: 'DKI Jakarta 2026/2027: 103 private schools made free, with a Rp253.6 billion budget.' }, src: 'dki' },
];

/** Home-page side panels (text reviewed before use). */
export const PANEL = {
  title: { id: 'Rencana Sekolah Swasta Gratis 2027', en: 'Free Private Schools Plan, 2027' } as T,
  lead: { id: 'Apa yang berubah, sekolah mana yang berhak, dan program yang sudah berjalan di Banten dan Jakarta.', en: 'What is changing, which schools qualify, and programmes already running in Banten and Jakarta.' } as T,
  heading: { id: 'Fakta cepat', en: 'Quick facts' } as T,
  more: { id: 'Baca panduan lengkap →', en: 'Read the full guide →' } as T,
};
