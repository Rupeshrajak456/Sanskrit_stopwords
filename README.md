# Sanskrit Stop Words (Indic NLP project)

Rupesh Rajak · MA Digital Humanities & Social Sciences · IIT (ISM) Dhanbad · Monsoon Semester 2026

- `Sanskrit_stopwords.py`: the stop-word list, in the required format
- `analysis.py`: categorises the list, prints the breakdown, draws the two PNG charts and writes `data.js` and `data.json`
- `index.html`, `data.js`, `stopword_categories.png`, `stopword_donut.png`: the GitHub Pages site

Run `python analysis.py` to rebuild the charts and data.

## Publish

```bash
git init && git add . && git commit -m "Sanskrit stop words project"
git branch -M main
git remote add origin https://github.com/<username>/<repository>.git
git push -u origin main
```
Then open **Settings → Pages → Deploy from a branch → main / (root)**. The site appears at `https://<username>.github.io/<repository>/`.

Licence: CC BY-NC 4.0 International.
