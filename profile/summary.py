# Callgrind ciktilarindan ozet tablo: f, hucre sayisi, hucre basina komut
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from cells import cells

runs = [("L=100 (500 cift)", "profile/cg_L100.txt", "data/pairs_L100.tsv"),
        ("L=150 (500 cift)", "profile/cg_L150.txt", "data/pairs_L150.tsv"),
        ("L=250 (500 cift)", "profile/cg_L250.txt", "data/pairs_L250.tsv"),
        ("L=150 (1000 cift)", "profile/callgrind_1k.txt", "data/pairs_1k.tsv")]
num = lambda s: int(s.replace(",", ""))
print(f"{'Calisma':20} {'Toplam Ir':>14} {'sw_gotoh Ir':>14} {'f (%)':>7} {'Hucre':>12} {'Komut/hucre':>12}")
for name, cg, tsv in runs:
    tot = fn = None
    for line in open(cg):
        m = re.match(r"\s*([\d,]+) \(100\.0%\)\s+PROGRAM TOTALS", line)
        if m: tot = num(m.group(1))
        m = re.match(r"\s*([\d,]+) \([\d.]+%\)\s+ref/sw_gotoh\.c:sw_gotoh \[", line)
        if m and fn is None: fn = num(m.group(1))
    c = cells(tsv)
    print(f"{name:20} {tot:>14,} {fn:>14,} {100*fn/tot:>7.2f} {c:>12,} {fn/c:>12.2f}")
