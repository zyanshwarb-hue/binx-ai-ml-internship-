# ⚖️ Week 4 · Day 3 — Bias-Variance & Diagnosing Model Fit

**BinX Tech — AI & Machine Learning Internship Program**
**Phase 2 · Week 4 of 10 · Day 3 of 5**

---

## 🎯 Learning Objectives

- 🔍 Distinguish underfitting from overfitting by their symptoms.
- ⚖️ Explain the bias-variance trade-off and its role in tuning.
- 🩺 Diagnose model fit from the train-vs-validation score gap and apply regularization.

## 📚 Key Topics Covered

- Underfitting (high bias) vs. overfitting (high variance)
- The bias-variance trade-off
- Diagnosing fit from the train-vs-validation gap
- Regularization strength and its effect on the gap

## 🛠️ What I Did

- Reused the Day 1/Day 2 dataset and split for full continuity across the week.
- **Overfit demo:** trained an unrestricted `DecisionTreeClassifier` — it memorized the training data (Train F1 = 1.0000) but dropped noticeably on validation (0.9640), a **0.0360 gap** — the textbook overfitting symptom.
- **Underfit demo:** trained a depth-1 decision stump — both train (0.9431) and validation (0.9221) scores were low with a small gap, the textbook underfitting symptom.
- Swept `max_depth` from 1 to 15 and plotted the full bias-variance curve, visually identifying the sweet spot at `max_depth=5`.
- Applied regularization by sweeping `C` in a `LogisticRegression` model (scaled features), watching the train-validation gap shrink as regularization increased — until it became *too* strong and both scores dropped (underfitting again at very small `C`).
- Compared the overfit tree's gap against the best-regularized model's gap directly in a chart.
- Wrote a Markdown reflection explaining each diagnosis.

## 📊 Results

| Model | Train F1 | Validation F1 | Gap | Diagnosis |
|---|---|---|---|---|
| Overfit tree (unlimited depth) | 1.0000 | 0.9640 | 0.0360 | Overfitting |
| Underfit tree (max_depth=1) | 0.9431 | 0.9221 | 0.0210 | Underfitting |
| Best tree by curve sweep (max_depth=5) | — | 0.9640 | — | Good fit |
| Regularized LogisticRegression (best C=1) | 0.9907 | 0.9930 | -0.0023 | Good fit (gap essentially closed) |

**Gap reduction from regularization:** 0.0383 (from 0.0360 down to -0.0023)

## ✅ Deliverable Checklist

- [x] Overfit model built and diagnosed (large train-vs-validation gap)
- [x] Underfit model built and diagnosed (both scores low)
- [x] Bias-variance curve plotted across a range of `max_depth` values
- [x] Regularization applied and shown to shrink the overfitting gap
- [x] Markdown reflection written
- [x] Notebook committed to GitHub with a clear commit message

## 🧰 Tools Used

Scikit-learn (`DecisionTreeClassifier`, `LogisticRegression`, `StandardScaler`) · Pandas · Matplotlib · Seaborn · Jupyter Notebook

---
📁 Files in this folder: `day3.ipynb`, `README_DAY_3.md`
