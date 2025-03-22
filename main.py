import streamlit as st
import joblib
import os

def load_model():
    file_path = os.path.join(os.path.dirname(__file__), "size_recommender.pkl")
    
    # Debugging: Check if the file exists
    if not os.path.exists(file_path):
        st.error(f"Model file not found at {file_path}")
        return None
    
    return joblib.load(file_path)

st.title("Nyx Size Recommender")
st.write("Welcome to the Nyx Size Recommender app!")

# Try loading the model
model = load_model()
if model:
    st.success("Model loaded successfully!")
else:
    st.error("Failed to load model.")
