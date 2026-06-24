import os
import json
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "ml", "ai4i2020.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "public", "machines.json")
METRICS_PATH = os.path.join(BASE_DIR, "public", "model_metrics.json")

df = pd.read_csv(DATA_PATH)

original_df = df.copy()

df.drop(["UDI", "Product ID"], axis=1, inplace=True)
df = pd.get_dummies(df, columns=["Type"], drop_first=True)

X = df.drop(["Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF"], axis=1)
y = df["Machine failure"]

X.columns = [
    "Air_temperature",
    "Process_temperature",
    "Rotational_speed",
    "Torque",
    "Tool_wear",
    "Type_L",
    "Type_M"
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LGBMClassifier(random_state=42, class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

metrics = {
    "accuracy": round(accuracy_score(y_test, y_pred), 4),
    "precision": round(precision_score(y_test, y_pred, zero_division=0), 4),
    "recall": round(recall_score(y_test, y_pred, zero_division=0), 4),
    "f1_score": round(f1_score(y_test, y_pred, zero_division=0), 4),
    "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
}

probabilities = model.predict_proba(X)[:, 1] * 100

machines = []

for i, row in X.iterrows():
    prob = round(float(probabilities[i]), 2)

    if prob >= 75:
        status = "Critical"
    elif prob >= 40:
        status = "Warning"
    else:
        status = "Healthy"

    alert_reason = "Normal operating condition"

    if prob >= 75:
        alert_reason = "Critical failure risk detected"
    elif row["Process_temperature"] > 313:
        alert_reason = "High process temperature"
    elif row["Torque"] > 55:
        alert_reason = "High torque load"
    elif row["Tool_wear"] > 200:
        alert_reason = "Tool wear maintenance required"

    machines.append({
        "machine_id": f"M-{i + 1:03d}",
        "location": f"Plant {chr(65 + (i % 3))} - Line {(i % 4) + 1}",
        "Air_temperature": round(float(row["Air_temperature"]), 2),
        "Process_temperature": round(float(row["Process_temperature"]), 2),
        "Rotational_speed": int(row["Rotational_speed"]),
        "Torque": round(float(row["Torque"]), 2),
        "Tool_wear": int(row["Tool_wear"]),
        "failure_probability": prob,
        "status": status,
        "alert_reason": alert_reason
    })

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

with open(OUTPUT_PATH, "w") as f:
    json.dump(machines[:100], f, indent=2)

with open(METRICS_PATH, "w") as f:
    json.dump(metrics, f, indent=2)

print("Generated public/machines.json")
print("Generated public/model_metrics.json")