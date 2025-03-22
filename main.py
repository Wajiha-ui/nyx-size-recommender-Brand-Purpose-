import streamlit as st
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("size_recommender.pkl")

model = load_model()

# Streamlit UI
st.title("Nyx Size Recommender")
st.write("Enter your details to get a recommended size.")

# Example input fields
height = st.number_input("Enter your height (cm)", min_value=100, max_value=250)
weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200)

if st.button("Get Recommendation"):
    features = np.array([[height, weight]])
    size_prediction = model.predict(features)  # Predict size
    st.write(f"Recommended Size: **{size_prediction[0]}**")
