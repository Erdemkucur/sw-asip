# Rapor sekilleri. Sayilar olcumlerden alinmistir:
#   profile/ozet_tablo.txt (Callgrind)  ve  profile/ic_dongu_ozet.txt (mix.py)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- Sekil 1: profil (Callgrind, x86-64, gcc -O2) ----
L      = [100, 150, 250]
f_pct  = [99.61, 99.80, 99.91]      # sw_gotoh payi, 500 cift
per_c  = [29.11, 29.08, 29.05]      # komut/hucre
fig, ax = plt.subplots(1, 2, figsize=(7.2, 2.6))
ax[0].bar([str(x) for x in L], f_pct, color="#2a6fb0")
ax[0].set_ylim(99.0, 100.0); ax[0].set_xlabel("Okuma uzunluğu (baz)")
ax[0].set_ylabel("sw_gotoh payı (%)"); ax[0].set_title("(a) Sıcak nokta payı f", fontsize=9)
for i, v in enumerate(f_pct): ax[0].text(i, v + 0.02, f"{v:.2f}", ha="center", fontsize=8)
ax[1].bar([str(x) for x in L], per_c, color="#d98c1f")
ax[1].set_ylim(0, 35); ax[1].set_xlabel("Okuma uzunluğu (baz)")
ax[1].set_ylabel("Komut / hücre"); ax[1].set_title("(b) Hücre başına komut", fontsize=9)
for i, v in enumerate(per_c): ax[1].text(i, v + 0.6, f"{v:.2f}", ha="center", fontsize=8)
plt.tight_layout(); plt.savefig("report/fig_profil.png", dpi=220); plt.close()

# ---- Sekil 2: ic dongu komut karisimi (statik, RISC-V) ----
cats = ["Toplama/çıkarma", "max", "Dal/atlama", "Mantık/kaydırma", "mv", "Bellek yükleme", "Bellek yazma"]
base = [10, 0, 7, 6, 6, 3, 2]       # RV32IM  = 34
zbb  = [10, 6, 1, 3, 1, 3, 2]       # RV32IM+Zbb = 26
assert sum(base) == 34 and sum(zbb) == 26
colors = ["#2a6fb0", "#c0392b", "#7f8c8d", "#8e44ad", "#f1c40f", "#27ae60", "#16a085"]
fig, ax = plt.subplots(figsize=(7.2, 2.4))
for row, (name, vals) in enumerate([("RV32IM (34)", base), ("RV32IM+Zbb (26)", zbb)]):
    left = 0
    for c, v, col in zip(cats, vals, colors):
        if v:
            ax.barh(row, v, left=left, color=col, label=c if row == 0 or c == "max" else None)
            ax.text(left + v/2, row, str(v), ha="center", va="center", fontsize=8, color="white")
        left += v
ax.set_yticks([0, 1]); ax.set_yticklabels(["RV32IM (34)", "RV32IM+Zbb (26)"])
ax.set_xlabel("Hücre başına statik komut sayısı"); ax.invert_yaxis()
h, l = ax.get_legend_handles_labels(); d = dict(zip(l, h))
ax.legend(d.values(), d.keys(), ncol=4, fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.32), frameon=False)
plt.tight_layout(); plt.savefig("report/fig_karisim.png", dpi=220); plt.close()
print("olustu: report/fig_profil.png, report/fig_karisim.png")
