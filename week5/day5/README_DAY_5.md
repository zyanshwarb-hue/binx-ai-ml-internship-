# Week 5 — Day 5: Unsupervised Learning Mini-Project

**BinX Tech — AI & Machine Learning Internship Program**
**Topics:** K-Means · DBSCAN · Hierarchical Clustering · PCA · t-SNE · Anomaly Detection — all combined

## Objectives
This closing mini-project pulls together every unsupervised technique from Week 5 onto one dataset, in one coherent story — mirroring the Week 4 Day 5 tuned-pipeline mini-project structure.

## Dataset
Breast Cancer Wisconsin dataset (`sklearn.datasets.load_breast_cancer`) — same dataset used across Weeks 4–5. 569 samples, 30 numeric features. The diagnosis label is held aside and used **only in the final section**, to check how well the fully unsupervised pipeline aligns with ground truth.

## What This Notebook Does
1. **K-Means** — `k` chosen via elbow method + silhouette score (best k=2, silhouette=0.343), fit and cluster sizes reported.
2. **DBSCAN & Hierarchical Clustering** — both run on the same scaled data and compared against K-Means in a summary table, including an honest discussion of where DBSCAN struggled.
3. **PCA & t-SNE** — both computed and plotted side-by-side, colored by the K-Means clusters (not the true label), to visualize the discovered structure two different ways.
4. **Anomaly Detection** — Isolation Forest run, and its flagged points cross-checked against DBSCAN's noise points for overlap.
5. **Synthesis** — Adjusted Rand Index (ARI) computed between K-Means clusters and the true diagnosis label, plus a cluster-vs-diagnosis heatmap, as the single moment the label is used in the whole notebook.

## Key Results
| Technique | Result |
|---|---|
| K-Means best k | 2 (silhouette score = 0.343) |
| K-Means cluster sizes | 375 / 194 |
| DBSCAN | Found 1 dense cluster + 121 noise points (21.3%) — eps sensitivity, discussed honestly rather than hidden |
| Hierarchical clustering (cut at k=2) | 385 / 184 |
| Isolation Forest anomalies | 29 points (5.1%) |
| Overlap: Isolation Forest ∩ DBSCAN noise | 29 / 29 — every Isolation Forest anomaly was also flagged as DBSCAN noise |
| **Adjusted Rand Index (K-Means vs. true diagnosis)** | **0.654** |

**Headline finding:** K-Means clusters — built with **zero** access to the diagnosis label — still achieve an Adjusted Rand Index of 0.654 against the true malignant/benign diagnosis. This is strong evidence that the 30 clinical features carry real, medically meaningful structure that unsupervised learning can recover purely from feature geometry.

**Honest finding on DBSCAN:** with `eps=3.0`, DBSCAN collapsed the data into a single dense cluster plus a large noise band (21.3%) rather than cleanly separating two groups — a known DBSCAN limitation on data without clear density gaps, documented rather than hidden or silently re-tuned to look better.

## How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter
jupyter notebook day5.ipynb
# Kernel -> Restart & Run All
```
Runs top to bottom with no manual steps. t-SNE may take slightly longer to compute than the other steps — expected.

## Tools Used
Scikit-learn (`KMeans`, `DBSCAN`, `PCA`, `TSNE`, `IsolationForest`, `silhouette_score`, `adjusted_rand_score`) · SciPy (`linkage`, `dendrogram`, `fcluster`) · Pandas · Matplotlib · Seaborn · Jupyter Notebook
