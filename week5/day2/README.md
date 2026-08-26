# 🧠 Week 5 · Day 2 — DBSCAN & Hierarchical Clustering

BinX Tech — AI & Machine Learning Internship Program Phase 2 · Week 5 of 10 · Day 2 of 5

---

## 🎯 Learning Objectives

- ⚠️ Understand K-Means's limitations and when to look elsewhere.
- 🌫️ Run DBSCAN and interpret clusters & noise points.
- 🌳 Build a hierarchical clustering dendrogram and choose a cut height.
- ⚖️ Compare all three methods (K-Means, DBSCAN, Hierarchical) and recommend the best fit.

## 📘 Key Topics Covered

- Why K-Means struggles on non-round, irregularly-shaped clusters
- DBSCAN: density-based clustering, the `eps` and `min_samples` parameters, and noise points (label = -1)
- Hierarchical clustering: building a dendrogram with Ward linkage and cutting it at a chosen height
- Side-by-side visual comparison of K-Means vs. DBSCAN vs. Hierarchical
- Matching a clustering method to the actual shape of the data

## 🛠️ What I Did

- Generated a demo dataset with irregular shapes and noise using `make_moons`, then scaled it with `StandardScaler`.
- Ran K-Means (k=2) on the moon-shaped data first, to see it fail — it split the shapes with a straight line since it assumes round, similarly-sized clusters.
- Ran **DBSCAN** (`eps=0.3`, `min_samples=5`), which found clusters automatically and flagged sparse points as noise.
- Built a **hierarchical clustering dendrogram** (Ward linkage), picked a cut height, and used `fcluster` to extract cluster labels at that height.
- Plotted all three methods side-by-side (K-Means / DBSCAN / Hierarchical) on the same data for direct comparison.
- Filled in the interpretation: which method captured the true shape of the data best, and why.

## ✅ Wrap-Up

- Saw K-Means's limitations on non-round data.
- Ran DBSCAN and identified clusters + noise points.
- Built and cut a hierarchical dendrogram.
- Compared all three methods side-by-side.
- **Key takeaway:** the right clustering method depends on the *shape* of the data — K-Means forces round clusters, DBSCAN auto-detects cluster count and flags outliers, and Hierarchical reveals nested structure with no `k` needed upfront.

**Up next:** PCA & Dimensionality Reduction.
