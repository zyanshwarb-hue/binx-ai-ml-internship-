# 📈 Day 2 — Linear Regression

**BinX Tech — AI & Machine Learning Internship Program**
**Week 3: Supervised Learning | Phase 2 — Core ML Training**

![status](https://img.shields.io/badge/status-complete-brightgreen)
![phase](https://img.shields.io/badge/phase-2%20%7C%20Core%20ML%20Training-9146FF)
![dataset](https://img.shields.io/badge/dataset-Diamonds-red)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![libraries](https://img.shields.io/badge/libraries-Scikit--learn%20%7C%20Pandas%20%7C%20Matplotlib-orange)
![R²](https://img.shields.io/badge/R²-0.859-success)

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 2 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day2.ipynb` |
| **Dataset** | Diamonds — same features/split as Day 1 |
| **Model** | `sklearn.linear_model.LinearRegression` |

The first real predictive model of the internship — trained, evaluated, and interpreted against
a baseline, using the exact train/test split established in Day 1.

---

## 🎯 Objectives

- Train a linear regression model and generate predictions.
- Interpret the model's coefficients and intercept.
- Evaluate a regression model with MAE, RMSE, and R² against a baseline.

---

## 🧠 Approach

1. Reused the Day 1 features/target split (`random_state=42`) for direct comparability.
2. Trained a `LinearRegression` model on the training set and generated predictions on the test set.
3. Interpreted every feature's coefficient, including diagnosing a multicollinearity effect
   between `carat`, `x`, `y`, and `z`.
4. Computed MAE, RMSE, and R² on the test set.
5. Compared the model's error against a naive baseline (always predicting the mean price).
6. Visualized predicted vs. actual prices to spot where the model struggles most.

---

## 📈 Key Results

| Metric | Baseline (predict mean) | Linear Regression |
|---|---|---|
| **MAE** | ≈ \$3,021 | **≈ \$888** |
| **RMSE** | ≈ \$3,987 | **≈ \$1,497** |
| **R²** | 0 | **≈ 0.859 (86%)** |

**→ The model cut average prediction error by roughly 70% compared to the baseline** — clear
proof it learned genuine, useful patterns rather than noise.

---

## 🔍 Notable Insight: Multicollinearity

`carat` was by far the strongest positive price driver (**coefficient ≈ +10,683**), exactly as
expected physically. However, `x` (one of the physical dimensions) showed a **negative**
coefficient (≈ -1,287) despite larger diamonds generally costing more — a textbook symptom of
**multicollinearity**, since `carat`, `x`, `y`, and `z` are all highly correlated measures of the
same underlying "size." This is a deliberately advanced finding included to demonstrate that
individual linear regression coefficients can be misleading when features overlap.

---

## 📉 Where the Model Struggles

The predicted-vs-actual scatter plot showed tight clustering around the perfect-prediction line
for low and mid-range prices, but a widening spread for diamonds priced above ~\$10,000 —
consistent with the right-skewed, outlier-heavy price distribution first identified back in
Week 2's EDA.

*(Full code, visualizations, and detailed interpretation are in the notebook itself.)*

---

## 🛠️ Tools Used

Scikit-learn (LinearRegression) • Pandas • Matplotlib • Jupyter Notebook

---

## 📚 Resources

| Resource | Type | Focus |
|---|---|---|
| [Linear Regression (Video)](https://www.youtube.com/watch?v=xLdvMG5qAmo) | Video | Core concepts covered today |
| [Scikit-learn — LinearRegression Docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) | Docs | Official API reference |

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 3 — Logistic Regression & Classification Metrics**
