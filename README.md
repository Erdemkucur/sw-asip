# sw-asip: Affine-gap Smith-Waterman için ASIP analizi (BIL523 Ödev 1)

Uygulama: affine-gap yerel hizalama (Gotoh), yalnızca skor.
Skorlama: eşleşme +2, uyuşmazlık -4, gap uzunluğu k için ceza 4 + 2k.

## Tekrarlama
    make test
    python3 data/gen_pairs.py 1000 150 0.05 42 > data/pairs_1k.tsv
    valgrind --tool=callgrind --callgrind-out-file=profile/callgrind_1k.out ./ref/sw_gotoh < data/pairs_1k.tsv > /dev/null
    python3 profile/summary.py
    python3 profile/mix.py profile/sw_gotoh_rv32im_zbb.s .L12
    python3 profile/bitwidth.py data/pairs_L250.tsv 100
    python3 profile/amdahl.py
    python3 report/make_figures.py

## Dizin
- ref/: referans C kodu, Python altın model, RISC-V çekirdek dosyası
- data/: test verisi üretici (veri dosyaları depoda tutulmaz, seed ile yeniden üretilir)
- profile/: profil çıktıları, assembly, analiz betikleri
- report/: şekiller ve literatür notları

Ortam: Kali Linux (VirtualBox), gcc, Valgrind 3.27.1, riscv64-linux-gnu-gcc 16.2.0.
