from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("lightgbm_failure_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")


class MachineInput(BaseModel):
    Air_temperature: float
    Process_temperature: float
    Rotational_speed: float
    Torque: float
    Tool_wear: float
    Type_L: int
    Type_M: int


@app.post("/predict")
def predict(data: MachineInput):
    row = pd.DataFrame([data.dict()])
    row = row[feature_columns]

    prob = model.predict_proba(row)[0][1]

    if prob >= 0.75:
        status = "Critical"
    elif prob >= 0.40:
        status = "Warning"
    else:
        status = "Healthy"

    return {
        "failure_probability": round(prob * 100, 2),
        "status": status
    }