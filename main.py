import streamlit as st
import joblib
import os
import requests

MODEL_URL = "https://raw.githubusercontent.com/Wajiha-ui/nyx-size-recommender-Brand-Purpose-/main/size_recommender.pkl"
MODEL_PATH = "size_recommender.pkl"

def download_model():
    response = requests.get(MODEL_URL)
    if response.status_code == 200:
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
        return True
    return False

def load_model():
    if not os.path.exists(MODEL_PATH):
        st.warning("Downloading model...")
        if not download_model():
            st.error("Failed to download model")
            return None
    return joblib.load(MODEL_PATH)

st.title("Nyx Size Recommender")
st.write("Welcome to the Nyx Size Recommender app!")

model = load_model()
if model:
    st.success("Model loaded successfully!")
else:
    st.error("Failed to load model.")
