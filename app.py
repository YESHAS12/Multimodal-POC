import streamlit as st
from orchestrator import run_pipeline

st.title(" Multimodal Content Generator (POC)")
prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    img, audio, music, video = run_pipeline(prompt)

    st.image(img, caption="Generated Image")
    st.audio(audio, format="audio/wav")
    st.audio(music, format="audio/wav")
    st.video(video)
