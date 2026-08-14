# 🫀 Cardiac Patient Monitoring System
### AI & Machine Learning Track — Individual Capstone Project (BinX Tech)

An end-to-end, curriculum-aligned machine-learning analysis of cardiac patient data: data cleaning, exploratory analysis, supervised classification (baseline + comparison model), rigorous evaluation with cross-validation, feature engineering inside a leak-free Scikit-learn `Pipeline` tuned with `GridSearchCV`, and an unsupervised analysis (KMeans + PCA).

> **Scope note:** This project is a machine-learning skills demonstration on public, de-identified data. It performs **no clinical diagnosis** and gives **no treatment recommendations** — strictly notebook/script based, no API, frontend, or deployment.

---

## 📊 Dataset

**Heart Failure Prediction Dataset** — [Kaggle, fedesoriano](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
918 patients · 11 clinical features · 1 binary target (`HeartDisease`)
Public, de-identified. See [`data/data_dictionary.md`](data/data_dictionary.md) for full column descriptions and known data-quality notes.

## 🎯 Objective

Build a complete, reproducible ML workflow that:
1. Cleans and explores the dataset (including hidden invalid values: zero-encoded missing `Cholesterol`/`RestingBP`).
2. Trains and fairly compares two supervised classifiers (Logistic Regression baseline vs. Random Forest).
3. Evaluates both with stratified 5-fold cross-validation, confusion matrices, precision/recall/F1/ROC-AUC.
4. Engineers domain-informed features and wraps the entire workflow in one leak-free `Pipeline`, tuned with `GridSearchCV`.
5. Adds an unsupervised layer (KMeans clustering + PCA) to explore patient groupings independent of the target label.

## 📁 Project Structure

```
cardiac_project/
├── data/
│   ├── heart.csv                  # raw dataset (public Kaggle source)
│   └── data_dictionary.md         # column descriptions + data-quality notes
├── notebooks/
│   └── cardiac_monitoring_analysis.ipynb   # full analysis, executed top-to-bottom
├── models/
│   └── tuned_cardiac_pipeline.joblib       # final saved, tuned Pipeline
├── outputs/
│   └── *.png                      # all generated plots (EDA, confusion matrices, ROC, PCA, etc.)
├── src/
│   └── (reserved for reusable helper functions if the analysis is extended)
├── requirements.txt
└── README.md
```

## ⚙️ Setup & Run Instructions

```bash
# 1. Create environment (Python 3.10+)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Jupyter and run the notebook top to bottom
jupyter notebook notebooks/cardiac_monitoring_analysis.ipynb
# In Jupyter: Kernel -> Restart & Run All
```

The notebook runs fully from top to bottom with no manual/hidden steps and re-generates every plot in `outputs/` and the saved pipeline in `models/`.

## 🧪 Methodology Summary

| Step | What was done |
|---|---|
| **Data Prep** | Zero-encoded missing values in `RestingBP`/`Cholesterol` identified and handled via median imputation *inside* the pipeline (no leakage). |
| **EDA** | Class balance, distributions by target, correlation heatmap, categorical breakdowns, outlier boxplots. |
| **Split discipline** | 60% train / 20% validation / 20% test — test set touched exactly once, at the very end. |
| **Baseline** | Logistic Regression (median-impute + scale + one-hot encode). |
| **Comparison model** | Random Forest, same split & evaluation approach. |
| **Evaluation** | Stratified 5-fold cross-validation (mean ± std F1), confusion matrices, precision/recall/F1, ROC-AUC. |
| **Feature engineering** | `HR_Reserve_Ratio` (MaxHR vs. age-predicted max) and `High_Chol_Older_Patient` (compounded risk flag). |
| **Pipeline & tuning** | Full `ColumnTransformer` + `Pipeline`, tuned end-to-end with `GridSearchCV` (5-fold CV) over Random Forest hyperparameters. |
| **Unsupervised** | KMeans (k chosen via elbow + silhouette score) and PCA (2D projection), compared against actual disease labels. |

## 📈 Final Results (held-out test set, evaluated once)

| Metric | Score |
|---|---|
| Accuracy | 0.848 |
| Precision | 0.849 |
| Recall | 0.882 |
| F1-score | 0.865 |
| ROC-AUC | 0.915 |

## ⚠️ Limitations

- Dataset size (918 rows) is modest — results may not generalize across hospitals, populations, or measurement equipment.
- No deep learning, cloud deployment, or clinical validation — intentionally out of scope per the project guide.
- `Cholesterol` imputation (median fill for ~19% of records) is a statistical simplification, not a clinical solution.
- Educational project only — **not** a diagnostic tool.

## ✅ Alignment with Project Guide

This project satisfies every item in the BinX Tech "Cardiac Patient Monitoring System" Individual Project Guide: reproducible environment, full data preparation, EDA & statistics, supervised baseline + comparison model, cross-validated evaluation with confusion matrix and metrics, feature engineering + leak-free Pipeline, unsupervised clustering/PCA with visualization and interpretation, and complete documentation.
