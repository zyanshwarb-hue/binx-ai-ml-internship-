# 🎯 Day 3 — Logistic Regression & Classification Metrics

**BinX Tech — AI & Machine Learning Internship Program**
**Week 3: Supervised Learning | Phase 2 — Core ML Training**

![status](https://img.shields.io/badge/status-complete-brightgreen)
![phase](https://img.shields.io/badge/phase-2%20%7C%20Core%20ML%20Training-9146FF)
![dataset](https://img.shields.io/badge/dataset-Titanic-red)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![libraries](https://img.shields.io/badge/libraries-Scikit--learn%20%7C%20Pandas%20%7C%20Matplotlib-orange)
![AUC](https://img.shields.io/badge/AUC--ROC-0.863-success)
![accuracy](https://img.shields.io/badge/accuracy-80.4%25-success)

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 3 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day3.ipynb` |
| **Dataset** | Titanic — 714 rows after cleaning |
| **Model** | `sklearn.linear_model.LogisticRegression` |
| **Task** | Binary classification — predict `survived` |

The first classification model of the internship — trained, evaluated with a full metrics suite,
and benchmarked against a baseline.

---

## 🎯 Objectives

- Train a logistic regression classifier and obtain class probabilities.
- Explain why accuracy alone is misleading on imbalanced data.
- Read a confusion matrix and compute precision, recall, F1, and AUC-ROC.

---

## 🧠 Approach

1. Cleaned the Titanic dataset (dropped missing values, encoded `sex` numerically).
2. Performed a **stratified** 80/20 train/test split to preserve the survival rate in both sets.
3. Trained a logistic regression model and interpreted every feature's coefficient.
4. Established a majority-class baseline to prove the model adds real value.
5. Built and interpreted a confusion matrix.
6. Computed precision, recall, and F1-score, and discussed the precision/recall trade-off.
7. Plotted the ROC curve and computed AUC-ROC as a threshold-independent performance measure.

---

## 📈 Key Results

| Metric | Baseline (majority class) | Logistic Regression |
|---|---|---|
| **Accuracy** | 59.4% | **80.4%** |
| **Precision (Survived)** | — | **0.76** |
| **Recall (Survived)** | — | **0.76** |
| **F1-score (Survived)** | — | **0.76** |
| **AUC-ROC** | 0.5 (random) | **0.863** |

**→ The model beat the naive baseline by 21 accuracy points**, and its AUC-ROC of 0.863 confirms
strong discriminative power across virtually every probability threshold, not just the default 0.5.

---

## 🔍 Notable Insight: What Actually Drove Survival

| Feature | Coefficient | Direction |
|---|---|---|
| `sex` | **+2.43** | Strongest predictor — female passengers far more likely to survive |
| `pclass` | -1.22 | Lower class (higher number) → lower survival odds |
| `sibsp` | -0.33 | More siblings/spouses aboard → slightly lower survival odds |
| `age`, `parch`, `fare` | small | Minor secondary effects |

The model's strongest signal — `sex` — independently confirms the historical "women and children
first" account of the disaster, purely from the data.

---

## 🧾 Confusion Matrix Breakdown

Out of 143 test passengers: **71 true negatives**, **44 true positives**, **14 false positives**,
**14 false negatives** — a perfectly balanced error pattern, with no systematic bias toward
over- or under-predicting survival.

*(Full code, visualizations, and detailed interpretation are in the notebook itself.)*

---

## 🛠️ Tools Used

Scikit-learn (LogisticRegression) • Pandas • Matplotlib • Jupyter Notebook

---

## 📚 Resources

| Resource | Type | Focus |
|---|---|---|
| [Logistic Regression & Classification (Video)](https://youtu.be/29F-fXvowoI?si=WvVX2a1kLDPLGYwR) | Video | Core concepts covered today |
| [Scikit-learn — LogisticRegression Docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) | Docs | Official API reference |

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 4 — Trees, Forests, SVMs & k-NN**
