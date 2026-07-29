# 🔍 Day 4 — EDA Part 1: Distributions & Outliers

**BinX Tech — AI & Machine Learning Internship Program**
**Week 2: Math Foundations & EDA | Phase 1 → 2 Transition**

![status](https://img.shields.io/badge/status-complete-brightgreen)
![dataset](https://img.shields.io/badge/dataset-Titanic-red)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![libraries](https://img.shields.io/badge/libraries-Seaborn%20%7C%20Pandas%20%7C%20Matplotlib-orange)

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 4 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day4.ipynb` |
| **Dataset** | Titanic (Seaborn built-in) |
| **Columns Analyzed** | `age`, `fare`, `class` |

This day marks the beginning of formal **Exploratory Data Analysis (EDA)** — moving beyond
describing single numbers (Day 1) into visualizing full distributions, spotting class imbalance,
and systematically detecting outliers before any modeling begins.

---

## 🎯 Objectives

- Explain why EDA is a required first step before modeling.
- Perform univariate analysis using Seaborn histograms, box plots, and count plots.
- Detect outliers using the IQR method and decide how to handle them — keep, cap, or remove.

---

## 🧠 Approach

1. Loaded the Titanic dataset directly via Seaborn.
2. Visualized the `age` distribution with a histogram + KDE curve to assess symmetry and skew.
3. Visualized the `fare` distribution with a box plot to spot outliers visually.
4. Visualized the `class` column with a count plot to check for class imbalance.
5. Applied the IQR method programmatically on `fare` to formally flag outliers.
6. Cross-referenced the flagged outliers against passenger `class` to judge whether they were
   genuine values or data errors.
7. Documented every result with plain-language interpretation (data storytelling).

---

## 📈 Key Findings

| Finding | Detail |
|---|---|
| **Age distribution** | Right-skewed, peak around 20–40, with a secondary spike near ages 0–5 (young children) and a small gap around age 10–13 |
| **Fare distribution** | Extremely right-skewed — box compressed near $0–65, with a long tail of outliers reaching ~$500 |
| **Class imbalance** | Third class (~490 passengers) vastly outnumbers First (~215) and Second (~185) |
| **Outlier decision** | All top fare outliers belonged to First class passengers — genuine premium fares, **kept** rather than removed |

*(Full code, charts, and detailed interpretation are in the notebook itself.)*

---

## ⚠️ Data Quality Notes

- The fare outliers are **not data errors** — they correlate cleanly with First class, and repeated
  identical values (e.g. $263.00 appearing multiple times) suggest shared group/family bookings.
- The strong class imbalance (Third class ≈ 45% of all passengers) is an important consideration
  for any future model trained on this data — it could bias predictions toward majority-class
  patterns if not addressed.

---

## 🛠️ Tools Used

Seaborn • Pandas • Matplotlib • Jupyter Notebook

---

## 📚 Resources

| Resource | Type | Focus |
|---|---|---|
| [Seaborn Documentation](https://seaborn.pydata.org/) | Docs | Statistical visualization reference |
| [Khan Academy — Box Plots and IQR](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots) | Course / Video | Understanding IQR and outlier detection |

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 5 — EDA Part 2: Correlation & Data Storytelling**
