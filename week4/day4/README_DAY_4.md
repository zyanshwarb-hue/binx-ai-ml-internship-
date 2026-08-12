# Week 4 — Day 4: Feature Engineering & Hyperparameter Tuning

**BinX Tech — AI & Machine Learning Internship Program**
**Topics:** Feature engineering techniques · Hyperparameters vs. parameters · GridSearchCV · RandomizedSearchCV (concept)

## Objectives
- Engineer new features and apply appropriate transformations.
- Distinguish hyperparameters from learned parameters.
- Tune a model systematically with `GridSearchCV` and cross-validation.

## Dataset
Heart Failure Prediction Dataset (same dataset used across the internship track) — 918 patients, 11 clinical features, binary target `HeartDisease`. `heart.csv` is included in this folder for a fully standalone, reproducible run.

## What This Notebook Does
1. **Untuned Week 3 baseline** — plain Random Forest (default hyperparameters, raw features), evaluated with 5-fold cross-validation, as the point of comparison.
2. **Feature engineering** — two new features, each justified in Markdown:
   - `HR_Reserve_Ratio` = `MaxHR / (220 - Age)` — normalizes peak heart rate by the age-predicted maximum.
   - `High_Chol_Older_Patient` — binary flag for the compounded risk pattern of high cholesterol (>240) combined with older age (>50).
3. **Hyperparameter grid** defined for Random Forest (`n_estimators`, `max_depth`, `min_samples_leaf`) and tuned with `GridSearchCV` (5-fold CV, 36 combinations, 180 total model fits).
4. **Comparison** of all three stages (baseline → + features → + tuning) on the identical CV scheme.
5. **Documentation** of which change (features vs. tuning) actually mattered, backed by the numbers rather than assumed — including a feature-importance chart for the final tuned pipeline.

## Key Result
| Stage | CV F1 (mean ± std) |
|---|---|
| Week 3 baseline (default RF, no new features) | 0.867 ± 0.026 |
| + Engineered features (still default RF) | 0.862 ± 0.025 |
| + Engineered features + GridSearchCV tuning | **0.874** |

**Best hyperparameters found:** `max_depth=6`, `min_samples_leaf=4`, `n_estimators=100`

**Honest finding:** the engineered features alone did *not* improve the untuned Random Forest (a small dip, within one standard deviation) — Random Forest already captures Age×MaxHR-style interactions reasonably well on its own. The improvement over baseline came primarily from **hyperparameter tuning** (restricting tree depth / leaf size reduced overfitting on this ~900-row dataset). This distinction is documented explicitly in the notebook rather than glossed over.

## How to Run
```bash
pip install -r ../../requirements.txt   # or pandas, numpy, matplotlib, scikit-learn, jupyter
jupyter notebook day4.ipynb
# Kernel -> Restart & Run All
```
Runs top to bottom with no manual steps. Outputs two plots (`day4_comparison.png`, `day4_feature_importance.png`) saved in this folder.

## Tools Used
Scikit-learn (`GridSearchCV`, `RandomForestClassifier`, `ColumnTransformer`, `FunctionTransformer`) · Pandas · Matplotlib · Jupyter Notebook
