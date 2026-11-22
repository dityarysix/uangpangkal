import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

/** Rupiah amount, stored as a plain integer (e.g. 47500000). */
const rupiah = z.number().int().nonnegative();

const bilingual = z.object({ id: z.string(), en: z.string() });

const source = z.object({
  title: z.string(),
  url: z.string().url(),
  /** Publish date of the source, if known (YYYY-MM-DD). */
  published: z.string().optional(),
});

const feeEntry = z.object({
  level: z.enum(['KB', 'TK', 'SD', 'SMP', 'SMA', 'SMK']),
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
    area: z.enum(['jabodetabek', 'bandung', 'semarang', 'surabaya', 'yogyakarta']),
    /** City / kota / kabupaten, e.g. "Jakarta Selatan", "Tangerang Selatan". */
    city: z.string(),
    district: z.string().optional(),
    address: z.string().optional(),
    npsn: z.string().optional(),
    levels: z.array(z.enum(['KB', 'TK', 'SD', 'SMP', 'SMA', 'SMK'])).min(1),
    curriculum: z.array(z.string()).default([]),
    religion: z.enum(['Umum', 'Islam', 'Kristen', 'Katolik', 'Buddha', 'Hindu']).optional(),
    website: z.string().url().optional(),
    phone: z.string().optional(),
    fees: z.array(feeEntry).default([]),
    admission: z
      .object({
        academicYear: z.string().optional(),
        period: bilingual.optional(),
        steps: z.array(bilingual).default([]),
        documents: z.array(bilingual).default([]),
        test: bilingual.optional(),
        source: source.optional(),
      })
      .optional(),
  }),
});

export const collections = { schools };
