export type Area = 'jabodetabek' | 'bandung' | 'semarang' | 'surabaya' | 'yogyakarta';

export const AREAS: { slug: Area; name: { id: string; en: string }; cities: string[] }[] = [
  {
    slug: 'jabodetabek',
    name: { id: 'Jakarta Raya (Jabodetabek)', en: 'Greater Jakarta (Jabodetabek)' },
    cities: [
      'Jakarta Pusat', 'Jakarta Selatan', 'Jakarta Barat', 'Jakarta Timur', 'Jakarta Utara',
      'Kota Bogor', 'Kabupaten Bogor', 'Depok', 'Kota Tangerang', 'Kabupaten Tangerang', 'Tangerang Selatan',
      'Kota Bekasi', 'Kabupaten Bekasi',
    ],
  },
  { slug: 'bandung', name: { id: 'Bandung Raya', en: 'Greater Bandung' }, cities: ['Kota Bandung', 'Kabupaten Bandung', 'Cimahi', 'Bandung Barat'] },
  { slug: 'semarang', name: { id: 'Semarang', en: 'Semarang' }, cities: ['Kota Semarang', 'Kabupaten Semarang'] },
  { slug: 'surabaya', name: { id: 'Surabaya Raya', en: 'Greater Surabaya' }, cities: ['Surabaya', 'Sidoarjo', 'Gresik'] },
  { slug: 'yogyakarta', name: { id: 'Yogyakarta', en: 'Yogyakarta' }, cities: ['Kota Yogyakarta', 'Sleman', 'Bantul'] },
];

export const areaBySlug = (slug: string) => AREAS.find((a) => a.slug === slug);
