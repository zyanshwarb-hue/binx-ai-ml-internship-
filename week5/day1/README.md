# 🧠 Week 5 · Day 1 — K-Means Clustering

BinX Tech — AI & Machine Learning Internship Program Phase 2 · Week 5 of 10 · Day 1 of 5

---

## 🎯 Learning Objectives

- 🎯 Understand how K-Means groups unlabeled data into clusters.
- 📈 Use the Elbow Method to estimate the optimal number of clusters (k).
- 🥈 Use the Silhouette Score to numerically validate cluster quality.
- 🖼️ Visualize final clusters and interpret the cluster centers.

## 📘 Key Topics Covered

- How K-Means assigns points to clusters and updates centroids
- The Elbow Method: plotting inertia vs. k to find the "bend"
- The Silhouette Score: quantifying how well-separated clusters are
- Visualizing final clusters with centroids
- Interpreting cluster centers in terms of the original features

## 🛠️ What I Did

- Generated a synthetic dataset (`feature_1`, `feature_2`) and scaled it.
- Tried k values from 1 to 10 and computed inertia for each, then plotted the **Elbow Curve** — it bent sharply around k=3–4.
- Computed **Silhouette Scores** for candidate k values: k=3 → 0.7332, k=4 → 0.7780, and picked **k=4** as the best fit.
- Trained the final `KMeans` model with k=4 and visualized the clusters (scatter plot with centroids marked with red X's).
- Summarized cluster centers:
  - Cluster 0: upper-left region, moderate feature_1, high feature_2
  - Cluster 1: lower-left region, most isolated cluster
  - Cluster 2: only cluster with positive feature_1, right-center region
  - Cluster 3: farthest-left cluster, upper region
- Confirmed K-Means correctly recovered the 4 underlying groups the synthetic data was designed to have.

## ✅ Wrap-Up

K-Means with k=4 (chosen via the Elbow Method + confirmed by Silhouette Score) produced four clean, well-separated clusters, matching the synthetic dataset's true structure. On real-world data, `feature_1`/`feature_2` would represent actual measurable attributes (e.g., income and age), and this same table would reveal meaningful customer segments.
