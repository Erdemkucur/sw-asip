# RISC-V assembly ic dongu komut karisimi (statik sayim)
# Kullanim: python3 profile/mix.py dosya.s BASLANGIC_ETIKETI
# Dongu = etiket satirindan, o etikete geri atlayan ilk komuta kadar.
import re, sys
from collections import Counter

path, label = sys.argv[1], sys.argv[2]
lines = [l.split("#")[0].strip() for l in open(path)]
lines = [l for l in lines if l and not l.startswith(".cfi") and not l.startswith(".size")]

start = next(i for i, l in enumerate(lines) if l == label + ":")
body = []
for l in lines[start + 1:]:
    if l.endswith(":"):                 # ara etiketler govdede kalir
        continue
    body.append(l)
    parts = l.split(None, 1)
    if len(parts) == 2 and parts[1].split(",")[-1].strip() == label:   # geri dal
        break
else:
    sys.exit("Geri dal bulunamadi: etiketi kontrol et")

cat = {"lbu":"bellek yukleme","lw":"bellek yukleme","sw":"bellek yazma",
       "max":"max","add":"toplama/cikarma","addi":"toplama/cikarma","sub":"toplama/cikarma",
       "snez":"mantik/kaydirma","neg":"mantik/kaydirma","andi":"mantik/kaydirma",
       "and":"mantik/kaydirma","not":"mantik/kaydirma","srai":"mantik/kaydirma",
       "mv":"mv (yazmac tasima)","beq":"dal/atlama","bne":"dal/atlama","bge":"dal/atlama",
       "blt":"dal/atlama","bgt":"dal/atlama","ble":"dal/atlama","j":"dal/atlama"}
mn = Counter(l.split()[0] for l in body)
ct = Counter(cat.get(m, "DIGER:" + m) for m in mn.elements())
n = sum(mn.values())
print(f"Dosya: {path}   Dongu: {label} ...geri dal   Toplam statik komut: {n}")
print("\nKomut bazinda:", dict(sorted(mn.items(), key=lambda x: -x[1])))
print(f"\n{'Kategori':22}{'Adet':>6}{'Pay %':>8}")
for k, v in sorted(ct.items(), key=lambda x: -x[1]):
    print(f"{k:22}{v:>6}{100*v/n:>8.1f}")
