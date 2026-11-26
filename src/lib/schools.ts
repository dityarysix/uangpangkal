import { getCollection, type CollectionEntry } from 'astro:content';
import { areaOfCity } from './areas';

export type School = CollectionEntry<'schools'>;

export async function allSchools() {
  const list = await getCollection('schools');
  // Schools sharing a name (chains, common names) must include their location, e.g. "SD Islam Al-Azhar Bekasi".
  const seen = new Map<string, string>();
  for (const s of list) {
    const key = s.data.name.toLowerCase();
    if (seen.has(key)) throw new Error(`Duplicate school name "${s.data.name}" in ${seen.get(key)} and ${s.id}: add the location to the name.`);
    seen.set(key, s.id);
  }
  return list.sort((a, b) => a.data.name.localeCompare(b.data.name, 'id'));
}

/** Most recent fee entry per level (newest academic year first). */
export function latestFees(s: School) {
  return [...s.data.fees].sort((a, b) => b.academicYear.localeCompare(a.academicYear));
}

/** Lowest entry fee across a school's fee entries, for sorting / filtering. */
export function minEntryFee(s: School): number | undefined {
  const vals = s.data.fees.map((f) => f.entryFee?.min).filter((v): v is number => v !== undefined);
  return vals.length ? Math.min(...vals) : undefined;
}

/** Lowest tuition as the school states it (amount + its own period), compared on a monthly basis. */
export function lowestTuition(s: School) {
  const per = { month: 1, quarter: 3, semester: 6, year: 12 } as const;
  const list = s.data.fees.map((f) => f.tuition).filter((t) => t !== undefined);
  if (!list.length) return undefined;
  return list.reduce((a, b) => (b.amount / per[b.period] < a.amount / per[a.period] ? b : a));
}

const PER = { month: 1, quarter: 3, semester: 6, year: 12 } as const;
type Fee = School['data']['fees'][number];

/** Newest fee entry for each level the school has data for. */
export function latestByLevel(s: School) {
  const m = new Map<string, Fee>();
  for (const f of latestFees(s)) if (!m.has(f.level)) m.set(f.level, f);
  return m;
}

export type Metric = { mine: number; year: string; n: number; min: number; max: number; rank: number };

const metricOf = (vals: number[], mine: number | undefined, year: string): Metric | undefined => {
  if (!mine || mine <= 0 || vals.length < 3) return undefined; // zero = free programme: not compared; need >= 3 schools
  return { mine, year, n: vals.length, min: Math.min(...vals), max: Math.max(...vals), rank: vals.filter((v) => v < mine).length + 1 };
};

/**
 * How a school's latest entry fee and monthly tuition for one level compare with the other schools of the same area
 * (each school's newest entry for that level; zero amounts excluded). Computed at build time from the data only.
 */
export function compareInArea(all: School[], school: School, level: string) {
  const area = areaOfCity(school.data.city).slug;
  const entry: number[] = [], tuition: number[] = [];
  for (const s of all) {
    if (areaOfCity(s.data.city).slug !== area) continue;
    const f = latestByLevel(s).get(level);
    if (!f) continue;
    if (f.entryFee && f.entryFee.min > 0) entry.push(f.entryFee.min);
    if (f.tuition && f.tuition.amount > 0) tuition.push(f.tuition.amount / PER[f.tuition.period]);
  }
  const mine = latestByLevel(school).get(level);
  if (!mine) return {};
  return {
    entry: metricOf(entry, mine.entryFee?.min, mine.academicYear),
    tuition: metricOf(tuition, mine.tuition ? Math.round(mine.tuition.amount / PER[mine.tuition.period]) : undefined, mine.academicYear),
  };
}

/** Other schools of the same area that share a level. Next `limit` schools in a name-ordered ring, so links spread evenly. */
export function relatedSchools(all: School[], school: School, limit = 6) {
  const area = areaOfCity(school.data.city).slug;
  const lv = new Set(school.data.levels);
  const cand = all.filter((s) => s.id !== school.id && areaOfCity(s.data.city).slug === area && s.data.levels.some((l) => lv.has(l)));
  if (!cand.length) return [];
  let start = cand.findIndex((s) => s.data.name.localeCompare(school.data.name, 'id') > 0);
  if (start < 0) start = 0;
  return Array.from({ length: Math.min(limit, cand.length) }, (_, i) => cand[(start + i) % cand.length]);
}
