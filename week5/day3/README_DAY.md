# Week 5 — Day 3: Dimensionality Reduction with PCA

**BinX Tech — AI & Machine Learning Internship Program**
**Topics:** The curse of dimensionality · Principal Component Analysis (PCA) · Explained variance · Choosing the number of components

## Objectives
- Explain the curse of dimensionality and why reduction helps.
- Apply PCA to reduce a dataset's dimensions.
- Interpret explained variance and choose how many components to keep.

## Dataset
Breast Cancer Wisconsin dataset (`sklearn.datasets.load_breast_cancer`) — same dataset used across Weeks 4–5 for consistency. 569 samples, 30 numeric features. The diagnosis label is used only for visualization coloring at the end — PCA itself is computed with no knowledge of it.

## What This Notebook Does
1. **Scaling** — `StandardScaler` applied before PCA, since PCA is variance-based and an unscaled large-range feature would dominate purely due to units.
2. **Full PCA fit** — all 30 components computed to study the cumulative explained-variance curve.
3. **Component selection** — the number of components needed to retain ≥95% of the total variance identified and justified.
4. **2D reduction & visualization** — data reduced to exactly 2 components and plotted as a scatter plot, colored by diagnosis for interpretability only.
5. **Reflection** — what was preserved and what was lost by reducing dimensionality, documented in Markdown.

## Key Result
| Metric | Value |
|---|---|
| Original features | 30 |
| Components needed for ≥95% variance | **10** |
| Variance retained with 10 components | 95.16% |
| Dimensionality reduction | ~67% fewer dimensions |
| Variance explained by PC1 alone | 44.27% |
| Variance explained by PC2 alone | 18.97% |
| Total variance in the 2D visualization | 63.24% |

**Finding:** even in just 2 principal components (63% of total variance), the malignant and benign cases separate fairly cleanly on the scatter plot — despite PCA never seeing the diagnosis label. This is strong evidence that the original 30 features carry real, coherent structure related to the diagnosis, not noise.

## How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook day3.ipynb
# Kernel -> Restart & Run All
```
Runs top to bottom with no manual steps.

## Tools Used
Scikit-learn (`PCA`, `StandardScaler`) · Pandas · Matplotlib · Seaborn · Jupyter Notebook
