/**
 * Areas shown on the site. A school's area is derived from its `city`, so every
 * city used in the data must be listed here (the content schema enforces it).
 */
export const AREAS = [
  {
    slug: 'jakarta',
    name: { id: 'Jakarta', en: 'Jakarta' },
    cities: ['Jakarta Selatan', 'Jakarta Timur', 'Jakarta Barat', 'Jakarta Utara', 'Jakarta Pusat'],
  },
  {
    slug: 'tangerang-raya',
    name: { id: 'Tangerang Raya', en: 'Greater Tangerang' },
    cities: ['Tangerang Selatan', 'Kota Tangerang', 'Kabupaten Tangerang'],
  },
  {
    slug: 'depok-bogor-raya',
    name: { id: 'Depok/Bogor Raya', en: 'Depok & Bogor' },
    cities: ['Depok', 'Kota Bogor', 'Kabupaten Bogor'],
  },
  {
    slug: 'bekasi-raya',
    name: { id: 'Bekasi Raya', en: 'Greater Bekasi' },
    cities: ['Kota Bekasi', 'Kabupaten Bekasi'],
  },
  {
    slug: 'serang-raya',
    name: { id: 'Serang Raya', en: 'Greater Serang' },
    cities: ['Kota Serang', 'Kabupaten Serang', 'Cilegon', 'Pandeglang'],
  },
  {
    slug: 'bandung-raya',
    name: { id: 'Bandung Raya', en: 'Greater Bandung' },
    cities: ['Kota Bandung', 'Kabupaten Bandung', 'Kabupaten Bandung Barat', 'Cimahi', 'Kabupaten Sumedang'],
  },
  {
    slug: 'tasikmalaya-raya',
    name: { id: 'Tasikmalaya Raya', en: 'Greater Tasikmalaya' },
    cities: ['Kota Tasikmalaya', 'Kabupaten Tasikmalaya', 'Ciamis', 'Kota Banjar', 'Garut'],
  },
  {
    slug: 'semarang-raya',
    name: { id: 'Semarang Raya', en: 'Greater Semarang' },
    cities: ['Kota Semarang', 'Kabupaten Semarang', 'Salatiga', 'Kabupaten Kendal', 'Kabupaten Demak', 'Kabupaten Kudus'],
  },
  {
    slug: 'surabaya-raya',
    name: { id: 'Surabaya Raya', en: 'Greater Surabaya' },
    cities: ['Surabaya', 'Sidoarjo', 'Gresik', 'Kota Mojokerto', 'Kabupaten Mojokerto', 'Jombang'],
  },
  {
    slug: 'malang-raya',
    name: { id: 'Malang Raya', en: 'Greater Malang' },
    cities: ['Kota Malang', 'Kabupaten Malang', 'Kota Batu', 'Kota Blitar', 'Kabupaten Blitar', 'Kota Pasuruan', 'Kabupaten Pasuruan', 'Tulungagung'],
  },
  {
    slug: 'yogyakarta-raya',
    name: { id: 'Yogyakarta Raya', en: 'Greater Yogyakarta' },
    cities: ['Kota Yogyakarta', 'Sleman', 'Bantul', 'Kulon Progo', 'Gunungkidul'],
  },
  {
    slug: 'solo-raya',
    name: { id: 'Solo Raya', en: 'Greater Solo' },
    cities: ['Surakarta (Solo)', 'Sukoharjo', 'Karanganyar', 'Boyolali', 'Klaten', 'Sragen', 'Wonogiri'],
  },
  {
    slug: 'medan-raya',
    name: { id: 'Medan Raya', en: 'Greater Medan' },
    cities: ['Kota Medan', 'Deli Serdang', 'Binjai', 'Karo'],
  },
  {
    slug: 'pekanbaru-raya',
    name: { id: 'Pekanbaru Raya', en: 'Greater Pekanbaru' },
    cities: ['Kota Pekanbaru', 'Kampar', 'Siak', 'Pelalawan'],
  },
  {
    slug: 'padang-raya',
    name: { id: 'Padang Raya', en: 'Greater Padang' },
    cities: ['Kota Padang', 'Padang Pariaman', 'Kota Pariaman', 'Bukittinggi'],
  },
  {
    slug: 'batam-raya',
    name: { id: 'Batam Raya', en: 'Greater Batam' },
    cities: ['Kota Batam', 'Tanjungpinang', 'Bintan', 'Karimun'],
  },
  {
    slug: 'palembang-raya',
    name: { id: 'Palembang Raya', en: 'Greater Palembang' },
    cities: ['Kota Palembang', 'Banyuasin', 'Ogan Ilir'],
  },
  {
    slug: 'bali',
    name: { id: 'Bali', en: 'Bali' },
    cities: ['Kota Denpasar', 'Badung', 'Gianyar', 'Tabanan', 'Bangli', 'Klungkung', 'Karangasem', 'Buleleng', 'Jembrana'],
  },
  {
    slug: 'samarinda-raya',
    name: { id: 'Samarinda Raya', en: 'Greater Samarinda' },
    cities: ['Kota Samarinda', 'Kutai Kartanegara', 'Bontang', 'Balikpapan'],
  },
  {
    slug: 'makassar-raya',
    name: { id: 'Makassar Raya', en: 'Greater Makassar' },
    cities: ['Kota Makassar', 'Gowa', 'Maros', 'Takalar'],
  },
] as const;

export type Area = (typeof AREAS)[number];
export type AreaSlug = Area['slug'];
export const CITIES = AREAS.flatMap((a) => a.cities) as unknown as [string, ...string[]];

export const areaBySlug = (slug: string) => AREAS.find((a) => a.slug === slug);
export const areaOfCity = (city: string) => AREAS.find((a) => (a.cities as readonly string[]).includes(city))!;
