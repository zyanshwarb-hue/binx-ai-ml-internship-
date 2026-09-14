<p align="center">
  <img src="https://img.shields.io/badge/BINX%20TECH-AI%20%26%20ML%20INTERNSHIP-0B1F3A?style=for-the-badge" alt="BinX Tech"/>
</p>

<h1 align="center">🚀 Week 9 · Day 1</h1>
<h3 align="center">Sprint 4 Planning, Model Serialization &amp; MLOps</h3>

<p align="center">
  <img src="https://img.shields.io/badge/PHASE-3%20CAPSTONE-0B1F3A?style=for-the-badge" alt="Phase 3"/>
  <img src="https://img.shields.io/badge/SPRINT-4%20OF%204-1B4F8C?style=for-the-badge" alt="Sprint 4"/>
  <img src="https://img.shields.io/badge/DAY-1%20OF%205-0096C7?style=for-the-badge&logoColor=black" alt="Day 1 of 5"/>
  <img src="https://img.shields.io/badge/TOPIC-DEPLOYMENT%20PREP-0077B6?style=for-the-badge" alt="Deployment Prep"/>
  <img src="https://img.shields.io/badge/CAPSTONE-CARDIAC%20MONITORING-03045E?style=for-the-badge" alt="Cardiac Monitoring Capstone"/>
</p>

<p align="center"><i>"A model in a notebook helps no one. Deployment is what turns a trained model into something real users can actually use."</i></p>

---

## 📖 The Story So Far

Sprint 3 (Week 8) closed with an honest verdict: **Logistic Regression is the pragmatic choice** for the Cardiac
Monitoring capstone — Random Forest barely beat it (0.886 vs. 0.886 accuracy, 0.930 vs. 0.930 AUC) and only earned
its keep because `TreeExplainer` made SHAP convenient, not because it was actually better. Sprint 4 acts on that
retrospective directly: **this sprint ships the simple model.**

Day 1 opens the final sprint of the Phase 3 capstone with everything that has to happen *before* a single line of
serving code is written: plan the sprint, serialize the trained model and its preprocessing to disk, and lock down
the environment so today's result is reproducible tomorrow, next week, or on a teammate's machine.

## 🎯 Learning Objectives

| | Objective |
|---|---|
| 🗂️ | Complete Sprint 4 planning and define the deployment backlog |
| 💾 | Serialize the trained model *and* its preprocessing objects for production |
| 🔁 | Apply reproducibility practices (pinned requirements, MLflow tracking, fixed seeds) ahead of deployment |

## 🗂️ Sprint 4 Backlog

| Day | Backlog Item |
|---|---|
| 1 (today) | Serialize the trained model + preprocessing; freeze the deployment environment |
| 2 | Serve the model behind a FastAPI `/predict` endpoint with request validation |
| 3 | Build an interactive Streamlit dashboard for non-technical users |
| 4 | Deploy publicly (Hugging Face Spaces / Render / Railway) |
| 5 | Repository polish to the Definition of Done; Sprint Review + full-project Retrospective |

**Carried forward from the Sprint 3 retrospective:** ship Logistic Regression, not Random Forest — Sprint 3's own
honesty check showed the extra complexity never paid for itself.

## 💾 Model Serialization

| Object | Save Method | File |
|---|---|---|
| Scikit-learn classifier | `joblib.dump()` | `model.joblib` |
| Preprocessing (`ColumnTransformer`) | `joblib.dump()` | `preprocessor.joblib` |

> [!WARNING]
> **Training/serving skew rule (from Week 8):** the preprocessing object is saved *alongside* the model, never
> re-implemented by hand in the serving code. A hand-rewritten copy of the scaling/encoding logic that drifts even
> slightly out of sync with training is a top real-world deployment bug.

## ✅ Round-Trip Verification

Both artifacts are reloaded from disk and used to reproduce a known held-out prediction, asserting it matches the
original in-memory prediction exactly — the cheapest possible check that serialization actually worked, run before
tomorrow's API ever depends on it.

## 🔁 MLOps &amp; Reproducibility

| Practice | Where It Shows Up |
|---|---|
| Fixed random seeds | `random_state=42`, identical to every prior sprint |
| MLflow experiment tracking | Every model version logged with its parameters, metrics, and artifact |
| Pinned `requirements.txt` | Exact library versions frozen for the deployment environment |

## 📦 Artifacts Produced

- `model.joblib` — the trained Logistic Regression classifier
- `preprocessor.joblib` — the fitted `ColumnTransformer` (scaling + encoding)
- `requirements.txt` — pinned dependency versions for the deployment environment
- An MLflow run logging this model's parameters, metrics, and artifact

**Tomorrow (Day 2):** these two `.joblib` files get loaded into a FastAPI app behind a `/predict` endpoint, with
Pydantic validating every incoming request before it ever reaches the model.

## 🧰 Tools Used

![joblib](https://img.shields.io/badge/joblib-0B1F3A?style=flat-square)
![scikit-learn](https://img.shields.io/badge/Scikit--learn-1B4F8C?style=flat-square)
![MLflow](https://img.shields.io/badge/MLflow-0096C7?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-0B1F3A?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-0B1F3A?style=flat-square)
![Git](https://img.shields.io/badge/Git%20%26%20GitHub-0B1F3A?style=flat-square)

## 📓 The Notebook

**[→ Open day1.ipynb](./day1.ipynb)** for the full, executed walkthrough — code and real output, generated live on
the real 918-patient capstone dataset.

---

<p align="center"><sub>Week 9 · Sprint 4 · Day 1 of 5 → <b>Day 2: Serving the Model with FastAPI</b></sub></p>
