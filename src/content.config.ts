import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { CITIES } from './lib/areas';

/** Rupiah amount, stored as a plain integer (e.g. 47500000). */
const rupiah = z.number().int().nonnegative();

const bilingual = z.object({ id: z.string(), en: z.string() });

const source = z.object({
  title: z.string(),
  url: z.string().url(),
  /** Publish date of the source, if known (YYYY-MM-DD). */
  published: z.string().optional(),
});

const levelEnum = z.enum(['KB', 'TK', 'SD', 'SMP', 'SMA', 'SMK']);

const feeEntry = z.object({
  level: levelEnum,
  /** Academic year the fees apply to, e.g. "2026/2027". */
  academicYear: z.string().regex(/^\d{4}\/\d{4}$/),
  /** True when the source does not state the academic year and we inferred it from the publish date. */
  yearAssumed: z.boolean().optional(),
  registrationFee: rupiah.optional(),
  /** Uang pangkal (one-off entry / development fee). */
  entryFee: z.object({ min: rupiah, max: rupiah.optional() }).optional(),
  /** SPP / tuition. */
  tuition: z
    .object({ amount: rupiah, period: z.enum(['month', 'quarter', 'semester', 'year']) })
    .optional(),
  otherFees: z.array(z.object({ label: bilingual, amount: rupiah })).default([]),
  notes: bilingual.optional(),
  source,
  /** Date we last checked this figure against its source (YYYY-MM-DD). */
  checked: z.string(),
});

const schools = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/schools' }),
  schema: z.object({
    name: z.string(),
    /** City / kota / kabupaten exactly as listed in src/lib/areas.ts; the area is derived from it. */
    city: z.enum(CITIES),
    district: z.string().optional(),
    address: z.string().optional(),
    npsn: z.string().optional(),
    levels: z.array(levelEnum).min(1),
    curriculum: z.array(z.string()).default([]),
    religion: z.enum(['Umum', 'Islam', 'Kristen', 'Katolik', 'Buddha', 'Hindu']).optional(),
    website: z.string().url().optional(),
    phone: z.string().optional(),
    fees: z.array(feeEntry).default([]),
    /** Admission procedure, one entry per level (or one without level if it applies to all). */
    admission: z
      .array(
        z.object({
          level: levelEnum.optional(),
          academicYear: z.string().regex(/^\d{4}\/\d{4}$/),
          period: bilingual.optional(),
          steps: z.array(bilingual).default([]),
          documents: z.array(bilingual).default([]),
          test: bilingual.optional(),
          notes: bilingual.optional(),
          source,
          checked: z.string(),
        }),
      )
      .default([]),
  }),
});

export const collections = { schools };
