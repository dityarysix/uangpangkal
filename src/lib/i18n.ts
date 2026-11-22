export type Lang = 'id' | 'en';

const dict = {
  siteTagline: {
    id: 'Info biaya & pendaftaran sekolah swasta di Indonesia',
    en: 'Private school fees & admissions in Indonesia',
  },
  heroTitle: { id: 'Berapa biaya masuk sekolah swasta?', en: 'How much does a private school cost?' },
  heroLead: {
    id: 'Bandingkan uang pangkal, SPP, dan prosedur pendaftaran sekolah swasta di Jabodetabek, Bandung, Semarang, Surabaya, dan Yogyakarta.',
    en: 'Compare entry fees, tuition and admission procedures of private schools in Greater Jakarta, Bandung, Semarang, Surabaya and Yogyakarta.',
  },
  searchPlaceholder: { id: 'Cari nama sekolah…', en: 'Search school name…' },
  allAreas: { id: 'Semua wilayah', en: 'All areas' },
  allLevels: { id: 'Semua jenjang', en: 'All levels' },
  maxEntry: { id: 'Uang pangkal maks.', en: 'Max entry fee' },
  anyEntry: { id: 'Semua uang pangkal', en: 'Any entry fee' },
  any: { id: 'Berapa saja', en: 'Any' },
  areas: { id: 'Wilayah', en: 'Areas' },
  schools: { id: 'sekolah', en: 'schools' },
  noResults: { id: 'Tidak ada sekolah yang cocok.', en: 'No matching schools.' },
  entryFee: { id: 'Uang pangkal', en: 'Entry fee' },
  registrationFee: { id: 'Biaya pendaftaran', en: 'Registration fee' },
  tuition: { id: 'SPP', en: 'Tuition' },
  otherFees: { id: 'Biaya lain', en: 'Other fees' },
  level: { id: 'Jenjang', en: 'Level' },
  year: { id: 'Tahun ajaran', en: 'Academic year' },
  source: { id: 'Sumber', en: 'Source' },
  checked: { id: 'Dicek', en: 'Checked' },
  feesTitle: { id: 'Biaya sekolah', en: 'School fees' },
  noFees: {
    id: 'Sekolah ini belum mempublikasikan biaya. Hubungi sekolah langsung.',
    en: 'This school has not published its fees. Contact the school directly.',
  },
  admissionTitle: { id: 'Prosedur pendaftaran', en: 'Admission procedure' },
  documents: { id: 'Dokumen yang diperlukan', en: 'Required documents' },
  test: { id: 'Tes masuk', en: 'Entrance test' },
  period: { id: 'Periode pendaftaran', en: 'Registration period' },
  noAdmission: {
    id: 'Info pendaftaran belum tersedia.',
    en: 'Admission information not yet available.',
  },
  website: { id: 'Situs web', en: 'Website' },
  curriculum: { id: 'Kurikulum', en: 'Curriculum' },
  disclaimer: {
    id: 'Biaya dapat berubah setiap tahun ajaran. Selalu konfirmasi ke sekolah sebelum mendaftar.',
    en: 'Fees change every academic year. Always confirm with the school before applying.',
  },
  olderData: {
    id: 'Data dari tahun ajaran sebelumnya — biaya terbaru kemungkinan lebih tinggi.',
    en: 'Data from an earlier academic year — current fees are likely higher.',
  },
  about: { id: 'Tentang', en: 'About' },
  home: { id: 'Beranda', en: 'Home' },
  perPeriod_month: { id: '/bulan', en: '/month' },
  perPeriod_quarter: { id: '/3 bln', en: '/quarter' },
  perPeriod_semester: { id: '/semester', en: '/semester' },
  perPeriod_year: { id: '/tahun', en: '/year' },
  feeNotPublished: { id: 'Belum dipublikasikan', en: 'Not published' },
  yearAssumed: { id: 'diasumsikan; sumber tidak menyebut tahun ajaran', en: 'assumed; the source does not state the year' },
  free: { id: 'Gratis', en: 'Free' },
  latestFees: { id: 'Biaya terbaru', en: 'Latest fees' },
  reportCorrection: { id: 'Laporkan koreksi', en: 'Report a correction' },
} as const;

export type Key = keyof typeof dict;
export const t = (lang: Lang, key: Key) => dict[key][lang];

/** Latest academic year we currently target (admissions in progress). */
export const CURRENT_YEAR = '2027/2028';

export const paths = {
  home: (l: Lang) => (l === 'id' ? '/' : '/en/'),
  area: (l: Lang, slug: string) => (l === 'id' ? `/wilayah/${slug}/` : `/en/area/${slug}/`),
  school: (l: Lang, slug: string) => (l === 'id' ? `/sekolah/${slug}/` : `/en/school/${slug}/`),
  about: (l: Lang) => (l === 'id' ? '/tentang/' : '/en/about/'),
};

export function rupiah(n: number) {
  return 'Rp' + n.toLocaleString('id-ID');
}

/** Compact form for cards: Rp1,75 jt / Rp1.75 mn. Keeps up to 2 decimals so amounts are not rounded away. */
export function rupiahShort(n: number, lang: Lang) {
  const loc = lang === 'id' ? 'id-ID' : 'en-US';
  if (n >= 1_000_000) {
    const v = (n / 1_000_000).toLocaleString(loc, { maximumFractionDigits: 2 });
    return `Rp${v} ${lang === 'id' ? 'jt' : 'mn'}`;
  }
  if (n >= 1_000) return `Rp${(n / 1_000).toLocaleString(loc, { maximumFractionDigits: 1 })} ${lang === 'id' ? 'rb' : 'k'}`;
  return rupiah(n);
}
