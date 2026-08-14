"""
Reusable helper functions for the Cardiac Patient Monitoring System project.
These mirror the exact logic used inside the notebook, exposed here so they
can be imported and reused (e.g., for scoring new patient data with the
saved pipeline in models/tuned_cardiac_pipeline.joblib).
"""
import pandas as pd
import numpy as np

NUMERIC_FEATURES = ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]
CATEGORICAL_FEATURES = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]


def clean_invalid_zeros(df: pd.DataFrame) -> pd.DataFrame:
    """Replace physiologically impossible zero values with NaN so they can
    be properly imputed downstream instead of distorting statistics/models.
    """
    df = df.copy()
    df["RestingBP"] = df["RestingBP"].replace(0, np.nan)
    df["Cholesterol"] = df["Cholesterol"].replace(0, np.nan)
    return df


def engineer_features(X: pd.DataFrame) -> pd.DataFrame:
    """Add domain-informed engineered features used by the tuned pipeline.

    HR_Reserve_Ratio: MaxHR relative to the age-predicted maximum (220 - age).
    High_Chol_Older_Patient: compounded risk flag (cholesterol > 240 and age > 50).
    """
    X = X.copy()
    X["HR_Reserve_Ratio"] = X["MaxHR"] / (220 - X["Age"])
    X["High_Chol_Older_Patient"] = ((X["Cholesterol"] > 240) & (X["Age"] > 50)).astype(int)
    return X


def load_and_clean(csv_path: str) -> pd.DataFrame:
    """Convenience loader: reads the raw CSV and applies invalid-zero cleaning."""
    df = pd.read_csv(csv_path)
    return clean_invalid_zeros(df)


if __name__ == "__main__":
    # Quick smoke test
    df = load_and_clean("../data/heart.csv")
    print("Loaded & cleaned:", df.shape)
    print("Remaining NaNs in RestingBP/Cholesterol:",
          df[["RestingBP", "Cholesterol"]].isna().sum().to_dict())
