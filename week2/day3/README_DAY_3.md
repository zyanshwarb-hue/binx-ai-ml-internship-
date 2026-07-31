# 🧮 Day 3 — Linear Algebra for ML

**BinX Tech — AI & Machine Learning Internship Program**
**Week 2: Math Foundations & EDA | Phase 1 → 2 Transition**

![status](https://img.shields.io/badge/status-complete-brightgreen)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![libraries](https://img.shields.io/badge/libraries-NumPy%20%7C%20Matplotlib-orange)
![topic](https://img.shields.io/badge/topic-Vectors%20%7C%20Matrices%20%7C%20Dot%20Product-9146FF)

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 3 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day3.ipynb` |
| **Tools** | NumPy • Matplotlib • Jupyter Notebook |
| **Prerequisite** | Day 1 & Day 2 completed |

This day covers the mathematical language every ML model runs on internally — vectors, matrices,
the dot product, and matrix multiplication — building the bridge between raw data and how a model
actually computes a prediction.

---

## 🎯 Objectives

- Represent data samples as vectors and datasets as matrices.
- Compute a dot product and explain why it is central to model prediction.
- Perform matrix multiplication and reason about resulting shapes.

---

## 🧠 Approach

1. Represented a single data sample as a **vector**, and visualized a 2D vector geometrically as
   an arrow to build intuition for direction and magnitude.
2. Represented a full dataset as a **matrix**, and visualized it as a color-coded heatmap to see
   value patterns and scale differences across features at a glance.
3. Computed the **dot product** between a feature vector and a weight vector — the exact operation
   a linear model uses to produce a prediction.
4. Performed **matrix multiplication** to generate predictions for multiple samples in a single
   operation, then manually verified the result to confirm understanding of the underlying math.
5. Deliberately triggered a **shape-mismatch error** to understand exactly why it happens and how
   to read NumPy's error message.

---

## 📈 Key Findings

| Concept | What It Revealed |
|---|---|
| **Vector visualization** | Confirmed that a vector is geometrically a direction + magnitude, not just a list of numbers |
| **Matrix heatmap** | Made the scale difference between features (e.g. `income` vs. `age`) immediately visible |
| **Dot product** | Manually verified prediction matched NumPy's `np.dot()` result exactly |
| **Matrix multiplication** | Produced predictions for all samples in one operation — no loop needed |
| **Shape mismatch error** | Confirmed the rule: an `(m × n)` matrix can only multiply an `(n × p)` matrix — inner dimensions must match |

*(Full code, visualizations, and detailed interpretation are in the notebook itself.)*

---

## 🛠️ Tools Used

NumPy • Matplotlib • Jupyter Notebook

---

## 📚 Resources

| Resource | Type | Focus |
|---|---|---|
| [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) | Video Series | Visual, geometric intuition for vectors, matrices, and dot products |
| [Khan Academy — Vectors and Matrices](https://www.khanacademy.org/math/algebra-home/alg-matrices) | Course / Video | Core operations and rules |

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 4 — EDA Part 1: Distributions & Outliers**
