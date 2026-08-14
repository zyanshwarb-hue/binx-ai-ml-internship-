# Data Dictionary — Heart Failure Prediction Dataset

**Source:** Kaggle — "Heart Failure Prediction Dataset" by fedesoriano
**Rows:** 918 patients | **Columns:** 12 (11 features + 1 target)
**License / Privacy:** Public, de-identified clinical dataset. No directly identifiable patient data (no names, IDs, dates). Fully compliant with the project's "Out of Scope" rule on identifiable patient data.

| Column | Type | Description | Values / Range |
|---|---|---|---|
| Age | Numeric | Patient age in years | 28–77 |
| Sex | Categorical | Biological sex | M = Male, F = Female |
| ChestPainType | Categorical | Type of chest pain | TA = Typical Angina, ATA = Atypical Angina, NAP = Non-Anginal Pain, ASY = Asymptomatic |
| RestingBP | Numeric | Resting blood pressure (mm Hg) | 0–200 (0 = invalid/missing, see cleaning notes) |
| Cholesterol | Numeric | Serum cholesterol (mm/dl) | 0–603 (0 = invalid/missing, see cleaning notes) |
| FastingBS | Binary | Fasting blood sugar > 120 mg/dl | 1 = true, 0 = false |
| RestingECG | Categorical | Resting electrocardiogram results | Normal, ST = ST-T wave abnormality, LVH = left ventricular hypertrophy |
| MaxHR | Numeric | Maximum heart rate achieved | 60–202 |
| ExerciseAngina | Categorical | Exercise-induced angina | Y = Yes, N = No |
| Oldpeak | Numeric | ST depression induced by exercise relative to rest | -2.6–6.2 |
| ST_Slope | Categorical | Slope of the peak exercise ST segment | Up, Flat, Down |
| **HeartDisease** | **Target (binary)** | Presence of heart disease | 1 = disease, 0 = normal |

## Known Data-Quality Issues (addressed in Data Preparation)
- `Cholesterol == 0` for 172 patients (~19%) — physiologically impossible, treated as missing and imputed.
- `RestingBP == 0` for 1 patient — physiologically impossible, treated as missing and imputed.
- No duplicate rows found.
- No column-level nulls (NaN), but the above zero-encoded missing values required explicit handling.
