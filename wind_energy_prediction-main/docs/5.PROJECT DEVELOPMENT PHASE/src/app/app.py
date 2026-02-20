from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load ONLY the model (correct)
model = joblib.load("../model/wind_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Input values
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    dew = float(request.form["dewpoint"])
    ws10 = float(request.form["ws10"])
    ws100 = float(request.form["ws100"])
    gust = float(request.form["gust"])
    wd10 = float(request.form["wd10"])
    wd100 = float(request.form["wd100"])

    # Engineered features (only those used in training)
    wind_speed_ratio = ws100 / (ws10 + 0.1)
    temp_dew_diff = temp - dew

    # EXACTLY 10 FEATURES
    features = [[
        temp,
        humidity,
        dew,
        ws10,
        ws100,
        wd10,
        wd100,
        gust,
        wind_speed_ratio,
        temp_dew_diff
    ]]

    prediction = model.predict(features)[0]

    return render_template("index.html", result=round(prediction, 3))


if __name__ == "__main__":
    app.run(debug=True)
