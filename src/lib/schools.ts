import { getCollection, type CollectionEntry } from 'astro:content';

export type School = CollectionEntry<'schools'>;

export async function allSchools() {
  const list = await getCollection('schools');
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
