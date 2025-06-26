import streamlit as st
import torch
from transformers import pipeline, set_seed

# Set up the page
st.set_page_config(page_title="Simple Text Generator", layout="centered")
st.title("📝 Basic Text Generation")
st.write("Enter a starting phrase, and the model will generate text based on it.")

# Load text generation pipeline (distilgpt2 is small and fast)
@st.cache_resource
def load_model():
    generator = pipeline("text-generation", model="distilgpt2")
    return generator

generator = load_model()

# Text input from user
prompt = st.text_input("Enter your prompt here:", "Once upon a time")

# Button to trigger generation
if st.button("Generate Text"):
    with st.spinner("Generating..."):
        result = generator(prompt, max_length=100, num_return_sequences=1)
        st.subheader("Generated Output:")
        st.write(result[0]["generated_text"])
