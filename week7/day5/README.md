<div align="center">

# 🏆 Day 5 — The Verdict
### Four architectures explored this week. One project. Which one earned the right to be the core model?

**Week 7 · Sprint 2 · Phase 3 Capstone — Sprint Review** — BinX Tech AI & ML Internship

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Metrics-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Sprint](https://img.shields.io/badge/Sprint-2--Review-2ECC71?style=for-the-badge&logo=github&logoColor=white)

🗺️ Match → 🔧 Tune → 📊 Prove → 🏆 Decide

</div>

---

## 📖 The Story

This week, four architectures were built, proven, and stress-tested: a CNN that learned to see a lesion, an RNN and LSTM that learned to listen to a heartbeat over time, and a Transformer that learned to attend to everything at once. Each one was the *correct* tool — for the data shape it was given.

But the actual Phase 3 project — Cardiac Patient Monitoring — has never needed any of them. Its data is **tabular**: age, cholesterol, resting blood pressure, twelve columns of numbers. Not an image. Not a sequence. Not a sentence.

Day 5 isn't about building a fifth architecture. It's about proving, with evidence, that the *right* answer for this project was the simplest one all along — and then making that simple model as strong as it can possibly be.

## 🎯 What Gets Proven Today

| # | Question | How It's Answered |
|---|---|---|
| 5.1 | Why doesn't this project need this week's other architectures? | The decision table made explicit — CNN/LSTM/Transformer all lack a data shape to exploit here |
| 5.2 | How much can the Week 6 dense network actually improve? | Systematic, one-variable-at-a-time tuning: learning rate, width, dropout, batch norm |
| 5.3 | What does the best configuration look like fully evaluated? | Confusion matrix, ROC-AUC, EarlyStopping + ModelCheckpoint on the winning config |
| 5.4 | Does any of this actually beat the baseline? | Full experiment ledger, ranked, with the % improvement over Week 6 baseline computed directly |
| 5.5 | What's the final, defensible decision? | Documented — architecture, tuning discipline, and verdict, all in one place |

## 🖼️ What's Visualized

- Learning rate sweep — validation loss curves across 3 rates
- Final model — train/val loss and AUC curves
- Confusion matrix + ROC curve for the final tuned model
- Horizontal bar chart ranking every experiment by test AUC

## 🩺 Dataset

Cardiac Patient Monitoring dataset (`heart.csv`) — the same tabular clinical dataset used since Week 6, revisited with a full Sprint 2 tuning pass.

## 🎬 Director's Commentary — The Verdict

Four architectures. One project. And the project never needed any of the fancy ones.

That's not a disappointing ending — it's the actual lesson Sprint 2 was built to teach. Building a CNN, an LSTM, and a Transformer this week wasn't wasted effort just because the final model is "only" a tuned dense network. Each build proved something specific: parameter sharing, the mathematics of memory and its failure modes, and the cost-benefit tradeoff of parallel attention versus recurrence.

Knowing how to build the sophisticated option — and then choosing not to use it because the data doesn't call for it — is a stronger signal of understanding than defaulting to complexity by habit.

**◀️ Previous:** [Day 4](../day4/README.md) — attention, transformers, and the LSTM-vs-pretrained comparison.
**▶️ Next up:** Sprint 3 — same discipline, new goal.

---

<div align="center">

**Zayan Shawareb** · BinX Tech — AI & ML Internship · Palestine, Nablus

</div>
