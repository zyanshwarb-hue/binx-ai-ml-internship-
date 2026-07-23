<div align="center">

# 🐼 Day 4 — Pandas & Real-World Data
### Load · Clean · Filter · Aggregate

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Pandas](https://img.shields.io/badge/library-Pandas-150458)

</div>

---

## 📂 Contents

| File | Description |
|---|---|
| `day4.ipynb` | Titanic dataset: loading, cleaning, filtering, and grouping |
| `train.csv` | Raw Titanic passenger dataset |

---

## 🔍 What I Practiced

1. **Load & Inspect** — Loaded the Titanic dataset and examined shape, columns, and data types
2. **Clean** — Handled missing values with a documented strategy per column
3. **Filter** — Explored subsets of passengers by condition (e.g., age, class)
4. **Aggregate** — Used `groupby` to summarize data by category

## 🧹 Cleaning Decisions

| Column | Missing % | Action | Reason |
|---|---|---|---|
| `Cabin` | 77% | Dropped column | Too much missing data to reliably impute |
| `Age` | 20% | Filled with mean | Manageable amount, preserves the data |
| `Embarked` | <1% | Dropped rows | Only 2 rows affected, safe to remove |

---

## 🧰 Tools

`Pandas` `Jupyter Notebook`

---

<div align="center">

**— Zayan**  
*BinX Tech AI/ML Internship — Week 1, Day 4*

</div>
