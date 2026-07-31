<div align="center">

# 📊 Week 2 — Math Foundations & EDA

### BinX Tech · AI & Machine Learning Internship Program

**Statistics · Probability · Linear Algebra · Exploratory Data Analysis**

![Phase](https://img.shields.io/badge/Phase-1%20→%202-blue)
![Hours](https://img.shields.io/badge/Hours-40-informational)
![Days](https://img.shields.io/badge/Training%20Days-5-success)
![Track](https://img.shields.io/badge/Track-Hands--On-orange)

</div>

---

## 🧭 Overview

Week 2 is the bridge between **Phase 1** and **Phase 2** of the internship. It covers the
mathematical foundations every ML model rests on — descriptive statistics, probability,
and linear algebra — and immediately puts them to work in a full **Exploratory Data
Analysis (EDA)** on a real dataset using Seaborn and correlation analysis.

| | |
|---|---|
| 🗓️ **Week** | 2 of 10 — Phase 1 → Phase 2 transition |
| ⏱️ **Total Hours** | 40 hrs (full-time) / 20 hrs (part-time, combined with Week 3–4) |
| 💻 **Format** | On-site / Remote / Hybrid — all work in Jupyter notebooks, committed to GitHub |
| 🧩 **Prerequisite** | Week 1 completed — Python, NumPy, Pandas, Matplotlib fluency |
| 🧑‍🏫 **Mentor Supervision** | Daily check-in; the **Day 5 EDA notebook** is the first graded mini-deliverable |

---

## 🎯 Learning Objectives

By the end of this week, you should be able to:

- 🔢 Compute and interpret descriptive statistics (mean, median, mode, variance, std. dev.) and know when to use each.
- 🎲 Apply core probability concepts — including conditional probability and Bayes' theorem.
- 🧮 Explain the linear-algebra objects ML runs on: vectors, matrices, dot products, matrix multiplication.
- 🔗 Connect these math foundations to how ML models represent data and make predictions.
- 🔍 Perform a complete EDA: univariate and bivariate analysis, correlation, and outlier detection.
- 📝 Communicate findings clearly through Seaborn visualizations and a written data-storytelling summary.

---

## 🗓️ Daily Schedule

| Day | Folder | Hours | Focus |
|---|---|---|---|
| **1** | [`day1/`](./day1) | 8 hrs | 📐 Descriptive statistics — central tendency, spread, and what they mean *(+ bonus practice notebook)* |
| **2** | [`day2/`](./day2) | 8 hrs | 🎲 Probability fundamentals — rules, conditional probability, Bayes' theorem, distributions |
| **3** | [`day3/`](./day3) | 8 hrs | 🧮 Linear algebra for ML — vectors, matrices, dot products, matrix multiplication |
| **4** | [`day4/`](./day4) | 8 hrs | 📊 EDA Part 1 — univariate analysis, distributions, outlier detection (Seaborn) |
| **5** | [`day5/`](./day5) | 8 hrs | 🔥 EDA Part 2 — bivariate analysis, correlation, data storytelling, full EDA notebook |

---

## 📦 Repository Structure

```text
week2/
├── day1/                              📐 Descriptive statistics
│   ├── README_DAY_1.md
│   ├── day1.ipynb                     — core lesson notebook
│   └── day1_extra_practice_diamonds.ipynb   — bonus practice notebook
├── day2/                              🎲 Probability & distributions
│   ├── README_DAY_2.md
│   └── day2.ipynb
├── day3/                              🧮 Linear algebra for ML
│   ├── README.md
│   └── day3.ipynb
├── day4/                              📊 EDA Part 1 — distributions & outliers
│   ├── README_DAY_4.md
│   └── day4.ipynb
├── day5/                              🔥 EDA Part 2 — correlation & storytelling
│   ├── README.md
│   └── Week2_Day5_EDA_Notebook.ipynb
├── eda-project/                       🏆 Final Week 2 project — its own folder
│   └── EDA_Correlation_Analysis.ipynb
├── requirements.txt                   📋 Python dependencies
└── README.md                          📖 You are here
```

`day1/` is the only folder with a bonus notebook — `day1_extra_practice_diamonds.ipynb` is
extra practice beyond the core lesson, not a required deliverable.

Each `dayN/` folder is that day's **lesson + hands-on lab notebook** — practice work for that
specific topic. `eda-project/` is separate on purpose: it's the **milestone deliverable**, a
polished, standalone notebook your mentor grades — kept out of the daily folders so it reads
as a finished project, not just another day's exercise (the same pattern `week1/cve-project/`
already uses).

---

## 🏆 Week 2 Project

**[`eda-project/EDA_Correlation_Analysis.ipynb`](./eda-project/EDA_Correlation_Analysis.ipynb)**
is the capstone deliverable for the week, kept in its own folder so it stands on its own as a
finished project — a complete, narrated EDA notebook that ties every day together:

- 📈 Bivariate analysis (scatter plots, grouped box plots)
- 🔥 Correlation matrix & heatmap
- 🕸️ Pairplot across all numeric features
- 📝 A written data-storytelling narrative
- ✅ Key insights and next steps for modeling in Week 3

This notebook is the template for the EDA stage of **every** future project, through to the
Phase 3 capstone.

---

## ✅ Week 2 Deliverables

By the end of Week 2, every intern must submit the following to their mentor and GitHub repo:

- [X] A **descriptive-statistics** notebook — central tendency & spread on a real dataset
- [X] A **probability** notebook — coin-flip simulations, a normal distribution, a conditional-probability check
- [X] A **linear-algebra** notebook — vectors, matrices, dot product, matrix multiplication for prediction
- [X] A **univariate EDA** notebook — distributions, box plots, documented outlier handling
- [X] The **complete Week 2 EDA notebook** (statistics + univariate + bivariate + correlation) with a data-storytelling narrative
- [X] All notebooks **committed to GitHub** with clear, descriptive commit messages

---

## 📏 Evaluation Criteria

Scored by the assigned mentor at the end of Week 2, from the program's 100-point rubric:

| Criterion | 50–69 Developing | 70–84 Proficient | 85–100 Excellent |
|---|---|---|---|
| **Understanding of math concepts** | Recalls definitions, unclear on application | Explains most concepts, links to ML | Deep understanding, connects math to model behavior fluently |
| **Statistical & probability correctness** | Some calculations/interpretations off | Correct calculations, sound interpretation | Rigorous; chooses the right measure with clear justification |
| **EDA thoroughness** | Basic plots, shallow analysis | Thorough univariate + bivariate EDA, clear insights | Comprehensive, insight-driven, catches subtle data issues |
| **Visualization & data storytelling** | Unlabeled or unclear plots | Clear, labeled plots with a written narrative | Compelling narrative that drives modeling decisions |
| **Notebook quality & Git workflow** | Sporadic commits, weak documentation | Regular commits, clear Markdown narrative | Consistent, descriptive, well-organized, reproducible |
| **Attendance & punctuality** | 3–6 absences | 1–2 absences, on time | Perfect attendance, proactive |

---

## 🛠️ Technical Stack

| Category | Tools |
|---|---|
| **Numerical & Stats** | NumPy (statistics, random sampling, linear algebra) |
| **Tabular Data** | Pandas (`describe`, `corr`, `quantile`) |
| **Visualization** | Matplotlib, Seaborn (`histplot`, `boxplot`, `heatmap`, `pairplot`) |
| **Environment** | Python 3.10+, Jupyter Notebook, Git & GitHub |
| **Datasets** | Real tabular datasets (e.g. Titanic, Ames Housing, or a provided CSV) |

---

## 📚 Resources

| # | Resource | Link |
|---|---|---|
| 1 | Statistics | [YouTube video](https://www.youtube.com/watch?v=ZVGutgqBMUM) |
| 2 | Descriptive statistics | [YouTube video](https://www.youtube.com/watch?v=YrtFtdTTfv0) |
| 3 | EDA | [YouTube video](https://www.youtube.com/watch?v=Liv6eeb1VfE) |
| 4 | Linear Algebra | [Linear Algebra for Machine Learning](https://www.youtube.com/watch?v=rAI4ITRMkTY&list=PLTsu3dft3CWhLHbHTTzvG3Vx8XDWemG17) |
| 5 | Learn EDA in Python | [YouTube playlist](https://youtube.com/playlist?list=PLe9UEU4oeAuV7RtCbL76hca5ELO_IELk4&si=CuMAECzedGhExSjP) |

---

## 💡 Notes & Best Practices

> The math this week is taught **for use, not for its own sake** — every concept ties directly
> to how ML models represent data and predict. The **Day 5 EDA notebook** is the centerpiece of
> the week: invest in making its *narrative* clear, not just its charts correct. An outlier is a
> question, not a verdict — and correlation is never causation. 🎯

---

<div align="center">

**Prepared by BinX Tech** · Palestine | Nablus 🇵🇸

</div>
