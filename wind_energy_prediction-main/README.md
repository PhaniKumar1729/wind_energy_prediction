🌬 Wind Turbine Power Prediction Using Machine Learning
📌 Project Overview

The Wind Turbine Power Prediction Using Machine Learning project is designed to predict wind turbine power output using weather parameters.

The system uses historical data to train a machine learning model and integrates it with a Flask web application to provide real-time predictions.

This project helps improve energy planning and supports renewable energy management.

🎯 Objectives

Predict wind turbine power output accurately

Use machine learning regression techniques

Perform feature engineering for better performance

Develop a simple Flask web interface

Provide real-time prediction results

⚙ Features

User input for weather parameters

Automatic feature engineering

Trained ML model integration

Real-time prediction output

Simple and clean web interface

Fast response time

🛠 Technologies & Tools Used

Python

NumPy (Numerical Python – numerical operations library)

Pandas (Data handling library)

Scikit-learn (Machine Learning library)

Flask (Web framework for Python)

Joblib (Model saving/loading library)

HTML & CSS (Frontend design)

📂 Project Structure
project-folder/
│
├── model/
│   └── wind_model.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── wind_turbine_ml.ipynb
└── README.md

🚀 How to Run the Project

Install required libraries:

pip install flask numpy pandas scikit-learn joblib


Run the Flask application:

python app.py


Open browser and go to:

http://127.0.0.1:5000/


Enter weather values and click Predict.

📊 Model Details

Type: Regression Model

Input Features: 10

Engineered Features:

Wind Speed Ratio

Temperature–Dew Difference

Evaluation Metrics:

R² Score

MAE

RMSE

✅ Conclusion

This project demonstrates how machine learning can be used for renewable energy forecasting. The integration of ML model with Flask makes it suitable for real-time applications.