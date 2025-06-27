import streamlit as st
import joblib
import re
import base64
from PIL import Image

# Page configuration
st.set_page_config(page_title="Resume Classifier", layout="centered")

# Function to load background
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background
set_background("background.png")  # Use your background image file

# Load model and vectorizer
model = joblib.load("resume_classifier.pkl")
vectorizer = joblib.load("TfidfVectorizer.pkl")

# Clean text
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"#\S+", "", text)
    text = re.sub(r"@\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)
    return text.lower().strip()

# App layout
st.markdown('<h1 style="color:white;">🤖 Resume Category Classifier</h1>', unsafe_allow_html=True)
st.markdown("💼 Paste your resume content below to predict its category.")

resume_text = st.text_area("📄 Resume Input", height=300)

if st.button("🔍 Predict Category"):
    if resume_text.strip() != "":
        cleaned = clean_text(resume_text)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        st.success(f"🎯 Predicted Resume Category: **{prediction}**")
    else:
        st.warning("⚠️ Please enter your resume text.")

# Footer
st.markdown("---")
st.markdown('<div style="color:white; text-align:center;">🚀 Developed by <strong>Hari Krishna Kamana</strong></div>', unsafe_allow_html=True)
