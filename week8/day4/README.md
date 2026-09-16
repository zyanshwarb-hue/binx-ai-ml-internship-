<p align="center">
  <img src="https://img.shields.io/badge/BINX%20TECH-AI%20%26%20ML%20INTERNSHIP-061A33?style=for-the-badge" alt="BinX Tech"/>
</p>

<h1 align="center">⚙️ Week 8 · Day 4</h1>
<h3 align="center">Model Integration &amp; Error Analysis</h3>

<p align="center">
  <img src="https://img.shields.io/badge/SPRINT-3-0B2E59?style=for-the-badge" alt="Sprint 3"/>
  <img src="https://img.shields.io/badge/DAY-4%20OF%205-00A6C0?style=for-the-badge" alt="Day 4 of 5"/>
  <img src="https://img.shields.io/badge/DURATION-8%20HOURS-FFC857?style=for-the-badge&logoColor=black" alt="8 hours"/>
  <img src="https://img.shields.io/badge/TOPIC-MODEL%20INTEGRATION-1BAF7A?style=for-the-badge" alt="Model Integration"/>
  <img src="https://img.shields.io/badge/THREAD-CARDIAC%20MONITORING-8B5CF6?style=for-the-badge" alt="Cardiac Monitoring Thread"/>
</p>

<p align="center"><i>"A model in five separate notebook cells is a demo. A model behind one predict() function is a system."</i></p>

---

## 📖 The Story So Far

Day 3 closed with a working image pipeline for the capstone's own clinical modality — 12-lead ECG scans — but
Sprint 3's real goal was never "practice four separate skills." It was to turn the Cardiac Monitoring project into
something a stranger could trust. Day 4 comes home: back to the real `heart.csv` capstone model, and the work of
turning scattered notebook cells into **one callable, trustworthy object**.

## 🎯 Learning Objectives

| | Objective |
|---|---|
| 🧩 | Integrate preprocessing and the model into one end-to-end `predict()` pipeline |
| 🛡️ | Guarantee training/serving consistency — and demonstrate what breaks when it isn't guaranteed |
| 🔍 | Perform real error analysis: confusion matrix, then read the actual misclassified patients |

## 🔬 What Actually Happens in the Notebook

1. **Rebuild** the exact capstone pipeline — `heart.csv`, 918 patients, the same `random_state=42` split and
   Logistic Regression baseline every prior sprint has used.
2. **Wrap it** in a single `predict(raw_input)` function that takes a plain Python dict — the shape a real API
   caller would send — and verify its output matches the model's own prediction on that row exactly.
3. **Reproduce a real training/serving skew bug**: refit a `StandardScaler` on a single incoming row instead of
   reusing the fitted transformer, and show it silently zeroes out every feature.
4. **Run a confusion matrix** and identify the dominant error type.
5. **Read three real misclassified patients** individually and categorize each as a model weakness or a data
   issue — not just count them.

## 🛡️ The Golden Rule: `transform()`, Never `fit_transform()`

| | What it does | Safe at serving time? |
|---|---|---|
| `preprocessor.transform(new_row)` | Reuses the means/std/categories learned during training | ✅ Yes — this is the only correct choice |
| `StandardScaler().fit_transform(new_row)` | Fits a *brand-new* scaler on just that one row | 🚫 No — a single row always scales to exactly 0, erasing every feature |

> [!WARNING]
> **Sprint 3's fourth real bug**, in the same family as Day 1's dropped `"not"` and Day 3's BGR/RGB swap: this one
> doesn't crash and doesn't warn — it just quietly erases every feature's signal. Verified directly in the notebook
> on this capstone's own data, not asserted as a warning in a comment.

## 🔍 Error Analysis — Three Real Misclassified Patients

| # | Patient | Read | Category |
|---|---|---|---|
| 1 | 58, M, `ExerciseAngina=N`, `ST_Slope=Up` — actual **Disease**, predicted **No Disease** (prob. 0.14) | Confidently wrong: presents with exactly the pattern (`ST_Slope=Up`) the model trusts most as low-risk, yet has disease | **Model weakness** — over-reliance on one dominant feature |
| 2 | 49, **F**, `ExerciseAngina=N`, `ST_Slope=Flat` — actual **Disease**, predicted **No Disease** (prob. 0.246) | Also confidently wrong, and female in a cohort that skews male | **Data / representation issue** — likely less signal for this pattern in women |
| 3 | 44, M, `ChestPainType=ATA` — actual **No Disease**, predicted **Disease** (prob. 0.54) | Right at the decision boundary | **Genuinely borderline** — the honest kind of error |

> [!NOTE]
> This qualitative read is what separates a real evaluation from a checklist exercise: the confusion matrix says
> *how often* the model is wrong; reading the actual patients says *why*, and whether the fix is better data or a
> genuine model limitation.

## 📝 Documented Decision: what Day 4 changes

- The capstone is no longer "run these five cells in order" — it is one `predict()` function, verified to match
  training exactly on a raw, unprocessed input.
- The training/serving skew bug demonstrated here is the exact reason Sprint 4 will save `model.joblib` and
  `preprocessor.joblib` **as a matched pair**, never re-implementing the scaling logic by hand in the serving code.
- Two of three misclassified examples here point at the model's heavy reliance on `ST_Slope` — a thread picked back
  up in Day 5's SHAP global feature-importance section, which independently ranks it #1.

## 🧰 Tools Used

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0B2E59?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-0B2E59?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-0B2E59?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-0B2E59?style=flat-square)
![Git](https://img.shields.io/badge/Git%20%26%20GitHub-0B2E59?style=flat-square)

## 📓 The Notebook

**[→ Open day4.ipynb](./day4.ipynb)** for the full, executed walkthrough — code and real output, generated live on
the real 918-patient capstone dataset.

---

<p align="center"><sub>Week 8 · Sprint 3 · Day 4 of 5 → <b>Day 5: Full Evaluation, SHAP Explainability &amp; Sprint Review</b></sub></p>
