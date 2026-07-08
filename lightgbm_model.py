import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from lightgbm import LGBMClassifier

import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("ai4i2020.csv")

# Step 2: View first 5 rows
print(df.head())

# Step 3: Dataset information
print("\nDataset Information:")
print(df.info())

# Step 4: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Remove unnecessary columns
df.drop(['UDI', 'Product ID'], axis=1, inplace=True)

# Step 6: Convert the Type column (L, M, H) into numbers
df = pd.get_dummies(df, columns=['Type'], drop_first=True)

# Step 7: Check updated columns
print("\nColumns after preprocessing:")
print(df.columns)

# Step 8: Define features and target
X = df.drop(
    ['Machine failure', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'],
    axis=1
)

y = df['Machine failure']

X.columns = [
    'Air_temperature',
    'Process_temperature',
    'Rotational_speed',
    'Torque',
    'Tool_wear',
    'Type_L',
    'Type_M'
]

# Step 9: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Check shapes
print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Step 10: Train the LightGBM model

model = LGBMClassifier(random_state=42)

model.fit(X_train, y_train)

print("Model trained successfully!")

# Make predictions
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nModel Performance:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Plot Confusion Matrix
plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Failure", "Failure"],
    yticklabels=["No Failure", "Failure"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.savefig("confusion_matrix.png")

plt.show()
# Save trained model
joblib.dump(model, "lightgbm_model.pkl")

print("Model saved successfully as lightgbm_model.pkl")

import json

metrics = {
    "accuracy": round(accuracy, 4),
    "precision": round(precision, 4),
    "recall": round(recall, 4),
    "f1_score": round(f1, 4)
}

with open("metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

print("Metrics saved successfully as metrics.json")

import pandas as pd

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

importance.to_csv("feature_importance.csv", index=False)
print("Feature importance saved.")

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

print(f"Training LightGBM with random_state={42}")

metrics["train_samples"] = len(X_train)
metrics["test_samples"] = len(X_test)