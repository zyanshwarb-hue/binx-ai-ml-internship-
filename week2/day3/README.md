<div align="center">

# 🧮 Day 3 — Linear Algebra for ML

### BinX Tech · AI & Machine Learning Internship Program — Week 2

![Day](https://img.shields.io/badge/Day-3%20of%205-blue)
![Hours](https://img.shields.io/badge/Hours-8-informational)
![Topic](https://img.shields.io/badge/Topic-Linear%20Algebra-orange)

</div>

---

## 🧭 Overview

Every dataset in ML is a matrix. Every model's parameters are vectors or matrices. Training
is just a long sequence of matrix operations. Today isn't about proofs — it's about
recognizing the objects a model is built from, and understanding what it's *actually* doing
when it makes a prediction.

> 💡 You don't need to derive anything today. You need to be fluent enough to look at a
> line of model code and know exactly what shape everything is.

---

## 🎯 Learning Objectives

- 🧩 Represent data samples as **vectors** and datasets as **matrices**.
- ⚡ Compute a **dot product** and explain why it's central to model prediction.
- 🔗 Perform **matrix multiplication** and reason correctly about the resulting shapes.

---

## 📚 Key Topics

| # | Topic |
|---|---|
| 1 | Why linear algebra is the language of ML |
| 2 | Vectors — one sample's features |
| 3 | Matrices — a full dataset (samples × features) |
| 4 | The dot product and how models predict with it |
| 5 | Matrix multiplication and the shape-matching rule |

---

## 📖 Lesson Content

### 3.1 — Why Linear Algebra Is the Language of ML

Rows are samples. Columns are features. That's it — that's a dataset, and it's already a
matrix. A model's parameters are vectors or matrices too, and training is nothing more than
a sequence of matrix operations applied over and over. Understanding these objects *is*
understanding what a model does internally.

### 3.2 — Vectors 🎯

A vector is an ordered list of numbers — in ML, usually one data sample's features.

```python
import numpy as np
v = np.array([25, 50000, 3])   # a customer: age, income, tenure
```

### 3.3 — Matrices 🗂️

A matrix is a 2D grid — a full dataset, where each **row** is a sample and each **column**
is a feature. Shape = `(rows, columns)` = `(samples, features)`.

```python
X = np.array([[25, 50000, 3],
              [40, 80000, 10],
              [33, 62000, 5]])
print(X.shape)   # (3, 3): 3 samples, 3 features
```

### 3.4 — The Dot Product ⚡

The single most important operation in ML. Multiply two vectors element-by-element, sum the
result — that's a linear model's prediction, right there.

```python
features = np.array([25, 50000, 3])
weights  = np.array([0.1, 0.0002, 1.5])
prediction = np.dot(features, weights)   # 2.5 + 10 + 4.5 = 17.0
```

This is *exactly* how linear and logistic regression compute their output next week:
`prediction = dot(features, weights) + bias`.

### 3.5 — Matrix Multiplication 🔗

Apply the dot product across a whole matrix at once — predictions for every sample, in one
operation. The rule: an `(m × n)` matrix times an `(n × p)` matrix gives an `(m × p)` matrix.
**The inner dimensions must match** — this is why shape mismatches are the #1 bug in ML code.

```python
X = np.array([[25, 50000, 3], [40, 80000, 10]])   # (2, 3)
w = np.array([0.1, 0.0002, 1.5])                  # (3,)
predictions = X @ w                                # (2,): one prediction per sample
```

---

## 🧪 Hands-On Lab: Vectors, Matrices & Predictions

- [ ] **Step 1:** Represent three data samples as a `(3 × features)` NumPy matrix.
- [ ] **Step 2:** Compute the dot product of one sample vector with a weight vector by hand, then verify it with `np.dot`.
- [ ] **Step 3:** Use matrix multiplication (`@`) to produce a prediction for all three samples at once.
- [ ] **Step 4:** Deliberately create a shape-mismatch error, read the message, and explain in Markdown why it occurred and how to fix it.

---

## 🛠️ Tools Used

`NumPy` · `Jupyter Notebook`

---

## 📁 In This Folder

```text
day3/
├── README.md          📖 You are here
└── day3.ipynb          🧮 Vectors, matrices, dot products & matrix multiplication
```

---

<div align="center">

💥 **The takeaway:** if you understand `X @ w`, you understand what every linear model in
this internship is doing under the hood. 💥

</div>
