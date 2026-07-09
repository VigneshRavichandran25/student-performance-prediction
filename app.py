import streamlit as st
import pandas as pd
import joblib


# Load model
model = joblib.load("models/student_model.pkl")


st.title("Academic Score Predictor")

st.write("Predict your final score based on study time, attendance and internal marks.")