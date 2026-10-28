# Python altin model: tam H/E/F matrisleriyle, C kodundan bagimsiz yazilmis
import sys
MATCH, MISMATCH, GAP_O, GAP_E = 2, -4, 4, 2
NEG = -10**6

def sw_gotoh(q, t):
    m, n = len(q), len(t)
    H = [[0]*(n+1) for _ in range(m+1)]
    E = [[NEG]*(n+1) for _ in range(m+1)]
    F = [[NEG]*(n+1) for _ in range(m+1)]
    best = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            E[i][j] = max(H[i-1][j] - GAP_O - GAP_E, E[i-1][j] - GAP_E)
            F[i][j] = max(H[i][j-1] - GAP_O - GAP_E, F[i][j-1] - GAP_E)
            s = MATCH if q[i-1] == t[j-1] else MISMATCH
            H[i][j] = max(0, H[i-1][j-1] + s, E[i][j], F[i][j])
            best = max(best, H[i][j])
    return best

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip("\r\n")
        if "\t" not in line: continue
        q, t = line.split("\t")
        print(sw_gotoh(q, t))
