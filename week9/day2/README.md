<p align="center">
  <img src="https://img.shields.io/badge/BINX%20TECH-AI%20%26%20ML%20INTERNSHIP-0B1F3A?style=for-the-badge" alt="BinX Tech"/>
</p>

<h1 align="center">🌐 Week 9 · Day 2</h1>
<h3 align="center">Serving the Model with FastAPI</h3>

<p align="center">
  <img src="https://img.shields.io/badge/PHASE-3%20CAPSTONE-0B1F3A?style=for-the-badge" alt="Phase 3"/>
  <img src="https://img.shields.io/badge/SPRINT-4%20OF%204-1B4F8C?style=for-the-badge" alt="Sprint 4"/>
  <img src="https://img.shields.io/badge/DAY-2%20OF%205-0096C7?style=for-the-badge&logoColor=black" alt="Day 2 of 5"/>
  <img src="https://img.shields.io/badge/TOPIC-REST%20API-0077B6?style=for-the-badge" alt="REST API"/>
  <img src="https://img.shields.io/badge/CAPSTONE-CARDIAC%20MONITORING-03045E?style=for-the-badge" alt="Cardiac Monitoring Capstone"/>
</p>

<p align="center"><i>"Serving a model with FastAPI means exposing a URL that accepts input data in a request and returns the model's prediction in the response."</i></p>

---

## 📖 The Story So Far

Day 1 ended with two files on disk — `model.joblib` and `preprocessor.joblib` — verified with a round-trip
prediction and backed by a pinned `requirements.txt` and an MLflow-logged run. Today those two files become the
brain behind a real, callable web service: a FastAPI application with a `/predict` endpoint that any other
program — a website, a mobile app, tomorrow's Streamlit dashboard — can call over HTTP.

## 🎯 Learning Objectives

| | Objective |
|---|---|
| 🏗️ | Build a FastAPI app that loads a serialized model and preprocessing |
| 📮 | Create a `/predict` POST endpoint that validates input with Pydantic |
| 🧪 | Test the endpoint locally using FastAPI's automatic documentation |

## 🏗️ What Gets Built

`main.py` — a real, standalone FastAPI application (not just notebook code):

- Loads `model.joblib` and `preprocessor.joblib` from Day 1 unchanged.
- Defines `PatientData`, a Pydantic schema matching the capstone's exact 11 input features (`Age`, `Sex`,
  `ChestPainType`, `RestingBP`, `Cholesterol`, `FastingBS`, `RestingECG`, `MaxHR`, `ExerciseAngina`, `Oldpeak`,
  `ST_Slope`), with realistic constraints (e.g. `Sex` restricted to `"M"`/`"F"`, `Age` bounded 0–120).
- Exposes `POST /predict`, returning the prediction, a human-readable label, and the model's probability.

## ✅ Pydantic Validation in Action

Tested inside the notebook with FastAPI's `TestClient` — the same request → validation → preprocessing → model →
response chain a live server would run:

| Request | Result |
|---|---|
| Valid patient payload | `200 OK` — `{"prediction": 1, "label": "Disease", "probability": 0.8214}` |
| `"Age": "fifty-four"`, `"Sex": "unknown"` | `422 Unprocessable Entity` — rejected before ever reaching the model, with a clear per-field error message |

> [!NOTE]
> **The deployment payoff of Day 1:** the endpoint applies the *exact same* preprocessing as training, loaded from
> `preprocessor.joblib` — not re-implemented. That one line is what makes today's service trustworthy: there is no
> second, hand-written copy of the scaling/encoding logic that could ever drift out of sync with training.

## ▶️ Running It for Real

```bash
uvicorn main:app --reload
# Then open http://127.0.0.1:8000/docs to test /predict interactively in the browser
```

`/docs` is generated automatically from the `PatientData` schema — including a worked example — so anyone on the
team can try the API without reading a line of code.

## 📦 Artifacts Produced

- `main.py` — the real, deployable FastAPI application
- A verified request → validation → preprocessing → model → response chain, tested for both valid and invalid input

**Tomorrow (Day 3):** this API becomes the backend for an interactive Streamlit dashboard, so a non-technical user
can get a prediction without ever touching `/docs` or JSON.

## 🧰 Tools Used

![FastAPI](https://img.shields.io/badge/FastAPI-0B1F3A?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-1B4F8C?style=flat-square)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0096C7?style=flat-square)
![joblib](https://img.shields.io/badge/joblib-0B1F3A?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-0B1F3A?style=flat-square)
![Git](https://img.shields.io/badge/Git%20%26%20GitHub-0B1F3A?style=flat-square)

## 📓 The Notebook

**[→ Open day2.ipynb](./day2.ipynb)** for the full, executed walkthrough — including live `TestClient` requests and
their real responses.

---

<p align="center"><sub>Week 9 · Sprint 4 · Day 2 of 5 → <b>Day 3: Interactive Streamlit Dashboard</b></sub></p>
