# 🧪 Week 4 · Day 1 — Train / Validation / Test Splits

**BinX Tech — AI & Machine Learning Internship Program**
**Phase 2 · Week 4 of 10 · Day 1 of 5**

---

## 🎯 Learning Objectives

- 🧠 Explain why a validation set is needed in addition to a test set.
- ✂️ Create a correct three-way split in Scikit-learn.
- 🚫 Explain why tuning against the test set produces misleading results.

## 📚 Key Topics Covered

- The problem with tuning against a single test set
- The three-way split: train, validation, test
- Creating a three-way split in code with `train_test_split`
- Why one validation set can still mislead (motivating cross-validation on Day 2)

## 🛠️ What I Did

- Loaded the Scikit-learn Breast Cancer dataset (569 samples, 30 features) and checked the class balance (357 benign / 212 malignant).
- Built a **60/20/20 train/validation/test split** using two calls to `train_test_split` with a fixed `random_state=42` and `stratify` to keep class proportions balanced across all three sets.
- Trained a `RandomForestClassifier` and tuned `max_depth` (`3, 5, 10, None`) by checking scores on the **validation set only** — the test set stayed untouched.
- Selected the best `max_depth` based on validation F1, retrained on the training set, and evaluated the **final model on the test set exactly once**.
- Added visualizations: class distribution (bar + pie), split composition chart, validation F1 comparison across `max_depth` values, and a confusion matrix for the final test result.
- Wrote a Markdown reflection on why tuning against the test set would produce a misleading, overly optimistic score.

## 📊 Results

| Metric | Value |
|---|---|
| Best `max_depth` (chosen on validation set) | 3 |
| Test F1 score | 0.9583 |
| Test accuracy | 0.9474 |

## ✅ Deliverable Checklist

- [x] 60/20/20 split created with a fixed `random_state`
- [x] One hyperparameter tuned using the validation set only
- [x] Test set evaluated exactly once, at the end
- [x] Markdown reflection written
- [x] Notebook committed to GitHub with a clear commit message

## 🧰 Tools Used

Scikit-learn (`train_test_split`) · Pandas · Matplotlib · Seaborn · Jupyter Notebook

---
📁 Files in this folder: `day1.ipynb`, `README_DAY_1.md`
