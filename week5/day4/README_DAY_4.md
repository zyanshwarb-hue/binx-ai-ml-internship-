# Week 5 — Day 4: t-SNE & Anomaly Detection

**BinX Tech — AI & Machine Learning Internship Program**
**Topics:** t-SNE for local-structure visualization · PCA vs. t-SNE · Anomaly detection · Isolation Forest

## Objectives
- Use t-SNE to visualize high-dimensional data and distinguish it from PCA.
- Explain what anomaly detection is and why it is often unsupervised.
- Detect anomalies with Isolation Forest and interpret the flagged points.

## Dataset
Breast Cancer Wisconsin dataset (`sklearn.datasets.load_breast_cancer`) — same dataset used across Weeks 4–5. 569 samples, 30 numeric features (scaled). The diagnosis label is used only for visualization coloring, since this is a standalone notebook and no Day 1–2 cluster assignments are available to reuse.

## What This Notebook Does
1. **t-SNE projection** — the 30-dimensional dataset reduced to 2D using t-SNE (`perplexity=30`), which preserves local neighborhoods rather than global variance.
2. **Direct PCA vs. t-SNE comparison** — the Day 3 PCA 2D projection rebuilt side-by-side with today's t-SNE projection, to make the "global variance vs. local neighborhoods" distinction visible rather than just described.
3. **Anomaly detection** — `IsolationForest` (`contamination=0.05`) run on the scaled data; anomalies visualized directly on the t-SNE plot.
4. **Point-level inspection** — two flagged anomalies pulled out and compared feature-by-feature against the dataset mean (in standard deviations) to hypothesize why they were isolated so easily.
5. **Reflection** — differences between PCA and t-SNE, why t-SNE output isn't reused as model input, and whether the flagged anomalies make sense.

## Key Result
| Metric | Value |
|---|---|
| Contamination parameter | 0.05 (expected ~5%) |
| Points flagged as anomalies | **29 out of 569 (5.1%)** |
| t-SNE perplexity | 30 |

**Finding:** the t-SNE projection pulls the two diagnosis groups into tighter, more visually separated clusters than the Day 3 PCA projection — consistent with t-SNE's design goal of preserving local neighborhoods rather than global variance. The 5.1% anomaly rate closely matches the expected 5% contamination setting, and the flagged points show several features sitting multiple standard deviations from the dataset mean simultaneously — exactly the pattern Isolation Forest is designed to catch quickly.

## How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook day4.ipynb
# Kernel -> Restart & Run All
```
Runs top to bottom with no manual steps. Note: t-SNE can take a little longer to run than PCA — this is expected and mentioned explicitly in the Week 5 curriculum (t-SNE is slower on larger datasets).

## Tools Used
Scikit-learn (`TSNE`, `IsolationForest`, `PCA`, `StandardScaler`) · Pandas · Matplotlib · Seaborn · Jupyter Notebook
