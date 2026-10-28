// Sadece hizalama cekirdegi (RISC-V assembly uretmek icin). ref/sw_gotoh.c ile ayni algoritma.
#include <stdint.h>

#define MATCH    2
#define MISMATCH (-4)
#define GAP_O    4
#define GAP_E    2
#define NEG_INF  (-1000000)
#define MAXLEN   4096

static inline int32_t max2(int32_t a, int32_t b) { return a > b ? a : b; }

int32_t sw_gotoh(const char *q, int m, const char *t, int n) {
    static int32_t H[MAXLEN + 1], E[MAXLEN + 1];
    int32_t best = 0;
    for (int j = 0; j <= n; j++) { H[j] = 0; E[j] = NEG_INF; }
    for (int i = 1; i <= m; i++) {
        int32_t diag = 0;
        int32_t Hleft = 0;
        int32_t F = NEG_INF;
        for (int j = 1; j <= n; j++) {
            int32_t s  = (q[i-1] == t[j-1]) ? MATCH : MISMATCH;
            int32_t Hup = H[j];
            E[j] = max2(Hup   - GAP_O - GAP_E, E[j] - GAP_E);
            F    = max2(Hleft - GAP_O - GAP_E, F    - GAP_E);
            int32_t h = max2(0, max2(diag + s, max2(E[j], F)));
            diag = Hup;
            H[j] = h;
            Hleft = h;
            if (h > best) best = h;
        }
    }
    return best;
}
