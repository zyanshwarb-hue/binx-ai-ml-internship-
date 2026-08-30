# Week 6 — Day 4: Building & Training a Neural Network in Keras

**Phase 3 — Deep Learning & Applied Project | Sprint 1, Day 4 of 5**
**Intern:** Zayan Shawareb
**Capstone:** Cardiac Patient Monitoring System

![status](https://img.shields.io/badge/status-complete-brightgreen) ![phase](https://img.shields.io/badge/phase-3%20%7C%20Deep%20Learning-blueviolet) ![dataset](https://img.shields.io/badge/dataset-Heart%20Failure-red) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![libraries](https://img.shields.io/badge/libraries-TensorFlow%20%7C%20Keras%20%7C%20Scikit--learn-orange)

## 🎯 Objectives
- Build a neural network with the Keras Sequential API.
- Compile, train, and evaluate the network, and read its training history.
- Apply batch normalization and dropout to stabilize training and reduce overfitting.

## 🗂️ Contents
- `day4.ipynb` — self-contained notebook: data prep, **Model v1** (plain Sequential network),
  training-history diagnostics, **Model v2** (BatchNorm + Dropout), and a side-by-side comparison
  against the Day 1 baseline.

## 🏗️ Architecture Summary
| Model | Layers | Regularization |
|---|---|---|
| v1 | Dense(64, relu) → Dense(32, relu) → Dense(1, sigmoid) | None |
| v2 | Dense(64, relu) → BatchNorm → Dropout(0.3) → Dense(32, relu) → BatchNorm → Dropout(0.2) → Dense(1, sigmoid) | BatchNorm + Dropout |

## 📌 Results (fill in after running the notebook)
| Model | Accuracy | ROC-AUC | Beats Baseline? |
|---|---|---|---|
| Baseline (Logistic Regression, Day 1) | `____` | `____` | — |
| Model v1 (plain NN) | `____` | `____` | `____` |
| Model v2 (BatchNorm + Dropout) | `____` | `____` | `____` |

## ✅ Deliverables Checklist (Day 4)
- [ ] Keras Sequential model built with correct output layer/loss for binary classification
- [ ] Model compiled with Adam + binary cross-entropy, trained ≥30 epochs with validation split
- [ ] Training vs. validation loss/accuracy plotted and diagnosed
- [ ] Dropout / BatchNormalization added and compared against the unregularized run
- [ ] Test-set score compared to the Day 1 baseline
- [ ] Committed to the sprint branch / PR updated

## ➡️ Next: Day 5
Systematic tuning (learning rate, batch size), `EarlyStopping` and `ModelCheckpoint`, and the full Sprint 1 Review & Retrospective.
