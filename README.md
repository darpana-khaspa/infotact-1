# Contextual Predictive Maintenance

A machine learning-based predictive maintenance system that estimates the probability of machine failure by combining machine sensor data with contextual information. The project provides an interactive dashboard for monitoring machine health, visualizing failure probabilities, and evaluating model performance.

---

# Problem Statement

Industries commonly rely on either scheduled maintenance or reactive maintenance, both of which can lead to unnecessary servicing, unexpected machine failures, increased downtime, and higher maintenance costs.

Traditional predictive maintenance systems primarily use internal machine sensor data while overlooking external contextual factors such as operating conditions, ambient temperature, and machine load.

This project addresses these limitations by integrating machine telemetry with contextual information to predict machine failures before they occur.

---

# Objectives

- Predict machine failures before breakdown.
- Reduce unexpected machine downtime.
- Improve maintenance planning and scheduling.
- Visualize machine health using an interactive dashboard.
- Display model performance using multiple evaluation metrics.

---

# Scope

This project serves as a prototype for predictive maintenance using machine learning.

It includes:

- Machine health dashboard
- Failure probability prediction
- Machine monitoring
- Performance visualization
- Maintenance alerts

> **Note:** Contextual information used in this project is simulated for demonstration purposes.

---

# Technologies Used

## Frontend

- React
- Vite
- TypeScript
- Tailwind CSS
- Lucide React Icons

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- SMOTE (Imbalanced Learning)

## Visualization

- Recharts
- Confusion Matrix
- Precision-Recall Curve
- ROC Curve

---

# System Workflow

```text
Machine Sensor Data
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Contextual Data Fusion
        │
        ▼
LightGBM Prediction Model
        │
        ▼
Failure Probability
        │
        ▼
Dashboard Visualization
```

---

# Machine Learning Pipeline

1. Load the dataset
2. Perform data preprocessing
3. Handle missing values
4. Feature scaling
5. Balance the dataset using SMOTE
6. Train the LightGBM classifier
7. Evaluate model performance
8. Export predictions

---

# Performance Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- Macro F1 Score
- ROC-AUC Score
- Confusion Matrix

---

# Dashboard Features

- Machine Health Monitoring
- Failure Probability Prediction
- Machine Status Overview
- Performance Metrics Visualization
- Interactive Charts
- Maintenance Alerts

---

# Advantages

- Easy-to-understand dashboard
- Interactive monitoring interface
- Predictive maintenance visualization
- Modular project architecture
- Scalable design for future enhancements

---

# Limitations

- Uses a public dataset instead of real industrial sensor data.
- External contextual information is simulated.
- Prototype focuses on prediction and visualization rather than production deployment.
- No real-time IoT device integration.

---

# Future Enhancements

- Live IoT sensor integration
- MQTT-based communication
- NVIDIA Jetson Edge AI deployment
- Cloud synchronization
- Email and SMS maintenance alerts
- Digital Twin integration
- Real-time streaming dashboards

---

# Expected Outcome

The system predicts potential machine failures using machine learning and presents the results through an intuitive dashboard. This enables maintenance teams to identify high-risk machines, prioritize maintenance activities, reduce downtime, and improve operational efficiency.

---

# Project Structure

```
Contextual_Predictive_Maintenance/
│
├── backend/
│   ├── model/
│   ├── dataset/
│   ├── training/
│   ├── prediction/
│   └── evaluation/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── assets/
│
├── saved_models/
│
├── reports/
│
├── README.md
│
└── requirements.txt
```

---

# Model

- **Algorithm:** LightGBM Classifier
- **Class Imbalance Handling:** SMOTE
- **Evaluation Metrics:** Accuracy, Precision, Recall, Macro F1, ROC-AUC

---

# Applications

- Manufacturing Industry
- Smart Factories
- Industrial IoT
- Automotive Maintenance
- Predictive Asset Monitoring
- Industry 4.0 Solutions

---

# Future Deployment

The project can be extended for deployment on:

- NVIDIA Jetson Edge Devices
- Industrial IoT Gateways
- Cloud Platforms
- Smart Manufacturing Systems

---

# Author

**Srimani Deepika Krishna Chintalapudi**

Contextual Predictive Maintenance using Machine Learning and Interactive Dashboard Visualization.
