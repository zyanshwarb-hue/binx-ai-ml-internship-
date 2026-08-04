# 🤖 Day 1 — Supervised Learning Concepts & the Scikit-learn API

**BinX Tech — AI & Machine Learning Internship Program**
**Week 3: Supervised Learning | Phase 2 — Core ML Training**

![status](https://img.shields.io/badge/status-complete-brightgreen)
![phase](https://img.shields.io/badge/phase-2%20%7C%20Core%20ML%20Training-9146FF)
![dataset](https://img.shields.io/badge/dataset-Diamonds-red)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![libraries](https://img.shields.io/badge/libraries-Scikit--learn%20%7C%20Pandas%20%7C%20Matplotlib-orange)

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 1 of 5 — first day of Phase 2 |
| **Duration** | 8 hours |
| **Notebook** | `day1.ipynb` |
| **Dataset** | Diamonds (~53,940 rows) |
| **Prerequisite** | Weeks 1–2 completed |

This day marks the transition from pure data analysis into **building models that predict** — the
foundation every subsequent notebook in Phase 2 depends on.

---

## 🎯 Objectives

- Explain what supervised learning is and distinguish regression from classification.
- Separate a dataset into features (X) and target (y).
- Perform a train/test split and explain why evaluating on unseen data is essential.

---

## 🧠 Approach

1. Defined supervised learning and the regression-vs-classification distinction with concrete
   examples.
2. Split the Diamonds dataset into features `X` (carat, depth, table, x, y, z) and target `y`
   (price).
3. Performed an 80/20 train/test split with a fixed `random_state=42` for reproducibility.
4. Visualized the split two ways: a donut chart showing the train/test proportions, and a
   spatial scatter plot confirming the split was a genuinely random, representative sample —
   not skewed toward any price range.
5. Reviewed the four-step Scikit-learn API (Instantiate → Fit → Predict → Score) used by every
   model in the library.
6. Ran shape-consistency checks to confirm the data was correctly prepared before modeling begins.

---

## 📈 Key Findings

| Finding | Detail |
|---|---|
| **Train / Test split** | 80% train (~43,152 rows) / 20% test (~10,788 rows) |
| **Features (X)** | 6 numeric columns: carat, depth, table, x, y, z |
| **Target (y)** | `price` — a continuous number → this is a **regression** problem |
| **Spatial split check** | Train and test points were evenly distributed across the full carat/price range — confirming a genuine random sample |
| **Reproducibility** | `random_state=42` guarantees the exact same split every time the code runs |

*(Full code, visualizations, and detailed interpretation are in the notebook itself.)*

---

## ⚠️ The Golden Rule Established Today

> A model must **never** see the test set during training — doing so lets it memorize answers
> instead of learning generalizable patterns, making any resulting evaluation dishonest. This
> single principle underlies every notebook for the rest of Phase 2.

---

## 🛠️ Tools Used

Scikit-learn • Pandas • Matplotlib • Jupyter Notebook

---

## 📚 Resources

| Resource | Type | Focus |
|---|---|---|
| [Supervised Learning Concepts (Video)](https://www.youtube.com/watch?v=0B5eIE_1vpU) | Video | Core concepts covered today |
| [Scikit-learn Documentation](https://scikit-learn.org/stable/) | Docs | Official API reference |

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 2 — Linear Regression**
