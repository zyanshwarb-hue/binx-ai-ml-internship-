
import streamlit as st
import pandas as pd
import joblib

def engineer_features(X):
    X = X.copy()
    X["HR_Reserve_Ratio"] = X["MaxHR"] / (220 - X["Age"])
    X["High_Chol_Older_Patient"] = ((X["Cholesterol"] > 240) & (X["Age"] > 50)).astype(int)
    return X

st.set_page_config(page_title="Cardiac Risk Screening (Educational Demo)", page_icon="")
st.title(" Cardiac Patient Monitoring System")
st.caption("Educational ML demo — not a diagnostic tool. No medical advice is provided.")

@st.cache_resource
def load_model():
    return joblib.load("tuned_cardiac_pipeline.joblib")

model = load_model()

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 18, 100, 50)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
    resting_bp = st.number_input("Resting Blood Pressure", 80, 220, 130)
    cholesterol = st.number_input("Cholesterol", 0, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
with col2:
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.number_input("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise Angina", ["N", "Y"])
    oldpeak = st.number_input("Oldpeak", -3.0, 7.0, 0.0, step=0.1)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    patient = pd.DataFrame([{
        "Age": age, "Sex": sex, "ChestPainType": chest_pain_type,
        "RestingBP": resting_bp, "Cholesterol": cholesterol, "FastingBS": fasting_bs,
        "RestingECG": resting_ecg, "MaxHR": max_hr, "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak, "ST_Slope": st_slope,
    }])
    pred = model.predict(patient)[0]
    proba = model.predict_proba(patient)[0, 1]

    if pred == 1:
        st.error(f" Model flags elevated risk — probability: {proba:.1%}")
    else:
        st.success(f" Model does not flag elevated risk — probability: {proba:.1%}")
    st.caption("This is an educational demo only. Always consult a qualified clinician.")
