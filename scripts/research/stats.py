"""Site statistics: schools per area, fee entries per academic year, and (with --stale N) the N schools
whose newest fee data is oldest. Run from the repo root: python3 scripts/research/stats.py [--stale 60]"""
import json, glob, re, sys
from collections import Counter
areas = open('src/lib/areas.ts').read()
city_area = {}
for slug, cities in re.findall(r"slug: '([^']+)'.*?cities: \[([^\]]*)\]", areas, re.S):
    for c in re.findall(r"'([^']+)'", cities):
        city_area[c] = slug
docs = {f.split('/')[-1][:-5]: json.load(open(f)) for f in glob.glob('src/content/schools/*.json')}
print('schools:', len(docs))
print('per area:', sorted(Counter(city_area[d['city']] for d in docs.values()).items(), key=lambda x: x[1]))
print('fee entries per year:', sorted(Counter(e['academicYear'] for d in docs.values() for e in d.get('fees', [])).items()))
if '--stale' in sys.argv:
    n = int(sys.argv[sys.argv.index('--stale') + 1])
    def newest(d):
        ys = [e['academicYear'] for e in d.get('fees', [])]
        return max(ys) if ys else '0000/0000'
    rows = sorted(docs.items(), key=lambda kv: (newest(kv[1]), max([e['checked'] for e in kv[1].get('fees', [])] or [''])))
    for slug, d in rows[:n]:
        srcs = sorted({e['source']['url'] for e in d.get('fees', [])})
        print(f"{newest(d)}  {slug}  | {d['name']} | {d['city']} | {d.get('website','')} | {srcs[:2]}")
