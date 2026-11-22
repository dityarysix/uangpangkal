"""Helpers for hand-transcribed seed scripts.

Each seed script copies figures from ONE source, verbatim. upsert() merges a
school's fee entry into src/content/schools/<slug>.json, so one school can hold
several levels and sources. Re-running a seed script is safe: an entry with the
same level + academic year + source URL is replaced, not duplicated.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "src/content/schools"
LEVEL_ORDER = ["KB", "TK", "SD", "SMP", "SMA", "SMK"]


def L(i, e):
    return {"id": i, "en": e}


def fee(label_id, label_en, amount):
    return {"label": L(label_id, label_en), "amount": amount}


UNIFORM = ("Seragam", "Uniforms")
BOOKS = ("Buku", "Books")
ACTIVITY = ("Uang kegiatan", "Activity fee")


def upsert(slug, *, name, area, city, level, source, checked, year,
           district=None, address=None, website=None, phone=None, religion=None,
           curriculum=None, **fee_fields):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{slug}.json"
    doc = json.loads(path.read_text()) if path.exists() else {}
    doc["name"] = name
    doc["area"] = area
    doc["city"] = city
    for k, v in (("district", district), ("address", address), ("website", website),
                 ("phone", phone), ("religion", religion)):
        if v is not None:
            doc[k] = v
    if curriculum:
        doc["curriculum"] = sorted(set(doc.get("curriculum", [])) | set(curriculum))
    levels = set(doc.get("levels", [])) | {level}
    doc["levels"] = [l for l in LEVEL_ORDER if l in levels]
    entry = {"level": level, "academicYear": year, **fee_fields, "source": source, "checked": checked}
    fees = [f for f in doc.get("fees", [])
            if not (f["level"] == level and f["academicYear"] == year and f["source"]["url"] == source["url"])]
    fees.append(entry)
    fees.sort(key=lambda f: (LEVEL_ORDER.index(f["level"]), f["academicYear"]))
    doc["fees"] = fees
    order = ["name", "area", "city", "district", "address", "npsn", "levels", "curriculum", "religion",
             "website", "phone", "fees", "admission"]
    doc = {k: doc[k] for k in order if k in doc}
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n")
    return path
