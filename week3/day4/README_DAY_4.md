# 🌲 Day 4 — Trees, Forests, SVMs & k-NN

**BinX Tech — AI & Machine Learning Internship Program**
**Week 3: Supervised Learning | Phase 2 — Core ML Training**

![status](https://img.shields.io/badge/status-complete-brightgreen)
![phase](https://img.shields.io/badge/phase-2%20%7C%20Core%20ML%20Training-9146FF)
![dataset](https://img.shields.io/badge/dataset-Titanic-red)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![libraries](https://img.shields.io/badge/libraries-Scikit--learn%20%7C%20Pandas%20%7C%20Matplotlib-orange)
![best_model](https://img.shields.io/badge/best%20model-SVM%20(scaled)%20%7C%2081.8%25-success)

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 4 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day4.ipynb` |
| **Dataset** | Titanic — same split as Day 3 |
| **Models Compared** | Decision Tree, Random Forest, SVM, k-NN (each with/without scaling) |

Four classifiers, one fair comparison, and one experiment that overturned the "safe default"
assumption about which model wins.

---

## 🎯 Objectives

- Train and interpret decision trees and random forests, including feature importances.
- Train SVM and k-NN classifiers and explain how each makes decisions.
- Compare multiple classifiers fairly on the same train/test split and metric.

---

## 🧠 Approach

1. Reused the exact Day 3 stratified train/test split for a fair, apples-to-apples comparison.
2. Trained a Decision Tree (`max_depth=5`) and diagnosed a train-test overfitting gap.
3. Trained a Random Forest and extracted feature importances.
4. Trained SVM and k-NN "out of the box" — both underperformed unexpectedly.
5. **Diagnosed the cause** (unscaled features) and re-ran both models with `StandardScaler`
   (fit on train only, to avoid data leakage).
6. Assembled a final, fair comparison table across all 6 model variants, ranked by F1-score.

---

## 🏆 Final Model Comparison

| Rank | Model | Accuracy | F1-score |
|---|---|---|---|
| 🥇 | **SVM (scaled)** | **81.8%** | **0.735** |
| 🥈 | k-NN (scaled) | 76.2% | 0.702 |
| 🥉 | Random Forest | 75.5% | 0.690 |
| 4 | Decision Tree | 74.8% | 0.667 |
| 5 | SVM (unscaled) | 68.5% | 0.526 |
| 6 | k-NN (unscaled) | 62.9% | 0.539 |

---

## ⚡ The Headline Finding: Scaling Beat Algorithm Choice

SVM and k-NN were trained twice — once on raw features, once on `StandardScaler`-transformed
features. The result:

| Model | Unscaled Accuracy | Scaled Accuracy | Improvement |
|---|---|---|---|
| **SVM** | 68.5% | **81.8%** | **+13.3 points** |
| **k-NN** | 62.9% | **76.2%** | **+13.3 points** |

This single preprocessing change produced a bigger accuracy jump than switching between any two
algorithms in this notebook — proving that **for distance-based models, feature scaling can
matter more than the choice of algorithm itself**. After scaling, SVM became the single
best-performing model in the entire comparison, ahead of Random Forest.

---

## 🔍 Notable Insight: Random Forest Didn't Fully Solve Overfitting

| Model | Train Accuracy | Test Accuracy | Gap |
|---|---|---|---|
| Decision Tree | 86.9% | 74.8% | 12.1 pts |
| Random Forest | **98.9%** | 75.5% | **23.4 pts** |

Counter-intuitively, the random forest's train-test gap was *larger* than the single tree's, even
though its test accuracy was slightly better. This is explained in the notebook: random forests
reduce overfitting by **averaging many trees' predictions**, not by making any individual tree
simpler — so a high training score alone doesn't mean the ensemble failed to generalize.

---

## 🔍 Feature Importances (Random Forest)

`fare` (28.4%) and `age` (27.6%) narrowly edged out `sex` (25.1%) as the top predictors —
notably different from logistic regression's coefficients in Day 3, where `sex` dominated.
Different model families can extract different, equally valid signals from the same data.

*(Full code, visualizations, and detailed interpretation are in the notebook itself.)*

---

## 🛠️ Tools Used

Scikit-learn (tree, ensemble, svm, neighbors, preprocessing) • Pandas • Matplotlib • Jupyter Notebook

---

## 📚 Resources

| Resource | Type | Focus |
|---|---|---|
| [Decision Trees, Random Forests, SVMs, k-NN (Video)](https://www.youtube.com/watch?v=Mo9nBd1Qqyg) | Video | Core concepts covered today |
| [Scikit-learn — StandardScaler Docs](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) | Docs | Feature scaling reference |

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 5 — Supervised-Learning Mini-Project**
