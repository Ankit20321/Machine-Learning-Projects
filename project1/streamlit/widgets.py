import streamlit as st  # Import Streamlit for web app creation

st.write("Streamlit text Input")

name=st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}")