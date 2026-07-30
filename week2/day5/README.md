## 📊 Week 2 — Day 5: EDA Part 2 — Correlation & Data Storytelling

**BinX Tech — AI & Machine Learning Internship Program**

`status: in-progress` `python: 3.10+` `libraries: Seaborn | Pandas | Matplotlib`

---

| | |
|---|---|
| **Day** | Day 5 of 5 |
| **Duration** | 8 hours |
| **Tools** | Seaborn • Pandas • Matplotlib • Jupyter Notebook • Git & GitHub |
| **Dataset** | Simulated customer dataset (age, income, tenure, spend, satisfaction, plan, churn) |

---

### 🎯 Learning Objectives

- Perform bivariate analysis with scatter plots and grouped box plots.
- Compute and interpret a correlation matrix and heatmap.
- Assemble a complete, narrated EDA notebook on a real dataset.

---

### 🧭 Key Topics

- Bivariate analysis: scatter plots, grouped box plots
- Correlation and the correlation heatmap
- Correlation is not causation
- The pairplot for scanning relationships
- Data storytelling: turning analysis into a narrative

---

### 🔧 Step 0 — Environment Setup

```bash
pip install pandas numpy seaborn matplotlib jupyter
```

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="deep")
```

---

### 📥 Step 1 — Load the Dataset

Simulated a realistic customer table with built-in relationships (older/higher-income
customers spend more; longer tenure and higher satisfaction reduce churn) so the EDA has
genuine patterns to uncover. Swap this cell for `pd.read_csv("your_file.csv")` on a real file.

---

### 📐 Step 2 — Descriptive Statistics Recap

Quick recap of central tendency and spread for every numeric column — the vocabulary the rest
of the notebook builds on.

---

### 📊 Step 3 — Univariate Recap

Histograms + count plot to check each variable's shape, skew, and class balance before moving
to relationships between variables.

---

### 🚨 Step 4 — Outlier Detection (IQR Method)

Box plots + the IQR rule flag potential outliers in `income` and `monthly_spend`. An outlier is
a question, not a verdict — investigated, not silently deleted.

---

### 🔀 Step 5 — Bivariate Analysis

- Scatter plot: `age` vs. `income`, colored by `churn`
- Grouped box plot: `monthly_spend` across `plan` tiers

---

### 🌡️ Step 6 — Correlation Matrix & Heatmap

Annotated heatmap summarizing every numeric pair's linear relationship at once — the single
most information-dense chart in the notebook.

---

### 🕸️ Step 7 — Pairplot

`sns.pairplot()` across all numeric features, colored by `churn`, to scan every relationship in
one grid.

---

### 📖 Step 8 — Data Storytelling

Written narrative tying every chart back to a modeling implication: which features matter for
churn, which for spend, and what to watch out for (skew, outliers, multicollinearity) before
Week 3.

---

### ✅ Deliverable

`Week2_Day5_EDA_Notebook.ipynb` — the complete Week 2 EDA notebook (statistics + univariate +
outliers + bivariate + correlation), committed with a clear message.

---

### 🛠️ Tools Used

Seaborn • Pandas • Matplotlib • Jupyter Notebook • Git & GitHub
