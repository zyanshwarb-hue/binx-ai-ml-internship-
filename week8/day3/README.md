<p align="center">
  <img src="https://img.shields.io/badge/BINX%20TECH-AI%20%26%20ML%20INTERNSHIP-061A33?style=for-the-badge" alt="BinX Tech"/>
</p>

<h1 align="center">🩺 Week 8 · Day 3</h1>
<h3 align="center">Computer Vision Preprocessing — OpenCV on Real 12-Lead ECG Scans</h3>

<p align="center">
  <img src="https://img.shields.io/badge/SPRINT-3-0B2E59?style=for-the-badge" alt="Sprint 3"/>
  <img src="https://img.shields.io/badge/DAY-3%20OF%205-00A6C0?style=for-the-badge" alt="Day 3 of 5"/>
  <img src="https://img.shields.io/badge/DURATION-8%20HOURS-FFC857?style=for-the-badge&logoColor=black" alt="8 hours"/>
  <img src="https://img.shields.io/badge/TOPIC-IMAGE%20PREPROCESSING-1BAF7A?style=for-the-badge" alt="Image Preprocessing"/>
  <img src="https://img.shields.io/badge/THREAD-CARDIAC%20MONITORING-8B5CF6?style=for-the-badge" alt="Cardiac Monitoring Thread"/>
</p>

<p align="center"><i>"A model never sees a photo — it sees a grid of numbers. Get the grid wrong and nothing after it can be trusted."</i></p>

---

## 📖 The Story So Far

Day 2 turned clean text into numbers and picked the representation that fit the job. Day 3 switches modality
entirely: **images** — and for the first time this sprint, the images are not a borrowed dataset. This notebook runs
on real scanned 12-lead ECG reports from the **["ECG Images dataset of Cardiac Patients"](https://www.kaggle.com/datasets/jirathp/ecg-images-dataset-of-cardiac-patients)**
(Khan, A.H. & Hussain, M., University of Management and Technology, Mendeley Data, V2, 2021,
DOI: [10.17632/gwbz3fsgp8.2](https://doi.org/10.17632/gwbz3fsgp8.2)) — the same clinical modality as the **Cardiac
Monitoring capstone** itself, not a tangent through Week 7's skin-lesion dataset. Every preprocessing and
augmentation decision below is judged against what a 12-lead ECG scan actually encodes: waveform shape, timing, and
polarity — not color.

## 🎯 Learning Objectives

| | Objective |
|---|---|
| 🖼️ | Build an image preprocessing pipeline with OpenCV: color-space conversion, resizing, normalization |
| 🔄 | Apply data augmentation (flips, rotation, brightness/contrast) and inspect the results on real scans |
| ⚖️ | Judge which augmentations are safe for a diagnostic ECG scan — and explain why the answer differs from a photo dataset |

## 🗂️ About the Data

| | |
|---|---|
| Source | [Kaggle: ECG Images dataset of Cardiac Patients](https://www.kaggle.com/datasets/jirathp/ecg-images-dataset-of-cardiac-patients) (mirror of Mendeley Data) |
| Original authors | Ali Haider Khan, Muzammil Hussain — University of Management and Technology, 2021 |
| Full dataset size | 928 scans, ~203MB, 4 classes: Normal (284), Myocardial Infarction (240), Abnormal Heartbeat (233), History of MI (172) |
| Bundled in this repo | `day3_real_ecg_samples/` — a genuine 12-image sample (3 per class) so the notebook runs standalone without a 203MB download |

> [!NOTE]
> Only a small labeled sample ships in this repo to keep it lightweight — swap `IMAGE_DIR` in the notebook for the
> full downloaded Kaggle folder and every cell runs unchanged on all 928 scans.

## 🐛 The Bug: BGR vs. RGB

`cv2.imread` reads pixels in **BGR** order. Displaying that array with an RGB-expecting viewer (`matplotlib`)
visibly inverts the colors — on these scans, the pink calibration border around each report renders as blue. It's a
real, demonstrable bug, not just a warning in a comment.

| | Before fix | After fix |
|---|---|---|
| Channel order | BGR (as read) | RGB (converted) |
| Visual effect | Calibration border renders blue | True colors (pink border) restored |

> [!WARNING]
> This is Day 3's version of Day 1's dropped `"not"` and Day 2's TF-IDF choice — a one-line detail that's easy to
> skip and silently wrong until someone actually checks the output.

## 🎨 Why Grayscale Here (Unlike a Skin-Lesion Photo)

An ECG report's diagnostic signal lives entirely in the *shape* of the traced line against the grid — not in the
paper's pink tint or the printer's ink color. Converting to grayscale throws away noise, not signal. That's the
opposite conclusion from a task where color itself is the label (like melanoma classification) — the same
generic-sounding step ("convert to grayscale?") only has one correct answer once it's checked against the specific
image format.

## ⚖️ Which Augmentations Are Safe? (The Answer Flips vs. a Photo Dataset)

| Augmentation | Safe for a 12-lead ECG scan? | Why |
|---|---|---|
| Horizontal flip | 🚫 No | Reverses the P-QRS-T sequence in time — an ECG never runs backward |
| Vertical flip | 🚫 No | Inverts lead polarity — an upright R wave becomes an inverted one, which can look like a different diagnosis |
| Rotation beyond a few degrees | ⚠️ Risky | The grid encodes calibrated time (mm/s) and voltage (mm/mV); rotating distorts the exact measurements the diagnosis depends on |
| Mild brightness / contrast jitter | ✅ Yes | Mimics realistic scan/printer variation without touching the waveform |
| Small, label-preserving crop | ✅ Yes, with care | Simulates minor scanning-framing differences — as long as no lead panel is cut off |

This is the **opposite** conclusion from a melanoma-style photo dataset, where flips and rotation were free and color
was the risk. Neither table is "the augmentation rules for images" — each is what happens when the same generic
toolbox (`cv2.flip`, `cv2.warpAffine`, brightness scaling) gets checked against what a *specific* image format
actually encodes. The notebook's augmentation grid makes this visible directly: the flipped scan shows mirrored,
backward text, and the rotated scan visibly tilts off the calibration grid — concrete evidence, not just an
assertion.

## 📝 Documented Decision: preprocessing for the Cardiac Monitoring thread

- **This is the first Sprint 3 notebook that runs on the capstone's own clinical modality.** Day 1 and Day 2 borrowed
  the UCI Drug Review dataset for text practice; Day 3 runs on real 12-lead ECG scans — the same signal type the
  Cardiac Monitoring project ultimately cares about, even though the capstone's current model consumes structured
  vitals (`heart.csv`), not images.
- **If the capstone ever ingested scanned ECG reports directly**, this is the exact pipeline it would need: BGR→RGB,
  resize, grayscale, normalize, and augmentation restricted to brightness/contrast and careful cropping — never
  flips or real rotation.
- **The recurring theme across Sprint 3:** every representation choice this week — negation-aware stop words, TF-IDF
  vs. embeddings, and now grayscale-vs-color and safe-vs-unsafe augmentation — looks like a minor technical detail
  right up until it quietly flips the label the model is supposed to predict.

## 🧰 Tools Used

![OpenCV](https://img.shields.io/badge/OpenCV%20(cv2)-0B2E59?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-0B2E59?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-0B2E59?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-0B2E59?style=flat-square)
![Git](https://img.shields.io/badge/Git%20%26%20GitHub-0B2E59?style=flat-square)

## 📓 The Notebook

**[→ Open day3.ipynb](./day3.ipynb)** for the full, executed walkthrough — code and real output, generated live on
real ECG scans.

---

<p align="center"><sub>Week 8 · Sprint 3 · Day 3 of 5 → <b>Day 4: End-to-End predict() Pipeline &amp; Error Analysis</b></sub></p>
