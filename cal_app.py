import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import urllib.request
import os


base_url = "https://huggingface.co/sonic222/cal/resolve/main/"

model_file = "calories_model1.pkl"
scaler_file = "scaler1.pkl"

if not os.path.exists(model_file):
    urllib.request.urlretrieve(base_url + model_file, model_file)

if not os.path.exists(scaler_file):
    urllib.request.urlretrieve(base_url + scaler_file, scaler_file)

model = joblib.load(model_file)
scaler = joblib.load(scaler_file)

# -------- Streamlit UI --------
st.set_page_config(page_title="Calories Prediction App", page_icon="🔥", layout="wide")

st.title("🔥 Calories Prediction App")
st.markdown("### Predict the calories burned based on personal & physical activity details.")

st.sidebar.header("User Input Features")

gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
age = st.sidebar.number_input("Age", min_value=10, max_value=80, value=25)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=220, value=170)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
duration = st.sidebar.number_input("Exercise Duration (min)", min_value=1, max_value=120, value=30)
heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=60, max_value=200, value=120)
body_temp = st.sidebar.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=38.0)

gender_encoded = 1 if gender == "Male" else 0

input_data = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])
scaled_data = scaler.transform(input_data)

if st.sidebar.button(" Predict Calories"):
    prediction = model.predict(scaled_data)[0]
    st.success(f"Estimated Calories Burned: **{prediction:.2f} kcal**")

    fig, ax = plt.subplots(figsize=(5,3))
    ax.bar(["Calories Burned"], [prediction], color="orange")
    ax.set_ylabel("kcal")
    st.pyplot(fig)

st.markdown("---")
st.markdown("Developed by **Ahmed Hamdy** | Machine Learning & AI Enthusiast 🚀")

