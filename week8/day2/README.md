<p align="center">
  <img src="https://img.shields.io/badge/BINX%20TECH-AI%20%26%20ML%20INTERNSHIP-061A33?style=for-the-badge" alt="BinX Tech"/>
</p>

<h1 align="center">🩺 Week 8 · Day 2</h1>
<h3 align="center">Text Representation — TF-IDF &amp; Word Embeddings</h3>

<p align="center">
  <img src="https://img.shields.io/badge/SPRINT-3-0B2E59?style=for-the-badge" alt="Sprint 3"/>
  <img src="https://img.shields.io/badge/DAY-2%20OF%205-00A6C0?style=for-the-badge" alt="Day 2 of 5"/>
  <img src="https://img.shields.io/badge/DURATION-8%20HOURS-FFC857?style=for-the-badge&logoColor=black" alt="8 hours"/>
  <img src="https://img.shields.io/badge/TOPIC-TEXT%20REPRESENTATION-1BAF7A?style=for-the-badge" alt="Text Representation"/>
  <img src="https://img.shields.io/badge/THREAD-CARDIAC%20MONITORING-8B5CF6?style=for-the-badge" alt="Cardiac Monitoring Thread"/>
</p>

<p align="center"><i>"A model doesn't read words — it reads geometry. Today we build the map."</i></p>

---

## 📖 The Story So Far

Day 1 ended with clean, correctly-negated tokens instead of raw, messy sentences. That's progress, but a model still
can't do anything with a list of words — it needs **numbers**. Day 2 turns clean tokens into numeric vectors two
different ways, and asks which one actually deserves a place in a real pipeline.

## 🎯 Learning Objectives

| | Objective |
|---|---|
| 🔢 | Convert cleaned text to numeric vectors with TF-IDF |
| 🧭 | Explain word embeddings and how they capture meaning as geometry |
| ⚖️ | Choose between TF-IDF and embeddings for a given task — and justify it |

## 🔬 What Actually Happens in the Notebook

1. **Reload** the exact cleaning pipeline from Day 1 (bundled again here so this folder runs standalone).
2. **TF-IDF** the cleaned reviews with `scikit-learn`, and inspect which terms actually drive one review's score.
3. **Load real pre-trained GloVe embeddings** (50-dim, Wikipedia + Gigaword) and prove the geometry works — including
   the classic `king − man + woman ≈ queen`.
4. **Train a tiny TF-IDF + Logistic Regression sentiment classifier** on the bundled reviews, as an honest,
   achievable stand-in for "a simple classifier as a text baseline."
5. **Document** which representation actually fits this capstone, and why.

> [!NOTE]
> This folder's data file (`day2_sample_reviews.csv`) adds a `sentiment` label to the same reviews used on Day 1 —
> needed to give TF-IDF an actual prediction task, since the real capstone (Cardiac Monitoring) has no text target of
> its own.

## 🧮 TF-IDF: proof it actually works

Running TF-IDF on *"This medication did **NOT** help my symptoms at all, I was very disappointed"* surfaces
`disappoint`, `not`, and `symptom` as the top-weighted terms — the negation word Day 1 fought to protect is now
carrying real numeric weight in the vector. The fix from Day 1 wasn't just correct, it was necessary for Day 2 to
work at all.

## 🧭 Word Embeddings: proof the geometry is real

Real pre-trained GloVe vectors, not vectors trained on our tiny 20-row sample (too small for meaningful geometry):

| Word | Nearest neighbors |
|---|---|
| `doctor` | nurse, physician, patient |
| `pain` | suffering, stress, stomach |
| `help` | helping, bring, need |

...and the famous analogy holds exactly: `king − man + woman →` **`queen`** (top result, real GloVe vectors, no
cherry-picking).

## ⚖️ TF-IDF vs. Word Embeddings

| | TF-IDF | Word Embeddings |
|---|---|---|
| Represents | Word importance by frequency | Word meaning in vector space |
| Captures meaning? | No | Yes — similar words are close |
| Order / context? | No | Partially (contextual embeddings: yes) |
| Best for | Strong, fast baseline | Semantic tasks, deep learning input |

> [!TIP]
> **Contextual embeddings (Week 7: BERT)** go one step further — a word gets a *different* vector depending on its
> sentence, which is why transformer-based models outperform Word2Vec/GloVe on nuanced language.

## 📝 Documented Decision: which representation fits, and why

- **TF-IDF** — right default when data is scarce, speed matters, and interpretability matters (it can name the exact
  terms driving a prediction).
- **Word embeddings** — earn their cost when semantic similarity matters more than surface word overlap.
- **Contextual embeddings** — justified only when meaning genuinely shifts by context and the project can afford the
  compute (why Week 7 reached for DistilBERT, not plain Word2Vec).
- **For Cardiac Monitoring specifically:** none apply directly — the data is structured vitals, not text — but if
  physician notes ever entered the pipeline, TF-IDF would be the sane first baseline, same "start simple, prove
  value first" principle as Day 1's NegEx point.

> [!WARNING]
> **Honesty check on the classifier:** the tiny sentiment classifier above scores around chance level on 6 held-out
> reviews — expected and stated in the notebook. With only 20 rows total this is illustrative of the *mechanism*,
> not a real evaluation. Day 5's lesson on evaluating against a proper baseline applies here too.

## 🧰 Tools Used

![Scikit-learn](https://img.shields.io/badge/Scikit--learn%20(TfidfVectorizer)-0B2E59?style=flat-square)
![Gensim](https://img.shields.io/badge/Gensim%20%2F%20Pre--trained%20Embeddings-0B2E59?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-0B2E59?style=flat-square)
![Git](https://img.shields.io/badge/Git%20%26%20GitHub-0B2E59?style=flat-square)

## 📓 The Notebook

**[→ Open day2.ipynb](./day2.ipynb)** for the full, executed walkthrough — code and real output, generated live.

---

<p align="center"><sub>Week 8 · Sprint 3 · Day 2 of 5 → <b>Day 3: Computer Vision Preprocessing (OpenCV)</b></sub></p>
