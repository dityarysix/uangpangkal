"""Dump every HTML <table> in a saved page as pipe-separated rows (fee tables on school sites).
Usage: python3 -I scripts/research/tables.py page.html"""
import re, html, sys
s = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
for t in re.findall(r'<table.*?</table>', s, re.S):
    for r in re.findall(r'<tr.*?</tr>', t, re.S):
        cells = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', c))).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
        print(' | '.join(cells))
    print('---')
