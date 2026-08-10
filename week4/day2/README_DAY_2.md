# 🔄 Week 4 · Day 2 — Cross-Validation

**BinX Tech — AI & Machine Learning Internship Program**
**Phase 2 · Week 4 of 10 · Day 2 of 5**

---

## 🎯 Learning Objectives

- 🧠 Explain how k-fold cross-validation produces a reliable performance estimate.
- ⚙️ Run cross-validation with `cross_val_score` and interpret the mean and standard deviation.
- ⚖️ Explain why stratified k-fold matters for classification.

## 📚 Key Topics Covered

- Why cross-validation beats a single validation split
- How k-fold works: rotating folds
- `cross_val_score`: mean and standard deviation
- Stratified k-fold for balanced classification folds

## 🛠️ What I Did

- Reloaded the Day 1 dataset and recreated the exact same train/validation/test split (same `random_state`) so today's results are directly comparable to yesterday's.
- Recomputed yesterday's single validation-split F1 score as a baseline for comparison.
- Ran **5-fold cross-validation** (`cross_val_score`) on the same model (`max_depth=3`) and reported the mean and standard deviation across folds.
- Visualized fold-by-fold scores with the mean and ±1 standard deviation band.
- Compared the Day 1 single-split score against the Day 2 cross-validated mean.
- Confirmed that `cross_val_score` uses stratified folds automatically for classifiers, and proved it by comparing class-balance proportions across `StratifiedKFold` vs. plain `KFold`.
- Wrote a Markdown reflection on what the comparison reveals about trusting a single split.

## 📊 Results

| Metric | Value |
|---|---|
| Day 1 single-split F1 | 0.9650 |
| Day 2 cross-validated mean F1 | 0.9606 |
| Cross-validated standard deviation | ±0.0169 |
| Difference (single split vs. CV mean) | 0.0044 |

**Stratification check** — benign-class proportion per fold (overall = 0.6276):
- Stratified K-Fold: 0.623 – 0.632 (tight, consistent)
- Plain K-Fold: 0.544 – 0.706 (swings noticeably — proof stratification matters)

## ✅ Deliverable Checklist

- [x] Model evaluated with 5-fold cross-validation using `cross_val_score`
- [x] Mean and standard deviation of fold scores reported
- [x] Cross-validated estimate compared to Day 1's single-split score, with explanation
- [x] Stratified folds confirmed and explained for this classification task
- [x] Markdown reflection written
- [x] Notebook committed to GitHub with a clear commit message

## 🧰 Tools Used

Scikit-learn (`cross_val_score`, `StratifiedKFold`, `KFold`) · Pandas · Matplotlib · Seaborn · Jupyter Notebook

---
📁 Files in this folder: `day2.ipynb`, `README_DAY_2.md`
