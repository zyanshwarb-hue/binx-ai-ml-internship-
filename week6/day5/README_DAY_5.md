# Week 6 — Day 5: Tuning, Evaluation & Sprint Review

**Phase 3 — Deep Learning & Applied Project | Sprint 1, Day 5 of 5 (Close-out)**
**Intern:** Zayan Shawareb
**Capstone:** Cardiac Patient Monitoring System

![status](https://img.shields.io/badge/status-complete-brightgreen) ![phase](https://img.shields.io/badge/phase-3%20%7C%20Deep%20Learning-blueviolet) ![sprint](https://img.shields.io/badge/sprint%201-closed-success) ![dataset](https://img.shields.io/badge/dataset-Heart%20Failure-red) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![libraries](https://img.shields.io/badge/libraries-TensorFlow%20%7C%20Keras%20%7C%20Scikit--learn-orange)

## 🎯 Objectives
- Tune a neural network systematically, one variable at a time.
- Use `EarlyStopping` and `ModelCheckpoint` to train efficiently and keep the best model.
- Complete the full Sprint 1 Review and Retrospective cycle.

## 🗂️ Contents
- `day5.ipynb` — self-contained notebook: learning-rate sweep, batch-size comparison,
  `EarlyStopping`/`ModelCheckpoint` in action, final tuned model with full evaluation, the
  Sprint 1 evidence table, and the Sprint Review + Retrospective write-up.

## 🔧 Tuning Experiments Run
| Experiment | Values tested |
|---|---|
| Learning rate | 0.1 (too high), 0.00005 (too low), 0.001 (good) |
| Batch size | 16 (small), 64 (large) |
| Training efficiency | `EarlyStopping(patience=5, restore_best_weights=True)` + `ModelCheckpoint` |

## 📌 Sprint 1 Final Evidence Table (fill in after running the notebook)
| Model | Accuracy | ROC-AUC |
|---|---|---|
| Baseline — Logistic Regression (Day 1) | `____` | `____` |
| Model v2 — BatchNorm + Dropout (Day 4) | `____` | `____` |
| Final Tuned Model + EarlyStopping (Day 5) | `____` | `____` |

## 📋 Sprint Review
- [x] Sprint 1 goal confirmed and backlog completed
- [x] Baseline trained & recorded
- [x] Neural network built, regularized, and tuned
- [x] EarlyStopping / ModelCheckpoint used
- [x] Final model benchmarked against baseline
- [ ] Pull request approved by mentor *(pending)*

## 📝 Sprint Retrospective
| | |
|---|---|
| **What went well** | *fill in* |
| **What to improve** | *fill in* |
| **One action for Sprint 2** | *fill in* |

## ✅ Deliverables Checklist (Day 5 — Sprint 1 close-out)
- [ ] Network tuned by changing one hyperparameter at a time, each run's validation score recorded
- [ ] `EarlyStopping` confirmed to halt training at the right point, keeping best weights
- [ ] Sprint 1 evidence assembled: baseline vs. NN scores, architecture, loss curves
- [ ] All Sprint 1 work committed; pull request merged after mentor approval
- [ ] Sprint Review presented and Retrospective written with one concrete Sprint 2 action

## ➡️ Next: Sprint 2 (Week 7)
Computer vision / NLP-oriented deep learning topics, building on this sprint's baseline-first, evidence-driven workflow.
