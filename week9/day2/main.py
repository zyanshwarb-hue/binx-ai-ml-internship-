# Week 9 Day 2 -- Cardiac Monitoring prediction API.
# Loads Day 1's serialized model + preprocessing and serves a /predict endpoint.
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import pandas as pd
import joblib

app = FastAPI(
    title="Cardiac Monitoring Prediction API",
    description="BinX Tech AI & ML Internship -- Phase 3 Capstone (Sprint 4)",
    version="1.0.0",
)

model = joblib.load("model.joblib")
preprocessor = joblib.load("preprocessor.joblib")


# One patient's vitals -- matches heart.csv's 11 input features exactly.
class PatientData(BaseModel):
    Age: int = Field(..., ge=0, le=120, description="Age in years")
    Sex: Literal["M", "F"]
    ChestPainType: Literal["ATA", "NAP", "ASY", "TA"]
    RestingBP: float = Field(..., ge=0, description="Resting blood pressure (mm Hg)")
    Cholesterol: float = Field(..., ge=0, description="Serum cholesterol (mg/dl)")
    FastingBS: Literal[0, 1] = Field(..., description="1 if fasting blood sugar > 120 mg/dl, else 0")
    RestingECG: Literal["Normal", "ST", "LVH"]
    MaxHR: float = Field(..., ge=0, description="Maximum heart rate achieved")
    ExerciseAngina: Literal["Y", "N"]
    Oldpeak: float = Field(..., description="ST depression induced by exercise")
    ST_Slope: Literal["Up", "Flat", "Down"]

    class Config:
        json_schema_extra = {
            "example": {
                "Age": 54, "Sex": "M", "ChestPainType": "ASY", "RestingBP": 130,
                "Cholesterol": 246, "FastingBS": 0, "RestingECG": "Normal",
                "MaxHR": 150, "ExerciseAngina": "N", "Oldpeak": 1.0, "ST_Slope": "Flat",
            }
        }


class PredictionResponse(BaseModel):
    prediction: int
    label: Literal["Disease", "No Disease"]
    probability: float


@app.get("/")
def root():
    return {"status": "ok", "message": "Cardiac Monitoring Prediction API -- see /docs"}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: PatientData):
    row = pd.DataFrame([data.model_dump()])
    X_pre = preprocessor.transform(row)
    pred = int(model.predict(X_pre)[0])
    proba = float(model.predict_proba(X_pre)[0, 1])
    return PredictionResponse(
        prediction=pred,
        label="Disease" if pred == 1 else "No Disease",
        probability=round(proba, 4),
    )
