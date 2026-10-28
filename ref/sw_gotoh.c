// Affine-gap yerel hizalama (Smith-Waterman, Gotoh) - sadece skor
// Skorlama: match=+2, mismatch=-4, gap uzunlugu k icin ceza = GAP_O + k*GAP_E
// Girdi (stdin): her satir "sorgu<TAB>hedef"; Cikti: her satir bir skor
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

#define MATCH    2
#define MISMATCH (-4)
#define GAP_O    4
#define GAP_E    2
#define NEG_INF  (-1000000)
#define MAXLEN   4096

static inline int32_t max2(int32_t a, int32_t b) { return a > b ? a : b; }

// Referans (skalar) hizalama: skoru dondurur
int32_t sw_gotoh(const char *q, int m, const char *t, int n) {
    static int32_t H[MAXLEN + 1], E[MAXLEN + 1];   // tek satirlik tamponlar
    int32_t best = 0;
    for (int j = 0; j <= n; j++) { H[j] = 0; E[j] = NEG_INF; }
    for (int i = 1; i <= m; i++) {
        int32_t diag = 0;            // H[i-1][j-1]
        int32_t Hleft = 0;           // H[i][j-1]
        int32_t F = NEG_INF;         // F[i][j-1] satir boyunca tasinir
        for (int j = 1; j <= n; j++) {
            int32_t s  = (q[i-1] == t[j-1]) ? MATCH : MISMATCH;
            int32_t Hup = H[j];                                  // H[i-1][j]
            E[j] = max2(Hup   - GAP_O - GAP_E, E[j] - GAP_E);    // dikey gap
            F    = max2(Hleft - GAP_O - GAP_E, F    - GAP_E);    // yatay gap
            int32_t h = max2(0, max2(diag + s, max2(E[j], F)));
            diag = Hup;
            H[j] = h;
            Hleft = h;
            if (h > best) best = h;
        }
    }
    return best;
}

#ifndef NO_MAIN
int main(void) {
    static char line[2 * MAXLEN + 4];
    while (fgets(line, sizeof line, stdin)) {
        char *tab = strchr(line, '\t');
        if (!tab) continue;
        *tab = 0;
        char *q = line, *t = tab + 1;
        t[strcspn(t, "\r\n")] = 0;
        printf("%d\n", sw_gotoh(q, (int)strlen(q), t, (int)strlen(t)));
    }
    return 0;
}
#endif
