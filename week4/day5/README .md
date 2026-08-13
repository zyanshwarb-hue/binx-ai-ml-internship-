# Week 4 — Day 5: Scikit-learn Pipelines & Tuned Mini-Project

**BinX Tech — AI & Machine Learning Internship Program**
**Phase 2, Week 4 (Evaluation, Tuning & Pipelines) — Day 5 Deliverable**

## Objective

Build a single, leak-free Scikit-learn `Pipeline` that combines preprocessing and modeling, tune it
end-to-end with `GridSearchCV` and 5-fold cross-validation, and evaluate the final tuned pipeline
once on a held-out test set. This closes out Week 4 and mirrors the exact structure required for the
Phase 3 capstone project.

## What's in this notebook

1. **Baseline reproduction** — the untuned baseline model from earlier in the week is re-run for a
   fair before/after comparison.
2. **Full preprocessing Pipeline** — a `ColumnTransformer` that:
   - scales the numeric columns (`StandardScaler`)
   - one-hot encodes the categorical columns (`OneHotEncoder`), including the newly engineered
     `tumor_size_category` column (a genuine binned categorical feature, not just numeric)
3. **Feature engineering** — the features engineered on Day 4 are carried into this pipeline, plus
   the new `tumor_size_category` binned feature added to exercise the `ColumnTransformer`'s mixed
   numeric/categorical handling.
4. **Hyperparameter tuning** — `GridSearchCV` (5-fold cross-validation) tunes the full pipeline
   end-to-end (preprocessing + model together), using `step__param` syntax so no leakage is possible
   at any stage.
5. **Final evaluation** — the tuned pipeline is evaluated **once** on the held-out test set, after all
   tuning decisions were finalized using cross-validation only, and compared against the baseline.
6. **Reflection** — written answers on why in-pipeline feature engineering prevents leakage, what the
   added categorical feature actually demonstrated, and what it means when different modeling efforts
   converge on a similar F1 ceiling.
7. **Saved artifact** — the final tuned pipeline is persisted as a reusable model file so it can be
   reloaded and applied to new raw data directly (`model.predict(new_dataframe)`).

## Results

| Model | Test F1 |
|---|---|
| Baseline (Day 1) | 0.9583 |
| Tuned pipeline (Day 4) | 0.9583 |
| Tuned pipeline (Day 5, + engineered categorical feature) | 0.9583 |

All three converge on roughly the same F1 ceiling — see the Reflection section in the notebook for
interpretation (the dataset's available signal appears close to fully captured even by the simpler
baseline; further gains would likely require new data or features rather than more tuning).

## How to run

1. Clone this repository and `cd` into this folder.
2. Create the environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch Jupyter and open the notebook:
   ```bash
   jupyter notebook day5_tuned_pipeline.ipynb
   ```
4. Run all cells top to bottom (`Kernel → Restart & Run All`). No manual or hidden steps are
   required — the notebook loads the dataset, builds the pipeline, tunes it, and evaluates it fully
   on its own.

## Project structure

```
.
├── README.md
├── requirements.txt
├── day5_tuned_pipeline.ipynb
├── data/
│   └── (dataset used for this lab)
└── models/
    └── tuned_pipeline.joblib   # saved final pipeline artifact
```

## Limitations

- This is an internship training exercise, not a production or clinical tool.
- The final test-set score was checked exactly once, after tuning was complete, per the Week 4
  evaluation-rigor rule (test set never touched during tuning).
- Because baseline, Day 4, and Day 5 scores converge, this pipeline's remaining headroom is likely
  limited by the dataset itself rather than by further hyperparameter search.

## Tools used

Python 3, Pandas, Scikit-learn (`Pipeline`, `ColumnTransformer`, `GridSearchCV`, `StratifiedKFold`),
Matplotlib, Jupyter Notebook, Git & GitHub.
