# sw-asip: Affine-gap Smith-Waterman için ASIP analizi (BIL523 Ödev 1)

Uygulama: affine-gap yerel hizalama (Gotoh), yalnızca skor. Skorlama: eşleşme +2, uyuşmazlık -4, gap uzunluğu k için ceza 4 + 2k.

## Tekrarlama
Ortam: Kali Linux. Gerekenler: gcc, valgrind, python3, python3-matplotlib, gcc-riscv64-linux-gnu, graphviz. Komutları depo kök dizininde sırayla çalıştırın.

### 1. Referans ve doğrulama
    make test

### 2. Test verisi (tohumlu, her makinede aynı çıkar)
    for L in 100 150 250; do python3 data/gen_pairs.py 500 $L 0.05 42 > data/pairs_L$L.tsv; done
    python3 data/gen_pairs.py 1000 150 0.05 42 > data/pairs_1k.tsv
    python3 data/gen_pairs.py 20000 150 0.05 42 > data/pairs_20k.tsv

### 3. Profil
    valgrind --tool=callgrind --callgrind-out-file=profile/callgrind_1k.out ./ref/sw_gotoh < data/pairs_1k.tsv > /dev/null
    callgrind_annotate profile/callgrind_1k.out > profile/callgrind_1k.txt
    for L in 100 150 250; do valgrind --tool=callgrind --callgrind-out-file=profile/cg_L$L.out ./ref/sw_gotoh < data/pairs_L$L.tsv > /dev/null; callgrind_annotate profile/cg_L$L.out > profile/cg_L$L.txt; done
    python3 profile/summary.py
    gcc -O2 -g -pg -o ref/sw_gotoh_pg ref/sw_gotoh.c && ./ref/sw_gotoh_pg < data/pairs_20k.tsv > /dev/null && gprof -b -p ref/sw_gotoh_pg gmon.out

### 4. İç döngü analizi (RISC-V)
    riscv64-linux-gnu-gcc -march=rv32im -mabi=ilp32 -O2 -S -ffreestanding -o profile/sw_gotoh_rv32im.s ref/rv_kernel.c
    riscv64-linux-gnu-gcc -march=rv32im_zbb -mabi=ilp32 -O2 -S -ffreestanding -o profile/sw_gotoh_rv32im_zbb.s ref/rv_kernel.c
    python3 profile/mix.py profile/sw_gotoh_rv32im.s .L13
    python3 profile/mix.py profile/sw_gotoh_rv32im_zbb.s .L12
    python3 profile/bitwidth.py data/pairs_L250.tsv 100
    dot -Tpng profile/dfg.dot -o profile/dfg.png

### 5. Sınır hesapları ve şekiller
    python3 profile/amdahl.py
    python3 report/make_figures.py

Notlar: Assembly etiketleri (.L13, .L12) derleyici sürümüne bağlıdır (riscv64-linux-gnu-gcc 16.2.0); farklı sürümde etiketleri profile/*.s dosyasından bakıp değiştirin. Callgrind toplam komut sayısı tekrar çalıştırmalarda birkaç yüz komut oynayabilir; hücre sayıları ve komut/hücre değişmez (1000 çift için 25.504.930 hücre).

## Dizin
- ref/: referans C kodu, Python altın model, RISC-V çekirdek dosyası
- data/: test verisi üretici (veri dosyaları depoda tutulmaz, tohumla yeniden üretilir)
- profile/: profil çıktıları, assembly, analiz betikleri
- report/: şekiller ve literatür notları
