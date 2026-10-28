CC=gcc
all: ref/sw_gotoh
ref/sw_gotoh: ref/sw_gotoh.c
	$(CC) -O2 -g -o $@ $<
test: all
	python3 data/gen_pairs.py 200 150 0.05 1 > data/test_small.tsv
	./ref/sw_gotoh < data/test_small.tsv > data/out_c.txt
	python3 ref/golden.py < data/test_small.tsv > data/out_py.txt
	cmp data/out_c.txt data/out_py.txt && echo "DOGRULAMA BASARILI: C ve Python skorlari ayni"
clean:
	rm -f ref/sw_gotoh data/*.tsv data/out_*.txt
