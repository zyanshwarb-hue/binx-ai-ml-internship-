<div align="center">

# 🚢 Day 5 — The Titanic Story
### The Complete Pipeline: Pandas → NumPy → Matplotlib

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=plotly&logoColor=white)

*The capstone notebook of Week 1 — every tool, one dataset, one complete story.*

</div>

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Files](#-files)
- [The Pipeline](#-the-pipeline)
- [Visualizations](#-visualizations)
- [Key Insight](#-key-insight)
- [Tools](#-tools)

---

## 🎯 Overview

> This notebook answers one question: **what determined who survived the Titanic?**
> Using the full Week 1 toolkit — Pandas for cleaning, NumPy for computation, and
> Matplotlib for storytelling — raw passenger records become real, visual insight.

---

## 📂 Files

| File | Description |
|---|---|


<details>
<summary><b>🧹 Click to see the cleaning decisions</b></summary>

| Column | Missing % | Action | Reason |
|---|---|---|---|
| `Cabin` | 77% | Dropped column | Too much missing data to reliably impute |
| `Age` | 20% | Filled with mean | Manageable amount, preserves the data |
| `Embarked` | <1% | Dropped rows | Only 2 rows affected, safe to remove |

</details>

<details>
<summary><b>🔢 Click to see the NumPy computation</b></summary>

```python
survival_rate = np.mean(df["Survived"]) * 100
```
A single line that turns a column of 0s and 1s into one clear percentage —
the entire voyage's outcome, summarized in one number.

</details>

---

## 📊 Visualizations

| Chart | Question It Answers |
|---|---|
| 📈 **Histogram** | What did the age distribution of passengers look like? |
| 📊 **Bar Chart** | Did passenger class affect survival chances? |
| 🔵 **Scatter Plot** | Was there a relationship between age and ticket fare? |

---

## 💡 Key Insight

> **First-class passengers survived at noticeably higher rates than second and third class**
> — suggesting socioeconomic status played a real role in survival odds aboard the Titanic.
> Age and fare, on the other hand, showed no strong linear relationship, aside from a
> handful of high-fare outliers.

---

## 🧰 Tools

`Python` `Pandas` `NumPy` `Matplotlib` `Jupyter Notebook` `Git & GitHub`

---

<div align="center">

### 🏁 This notebook ties together every skill from Week 1
**Load → Clean → Compute → Visualize** — the same shape every future project in this program will follow.

**— Zayan**
*BinX Tech AI/ML Internship — Week 1, Day 5*

</div>
| `day5.ipynb` | Full analysis notebook |
| `train.csv` | Titanic passenger dataset (891 records) |

---

## 🔗 The Pipeline
