import streamlit as st
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("size_recommender.pkl")

model = load_model()

st.title("Nyx Size Recommender")
st.write("Welcome to the Nyx Size Recommender app!")

# Create input fields
height = st.number_input("Enter height (cm):", min_value=100, max_value=250, value=170)
weight = st.number_input("Enter weight (kg):", min_value=30, max_value=200, value=70)
age = st.number_input("Enter age:", min_value=10, max_value=100, value=25)

# Button to make predictions
if st.button("Recommend Size"):
    # Convert input into a NumPy array
    input_data = np.array([[height, weight, age]])
    
    # Predict the size
    prediction = model.predict(input_data)

    st.success(f"Recommended Size: {prediction[0]}")
