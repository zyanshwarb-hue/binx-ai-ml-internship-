# 📊 Day 1 — Descriptive Statistics

**BinX Tech — AI & Machine Learning Internship Program**
**Week 2: Math Foundations & EDA | Phase 1 → 2 Transition**

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 1 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day1_descriptive_statistics.ipynb` |
| **Dataset** | Titanic (real-world tabular dataset) |
| **Column Analyzed** | `age` |

This day focuses on the foundation of every data analysis: **descriptive statistics** — the
vocabulary used to describe a dataset's center, spread, and shape before any modeling begins.

---

## 🎯 Objectives

- Compute and interpret **mean**, **median**, and **mode**, and justify which measure best
  represents a given dataset.
- Compute and interpret **variance**, **standard deviation**, and **IQR**.
- Understand how **outliers** affect each measure differently.

---

## 🧠 Approach

1. Loaded the Titanic dataset and isolated the `age` column.
2. Computed all three measures of central tendency (mean, median, mode) and compared them to
   detect any skew in the data.
3. Computed measures of spread (range, variance, standard deviation, IQR) to quantify how
   dispersed the ages are.
4. Computed Q1 and Q3 to identify the interquartile range — the range robust to outliers.
5. Consolidated every statistic into a single summary table for quick reference.
6. Interpreted each result in plain language (data storytelling), connecting the numbers to what
   they reveal about the passengers aboard.

---

## 📈 Key Findings

- Mean (≈29.7) and median (28) are close, with a mild right skew.
- Mode (24) shows early adulthood as the most common boarding age.
- IQR (17.88, spanning ages 20–38) confirms most passengers were working-age adults.
- No extreme outliers severe enough to badly distort the mean.

*(Full explanation and code in the notebook itself.)*

---

## 🛠️ Tools Used

NumPy • Pandas • Jupyter Notebook

---

## 📚 Resources

- [GeeksforGeeks — Descriptive Statistics for Data Science](https://www.geeksforgeeks.org/data-science/descriptive-statistic/)
- [Khan Academy — Summarizing Quantitative Data](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 2 — Probability & Distributions** (`day2_probability_distributions.ipynb`)