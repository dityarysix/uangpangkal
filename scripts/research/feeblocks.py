"""Print numbered list items (e.g. "3. SD Islam X") from a text file made by html2text.py,
keeping only blocks that contain a Rupiah figure, with their address/fee lines.
Usage: python3 -I scripts/research/feeblocks.py page.txt"""
import re, sys
lines = [l.strip() for l in open(sys.argv[1], encoding='utf-8', errors='ignore') if l.strip()]
starts = [i for i, l in enumerate(lines) if re.match(r'^\d{1,2}\.\s+\S', l) and len(l) < 90]
seen = set()
for n, i in enumerate(starts):
    end = starts[n + 1] if n + 1 < len(starts) else min(i + 20, len(lines))
    blk = lines[i:end]
    if not any(re.search(r'Rp ?\d', l) for l in blk[1:]) or blk[0] in seen:
        continue
    seen.add(blk[0])
    print(blk[0])
    for l in blk[1:]:
        if re.search(r'(?i)alamat|lokasi|rp ?\d|jl\.|jalan ', l) and not re.search(r'(?i)baca juga', l):
            print('   ', l[:220])
