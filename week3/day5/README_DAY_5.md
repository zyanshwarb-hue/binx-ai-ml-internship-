# Day 5 — Supervised-Learning Mini-Project

**BinX Tech · AI & Machine Learning Internship Program — Week 3, Day 5**

## Overview

End-to-end supervised-learning pipeline on the Wisconsin Breast Cancer dataset (binary classification: malignant vs. benign), following the full EDA → Preprocessing → Split → Modeling → Evaluation structure from Week 3.

## What's Inside (`day5.ipynb`)

- **EDA:** class balance, feature distributions by diagnosis, correlation heatmap, boxplots for outliers/separation
- **Preprocessing:** `StandardScaler` fit on training data only (no data leakage)
- **Baseline:** `DummyClassifier` (majority class) for a real comparison point
- **Models trained:** Logistic Regression, Random Forest
- **Evaluation:** confusion matrices, classification reports, ROC curves + AUC, precision-recall curves, Random Forest feature importances, side-by-side metric comparison table

## Key Result

Both trained models substantially outperform the baseline, with Random Forest slightly ahead on F1 and ROC-AUC. Recall on the malignant class was treated as the priority metric, since a missed malignant case is far more costly than a false alarm.

## Tools Used

Scikit-learn · Pandas · Matplotlib · Seaborn · Jupyter Notebook

## Author

**Zayan Shawareb** — BinX Tech, AI & Machine Learning Internship Program
