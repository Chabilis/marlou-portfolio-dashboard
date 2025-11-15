# app.py - Marlou Web Dev Portfolio Dashboard
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Marlou Test Web Dev", layout="wide")

st.title("Marlou - test full web dev")
st.markdown("**From Document Controller → Full-Stack Web Dev in 6 days**")
st.markdown(f"_{datetime.now().strftime('%B %d, %Y')}_")     

col1, col2 = st.columns([1, 2])
with col1:
    st.image("viber_image_2025-09-20_11-19-11-015.jpg", width=200)
with col2:
    st.markdown("""
    **Skills**: FastAPI - Streamlit - Groq AI - Render.com - GitHub  
    **Live APIs**: 3 production services deployed  
    **Still Learning**
    """)

st.divider()
st.header("Live Projects - Click to Test")

# Project 1
with st.expander("1. FastAPI Hello World API - LIVE"):
    st.markdown("• [Live API](https://marlou-fastapi-hello.onrender.com)  \n• [Docs](https://marlou-fastapi-hello.onrender.com/docs)")

# Project 2
with st.expander("2. File Upload API - Accepts Excel/CSV"):
    st.markdown("• [Live API](https://marlou-file-upload.onrender.com)  \n• [Docs](https://marlou-file-upload.onrender.com/docs)")

# Project 3 – AI Demo
with st.expander("3. LLM Summarizer API - Real AI (Llama 3.3)"):
    st.markdown("• [Live AI API](https://marlou-llm-summarizer.onrender.com)")
    file = st.file_uploader("Upload Excel/CSV for instant AI summary [if this live on Streamlit, it takes min to generate.]", type=["xlsx", "csv", "txt"], key="ai")
    if file:
        response = requests.post(
            "https://marlou-llm-summarizer.onrender.com/summarize",
            files={"file": file}
        )
        if response.status_code == 200:
            result = response.json()
            st.success("AI Summary Generated!")
            st.write(result["ai_summary"])
        else:
            st.error("API error. Check connection")

st.divider()        # line ------------------------
st.header("Test web dev")
st.markdown("""
still learning
""")

st.balloons()