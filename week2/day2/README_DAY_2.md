# 🎲 Day 2 — Probability & Distributions

**BinX Tech — AI & Machine Learning Internship Program**
**Week 2: Math Foundations & EDA | Phase 1 → 2 Transition**

---

## 📌 Overview

| | |
|---|---|
| **Day** | Day 2 of 5 |
| **Duration** | 8 hours |
| **Notebook** | `day2.ipynb` |
| **Tools** | NumPy • Matplotlib • Jupyter Notebook |

This day covers the mathematical language of uncertainty — probability rules, conditional
probability, Bayes' Theorem, and the distributions that ML models rely on to represent and reason
about data.

---

## 🎯 Objectives

- Apply the complement, addition, and multiplication rules of probability.
- Explain conditional probability and Bayes' Theorem, and where they appear in ML.
- Recognize the normal, binomial, and uniform distributions.

---

## 🧠 Approach

1. Simulated 10,000 coin flips with NumPy to confirm the theoretical probability (0.5) emerges
   from a large number of trials.
2. Worked through a conditional probability example (die roll) both theoretically and by
   simulation, to verify P(A | B) calculations.
3. Applied Bayes' Theorem to a realistic medical test scenario, showing how a low prior
   probability dramatically affects the interpretation of a positive test result.
4. Sampled from normal and binomial distributions and visualized both to confirm their expected
   shapes.
5. Documented every result with plain-language interpretation connecting the math to real-world
   meaning.

---

## 📈 Key Findings

- The simulated coin-flip proportion converged almost exactly to the theoretical 0.5.
- Bayes' Theorem revealed that even a 95%-accurate medical test yields only a ~16% true
  probability of disease when the prior (1% disease rate) is factored in — highlighting why the
  prior matters as much as test accuracy.
- Normal and binomial simulations matched their theoretical shapes closely at scale (10,000
  samples/experiments).

*(Full explanation and code in the notebook itself.)*

---

## 🛠️ Tools Used

NumPy • Matplotlib • Jupyter Notebook

---

## 📚 Resources

- [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability/probability-library)
- [University of Illinois — Bayes' Theorem for Data Science](https://discovery.cs.illinois.edu/learn/Prediction-and-Probability/Bayes-Theorem/)

---

## ✍️ Author

**Zayan Shawareb**
BinX Tech — AI & Machine Learning Internship Program

---

## 🔗 Next

Proceed to **Day 3 — Linear Algebra for ML**
