# Toplam DP hucre sayisi = sum(sorgu_uzunlugu * hedef_uzunlugu)
import sys
def cells(path):
    s = 0
    for l in open(path):
        l = l.rstrip("\r\n")
        if "\t" in l:
            a, b = l.split("\t")
            s += len(a) * len(b)
    return s
if __name__ == "__main__":
    print(cells(sys.argv[1]))
