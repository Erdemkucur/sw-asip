# Amdahl senaryolari. f, Callgrind olcumunden okunur (profile/callgrind_1k.txt).
# k = hucre basina komut (kernel). Baz cizgi: RV32IM+Zbb = 26 komut/hucre (profile/mix.py ile olculdu).
# UYARI: senaryolar (B, C, D) olculmus degil, mix.py kategorilerinden turetilmis IDEAL komut sayisi varsayimlaridir.
import re
num = lambda s: int(s.replace(",", ""))
tot = fn = None
for line in open("profile/callgrind_1k.txt"):
    m = re.match(r"\s*([\d,]+) \(100\.0%\)\s+PROGRAM TOTALS", line)
    if m: tot = num(m.group(1))
    m = re.match(r"\s*([\d,]+) \([\d.]+%\)\s+ref/sw_gotoh\.c:sw_gotoh \[", line)
    if m and fn is None: fn = num(m.group(1))
f = fn / tot
print(f"Olculen f = {fn:,} / {tot:,} = {f:.6f}")
print(f"Amdahl tavani 1/(1-f) = {1/(1-f):.1f}x\n")

BASE = 26
scen = [
 ("A  RV32IM+Zbb (baz cizgi)",                          26),
 ("B  A + skor secimi tek komut (5 -> 1)",              26 - 4),
 ("C  B + isaretci/dongu yonetimi donanima (4 -> 0)",   26 - 4 - 4),
 ("D  C + 2x16 bit paketli (hucre basina komut /2)",    (26 - 4 - 4) / 2),
]
print(f"{'Senaryo':52}{'k':>6}{'s=26/k':>9}{'S_toplam':>10}")
for name, k in scen:
    s = BASE / k
    S = 1 / ((1 - f) + f / s)
    print(f"{name:52}{k:>6.1f}{s:>9.2f}{S:>10.2f}")

print("\nZbb'nin temel RV32IM'e gore kazanci (statik komut sayisi):")
for k in (29, 34):
    print(f"  {k} -> 26 : {k/26:.2f}x  ({100*(1-26/k):.1f}% daha kisa)")
