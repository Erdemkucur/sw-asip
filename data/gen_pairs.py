# Tekrarlanabilir test verisi: hedeften okuma uretir, hata ekler.
# Kullanim: python3 gen_pairs.py <cift_sayisi> <okuma_uzunlugu> <hata_orani> <seed> > pairs.tsv
import random, sys
n_pairs, rlen, err, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
rnd = random.Random(seed)
B = "ACGT"
for _ in range(n_pairs):
    target = "".join(rnd.choice(B) for _ in range(rlen + 20))
    start = rnd.randint(0, 20)
    src = target[start:start + rlen]
    q = []
    for c in src:
        r = rnd.random()
        if r < err * 0.7:
            q.append(rnd.choice([x for x in B if x != c]))   # yerine koyma
        elif r < err * 0.85:
            q.append(c); q.append(rnd.choice(B))             # ekleme
        elif r < err:
            continue                                         # silme
        else:
            q.append(c)
    print("".join(q) + "\t" + target)
