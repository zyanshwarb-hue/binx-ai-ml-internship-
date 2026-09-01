<div align="center">

# 💓 Day 3 — The Rhythm of Memory
### Teaching a network to hear a heartbeat the way a cardiologist reads one — in order, over time

**Week 7 · Sprint 2 · Phase 3 Capstone** — BinX Tech AI & ML Internship

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-LSTM-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-MIT--BIH-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Metrics-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

💓 Listen → 🧩 Remember → 🔁 Compare → 🧠 Diagnose

</div>

---

## 📖 The Story

A single heartbeat isn't a photo — it's a *story told over time*. A cardiologist doesn't diagnose an arrhythmia from one still frame; they read the shape of the wave as it unfolds, millisecond by millisecond, because the **order** of the signal carries the diagnosis. Flip two segments of the same waveform and it means something completely different — exactly like "the movie was not good" versus "good, the movie was not."

Day 1-2 gave this project a way to *see* (CNNs). Day 3 gives it a way to *listen* — an architecture with memory, built specifically for data where order is the whole point.

## 🎯 What Gets Proven Today

| # | Question | How It's Answered |
|---|---|---|
| 3.1 | Why can't a CNN just handle this too? | Order-dependence proven with a simple counter-example |
| 3.2 | What is an RNN, mathematically? | Hidden-state equation implemented by hand in NumPy, traced step by step on a real ECG beat |
| 3.3 | Why do plain RNNs fail on long sequences? | Vanishing-gradient magnitude computed directly: ≤0.25^187 across a full heartbeat |
| 3.4 | How does LSTM actually fix it? | Full gate equations (forget, input, output, cell state) — the additive cell-state update explained as the key fix |
| 3.5 | Is the dataset balanced? | Checked first: ~83% Normal beats — worse imbalance than Week 7's melanoma dataset |
| Lab | Does LSTM really beat plain RNN here? | Head-to-head training curves, per-class confusion matrices, not just accuracy |

## 🖼️ What's Visualized

- Class distribution bar chart (5 arrhythmia classes)
- One real waveform plotted per class — what the network has to tell apart
- Validation loss + accuracy: Plain RNN vs. LSTM, side by side
- Confusion matrix per model (5×5, per-class recall visible)

## 🩺 Dataset

[ECG Heartbeat Categorization Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat) — MIT-BIH Arrhythmia Database (Kaggle), 187-timestep heartbeat sequences, 5 classes.

## 🎬 Director's Commentary — From Seeing to Listening

Day 1-2 gave the project eyes — a CNN that reads spatial structure in an image. Day 3 gave it ears — an architecture that reads a signal unfolding over time, and understands *why* order changes meaning.

The vanishing-gradient proof isn't decoration — it's the reason LSTM's gated, additive memory exists at all, and the head-to-head comparison is the same idea from Week 6's playbook: never trust an architecture choice you haven't benchmarked against a simpler baseline.

Every result today traces back to one idea: **a model's architecture should match the shape of the data**, not the other way around.

**◀️ Previous:** [Day 2](../day2/README.md) — building and explaining the vision model.
**▶️ Next up:** Day 4 — attention and Transformers: what happens when a network stops processing a sequence step-by-step, and looks at everything at once.

---

<div align="center">

**Zayan Shawareb** · BinX Tech — AI & ML Internship · Palestine, Nablus

</div>
