<p align="center">
  <img src="https://img.shields.io/badge/BINX%20TECH-AI%20%26%20ML%20INTERNSHIP-3A0A12?style=for-the-badge" alt="BinX Tech"/>
</p>

<h1 align="center">❤️ Week 8 · Day 5</h1>
<h3 align="center">Full Model Evaluation, SHAP Explainability &amp; Sprint Review</h3>

<p align="center">
  <img src="https://img.shields.io/badge/SPRINT-3-3A0A12?style=for-the-badge" alt="Sprint 3"/>
  <img src="https://img.shields.io/badge/DAY-5%20OF%205-B3132C?style=for-the-badge" alt="Day 5 of 5"/>
  <img src="https://img.shields.io/badge/DURATION-8%20HOURS-E63946?style=for-the-badge" alt="8 hours"/>
  <img src="https://img.shields.io/badge/TOPIC-EXPLAINABILITY-F4A6A6?style=for-the-badge&logoColor=black" alt="Explainability"/>
  <img src="https://img.shields.io/badge/CAPSTONE-CARDIAC%20MONITORING-6B0F1A?style=for-the-badge" alt="Cardiac Monitoring Capstone"/>
</p>

<p align="center"><i>"A model that's right for reasons you can't explain isn't ready for a patient."</i></p>

---

## 🎨 Design Note

Every chart in this notebook (and this README) uses a **single-hue red scale** — light to dark — instead of
red/green. Color-vision deficiency almost always confuses *red vs. green*, not *light red vs. dark red*, so class,
severity, and magnitude are encoded with **lightness and line style**, not hue, and every chart also carries numeric
labels so nothing depends on color alone.

## 📖 The Story So Far

Sprint 3 spent four days turning raw, messy inputs — text, then images — into disciplined, justified pipelines:
negation-aware cleaning (Day 1), TF-IDF vs. embeddings (Day 2), OpenCV preprocessing on real 12-lead ECG scans
(Day 3), and an end-to-end `predict()` pipeline with error analysis (Day 4). Day 5 closes the sprint by turning back
to the capstone's own model — the **Cardiac Monitoring** heart-disease classifier — and asking the two questions a
tabular ML project can't ship without: **is it actually good** (full evaluation, not just accuracy), and **can
anyone trust why it says what it says** (SHAP explainability). It closes with a sprint review and retrospective.

## 🎯 Learning Objectives

| | Objective |
|---|---|
| 📊 | Evaluate a classifier properly: confusion matrix, precision/recall/F1, ROC-AUC — not just accuracy |
| 🔍 | Use SHAP to explain both global feature importance and one individual patient's prediction |
| 🔁 | Run a sprint review and retrospective — what shipped, what was learned, what changes next sprint |

## 🔬 What Actually Happens in the Notebook

1. **Reload** the real capstone data — `heart.csv`, 918 patients, 12 columns (same data as the Week 4 Day 1
   Logistic Regression baseline).
2. **Train** that same Logistic Regression baseline alongside a Random Forest candidate, and compare them honestly.
3. **Evaluate fully**: confusion matrix, precision/recall/F1, ROC curve and AUC — not accuracy alone.
4. **Explain with SHAP**: global feature importance across all patients, then one individual patient's prediction
   broken down feature by feature.
5. **Sprint Review & Retrospective**: what Sprint 3 shipped across all 5 days, what went well, what to improve.

## ⚖️ Honesty Check: Did the Fancier Model Actually Win?

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression (Day 1 baseline) | 0.886 | 0.930 |
| Random Forest (candidate) | 0.886 | 0.930 |

Random Forest's AUC comes out only a hair above Logistic Regression's — not a meaningful win. This is Day 1's
"start simple" lesson holding up under its own rule: the fancier model doesn't automatically earn its place. Random
Forest is kept for the SHAP section anyway, purely because it unlocks fast, exact SHAP values (`TreeExplainer`) —
not because it decisively beat the baseline. In a real handoff, Logistic Regression's near-identical accuracy and
far greater simplicity would make it the pragmatic choice.

## 🔍 SHAP: Explaining the Model, Not Just Scoring It

A confusion matrix says *how often* the model is right. SHAP says *why*. The notebook builds two views:

- **Global importance** — which features move the model's predictions most, on average, across all patients
  (`ST_Slope`, `ChestPainType`, and `ExerciseAngina` come out on top).
- **One patient, explained** — a single test-set patient's prediction broken into each feature's push toward
  "Disease" (dark crimson) or away from it (light coral), built as a custom chart in the same red scale rather than
  SHAP's default red/blue waterfall. The notebook happens to land on one of the model's own **false negatives** —
  turning the chart into a real error-analysis example, not just a clean success story.

This is the same principle as Day 1's negation fix and Day 3's BGR/RGB bug, one level up: it's not enough for a
pipeline to be *technically correct* — for a health application, every step also has to be **inspectable**.

## 🏁 Sprint 3 Review

| Day | Shipped |
|---|---|
| 1 | Text preprocessing pipeline — caught and fixed a real negation-deletion bug |
| 2 | TF-IDF vs. word embeddings, with a documented, justified choice between them |
| 3 | OpenCV preprocessing on real 12-lead ECG scans — caught a real BGR/RGB bug, reasoned out domain-specific augmentation safety |
| 4 | End-to-end `predict()` pipeline with error analysis |
| 5 | Full evaluation (confusion matrix, ROC-AUC) and SHAP explainability for the capstone model, honestly checked against the Day 1 baseline |

**What went well:** every day this sprint produced a real, executed artifact backed by a real bug or a real,
justified decision — not a checklist exercise.

**What to improve next sprint:** Random Forest was kept mainly for `TreeExplainer` convenience despite barely
beating the baseline — a cleaner approach would apply SHAP's model-agnostic explainer directly to Logistic
Regression, so the explainability step doesn't quietly bias the model choice.

**Technical question for next sprint:** now that the model is evaluated and explainable, what does it take to serve
it reliably — monitoring for data drift, versioning the pipeline, and deciding what accuracy drop should trigger a
retrain?

## 🧰 Tools Used

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-3A0A12?style=flat-square)
![SHAP](https://img.shields.io/badge/SHAP-B3132C?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3A0A12?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-3A0A12?style=flat-square)
![Git](https://img.shields.io/badge/Git%20%26%20GitHub-3A0A12?style=flat-square)

## 📓 The Notebook

**[→ Open day5.ipynb](./day5.ipynb)** for the full, executed walkthrough — code and real output, generated live on
the real 918-patient capstone dataset.

---

<p align="center"><sub>Week 8 · Sprint 3 · Day 5 of 5 — <b>Sprint Complete ✅</b></sub></p>
