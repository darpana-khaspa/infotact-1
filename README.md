### Week 1: Data Preparation, Feature Engineering and Initial Model Building

In the first week, we focused on understanding the predictive maintenance problem and preparing the dataset for machine learning.

We started by studying the machine sensor data such as air temperature, process temperature, rotational speed, torque, tool wear, and failure labels. The main objective was to identify whether a machine is likely to fail based on these operational parameters.

The dataset was cleaned by checking missing values, duplicate records, incorrect values, and data imbalance. Since machine failure cases are usually fewer than normal cases, class imbalance was considered as an important challenge.

After data cleaning, exploratory data analysis was performed to understand the relationship between sensor parameters and machine failure. Important patterns such as high torque, high tool wear, abnormal temperature, and speed variations were analyzed.

Feature engineering was also done to improve model performance. Useful derived features were created from the available sensor data to help the model understand machine behavior better.

After preparing the data, we split it into training and testing sets. Basic machine learning models were tested first to create a baseline performance. This helped us understand how well simple models could predict machine failure.

By the end of Week 1, the dataset was cleaned, analyzed, prepared, and ready for advanced model training.

### Week 2: LightGBM Training, Evaluation and Dashboard Integration

In the second week, we focused on training the final predictive maintenance model and integrating it with the dashboard.

LightGBM was selected as the main machine learning model because it performs well on structured/tabular data, handles large datasets efficiently, and provides good accuracy with faster training time. It is suitable for predictive maintenance because it can learn complex relationships between machine parameters and failure conditions.

The LightGBM model was trained using the processed training data. Important parameters such as learning rate, number of estimators, maximum depth, and class weight were considered to improve model performance and reduce false predictions.

After training, the model was tested on unseen data. Evaluation metrics such as accuracy, precision, recall, F1-score, confusion matrix, and failure prediction performance were checked. Since failure detection is more important than only overall accuracy, recall and F1-score were given more importance.

The trained model was then saved and connected with the dashboard. The dashboard allows users to enter or view machine sensor values and get predictions about whether the machine is in normal condition or at risk of failure.

The dashboard also displays useful outputs such as failure prediction result, probability/risk level, and important parameters affecting the prediction. This makes the system more understandable and useful for real-time maintenance decisions.

By the end of Week 2, the LightGBM model was trained, evaluated, saved, and integrated into the predictive maintenance dashboard.

## Final Outcome

The project successfully builds a contextual predictive maintenance system using machine learning. It predicts possible machine failure using sensor-based operational data and presents the result through an interactive dashboard. The system helps in moving from reactive maintenance to proactive maintenance, reducing unexpected breakdowns and improving machine reliability.
```
