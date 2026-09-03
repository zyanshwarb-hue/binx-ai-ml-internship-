<div align="center">

# 🧬 Week 7 — Sprint 2
## CNNs, RNNs & Transformers: From a Single Neuron to Attending to Everything at Once

**Phase 3 Capstone · BinX Tech AI & ML Internship**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Kaggle](https://img.shields.io/badge/Kaggle-4--Datasets-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)

🧬 See → 💓 Listen → 👁️ Attend → 🏆 Decide

</div>

---

## 📖 The Story

Five days. Four architectures. One recurring question, asked in a different mathematical language every time:

**How do we get the right information to the right place, with the least loss possible?**

A CNN answered it with depth and shared filters. An RNN answered it with a hidden state carried through time. LSTM answered it with gates and an additive memory. A Transformer answered it by removing the wait entirely — letting every element see every other element at once.

And on the last day, the project came home: proof that the actual Phase 3 model — tabular, clinical, cardiac data — never needed any of them. Building the sophisticated tools and then choosing not to use them, with evidence, is the real skill this Sprint was built to test.

## 🗺️ The Five Days

| Day | Title | Core Question | Dataset |
|---|---|---|---|
| [Day 1](day1/README.md) | The Anatomy of Sight 🧬 | Why does convolution beat a dense layer on images? | Melanoma Skin Cancer (Kaggle) |
| [Day 2](day2/README.md) | Building the Diagnostician 🏗️ | Can a model be both accurate *and* explainable? | Melanoma Skin Cancer (Kaggle) |
| [Day 3](day3/README.md) | The Rhythm of Memory 💓 | Why do plain RNNs forget, and how does LSTM fix it? | ECG Heartbeat Categorization (Kaggle) |
| [Day 4](day4/README.md) | Everything, All at Once 👁️ | What replaces waiting your turn in a sequence? | UCI ML Drug Review Dataset (Kaggle) |
| [Day 5](day5/README.md) | The Verdict 🏆 | Which architecture actually earns its place in *this* project? | Cardiac Patient Monitoring (heart.csv) |

## 🎯 What Was Proven, Not Just Applied

- **Convolution** — parameter sharing computed by hand, receptive fields derived layer by layer, MobileNetV2's efficiency traced to depthwise-separable math
- **The vanishing gradient problem** — proven numerically across a 187-timestep sequence, not just described
- **LSTM's fix** — every gate equation implemented from scratch, the additive cell-state update identified as the actual solution
- **Self-attention** — Q/K/V matrices computed by hand in NumPy on real text, before ever calling a library
- **Explainability** — Grad-CAM for images, attention-weight visualization for text — the same accountability standard applied to two completely different data types
- **The final decision** — a fully logged, one-variable-at-a-time tuning process proving the simplest model was the right one all along

## 🎬 Director's Commentary — The Verdict

Four architectures were built and proven this week. The project's actual core model still uses none of them — and that's not an anticlimax, it's the point.

Knowing how to build the sophisticated option, and then choosing not to, because the data doesn't call for it, is a stronger signal of understanding than reaching for complexity by default. Every number in the Day 5 comparison table exists because a simpler question was asked first: *does this architecture even match this data?*

That discipline — baseline first, one variable at a time, never trust an unproven claim — traces back to Week 6, and it's the actual thread connecting every week of this internship.

---

<div align="center">

**Zayan Shawareb** · BinX Tech — AI & ML Internship · Palestine, Nablus

</div>
