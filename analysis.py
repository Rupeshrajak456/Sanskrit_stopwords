"""Categorise the Sanskrit stop words, print the breakdown, draw the chart and write data.js."""
import json
from Sanskrit_stopwords import Sanskrit_stopwords as W

CATS = {
 "Personal Pronouns & Possessives": "aham vayam aavaam maam mayaa mahyam mama me asmaan asmaakam asmabhyam asmaabhih tvam yuvaam yuuyam tvaam tvayaa tava te tubhyam yushmaan yushmaakam bhavaan bhavatii svayam svam",
 "Demonstratives": "sah saa tat tam taam tasya tasyaah tena tayaa tasmai tasmaat tasmin teshaam taasaam taih tebhyah taah taani eshah eshaa etat etam etasya etena ete ayam iyam idam imam asya anena asmaat asmin ime eshaam",
 "Relative Pronouns": "yah yaa yat yam yasya yena yasmaat yasmin ye yeshaam",
 "Interrogatives": "kah kaa kim kam kasya kena kasmaat ke kaani katham kutra kva kutah",
 "Quantifiers & Determiners": "sarvah sarve sarvam sarveshaam anyah anyat aparah ekah ekam ubhau ubhayam bahu bhuuyah kevalam maatram kinchit kashchit kimapi kiyat iyat taavat yaavat",
 "Copula & Auxiliary Verbs": "asti santi asmi asi aasiit aasan syaat bhavati bhavanti bhavet abhavat",
 "Conjunctions & Connectives": "ca vaa atha athavaa",
 "Conditionals & Concessives": "yadi cet tarhi yadyapi tathaapi",
 "Negation & Prohibition": "na maa nahi alam",
 "Particles & Emphatic Forms": "api eva tu hi iti iva uta kila khalu nanu naama",
 "Adverbs of Place": "atra tatra yatra sarvatra anyatra iha antah bahih upari adhah",
 "Adverbs of Time": "tadaa yadaa kadaa adhunaa idaaniim samprati adya shvah hyah sadaa kadaapi kadaachit nityam puraa puurvam pashchaat anantaram punah",
 "Adverbs of Manner & Reason": "yatah tatah atah itah evam ittham yathaa tathaa sahasaa shiighram nuunam samyak parasparam praayah anyathaa",
 "Prepositions & Preverbs (Upasargas)": "saha saardham vinaa prati anu abhi upa adhi pari aa ati param",
 "Interjections & Vocatives": "aho he bhoh are",
}
C = {k: v.split() for k, v in CATS.items()}
flat = [w for v in C.values() for w in v]
uniq = list(dict.fromkeys(W))
print(f"Entries in file: {len(W)} | unique: {len(uniq)} | duplicates: {sorted({w for w in W if W.count(w) > 1})}")
print("Uncategorised:", sorted(set(uniq) - set(flat)), "| Not in list:", sorted(set(flat) - set(uniq)), "| Repeated across categories:", sorted({w for w in flat if flat.count(w) > 1}))
print(f"\n{'Category':42}{'Count':>6}{'%':>7}")
for k, v in sorted(C.items(), key=lambda x: -len(x[1])):
    print(f"{k:42}{len(v):>6}{100*len(v)/len(flat):>6.1f}%")
json.dump(C, open("data.json", "w"), ensure_ascii=False, indent=1)
open("data.js", "w").write("window.DATA=" + json.dumps(C) + ";")

import colorsys, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
BG, INK = "#fbf7ef", "#2b2218"
pal = lambda i: colorsys.hls_to_rgb(((i*24+20) % 360)/360, .44+(i % 2)*.08, .42)
rank = sorted(C.items(), key=lambda x: -len(x[1]))
cols = {k: pal(i) for i, (k, _) in enumerate(rank)}
items = rank[::-1]
fig, ax = plt.subplots(figsize=(10, 6.4), facecolor=BG); ax.set_facecolor(BG)
bars = ax.barh([k for k, _ in items], [len(v) for _, v in items], color=[cols[k] for k, _ in items], height=.66)
for b, (_, v) in zip(bars, items):
    ax.text(b.get_width()+.6, b.get_y()+b.get_height()/2, str(len(v)), va="center", color=INK, fontsize=10)
ax.tick_params(colors=INK, labelsize=10); [sp.set_visible(False) for sp in ax.spines.values()]; ax.xaxis.set_visible(False)
ax.set_title(f"Sanskrit stop words by category (n = {len(flat)})", color="#7a4a1a", fontsize=14, loc="left", pad=14)
plt.tight_layout(); plt.savefig("stopword_categories.png", dpi=160, facecolor=BG); plt.close()
fig, ax = plt.subplots(figsize=(8.5, 6), facecolor=BG)
ax.pie([len(v) for _, v in rank], colors=[cols[k] for k, _ in rank], startangle=90, counterclock=False,
       wedgeprops=dict(width=.38, edgecolor=BG, linewidth=2))
ax.text(0, .04, str(len(flat)), ha="center", fontsize=30, color="#7a4a1a"); ax.text(0, -.17, "stop words", ha="center", fontsize=11, color=INK)
ax.legend([f"{k} ({len(v)})" for k, v in rank], loc="center left", bbox_to_anchor=(1, .5), frameon=False, labelcolor=INK, fontsize=9)
plt.tight_layout(); plt.savefig("stopword_donut.png", dpi=160, facecolor=BG, bbox_inches="tight")
