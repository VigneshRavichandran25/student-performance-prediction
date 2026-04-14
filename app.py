import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("student_data.csv")

# Features and target
X = df[['studytime', 'absences', 'G1', 'G2']]
y = df['G3']

# Train model
model = LinearRegression()
model.fit(X, y)

# UI
st.title("Student Performance Prediction System")

studytime = st.number_input("Enter Study Time", min_value=1, max_value=10)
absences = st.number_input("Enter Absences", min_value=0)
G1 = st.number_input("Enter G1 Marks", min_value=0, max_value=20)
G2 = st.number_input("Enter G2 Marks", min_value=0, max_value=20)

if st.button("Predict Final Mark"):
    new_data = pd.DataFrame({
        'studytime': [studytime],
        'absences': [absences],
        'G1': [G1],
        'G2': [G2]
    })
    
    prediction = model.predict(new_data)
    st.success(f"Predicted Final G3 Mark: {prediction[0]:.2f}")
