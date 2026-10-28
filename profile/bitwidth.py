# H, E, F degerlerinin gozlenen min/max'i (i>=1, j>=1) ve gereken bit genisligi
# Kullanim: python3 profile/bitwidth.py data/pairs_L250.tsv [en_fazla_cift]
import sys
MATCH, MISMATCH, GAP_O, GAP_E, NEG = 2, -4, 4, 2, -10**6
def need_bits(lo, hi):
    for b in range(1, 33):
        if -(1 << (b - 1)) <= lo and hi < (1 << (b - 1)):
            return b
def run(path, limit):
    mn = {"H": 10**9, "E": 10**9, "F": 10**9}
    mx = {"H": -10**9, "E": -10**9, "F": -10**9}
    pairs = 0
    for line in open(path):
        line = line.rstrip("\r\n")
        if "\t" not in line: continue
        q, t = line.split("\t"); m, n = len(q), len(t)
        Hp = [0] * (n + 1); Ep = [NEG] * (n + 1)
        for i in range(1, m + 1):
            Hc = [0] * (n + 1); Ec = [NEG] * (n + 1); F = NEG
            for j in range(1, n + 1):
                Ec[j] = max(Hp[j] - GAP_O - GAP_E, Ep[j] - GAP_E)
                F = max(Hc[j-1] - GAP_O - GAP_E, F - GAP_E)
                s = MATCH if q[i-1] == t[j-1] else MISMATCH
                Hc[j] = max(0, Hp[j-1] + s, Ec[j], F)
                for k, v in (("H", Hc[j]), ("E", Ec[j]), ("F", F)):
                    if v < mn[k]: mn[k] = v
                    if v > mx[k]: mx[k] = v
            Hp, Ep = Hc, Ec
        pairs += 1
        if pairs >= limit: break
    print(f"Dosya: {path}  ({pairs} cift)")
    print(f"{'Deger':6}{'min':>8}{'max':>8}{'gereken bit':>14}")
    for k in "HEF":
        print(f"{k:6}{mn[k]:>8}{mx[k]:>8}{need_bits(mn[k], mx[k]):>10} bit (isaretli)")
    allb = need_bits(min(mn.values()), max(mx.values()))
    print(f"Ortak: {allb} bit isaretli yeterli (32 bit yazmacin {100*allb/32:.0f}%'i)")
run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 100)
